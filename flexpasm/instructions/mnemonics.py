from enum import Enum
from typing import Union

from flexpasm.instructions.base import BaseMnemonic, BaseRegister
from flexpasm.settings import LinuxInterrupts, MnemonicSyntax


class MovMnemonic:
	"""
	MOV in assembly language is a command to move a value from a source to a destination. It copies the contents of
	the source and places that content into the destination.
	"""

	def __init__(self, dest: BaseRegister, source: Union[BaseRegister, str, int]):
		self.dest = dest.value
		self.source = source if not isinstance(source, Enum) else source.value

	def generate(self, syntax: MnemonicSyntax):
		if syntax == MnemonicSyntax.INTEL:
			return f"MOV {str(self.dest)}, {str(self.source)}	; {self.comment()}"

	def comment(self) -> str:
		return f"Loading {str(self.source)} value into {str(self.dest)} register."


class AddMnemonic(BaseMnemonic):
	"""
	The ADD instruction in assembler performs the addition of two operands. A mandatory rule is that the operands
	are equal in size; only two 16-bit numbers or two 8-bit numbers can be added to each other.
	"""

	def __init__(self, dest: BaseRegister, source: Union[BaseRegister, str, int]):
		self.dest = dest.value
		self.source = source if not isinstance(source, Enum) else source.value

	def generate(self, syntax: MnemonicSyntax) -> str:
		if syntax == MnemonicSyntax.INTEL:
			return f"ADD {str(self.dest)}, {str(self.source)}	 ; {self.comment()}"

	def comment(self) -> str:
		return f"Adding the {str(self.source)} value to the {str(self.dest)} register"


class IntMnemonic(BaseMnemonic):
	def __init__(self, interrupt_number: int | LinuxInterrupts):
		self.interrupt_number = interrupt_number
		self.additional_comments = None

		if isinstance(interrupt_number, LinuxInterrupts):
			self.interrupt_number = interrupt_number.value
			self.additional_comments = str(LinuxInterrupts(self.interrupt_number).name)

	def generate(self, syntax: MnemonicSyntax):
		if syntax == MnemonicSyntax.INTEL:
			return f"INT {self.interrupt_number}	; {self.comment()}"

	def comment(self) -> str:
		return (
			f"Call software interrupt {self.interrupt_number}"
			if self.additional_comments is None
			else f"Call software interrupt {self.interrupt_number}: {self.additional_comments}"
		)


class XorMnemonic(BaseMnemonic):
	def __init__(self, dest: BaseRegister, source: Union[str, int, BaseRegister]):
		self.dest = dest.value
		self.source = source if not isinstance(source, Enum) else source.value

	def generate(self, syntax: MnemonicSyntax) -> str:
		if syntax == MnemonicSyntax.INTEL:
			return f"XOR {str(self.dest)}, {str(self.source)}	 ; {self.comment()}"

	def comment(self) -> str:
		return f"Zeroing the {str(self.dest)} register using XOR"
