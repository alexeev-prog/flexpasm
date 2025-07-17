from flexpasm.base import BaseRegister
from flexpasm.constants import MAX_MESSAGE_LENGTH
from flexpasm.mnemonics.base import _DefaultMnemonic
from flexpasm.rich_highlighter import Highlighter

# push pop push XCHG SWAP


class MovMnemonic(_DefaultMnemonic):
    """
    MOV in assembly language is a command to move a value from a source to a destination. It copies the contents of
    the source and places that content into the destination.
    """

    def __init__(self, dest: BaseRegister, source: BaseRegister | str | int):
        super().__init__("MOV", dest, source)

    def comment(self) -> str:
        return f"Loading {self.source!s} value into {self.dest!s} register."


class PushaMnemonic(_DefaultMnemonic):
    """
    PUSHA is mnemonic for save registers
    """

    def __init__(self):
        super().__init__("PUSHA")

    def generate(self, indentation: str = ""):
        msg = "PUSHA"
        Highlighter.highlight(f"{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}")
        return f"{indentation}{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}"

    def comment(self) -> str:
        return "Saving registers"


class PopaMnemonic(_DefaultMnemonic):
    """
    POPA is mnemonic for comeback registers
    """

    def __init__(self):
        super().__init__("POPA")

    def generate(self, indentation: str = ""):
        msg = "POPA"
        Highlighter.highlight(f"{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}")
        return f"{indentation}{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}"

    def comment(self) -> str:
        return "Back registers"


class PopMnemonic(_DefaultMnemonic):
    """
    POP is an assembler mnemonic for popping a value from the stack.
    """

    def __init__(self, source: BaseRegister | str):
        super().__init__("POP", source=source)

    def generate(self, indentation: str = ""):
        msg = f"POP {self.source}"
        Highlighter.highlight(f"{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}")
        return f"{indentation}{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}"

    def comment(self) -> str:
        return f"Popping {self.source!s} from the stack"


class PushMnemonic(_DefaultMnemonic):
    """
    PUSH is an assembler mnemonic for pushing a value from the stack.
    """

    def __init__(self, source: BaseRegister | str):
        super().__init__("PUSH", source=source)

    def generate(self, indentation: str = ""):
        msg = f"PUSH {self.source}"
        Highlighter.highlight(f"{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}")
        return f"{indentation}{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}"

    def comment(self) -> str:
        return f"Pushing {self.source!s} into the stack"


class XchgMnemonic(_DefaultMnemonic):
    """
    XCHG in assembly language is a mnemonic: Exchange of values between cells (registers)
    """

    def __init__(self, dest: BaseRegister, source: BaseRegister | str | int):
        super().__init__("XCHG", dest, source)

    def comment(self) -> str:
        return f"Exchange values between {self.source!s} and {self.dest!s} registers."


class SwapMnemonic(_DefaultMnemonic):
    """
    SWAP mnemonic in assembly language: Swapping top stack elements
    """

    def __init__(self):
        super().__init__("SWAP")

    def generate(self, indentation: str = ""):
        msg = "SWAP"
        Highlighter.highlight(f"{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}")
        return f"{indentation}{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}"

    def comment(self) -> str:
        return "Swapping top stack elements"
