from dataclasses import dataclass, field


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
    files: list[File] = field(default_factory=list)
