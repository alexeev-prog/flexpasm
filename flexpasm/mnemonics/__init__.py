from flexpasm.mnemonics.arithmetic import (
	AddMnemonic,
	DecMnemonic,
	DivMnemonic,
	IncMnemonic,
	MulMnemonic,
	SubMnemonic,
)
from flexpasm.mnemonics.bitshift import (
	RolMnemonic,
	RorMnemonic,
	ShlMnemonic,
	ShrMnemonic,
)
from flexpasm.mnemonics.data import (
	MovMnemonic,
	PopMnemonic,
	PushMnemonic,
	SwapMnemonic,
	XchgMnemonic,
)
from flexpasm.mnemonics.flow import (
	CallMnemonic,
	JeMnemonic,
	JgeMnemonic,
	JgMnemonic,
	JleMnemonic,
	JLMnemonic,
	JmpMnemonic,
	JneMnemonic,
	RetMnemonic,
)
from flexpasm.mnemonics.io import IntMnemonic, IretMnemonic
from flexpasm.mnemonics.logical import (
	AndMnemonic,
	CmpMnemonic,
	NotMnemonic,
	OrMnemonic,
	XorMnemonic,
)

all = [
	MovMnemonic,
	IntMnemonic,
	XorMnemonic,
	AddMnemonic,
	SubMnemonic,
	JmpMnemonic,
	IncMnemonic,
	MulMnemonic,
	DecMnemonic,
	ShrMnemonic,
	RorMnemonic,
	RolMnemonic,
	AndMnemonic,
	OrMnemonic,
	NotMnemonic,
	DivMnemonic,
	JeMnemonic,
	JneMnemonic,
	JgMnemonic,
	JLMnemonic,
	JgeMnemonic,
	JleMnemonic,
	CallMnemonic,
	RetMnemonic,
	PushMnemonic,
	PopMnemonic,
	XchgMnemonic,
	SwapMnemonic,
	IretMnemonic,
	CmpMnemonic,
]
