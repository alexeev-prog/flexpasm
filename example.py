from flexpasm.instructions.segments import Label
from flexpasm.mnemonics.flow import JmpMnemonic
from flexpasm.program import ASMProgram
from flexpasm.settings import Settings
from flexpasm.templates import PrintStringTemplate


def main():
	settings = Settings(
		title="Example ASM Program",
		author="alexeev-prog",
		filename="example.asm",
		mode="32",
	)
	asmprogram = ASMProgram(settings)

	pst = PrintStringTemplate("Hello, World!")
	pst2 = PrintStringTemplate("Hello, World!", "msg2", "print_string2")
	start_lbl = Label("start")

	start_lbl.add_command(
		JmpMnemonic("print_string"), 1, comment="Jump to print strint template"
	)

	asmprogram.add_label(start_lbl)
	asmprogram.add_template(pst)
	asmprogram.add_template(pst2)

	asmprogram.save_code()


if __name__ == "__main__":
	main()
