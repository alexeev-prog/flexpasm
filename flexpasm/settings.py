from dataclasses import dataclass
from enum import Enum

MAX_MESSAGE_LENGTH = 48


class MnemonicSyntax(Enum):
	INTEL = "intel"


@dataclass
class Settings:
	title: str
	author: str
	filename: str
	mode: str = "64"
	start_entry: str = "start"
	indentation: str = "	"


class LinuxInterrupts(Enum):
	SYSCALL = 0x80
