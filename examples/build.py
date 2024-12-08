from flexpasm import ASMProgram
from flexpasm.builder import ASMBuilder, Compiler, File, FileChain, Linker
from flexpasm.constants import LinuxInterrupts
from flexpasm.instructions.registers import get_registers
from flexpasm.instructions.segments import Label
from flexpasm.mnemonics import IntMnemonic, JmpMnemonic, MovMnemonic, XorMnemonic
from flexpasm.settings import Settings
from flexpasm.templates import ExitTemplate

compiler = Compiler()
linker = Linker()
file = File(source_file="build.asm", binary_file="build", object_file="build")
filechain = FileChain(skip_linker=True, compiler=compiler, linker=linker, files=[file])
asmbuilder = ASMBuilder(filechain)


def main():
	settings = Settings(
		title="Example ASM Program",
		author="alexeev-prog",
		filename="build.asm",
		mode="64",
	)
	asmprogram = ASMProgram(settings, __name__)
	regs = get_registers(settings.mode)

	et = ExitTemplate(entry="exit", exit_code=-1)

	start_lbl = Label("start")

	start_lbl.add_instruction(MovMnemonic(regs.AX, 4))
	start_lbl.add_instruction(MovMnemonic(regs.CX, "message"))
	start_lbl.add_instruction(MovMnemonic(regs.DX, "message_size"))
	start_lbl.add_instruction(IntMnemonic(LinuxInterrupts.SYSCALL))
	start_lbl.add_instruction(MovMnemonic(regs.AX, 1))
	start_lbl.add_instruction(XorMnemonic(regs.BX, regs.BX))
	start_lbl.add_instruction(IntMnemonic(LinuxInterrupts.SYSCALL))
	start_lbl.add_instruction(JmpMnemonic(et.get_label(settings.mode)))

	asmprogram.add_label(start_lbl)
	asmprogram.add_template(et)
	asmprogram.main_rws.add_string("message", "Hello, World!")

	asmprogram.save_code()

	asmbuilder.run_build()


if __name__ == "__main__":
	main()
