from abc import ABC, abstractmethod

from flexpasm.settings import MnemonicSyntax


class BaseSegment(ABC):
	@abstractmethod
	def generate(self) -> str:
		raise NotImplementedError

	@abstractmethod
	def comment(self) -> str:
		raise NotImplementedError


class ReadableExecutableSegment(BaseSegment):
	def __init__(self, entry: str):
		self.labels = {}

		self._code = [
			f";; {self.comment()}",
			"segment readable executable",
		]

	def set_commands_for_label(
		self, label: str, commands: list, indentation: str = "	  "
	):
		result = ""

		for command in commands:
			result += f"{indentation}{command}\n"

		self.labels[label] = result

	def add_command_to_label(
		self,
		label: str,
		command: str,
		syntax: MnemonicSyntax,
		indentation: str = "	",
	):
		if label not in self.labels:
			raise ValueError(f'Label "{label}" not found')
		else:
			self.labels[label] += f"\n{indentation}{command}"

	def generate(self) -> str:
		for label_name, commands in self.labels.items():
			self._code.append(f"{label_name}:")
			self._code.append(f"{commands}")

		return "\n".join(self._code)

	def comment(self) -> str:
		return "Segment readable executable in FASM is a directive for defining a section of code with readable and executable attributes."


class ReadableWriteableSegment(BaseSegment):
	def __init__(self):
		self._code = [f";; {self.comment()}", "segment readable writeable"]

	def add_commands(self, commands: list):
		self._code += commands

	def add_string(self, var_name: str, string: str):
		self._code += [
			f"{var_name} db '{string}', 0xA\n",
			f"{var_name}_size = $-{var_name}\n",
		]

	def generate(self) -> str:
		return "\n".join(self._code)

	def comment(self) -> str:
		return "Segment readable writeable in FASM is a definition of a segment of program data codes, where the attributes readable (the contents of the segment can be read) and writeable (program commands can both read codes and change their values) are specified for it."
