from flexpasm.base import BaseRegister
from flexpasm.mnemonics.base import _DefaultMnemonic


class ShlMnemonic(_DefaultMnemonic):
    def __init__(self, dest: BaseRegister):
        super().__init__("SHL", dest)

    def generate(self, indentation: str = ""):
        msg = f"SHL {str(self.dest)}"
        Highlighter.highlight(f"{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}")
        return f"{indentation}{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}"

    def comment(self) -> str:
        return f"System call to shift left (SHL) register {str(self.dest)}"


class ShrMnemonic(_DefaultMnemonic):
    def __init__(self, dest: BaseRegister):
        super().__init__("SHR", dest)

    def generate(self, indentation: str = ""):
        msg = f"SHR {str(self.dest())}"
        Highlighter.highlight(f"{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}")
        return f"{indentation}{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}"

    def comment(self) -> str:
        return f"System call to shift right (SHR) register {str(self.dest)}"


class RorMnemonic(_DefaultMnemonic):
    def __init__(self, dest: BaseRegister):
        super().__init__("ROR", dest)

    def generate(self, indentation: str = ""):
        msg = f"ROR {str(self.dest())}"
        Highlighter.highlight(f"{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}")
        return f"{indentation}{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}"

    def comment(self) -> str:
        return f"System call to rotate right (ROR) register {str(self.dest)}"


class RolMnemonic(_DefaultMnemonic):
    def __init__(self, dest: BaseRegister):
        super().__init__("ROL", dest)

    def generate(self, indentation: str = ""):
        msg = f"ROL {str(self.dest())}"
        Highlighter.highlight(f"{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}")
        return f"{indentation}{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}"

    def comment(self) -> str:
        return f"System call to rotate left (ROL) register {str(self.dest)}"
