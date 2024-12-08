from enum import Enum
from typing import Union

from flexpasm.base import BaseMnemonic, BaseRegister
from flexpasm.constants import MAX_MESSAGE_LENGTH
from flexpasm.rich_highlighter import Highlighter


class _DefaultMnemonic(BaseMnemonic):
	def __init__(
		self,
		mnemonic_name: str,
		dest: BaseRegister = None,
		source: Union[BaseRegister, str, int] = None,
	):
		self.mnemonic_name = mnemonic_name
		self.dest = dest.value if dest is not None else None
		self.source = source if not isinstance(source, Enum) else source.value

	def generate(self, indentation: str = ""):
		msg = f"{self.mnemonic_name} {str(self.dest)}, {str(self.source)}"
		Highlighter.highlight(f"{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}")
		return f"{indentation}{f'MOV {str(self.dest)}, {str(self.source)}'.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}"

	def comment(self) -> str:
		return f"{self.mnemonic_name.upper()} from {str(self.source)} into {str(self.dest)}."
