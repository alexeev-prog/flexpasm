from flexpasm.base import BaseRegister
from flexpasm.mnemonics.base import _DefaultMnemonic


class ShlMnemonic(_DefaultMnemonic):
    def __init__(self, dest: BaseRegister):
        super().__init__("SHL", dest)

    def generate(self, indentation: str = ""):
        msg = f"SHL {self.dest!s}"
        Highlighter.highlight(
            f"{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}")
        return f"{indentation}{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}"

    def comment(self) -> str:
        return f"System call to shift left (SHL) register {self.dest!s}"


class ShrMnemonic(_DefaultMnemonic):
    def __init__(self, dest: BaseRegister):
        super().__init__("SHR", dest)

    def generate(self, indentation: str = ""):
        msg = f"SHR {self.dest()!s}"
        Highlighter.highlight(
            f"{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}")
        return f"{indentation}{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}"

    def comment(self) -> str:
        return f"System call to shift right (SHR) register {self.dest!s}"


class RorMnemonic(_DefaultMnemonic):
    def __init__(self, dest: BaseRegister):
        super().__init__("ROR", dest)

    def generate(self, indentation: str = ""):
        msg = f"ROR {self.dest()!s}"
        Highlighter.highlight(
            f"{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}")
        return f"{indentation}{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}"

    def comment(self) -> str:
        return f"System call to rotate right (ROR) register {self.dest!s}"


class RolMnemonic(_DefaultMnemonic):
    def __init__(self, dest: BaseRegister):
        super().__init__("ROL", dest)

    def generate(self, indentation: str = ""):
        msg = f"ROL {self.dest()!s}"
        Highlighter.highlight(
            f"{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}")
        return f"{indentation}{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}"

    def comment(self) -> str:
        return f"System call to rotate left (ROL) register {self.dest!s}"
