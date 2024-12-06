from flexpasm.mnemonics.base import _DefaultMnemonic
from flexpasm.rich_highlighter import Highlighter
from flexpasm.settings import MAX_MESSAGE_LENGTH, LinuxInterrupts


class IntMnemonic(_DefaultMnemonic):
	def __init__(self, interrupt_number: int | LinuxInterrupts):
		super().__init__("INT")
		self.interrupt_number = interrupt_number
		self.additional_comments = None

		if isinstance(interrupt_number, LinuxInterrupts):
			self.interrupt_number = interrupt_number.value
			self.additional_comments = str(LinuxInterrupts(self.interrupt_number).name)

	def generate(self):
		msg = f"INT {self.interrupt_number}"
		Highlighter.highlight(f"{msg.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}")
		return f"{f'INT {str(self.interrupt_number)}'.ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}"

	def comment(self) -> str:
		return (
			f"Call software interrupt {self.interrupt_number}"
			if self.additional_comments is None
			else f"Call software interrupt {self.interrupt_number}: {self.additional_comments}"
		)
