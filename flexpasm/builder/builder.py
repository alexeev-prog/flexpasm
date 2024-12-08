from flexpasm.builder.toolchain import File, FileChain
from flexpasm.utils import CommandManager


class ASMBuilder:
	def __init__(self, filechain: FileChain):
		self.filechain = filechain

	def add_to_filechain(self, file: File):
		self.filechain.files.append(file)

	def run_build(self):
		compiler = self.filechain.compiler
		compiler_flags = "" if compiler.flags is not None else ""
		linker = self.filechain.linker
		linker_flags = "" if linker.flags is not None else ""

		print("Start building\n")

		for file in self.filechain.files:
			print(f"=== {file.source_file} ===")

			compile_command = compiler.compiling_format.format(
				flags=compiler_flags,
				source_file=file.source_file,
				object_file=file.object_file,
			)
			print(f"Run compile command: {compile_command}")
			CommandManager.run_command(compile_command)

			if not self.filechain.skip_linker:
				link_command = linker.linking_format.format(
					flags=linker_flags,
					object_file=file.object_file,
					binary_file=file.binary_file,
				)
				print(f"Run link command: {link_command}")
				CommandManager.run_command(link_command)

			print()

		print("End")
