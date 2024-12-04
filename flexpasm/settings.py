from enum import Enum
from dataclasses import dataclass


class MnemonicSyntax(Enum):
	INTEL = 'intel'


@dataclass
class Settings:
	title: str
	author: str
	filename: str
	mnemonix_syntax: MnemonicSyntax = MnemonicSyntax.INTEL
	indentation: str = '    '
