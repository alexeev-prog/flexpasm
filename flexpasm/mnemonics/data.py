from typing import Union

from flexpasm.base import BaseRegister
from flexpasm.mnemonics.base import _DefaultMnemonic


class MovMnemonic(_DefaultMnemonic):
	"""
	MOV in assembly language is a command to move a value from a source to a destination. It copies the contents of
	the source and places that content into the destination.
	"""

	def __init__(self, dest: BaseRegister, source: Union[BaseRegister, str, int]):
		super().__init__("MOV", dest, source)

	def comment(self) -> str:
		return f"Loading {str(self.source)} value into {str(self.dest)} register."
