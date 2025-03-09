from flexpasm import ASMProgram
from flexpasm.base import BaseMnemonic, MnemonicTemplate
from flexpasm.constants import LinuxInterrupts
from flexpasm.instructions.registers import get_registers
from flexpasm.instructions.segments import Label
from flexpasm.mnemonics import IntMnemonic, MovMnemonic, XorMnemonic
from flexpasm.utils import get_indentation_by_level


class ExitTemplateWithoutCode(MnemonicTemplate):
    def __init__(self, entry: str = "exit"):
        self.entry = entry
        self._additional_code = []

    def add_instruction(self, command: str | BaseMnemonic, indentation_level: int = 1):
        indentation = get_indentation_by_level(indentation_level)

        command = command.generate() if isinstance(command, BaseMnemonic) else command

        self._additional_code.append(f"{indentation}{command}")

    def get_label(self, mode: str, indentation_level: int = 1):
        regs = get_registers(mode)

        exit_lbl = Label(self.entry)

        exit_lbl.add_instruction(
            f"{get_indentation_by_level(indentation_level)}; {self.comment()}"
        )

        for command in self._additional_code:
            exit_lbl.add_instruction(command, indentation_level=indentation_level)

        exit_lbl.add_instruction(
            MovMnemonic(regs.AX, 60), indentation_level=indentation_level
        )
        exit_lbl.add_instruction(
            MovMnemonic(regs.DI, regs.DI), indentation_level=indentation_level
        )
        exit_lbl.add_instruction(
            IntMnemonic(LinuxInterrupts.SYSCALL), indentation_level=indentation_level
        )

        return exit_lbl

    def generate(
        self, program: ASMProgram, mode: str, indentation_level: int = 1
    ) -> str:
        exit_lbl = self.get_label(mode, indentation_level)

        program.add_label(exit_lbl)

    def comment(self) -> str:
        return "Exit without code"


class ExitTemplate(MnemonicTemplate):
    def __init__(self, exit_code: int = 0, entry: str = "exit"):
        self.entry = entry
        self.exit_code = exit_code
        self._additional_code = []

    def add_instruction(self, command: str | BaseMnemonic, indentation_level: int = 1):
        indentation = get_indentation_by_level(indentation_level)

        command = command.generate() if isinstance(command, BaseMnemonic) else command

        self._additional_code.append(f"{indentation}{command}")

    def get_label(self, mode: str, indentation_level: int = 1):
        regs = get_registers(mode)

        exit_lbl = Label(self.entry)

        exit_lbl.add_instruction(
            f"{get_indentation_by_level(indentation_level)}; {self.comment()}"
        )

        for command in self._additional_code:
            exit_lbl.add_instruction(command, indentation_level=indentation_level)

        exit_lbl.add_instruction(
            MovMnemonic(regs.AX, 1), indentation_level=indentation_level
        )
        exit_lbl.add_instruction(
            MovMnemonic(regs.BX, self.exit_code), indentation_level=indentation_level
        )
        exit_lbl.add_instruction(
            IntMnemonic(LinuxInterrupts.SYSCALL), indentation_level=indentation_level
        )

        return exit_lbl

    def generate(
        self, program: ASMProgram, mode: str, indentation_level: int = 1
    ) -> str:
        exit_lbl = self.get_label(mode, indentation_level)

        program.add_label(exit_lbl)

    def comment(self) -> str:
        return f"Exit with code {self.exit_code}"


class PrintStringTemplate(MnemonicTemplate):
    def __init__(self, string: str, var: str = "msg", entry: str = "print_string"):
        self.string = string
        self.var = var
        self.entry = entry

        self._additional_code = []

    def add_instruction(self, command: str | BaseMnemonic, indentation_level: int = 1):
        indentation = get_indentation_by_level(indentation_level)

        command = command.generate() if isinstance(command, BaseMnemonic) else command

        self._additional_code.append(f"{indentation}{command}")

    def get_label(self, mode: str, indentation_level: int = 1):
        regs = get_registers(mode)

        print_lbl = Label(self.entry)

        print_lbl.add_instruction(
            f"{get_indentation_by_level(indentation_level)}; {self.comment()}",
            indentation_level=indentation_level,
        )
        print_lbl.add_instruction(
            MovMnemonic(regs.AX, 4), indentation_level=indentation_level
        )
        print_lbl.add_instruction(
            MovMnemonic(regs.CX, self.var), indentation_level=indentation_level
        )
        print_lbl.add_instruction(
            MovMnemonic(regs.DX, f"{self.var}_size"),
            indentation_level=indentation_level,
        )
        print_lbl.add_instruction(
            IntMnemonic(LinuxInterrupts.SYSCALL), indentation_level=indentation_level
        )
        print_lbl.add_instruction(
            MovMnemonic(regs.AX, 1), indentation_level=indentation_level
        )
        print_lbl.add_instruction(
            XorMnemonic(regs.BX, regs.BX), indentation_level=indentation_level
        )
        print_lbl.add_instruction(
            IntMnemonic(LinuxInterrupts.SYSCALL), indentation_level=indentation_level
        )

        for command in self._additional_code:
            print_lbl.add_instruction(command)

        return print_lbl

    def generate(
        self, program: ASMProgram, mode: str, indentation_level: int = 1
    ) -> str:
        print_lbl = self.get_label(mode, indentation_level)

        program.add_label(print_lbl)
        program.main_rws.add_string(self.var, "Hello, World!")

    def comment(self) -> str:
        return f"Printing the string '{self.string}' to stdout"
