from flexpasm.base import BaseRegister
from flexpasm.constants import MAX_MESSAGE_LENGTH
from flexpasm.mnemonics.base import _DefaultMnemonic
from flexpasm.rich_highlighter import Highlighter


class AddMnemonic(_DefaultMnemonic):
    """
    The ADD instruction in assembler performs the addition of two operands. A mandatory rule is that the operands
    are equal in size; only two 16-bit numbers or two 8-bit numbers can be added to each other.
    """

    def __init__(self, dest: BaseRegister, source: BaseRegister | str | int):
        super().__init__("ADD", dest, source)

    def comment(self) -> str:
        return f"Adding the {self.source!s} value to the {self.dest!s} register"


class SubMnemonic(_DefaultMnemonic):
    """
    The ASM sub mnemonic is a subtraction instruction. It subtracts the source operand from the destination
    operand and replaces the destination with the result.
    """

    def __init__(self, dest: BaseRegister, source: BaseRegister | str | int):
        super().__init__("SUB", dest, source)

    def comment(self) -> str:
        return f"Substracting the {self.source!s} value to the {self.dest!s} register"


class DivMnemonic(_DefaultMnemonic):
    """
    The ASM DIV mnemonic is a division instruction. It divise the source operand from the destination
    operand and replaces the destination with the result.
    """

    def __init__(self, dest: BaseRegister, source: BaseRegister | str | int):
        super().__init__("DIV", dest, source)

    def comment(self) -> str:
        return f"Divising the {self.source!s} value to the {self.dest!s} register"


class MulMnemonic(_DefaultMnemonic):
    """
    The ASM MUL mnemonic is a multiplication instruction. It multiplicates the source operand from the destination
    operand and replaces the destination with the result.
    """

    def __init__(self, dest: BaseRegister, source: BaseRegister | str | int):
        super().__init__("MUL", dest, source)

    def comment(self) -> str:
        return f"Multiplication the {self.source!s} value to the {self.dest!s} register"


class IncMnemonic(_DefaultMnemonic):
    """
    The ASM INC mnemonic is a increment instruction. It increments the register.
    """

    def __init__(self, dest: BaseRegister):
        super().__init__("INC", dest)

    def generate(self, indentation: str = ""):
        msg = f"{self.mnemonic_name} {self.dest!s}"
        Highlighter.highlight(
            f"{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}")
        return f'{indentation}{f"{self.mnemonic_name} {self.dest!s}".ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}'

    def comment(self) -> str:
        return f"Increment the {self.dest!s}"


class DecMnemonic(_DefaultMnemonic):
    """
    The ASM DEC mnemonic is a decrement instruction. It decrements the register.
    """

    def __init__(self, dest: BaseRegister):
        super().__init__("DEC", dest)

    def generate(self, indentation: str = ""):
        msg = f"{self.mnemonic_name} {self.dest!s}"
        Highlighter.highlight(
            f"{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}")
        return f'{indentation}{f"{self.mnemonic_name} {self.dest!s}".ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}'

    def comment(self) -> str:
        return f"Decrement the {self.dest!s}"
