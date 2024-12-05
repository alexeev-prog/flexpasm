from abc import ABC, abstractmethod

from flexpasm.instructions.mnemonics import IntMnemonic, MovMnemonic, XorMnemonic
from flexpasm.instructions.registers import get_registers
from flexpasm.instructions.segments import (
	ReadableExecutableSegment,
	ReadableWriteableSegment,
)
from flexpasm.settings import LinuxInterrupts, MnemonicSyntax


class MnemonicTemplate(ABC):
	@abstractmethod
	def generate(self, syntax: str, indentation: str = "") -> str:
		raise NotImplementedError

	@abstractmethod
	def comment(self) -> str:
		raise NotImplementedError


class PrintStringTemplate(MnemonicTemplate):
	def __init__(self, string: str, entry: str = "start"):
		self.string = string
		self.entry = entry

	def generate(
		self, mode: str, syntax: MnemonicSyntax, indentation: str = "	 "
	) -> str:
		comment = self.comment()

		regs = get_registers(mode)

		rec = ReadableExecutableSegment(self.entry)
		rws = ReadableWriteableSegment()

		if syntax == MnemonicSyntax.INTEL:
			rec.set_commands_for_label(
				self.entry,
				[
					MovMnemonic(regs.AX, 4).generate(syntax),
					MovMnemonic(regs.CX, "msg").generate(syntax),
					MovMnemonic(regs.DX, "msg_size").generate(syntax),
					IntMnemonic(LinuxInterrupts.SYSCALL).generate(syntax),
					MovMnemonic(regs.AX, 1).generate(syntax),
					XorMnemonic(regs.BX, regs.BX).generate(syntax),
					IntMnemonic(LinuxInterrupts.SYSCALL).generate(syntax),
				],
				indentation=indentation,
			)

			rws.add_string("msg", self.string)

			title = f"; Using PrintStringTemplate: {comment} ;"

			return (
				f"\n{';' * len(title)}\n{title}\n{';' * len(title)}\n"
				f"\n"
				f"{rec.generate()}\n"
				"\n"
				f"{rws.generate()}\n"
			)

	def comment(self) -> str:
		return f"Printing the string '{self.string}' to stdout"
