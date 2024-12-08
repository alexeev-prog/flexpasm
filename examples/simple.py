from flexpasm import ASMProgram
from flexpasm.constants import LinuxInterrupts
from flexpasm.instructions.registers import get_registers
from flexpasm.instructions.segments import Label
from flexpasm.mnemonics import IntMnemonic, MovMnemonic, XorMnemonic
from flexpasm.settings import Settings


def main():
    settings = Settings(
        title="Example ASM Program",
        author="alexeev-prog",
        filename="example.asm",
        mode="64",
    )
    asmprogram = ASMProgram(settings, __name__)
    regs = get_registers(settings.mode)

    start_lbl = Label("start")

    start_lbl.add_instruction(MovMnemonic(regs.AX, 4))
    start_lbl.add_instruction(MovMnemonic(regs.CX, "message"))
    start_lbl.add_instruction(MovMnemonic(regs.DX, "message_size"))
    start_lbl.add_instruction(IntMnemonic(LinuxInterrupts.SYSCALL))
    start_lbl.add_instruction(MovMnemonic(regs.AX, 1))
    start_lbl.add_instruction(XorMnemonic(regs.BX, regs.BX))
    start_lbl.add_instruction(IntMnemonic(LinuxInterrupts.SYSCALL))

    asmprogram.add_label(start_lbl)
    asmprogram.main_rws.add_string("message", "Hello, World!")

    asmprogram.save_code()
    # asmprogram.restore_backup()


if __name__ == "__main__":
    main()
