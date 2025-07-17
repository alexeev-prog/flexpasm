from flexpasm.constants import MAX_MESSAGE_LENGTH, LinuxInterrupts
from flexpasm.mnemonics.base import _DefaultMnemonic
from flexpasm.rich_highlighter import Highlighter


class IntMnemonic(_DefaultMnemonic):
    """
    INT is an assembly language instruction for an x86 processor that generates a software interrupt. Instruction
    syntax: int n, where n is the number of the interrupt that will be generated. As a rule, the interrupt
    number is written as a hexadecimal number with the suffix h (from the English hexadecimal).
    """

    def __init__(self, interrupt_number: int | LinuxInterrupts):
        super().__init__("INT")
        self.interrupt_number = interrupt_number
        self.additional_comments = None

        if isinstance(interrupt_number, LinuxInterrupts):
            self.interrupt_number = interrupt_number.value
            self.additional_comments = str(
                LinuxInterrupts(self.interrupt_number).name)

    def generate(self, indentation: str = ""):
        msg = f"INT {self.interrupt_number}"
        Highlighter.highlight(
            f"{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}")
        return f'{indentation}{f"INT {self.interrupt_number!s}".ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}'

    def comment(self) -> str:
        return (
            f"Call software interrupt {self.interrupt_number}"
            if self.additional_comments is None
            else f"Call software interrupt {self.interrupt_number}: {self.additional_comments}"
        )


class IretMnemonic(_DefaultMnemonic):
    """
    Return from interrupt
    """

    def __init__(self):
        super().__init__("IRET")

    def generate(self, indentation: str = ""):
        msg = "IRET"
        Highlighter.highlight(
            f"{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}")
        return f"{indentation}{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}"

    def comment(self) -> str:
        return "Return from interrupt"


class SyscallMnemonic(_DefaultMnemonic):
    """
    SYSCALL is a mnemonic for the launch syscall in assembly language.
    """

    def __init__(self):
        super().__init__("SYSCALL")

    def generate(self, indentation: str = ""):
        msg = "SYSCALL"
        Highlighter.highlight(
            f"{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}")
        return f"{indentation}{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}"

    def comment(self) -> str:
        return "Launch system call"
