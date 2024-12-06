from rich import print
from rich.syntax import Syntax


class Highlighter:
	@staticmethod
	def highlight(text: str) -> str:
		highlighted_text = Syntax(text, "asm", theme="ansi_dark")

		print(highlighted_text)
