from flexpasm.constants import MAX_MESSAGE_LENGTH
from flexpasm.instructions.segments import Label
from flexpasm.mnemonics.base import _DefaultMnemonic
from flexpasm.rich_highlighter import Highlighter

# je jne jg jl call ret


class JmpMnemonic(_DefaultMnemonic):
	"""
	JMP (short for "Jump") is an x86 assembly instruction that is used to jump to a specific address in code. This
	instruction changes the program's control flow by jumping to the specified location instead of the next
	instruction. After executing a JMP, the next instruction the processor will execute will be at the address
	specified in the JMP.
	"""

	def __init__(self, label: str | Label):
		super().__init__("JMP")

		self.label = label.entry if isinstance(label, Label) else label

	def generate(self, indentation: str = ""):
		msg = f"JMP {self.label}"
		Highlighter.highlight(f"{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}")
		return f"{indentation}{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}"

	def comment(self) -> str:
		return f"Unconditional jump to label {self.label}"


class JeMnemonic(_DefaultMnemonic):
	"""
	JE is an assembler mnemonic (instruction) that jumps if the first operand is equal to the second when performing a comparison operation using the CMP instruction.
	"""

	def __init__(self, label: str | Label):
		super().__init__("JE")

		self.label = label.entry if isinstance(label, Label) else label

	def generate(self, indentation: str = ""):
		msg = f"JE {self.label}"
		Highlighter.highlight(f"{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}")
		return f"{indentation}{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}"

	def comment(self) -> str:
		return f"Conditional (comparison is equal) jump to label {self.label}"


class JneMnemonic(_DefaultMnemonic):
	"""
	JNE in assembly language is a mnemonic for a conditional jump instruction that tests the condition ZF == 0 and jumps if both operands are NOT equal.
	"""

	def __init__(self, label: str | Label):
		super().__init__("JNE")

		self.label = label.entry if isinstance(label, Label) else label

	def generate(self, indentation: str = ""):
		msg = f"JNE {self.label}"
		Highlighter.highlight(f"{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}")
		return f"{indentation}{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}"

	def comment(self) -> str:
		return f"Conditional (comparison is not equal) jump to label {self.label}"


class JgMnemonic(_DefaultMnemonic):
	"""
	JG in assembly language mnemonics is a conditional jump instruction that jumps if the first operand is greater than the second (both operands are signed).
	"""

	def __init__(self, label: str | Label):
		super().__init__("JG")

		self.label = label.entry if isinstance(label, Label) else label

	def generate(self, indentation: str = ""):
		msg = f"JG {self.label}"
		Highlighter.highlight(f"{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}")
		return f"{indentation}{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}"

	def comment(self) -> str:
		return f"Go to label {self.label} if comparison yields more"


class JLMnemonic(_DefaultMnemonic):
	"""
	JL in assembly language mnemonics is a conditional jump instruction that jumps if the first operand is less than the second (both operands are signed).
	"""

	def __init__(self, label: str | Label):
		super().__init__("JL")

		self.label = label.entry if isinstance(label, Label) else label

	def generate(self, indentation: str = ""):
		msg = f"JL {self.label}"
		Highlighter.highlight(f"{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}")
		return f"{indentation}{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}"

	def comment(self) -> str:
		return f"Go to label {self.label} if comparison yields less"


class JgeMnemonic(_DefaultMnemonic):
	"""
	JGE in assembly language is a conditional jump instruction that jumps if the first operand is greater than or equal to the second when performing a comparison operation using the CMP instruction.
	"""

	def __init__(self, label: str | Label):
		super().__init__("JGE")

		self.label = label.entry if isinstance(label, Label) else label

	def generate(self, indentation: str = ""):
		msg = f"JGE {self.label}"
		Highlighter.highlight(f"{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}")
		return f"{indentation}{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}"

	def comment(self) -> str:
		return f"Conditional (comparison is equal or bigger) jump to label {self.label}"


class JleMnemonic(_DefaultMnemonic):
	"""
	JGE in assembly language is a conditional jump instruction that jumps if the first operand is less than or equal to the second when performing a comparison operation using the CMP instruction.
	"""

	def __init__(self, label: str | Label):
		super().__init__("JLE")

		self.label = label.entry if isinstance(label, Label) else label

	def generate(self, indentation: str = ""):
		msg = f"JLE {self.label}"
		Highlighter.highlight(f"{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}")
		return f"{indentation}{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}"

	def comment(self) -> str:
		return f"Conditional (comparison is equal or less) jump to label {self.label}"


class CallMnemonic(_DefaultMnemonic):
	"""
	CALL is a mnemonic for the command to call a subroutine in assembly language.
	"""

	def __init__(self, label: str | Label):
		super().__init__("CALL")

		self.label = label.entry if isinstance(label, Label) else label

	def generate(self, indentation: str = ""):
		msg = f"CALL {self.label}"
		Highlighter.highlight(f"{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}")
		return f"{indentation}{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}"

	def comment(self) -> str:
		return f"Call: {self.label}"


class RetMnemonic(_DefaultMnemonic):
	"""
	RET is a mnemonic for the return command from a subroutine in assembly language.
	"""

	def __init__(self):
		super().__init__("RET")

	def generate(self, indentation: str = ""):
		msg = "RET"
		Highlighter.highlight(f"{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}")
		return f"{indentation}{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}"

	def comment(self) -> str:
		return "Return from procedure"
