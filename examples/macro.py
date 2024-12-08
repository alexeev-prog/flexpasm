from flexpasm import ASMProgram
from flexpasm.constants import LinuxInterrupts
from flexpasm.instructions.registers import get_registers
from flexpasm.instructions.segments import Label
from flexpasm.macros import MacroManager
from flexpasm.mnemonics import IntMnemonic, JmpMnemonic, MovMnemonic, XorMnemonic
from flexpasm.settings import Settings
from flexpasm.templates import ExitTemplate

macromanager = MacroManager()


@macromanager.add_macro("test_macro")
def test_macro(regs, start_lbl: Label):
	start_lbl.add_instruction(MovMnemonic(regs.AX, 4))
	start_lbl.add_instruction(MovMnemonic(regs.CX, "message"))
	start_lbl.add_instruction(MovMnemonic(regs.DX, "message_size"))
	start_lbl.add_instruction(IntMnemonic(LinuxInterrupts.SYSCALL))
	start_lbl.add_instruction(MovMnemonic(regs.AX, 1))
	start_lbl.add_instruction(XorMnemonic(regs.BX, regs.BX))
	start_lbl.add_instruction(IntMnemonic(LinuxInterrupts.SYSCALL))


def main():
	settings = Settings(
		title="Example ASM Program",
		author="alexeev-prog",
		filename="macros.asm",
		mode="64",
	)
	asmprogram = ASMProgram(settings, __name__)
	regs = get_registers(settings.mode)

	et = ExitTemplate(entry="exit", exit_code=-1)

	start_lbl = Label("start")

	macromanager.exec("test_macro", regs=regs, start_lbl=start_lbl)
	start_lbl.add_instruction(JmpMnemonic(et.get_label(settings.mode)))

	asmprogram.add_label(start_lbl)
	asmprogram.add_template(et)
	asmprogram.main_rws.add_string("message", "Hello, World!")

	asmprogram.save_code()
	# asmprogram.restore_backup()


if __name__ == "__main__":
	main()
