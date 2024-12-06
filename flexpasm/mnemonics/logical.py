from typing import Union

from flexpasm.instructions.base import BaseRegister
from flexpasm.mnemonics.base import _DefaultMnemonic


class XorMnemonic(_DefaultMnemonic):
	def __init__(self, dest: BaseRegister, source: Union[BaseRegister, str, int]):
		super().__init__("XOR", dest, source)

	def comment(self) -> str:
		return f"Zeroing the {str(self.dest)} register using XOR"
