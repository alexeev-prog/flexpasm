from dataclasses import dataclass
from enum import Enum


class MnemonicSyntax(Enum):
	INTEL = "intel"


@dataclass
class Settings:
	title: str
	author: str
	filename: str
	mode: str = "64"
	start_entry: str = "start"
	mnemonix_syntax: MnemonicSyntax = MnemonicSyntax.INTEL
	indentation: str = "	"


class LinuxInterrupts(Enum):
	SYSCALL = 0x80
