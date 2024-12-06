# flexpasm
<a id="readme-top"></a> 

<div align="center">  
  <p align="center">
    Python library for writing assembly code through object abstractions. For Linux FASM.
    <br />
    <a href="./docs/en/index.md"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="#getting-started">Getting Started</a>
    ·
    <a href="#usage-examples">Basic Usage</a>
    ·
    <a href="https://github.com/alexeev-prog/flexpasm/blob/main/LICENSE">License</a>
  </p>
</div>
<br>
<p align="center">
    <img src="https://img.shields.io/github/languages/top/alexeev-prog/flexpasm?style=for-the-badge">
    <img src="https://img.shields.io/github/languages/count/alexeev-prog/flexpasm?style=for-the-badge">
    <img src="https://img.shields.io/github/license/alexeev-prog/flexpasm?style=for-the-badge">
    <img src="https://img.shields.io/github/stars/alexeev-prog/flexpasm?style=for-the-badge">
    <img src="https://img.shields.io/github/issues/alexeev-prog/flexpasm?style=for-the-badge">
    <img src="https://img.shields.io/github/last-commit/alexeev-prog/flexpasm?style=for-the-badge">
</p>

## Getting Started

flexpasm is available on [PyPI](https://pypi.org/project/flexpasm). Simply install the package into your project environment with PIP:

```bash
pip install flexpasm
```

Once installed, you can start using the library in your Python projects. Check out the [documentation](./docs/en/index.md) for detailed usage examples and API reference.

## Basic Usage
"Hello World":

```python
from flexpasm.instructions.segments import Label
from flexpasm.program import ASMProgram
from flexpasm.settings import Settings
from flexpasm.templates import PrintStringTemplate
from flexpasm.mnemonics.flow import JmpMnemonic


def main():
  settings = Settings(
    title="Example ASM Program",
    author="alexeev-prog",
    filename="example.asm",
    mode="32",
  )
  asmprogram = ASMProgram(settings)

  pst = PrintStringTemplate("Hello, World!")
  pst2 = PrintStringTemplate("Hello, World!", 'msg2', 'print_string2')
  start_lbl = Label("start")

  start_lbl.add_command(JmpMnemonic("print_string"), 1, comment='Jump to print strint template')

  asmprogram.add_label(start_lbl)
  asmprogram.add_template(pst)
  asmprogram.add_template(pst2)

  asmprogram.save_code()


if __name__ == "__main__":
  main()
```

```bash
$ fasm example.asm example
$ ./example

 Hello, World!
```

## Check Other My Projects

 + [SQLSymphony](https://github.com/alexeev-prog/SQLSymphony) - simple and fast ORM in sqlite (and you can add other DBMS)
 + [Burn-Build](https://github.com/alexeev-prog/burn-build) - simple and fast build system written in python for C/C++ and other projects. With multiprocessing, project creation and caches!
 + [OptiArch](https://github.com/alexeev-prog/optiarch) - shell script for fast optimization of Arch Linux
 + [libnumerixpp](https://github.com/alexeev-prog/libnumerixpp) - a Powerful C++ Library for High-Performance Numerical Computing
 + [pycolor-palette](https://github.com/alexeev-prog/pycolor-palette) - display beautiful log messages, logging, debugging.
 + [shegang](https://github.com/alexeev-prog/shegang) - powerful command interpreter (shell) for linux written in C
 + [aioconsole](https://github.com/alexeev-prog/aioconsole) - simple python library for creating async CLI applications

