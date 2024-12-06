from flexpasm.instructions.segments import Label
from flexpasm.mnemonics.base import _DefaultMnemonic
from flexpasm.rich_highlighter import Highlighter
from flexpasm.settings import MAX_MESSAGE_LENGTH


class JmpMnemonic(_DefaultMnemonic):
	def __init__(self, label: str | Label):
		super().__init__("JMP")

		self.label = label.entry if isinstance(label, Label) else label

	def generate(self):
		msg = f"JMP {self.label}"
		Highlighter.highlight(f"{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}")
		return f"{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}"

	def comment(self) -> str:
		return f"Unconditional jump to label {self.label}"
