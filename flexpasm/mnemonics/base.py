from enum import Enum

from flexpasm.base import BaseMnemonic, BaseRegister
from flexpasm.constants import MAX_MESSAGE_LENGTH
from flexpasm.rich_highlighter import Highlighter


class _DefaultMnemonic(BaseMnemonic):
    def __init__(
        self,
        mnemonic_name: str,
        dest: BaseRegister | str | int = None,
        source: BaseRegister | str | int = None,
    ):
        self.mnemonic_name = mnemonic_name
        self.dest = str(dest) if not isinstance(dest, Enum) else dest.value
        self.source = str(source) if not isinstance(
            source, Enum) else source.value

    def generate(self, indentation: str = ""):
        msg = f"{self.mnemonic_name} {self.dest!s}, {self.source!s}"
        Highlighter.highlight(
            f"{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}")
        return f'{indentation}{f"{self.mnemonic_name} {self.dest!s}, {self.source!s}".ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}'

    def comment(self) -> str:
        return f"{self.mnemonic_name.upper()} from {self.source!s} into {self.dest!s}."
