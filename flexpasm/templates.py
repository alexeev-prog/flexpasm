from abc import ABC, abstractmethod
from flexpasm.instructions.base import BaseMnemonic
from flexpasm.settings import MnemonicSyntax


class MnemonicTemplate(ABC):
	@abstractmethod
	def generate(self, syntax: str, indentation: str = '') -> str:
		raise NotImplementedError

	@abstractmethod
	def comment(self) -> str:
		raise NotImplementedError


class PrintStringTemplate(MnemonicTemplate):
	def __init__(self, string: str):
		self.string = string

	def generate(self, syntax: str, indentation: str = '    ') -> str:
		comment = self.comment()

		if syntax == MnemonicSyntax.INTEL:
			return (
				'\n'
				f';;; PrintStringTemplate {self.string}: {comment} ;;;\n'
				f'segment readable executable\n'
				f'start:\n'
				f'{indentation}MOV eax, 4\n'
				f'{indentation}MOV ebx, 1\n'
				f'{indentation}MOV ecx, msg\n'
				f'{indentation}MOV edx, msg_size\n'
				f'{indentation}INT 0x80\n'
				'\n'
				f'{indentation}MOV eax, 1\n'
				f'{indentation}XOR ebx, ebx\n'
				f'{indentation}INT 0x80\n'
				'\n'
				f'segment readable writeable\n'
				f"msg db '{self.string}', 0xA\n"
				f'msg_size = $-msg\n'
			)

	def comment(self) -> str:
		return f"Printing the string '{self.string}' to stdout"
