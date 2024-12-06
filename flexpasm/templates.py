from abc import ABC, abstractmethod


from flexpasm.instructions.registers import get_registers
from flexpasm.instructions.segments import ReadableWriteableSegment
from flexpasm.mnemonics.data import MovMnemonic
from flexpasm.mnemonics.io import IntMnemonic
from flexpasm.mnemonics.logical import XorMnemonic
from flexpasm.settings import LinuxInterrupts


class MnemonicTemplate(ABC):
	@abstractmethod
	def generate(self, syntax: str, indentation: str = "") -> str:
		raise NotImplementedError

	@abstractmethod
	def comment(self) -> str:
		raise NotImplementedError


class PrintStringTemplate(MnemonicTemplate):
	def __init__(self, string: str, var: str = "msg", entry: str = "print_string"):
		self.string = string
		self.var = var
		self.entry = entry

	def generate(self, mode: str, indentation: str = "\t") -> str:
		comment = self.comment()

		regs = get_registers(mode)

		rws = ReadableWriteableSegment(skip_title=True)

		rec = [
			MovMnemonic(regs.AX, 4).generate(),
			MovMnemonic(regs.CX, f"{self.var}").generate(),
			MovMnemonic(regs.DX, f"{self.var}_size").generate(),
			IntMnemonic(LinuxInterrupts.SYSCALL).generate(),
			MovMnemonic(regs.AX, 1).generate(),
			XorMnemonic(regs.BX, regs.BX).generate(),
			IntMnemonic(LinuxInterrupts.SYSCALL).generate(),
		]

		rws.add_string(f"{self.var}", self.string)

		title = f"; Using PrintStringTemplate: {comment} ;"

		text = (
			f"{';' * len(title)}\n{title}\n{';' * len(title)}\n\n{"\n".join(rec)}",
			f"{rws.generate()}",
		)

		return text

	def comment(self) -> str:
		return f"Printing the string '{self.string}' to stdout"
