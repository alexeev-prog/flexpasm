from flexpasm import ASMProgram
from flexpasm.base import BaseMnemonic, MnemonicTemplate
from flexpasm.constants import LinuxInterrupts
from flexpasm.instructions.registers import get_registers
from flexpasm.instructions.segments import Label
from flexpasm.mnemonics import IntMnemonic, MovMnemonic, XorMnemonic
from flexpasm.utils import get_indentation_by_level


class PrintStringTemplate(MnemonicTemplate):
	def __init__(self, string: str, var: str = "msg", entry: str = "print_string"):
		self.string = string
		self.var = var
		self.entry = entry

		self._additional_code = []

	def add_instruction(self, command: str | BaseMnemonic, indentation_level: int = 1):
		indentation = get_indentation_by_level(indentation_level)

		command = command.generate() if isinstance(command, BaseMnemonic) else command

		self._additional_code.append(f"{indentation}{command}")

	def generate(
		self, program: ASMProgram, mode: str, indentation_level: int = 0
	) -> str:
		regs = get_registers(mode)

		print_lbl = Label(self.entry, [])

		print_lbl.add_instruction(MovMnemonic(regs.AX, 4), indentation_level)
		print_lbl.add_instruction(MovMnemonic(regs.CX, self.var), indentation_level)
		print_lbl.add_instruction(
			MovMnemonic(regs.DX, f"{self.var}_size"), indentation_level
		)
		print_lbl.add_instruction(
			IntMnemonic(LinuxInterrupts.SYSCALL), indentation_level
		)
		print_lbl.add_instruction(MovMnemonic(regs.AX, 1), indentation_level)
		print_lbl.add_instruction(XorMnemonic(regs.BX, regs.BX), indentation_level)
		print_lbl.add_instruction(
			IntMnemonic(LinuxInterrupts.SYSCALL), indentation_level
		)

		for command in self._additional_code:
			print_lbl.add_instruction(command)

		program.add_label(print_lbl)
		program.main_rws.add_string("message", "Hello, World!")

	def comment(self) -> str:
		return f"Printing the string '{self.string}' to stdout"
