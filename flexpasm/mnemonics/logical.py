from typing import Union

from flexpasm.base import BaseRegister
from flexpasm.mnemonics.base import _DefaultMnemonic


class XorMnemonic(_DefaultMnemonic):
	"""
	XOR in assembly language is an instruction that performs an exclusive OR operation between all the bits of two
	operands. When performing an exclusive OR operation, the result value will be 1 if the bits being compared
	are different (not equal). If the compared bits have the same value, then the result will be 0.
	The command can be used to invert certain bits of the operand: those bits that are equal to 1 in the mask are
	inverted, the rest retain their value. The XOR operation is also often used to reset the contents of a
	register. For example:

	xor rax, rax; rax = 0
	"""

	def __init__(self, dest: BaseRegister, source: Union[BaseRegister, str, int]):
		super().__init__("XOR", dest, source)

	def comment(self) -> str:
		return (
			f"Exclusive OR operation {str(self.source)} and {str(self.dest)} using XOR"
		)
