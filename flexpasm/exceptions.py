class FlexPasmException(Exception):
	def __init__(self, *args):
		if args:
			self.message = args[0]
		else:
			self.message = None

	def get_explanation(self) -> str:
		return f"Message: {self.message if self.message else 'missing'}"

	def __str__(self):
		return f"FlexPasmException has been raised. {self.get_explanation()}"


class BackupError(FlexPasmException):
	def get_explanation(self) -> str:
		return f"FlexPASM Backup System Error. Message: {self.message if self.message else 'missing'}"
