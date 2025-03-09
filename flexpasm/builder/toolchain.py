from dataclasses import dataclass, field
from typing import List


@dataclass
class Compiler:
    command: str = "fasm"
    flags: str = None
    compiling_format: str = "fasm {flags} {source_file} {object_file}"


@dataclass
class Linker:
    command: str = "ld"
    flags: str = None
    linking_format: str = "ld {flags} {object_file} -o {binary_file}"


@dataclass
class File:
    source_file: str
    object_file: str
    binary_file: str


@dataclass
class FileChain:
    compiler: Compiler
    linker: Linker
    skip_linker: bool = True
    files: List[File] = field(default_factory=list)
