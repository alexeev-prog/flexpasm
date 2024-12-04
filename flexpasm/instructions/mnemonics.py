from flexpasm.instructions.base import BaseMnemonic, BaseRegister
from flexpasm.settings import MnemonicSyntax


class MovMnemonic:
	"""
	MOV in assembly language is a command to move a value from a source to a destination. It copies the contents of
	the source and places that content into the destination.
	"""

	def __init__(self, dest: BaseRegister, source: str):
		self.dest = dest
		self.source = source

	def generate(self, syntax: MnemonicSyntax, indentation: str = ''):
		if syntax == MnemonicSyntax.INTEL:
			return f'{indentation}MOV {str(self.dest)} {str(self.source)}'

	def comment(self) -> str:
		return f'Loading {str(self.source)} value into {str(self.dest)} register.'


class AddMnemonic(BaseMnemonic):
	"""
	The ADD instruction in assembler performs the addition of two operands. A mandatory rule is that the operands
	are equal in size; only two 16-bit numbers or two 8-bit numbers can be added to each other.
	"""

	def __init__(self, dest: BaseRegister, source: str):
		self.dest = dest
		self.source = source

	def generate(self, syntax: MnemonicSyntax, indentation: str = '') -> str:
		if syntax == MnemonicSyntax.INTEL:
			return f'{indentation}ADD {str(self.dest)}, {str(self.source)}'

	def comment(self) -> str:
		return f'Adding the {str(self.source)} value to the {str(self.dest)} register'

