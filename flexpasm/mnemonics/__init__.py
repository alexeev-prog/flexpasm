from flexpasm.mnemonics.arithmetic import AddMnemonic, SubMnemonic
from flexpasm.mnemonics.data import MovMnemonic
from flexpasm.mnemonics.flow import JmpMnemonic
from flexpasm.mnemonics.io import IntMnemonic
from flexpasm.mnemonics.logical import XorMnemonic

all = [
	MovMnemonic,
	IntMnemonic,
	XorMnemonic,
	AddMnemonic,
	SubMnemonic,
	JmpMnemonic,
]
