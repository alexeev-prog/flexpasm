from abc import ABC, abstractmethod

from flexpasm.base import BaseMnemonic
from flexpasm.constants import MAX_MESSAGE_LENGTH
from flexpasm.utils import get_indentation_by_level


class BaseSegment(ABC):
    @abstractmethod
    def comment(self) -> str:
        raise NotImplementedError

    def generate(self) -> str:
        return "\n".join(self._code)


class Label(BaseSegment):
    def __init__(self, entry: str):
        self.entry = entry
        self.commands = []

    def add_instruction(
        self,
        command: str | BaseMnemonic,
        indentation_level: int = 1,
        comment: str = None,
    ):
        indentation = get_indentation_by_level(indentation_level)

        command = (
            command.generate(indentation)
            if isinstance(command, BaseMnemonic)
            else command
        )

        if comment is None:
            self.commands.append(f"{command}")
        else:
            self.commands.append(f"{command.ljust(MAX_MESSAGE_LENGTH)}; {comment}")

    def add_instructions(
        self, commands: list, indentation_level: int = 1, comment: str | list = None
    ):
        indentation = get_indentation_by_level(indentation_level)

        single_comment = False

        if isinstance(comment, str):
            single_comment = True

        for command_index, command in enumerate(commands):
            command_code = (
                command.generate(indentation)
                if isinstance(command, BaseMnemonic)
                else command
            )

            if single_comment:
                self.commands.append(
                    f"{command_code.ljust(MAX_MESSAGE_LENGTH)}; {comment}"
                )
            else:
                command_comment = (
                    True
                    if comment is not None and len(comment) >= command_index
                    else False
                )

                if command_comment:
                    self.commands.append(
                        f"{command_code.ljust(MAX_MESSAGE_LENGTH)}; {comment[command_index]}"
                    )
                else:
                    self.commands.append(command_code)

    def generate(self, indentation: str = "") -> str:
        code = "\n".join([f"{indentation}{command}" for command in self.commands])
        return code

    def comment(self) -> str:
        commands = [
            command
            for command in self.commands
            if not command.replace("\t", "").startswith(";")
            and len(command.replace("\t", "")) > 1
        ]
        return f"Label {self.entry} with {len(commands)} commands"


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
        self,
        label: str | Label,
        commands: list | str,
        indentation_level: int = 0,
    ):
        indentation = get_indentation_by_level(indentation_level)

        if isinstance(label, str):
            label = Label(label)
            label.add_instructions(commands)

        result = ""

        if isinstance(commands, list):
            for command in commands:
                result += f"{indentation}{command}\n"
        else:
            result = commands

        self.labels[label] = result

    def add_instruction_to_label(
        self,
        label: str | Label,
        command: str | BaseMnemonic,
        indentation_level: int = 0,
    ):
        indentation = get_indentation_by_level(indentation_level)

        command = (
            command.generate(indentation)
            if isinstance(command, BaseMnemonic)
            else command
        )

        if isinstance(label, str):
            label = Label(label)
            label.add_instruction(command)

        if label not in self.labels:
            raise ValueError(f'Label "{label}" not found')
        self.labels[label] += f"\n{indentation}{command}"

    def generate(self) -> str:
        for label, commands in self.labels.items():
            self._code.append(
                f'{f"{label.entry}:".ljust(MAX_MESSAGE_LENGTH)}; {label.comment()}'
            )
            self._code.append(f"{commands}")

        return "\n".join(self._code)

    def comment(self) -> str:
        return "Segment readable executable in FASM is a directive for defining a section of code with readable and executable attributes."


class ReadableWriteableSegment(BaseSegment):
    def __init__(self, skip_title: bool = False):
        self.skip_title = skip_title
        self._code = [f"\n;; {self.comment()}", "segment readable writeable\n"]

        self.strings = {}

        if self.skip_title:
            self._code = []

    @property
    def code(self):
        return self._code

    def add_instruction(
        self,
        command: str | BaseMnemonic,
        indentation_level: int = 0,
    ):
        indentation = get_indentation_by_level(indentation_level)

        command = (
            command.generate(indentation)
            if isinstance(command, BaseMnemonic)
            else command
        )

        self._code.append(f"{indentation}{command}")

    def add_instructions(self, commands: list):
        self._code += commands

    def add_string(self, var_name: str, string: str, var_size_postfix: str = "_size"):
        var = f"{var_name} db '{string}', 0"
        var_size = f"{var_name}{var_size_postfix} = $-{var_name}"
        self._code += [
            f"{var.ljust(MAX_MESSAGE_LENGTH)}; Var {var_name} (string)",
            f"{var_size.ljust(MAX_MESSAGE_LENGTH)}; Var {var_name} (string) length\n",
        ]

    def comment(self) -> str:
        return "Segment readable writeable in FASM is a definition of a segment of program data codes, where the attributes readable (the contents of the segment can be read) and writeable (program commands can both read codes and change their values) are specified for it."
