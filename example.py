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

	asmprogram.add_template(pst)

	asmprogram.save_code()


if __name__ == "__main__":
	main()
