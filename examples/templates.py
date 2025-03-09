from flexpasm.instructions.segments import Label
from flexpasm.mnemonics import JmpMnemonic
from flexpasm.program import ASMProgram
from flexpasm.settings import Settings
from flexpasm.templates import PrintStringTemplate


def main():
    settings = Settings(
        title="Example ASM Program with Templates",
        author="alexeev-prog",
        filename="example_templates.asm",
        mode="32",
    )
    asmprogram = ASMProgram(settings, __name__)

    pst = PrintStringTemplate("Hello, World!")
    pst2 = PrintStringTemplate("Hello, World!", var="msg2", entry="print_string2")
    start_lbl = Label("start")

    start_lbl.add_instruction(
        JmpMnemonic("print_string"), 1, comment="Jump to print strint template"
    )

    asmprogram.add_label(start_lbl)
    asmprogram.add_template(pst)
    asmprogram.add_template(pst2)

    asmprogram.save_code()


if __name__ == "__main__":
    main()
