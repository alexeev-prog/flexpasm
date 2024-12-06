from abc import ABC, abstractmethod
from enum import Enum
from typing import Union


from flexpasm.instructions.base import BaseRegister
from flexpasm.rich_highlighter import Highlighter
from flexpasm.settings import MAX_MESSAGE_LENGTH


class BaseMnemonic(ABC):
	@abstractmethod
	def generate(self) -> str:
		raise NotImplementedError

	@abstractmethod
	def comment(self) -> str:
		raise NotImplementedError


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

	def generate(self):
		msg = f"{self.mnemonic_name} {str(self.dest)}, {str(self.source)}"
		Highlighter.highlight(f"{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}")
		return f"{f'MOV {str(self.dest)}, {str(self.source)}'.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}"

	def comment(self) -> str:
		return f"{self.mnemonic_name.upper()} from {str(self.source)} into {str(self.dest)}."
