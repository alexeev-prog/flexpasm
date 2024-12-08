from typing import Union

from flexpasm.base import BaseRegister
from flexpasm.mnemonics.base import _DefaultMnemonic


class CmpMnemonic(_DefaultMnemonic):
	"""
	CMP is a mnemonic in assembly language for comparison
	"""

	def __init__(self, dest: BaseRegister, source: Union[BaseRegister, str, int]):
		super().__init__("CMP", dest, source)

	def comment(self) -> str:
		return f"Register comparison {str(self.source)} and {str(self.dest)} using CMP"


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


class AndMnemonic(_DefaultMnemonic):
	"""
	AND in assembly language is a mnemonic for the logical AND operation.
	"""

	def __init__(self, dest: BaseRegister, source: Union[BaseRegister, str, int]):
		super().__init__("AND", dest, source)

	def comment(self) -> str:
		return (
			f"Logical AND operation of register {str(self.source)} and {str(self.dest)}"
		)


class OrMnemonic(_DefaultMnemonic):
	"""
	OR in assembly language is a mnemonic for the logical OR operation.
	"""

	def __init__(self, dest: BaseRegister, source: Union[BaseRegister, str, int]):
		super().__init__("OR", dest, source)

	def comment(self) -> str:
		return (
			f"Logical OR operation of register {str(self.source)} and {str(self.dest)}"
		)


class NotMnemonic(_DefaultMnemonic):
	"""
	NOT in assembly language is a mnemonic for the logical NOT operation.
	"""

	def __init__(self, dest: BaseRegister):
		super().__init__("NOT", dest)

	def comment(self) -> str:
		return (
			f"Logical NOT operation of register {str(self.source)} and {str(self.dest)}"
		)
