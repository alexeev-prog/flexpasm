from flexpasm.constants import MAX_MESSAGE_LENGTH
from flexpasm.instructions.segments import Label
from flexpasm.mnemonics.base import _DefaultMnemonic
from flexpasm.rich_highlighter import Highlighter


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
