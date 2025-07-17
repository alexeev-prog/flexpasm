import os
import shlex
import subprocess
from pathlib import Path


def get_indentation_by_level(indentation_level: int = 0):
    if indentation_level == 0:
        return ""
    return "\t" * indentation_level


class CommandManager:
    @staticmethod
    def run_command(command: str) -> int:
        result = subprocess.run(
            shlex.split(command),
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        if result.returncode != 0:
            raise RuntimeError(
                f'Command "{command}" failed with exit code {result.returncode}:\n{result.stderr.decode()}'
            )
        print(f"Execute command: {command}")

        return result.returncode

    @staticmethod
    def change_directory(path: Path):
        os.chdir(path)
