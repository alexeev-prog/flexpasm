from typing import Union

from flexpasm.base import BaseRegister
from flexpasm.mnemonics.base import _DefaultMnemonic


class AddMnemonic(_DefaultMnemonic):
	"""
	The ADD instruction in assembler performs the addition of two operands. A mandatory rule is that the operands
	are equal in size; only two 16-bit numbers or two 8-bit numbers can be added to each other.
	"""

	def __init__(self, dest: BaseRegister, source: Union[BaseRegister, str, int]):
		super().__init__("ADD", dest, source)

	def comment(self) -> str:
		return f"Adding the {str(self.source)} value to the {str(self.dest)} register"


class SubMnemonic(_DefaultMnemonic):
	"""
	The ASM sub mnemonic is a subtraction instruction. It subtracts the source operand from the destination
	operand and replaces the destination with the result.
	"""

	def __init__(self, dest: BaseRegister, source: Union[BaseRegister, str, int]):
		super().__init__("SUB", dest, source)

	def comment(self) -> str:
		return f"Substracting the {str(self.source)} value to the {str(self.dest)} register"
