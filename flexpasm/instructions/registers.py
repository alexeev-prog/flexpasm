from enum import Enum
from typing import Union

from flexpasm.base import BaseRegister


class Register16(BaseRegister):
	def __init__(self, name: str):
		self._name = name

	def __str__(self):
		return self._name


class Register32(BaseRegister):
	def __init__(self, name: str):
		self._name = name

	def __str__(self):
		return self._name


class Register64(BaseRegister):
	def __init__(self, name: str):
		self._name = name

	def __str__(self):
		return self._name


class Registers16(Enum):
	AX = Register16("AX")
	BX = Register16("BX")
	CX = Register16("CX")
	DX = Register16("DX")
	SP = Register16("SP")
	BP = Register16("BP")
	SI = Register16("SI")
	DI = Register16("DI")

	r10 = Register16("10")
	r8 = Register16("8")
	r9 = Register16("9")


class Registers32(Enum):
	AX = Register32("EAX")
	BX = Register32("EBX")
	CX = Register32("ECX")
	DX = Register32("EDX")
	SP = Register32("ESP")
	BP = Register32("EBP")
	SI = Register32("ESI")
	DI = Register32("EDI")

	r10 = Register32("e10")
	r8 = Register32("e8")
	r9 = Register32("e9")


class Registers64(Enum):
	AX = Register64("RAX")
	BX = Register64("RBX")
	CX = Register64("RCX")
	DX = Register64("RDX")
	SP = Register64("RSP")
	BP = Register64("RBP")
	SI = Register64("RSI")
	DI = Register64("RDI")

	r10 = Register64("r10")
	r8 = Register64("r8")
	r9 = Register64("r9")


def get_registers(mode: str) -> Union[Register16, Register32, Registers64]:
	if mode == "16":
		return Registers16
	elif mode == "32":
		return Registers32
	elif mode == "64":
		return Registers64
