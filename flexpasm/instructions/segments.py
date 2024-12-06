from abc import ABC, abstractmethod


from flexpasm.mnemonics.base import BaseMnemonic
from flexpasm.settings import MAX_MESSAGE_LENGTH


class BaseSegment(ABC):
	@abstractmethod
	def comment(self) -> str:
		raise NotImplementedError

	def generate(self) -> str:
		return "\n".join(self._code)


class Label(BaseSegment):
	def __init__(self, entry: str, commands: list = []):
		self.entry = entry
		self.commands = commands

	def add_command(
		self,
		command: str | BaseMnemonic,
		indentation_level: int = 0,
		comment: str = None,
	):
		if indentation_level == 0:
			indentation = ""
		else:
			indentation = "\t" * indentation_level

		command = command.generate() if isinstance(command, BaseMnemonic) else command

		if comment is None:
			self.commands.append(f"{indentation}{command}")
		else:
			self.commands.append(
				f'{indentation}{f"{command}".ljust(MAX_MESSAGE_LENGTH)}; {comment}'
			)

	def add_commands(self, commands: list):
		self.commands += commands

	def generate(self) -> str:
		code = f'{f"{self.entry}:".ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}:\n{"\n".join(self.commands)}'
		return code

	def comment(self) -> str:
		return f"Label {self.entry} with {len(self.commands)} commands"


class ReadableExecutableSegment(BaseSegment):
	def __init__(self, skip_title: bool = False):
		self.labels = {}
		self.skip_title = skip_title

		self._code = [
			f"\n;; {self.comment()}",
			"segment readable executable\n",
		]

		if self.skip_title:
			self._code = []

	@property
	def code(self):
		return self._code

	def set_commands_for_label(
		self, label: str, commands: list, indentation: str = "\t"
	):
		result = ""

		for command in commands:
			result += f"{indentation}{command}\n"

		self.labels[label] = result

	def add_command_to_label(
		self,
		label: str,
		command: str | BaseMnemonic,
		indentation_level: int = 0,
	):
		command = command.generate() if isinstance(command, BaseMnemonic) else command

		if indentation_level == 0:
			indentation = ""
		else:
			indentation = "\t" * indentation_level

		if label not in self.labels:
			raise ValueError(f'Label "{label}" not found')
		else:
			self.labels[label] += f"\n{indentation}{command}"

	def generate(self) -> str:
		for label_name, commands in self.labels.items():
			self._code.append(
				f'{f"{label_name}:".ljust(MAX_MESSAGE_LENGTH)}; {self.comment()}'
			)
			self._code.append(f"{commands}")

		return "\n".join(self._code)

	def comment(self) -> str:
		return "Segment readable executable in FASM is a directive for defining a section of code with readable and executable attributes."


class ReadableWriteableSegment(BaseSegment):
	def __init__(self, skip_title: bool = False):
		self.skip_title = skip_title
		self._code = [f"\n;; {self.comment()}", "segment readable writeable\n"]

		if self.skip_title:
			self._code = []

	@property
	def code(self):
		return self._code

	def add_command(
		self,
		command: str | BaseMnemonic,
		indentation_level: int = 0,
	):
		command = command.generate() if isinstance(command, BaseMnemonic) else command

		if indentation_level == 0:
			indentation = ""
		else:
			indentation = "\t" * indentation_level

		self._code.append(f"{indentation}{command}")

	def add_commands(self, commands: list):
		self._code += commands

	def add_string(self, var_name: str, string: str):
		var = f"{var_name} db '{string}', 0xA"
		var_size = f"{var_name}_size = $-{var_name}"
		self._code += [
			f"{var.ljust(MAX_MESSAGE_LENGTH)}; Var {var_name} (string)",
			f"{var_size.ljust(MAX_MESSAGE_LENGTH)}; Var {var_name} (string) length\n",
		]

	def comment(self) -> str:
		return "Segment readable writeable in FASM is a definition of a segment of program data codes, where the attributes readable (the contents of the segment can be read) and writeable (program commands can both read codes and change their values) are specified for it."
