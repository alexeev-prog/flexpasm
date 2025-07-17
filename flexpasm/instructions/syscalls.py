from flexpasm.instructions.registers import get_registers
from flexpasm.mnemonics.data import MovMnemonic
from flexpasm.utils import get_indentation_by_level


class Syscall:
    SYS_EXIT = 60
    SYS_WRITE = 1
    SYS_READ = 0
    SYS_FORK = 57
    SYS_WAITPID = 61
    SYS_EXECVE = 59

    @staticmethod
    def syscall_instruction(mode: str, rax: int, *args, indentation_level: int = 0):
        indentation = get_indentation_by_level(indentation_level)

        regs = get_registers(mode)
        instructions = [MovMnemonic(regs.AX, rax).generate(indentation)]
        arg_mapping = {
            0: regs.DI,
            1: regs.SI,
            2: regs.DX,
            3: regs.r10,
            4: regs.r8,
            5: regs.r9,
        }

        for i, arg in enumerate(args):
            instructions.append(MovMnemonic(
                arg_mapping[i], arg).generate(indentation))

        instructions.append(f"{indentation}syscall")

        return f'\n{"\n".join(instructions)}'

    @staticmethod
    def exit(code: int, indentation_level: int = 0, mode: str = "64"):
        return Syscall.syscall_instruction(
            mode, Syscall.SYS_EXIT, code, indentation_level=indentation_level
        )

    @staticmethod
    def write(
        fd: int, buf: str, count: int, indentation_level: int = 0, mode: str = "64"
    ):
        return Syscall.syscall_instruction(
            mode, Syscall.SYS_WRITE, fd, buf, count, indentation_level=indentation_level
        )

    @staticmethod
    def read(
        fd: int, buf: str, count: int, indentation_level: int = 0, mode: str = "64"
    ):
        return Syscall.syscall_instruction(
            mode, Syscall.SYS_READ, fd, buf, count, indentation_level=indentation_level
        )

    @staticmethod
    def fork(indentation_level: int = 0, mode: str = "64"):
        return Syscall.syscall_instruction(
            mode, Syscall.SYS_FORK, indentation_level=indentation_level
        )

    @staticmethod
    def waitpid(pid: int, indentation_level: int = 0, mode: str = "64"):
        return Syscall.syscall_instruction(
            mode, Syscall.SYS_WAITPID, pid, 0, 0, indentation_level=indentation_level
        )

    @staticmethod
    def execve(
        path: str, argv: str, envp: str, indentation_level: int = 0, mode: str = "64"
    ):
        return Syscall.syscall_instruction(
            mode,
            Syscall.SYS_EXECVE,
            path.argv,
            envp,
            indentation_level=indentation_level,
        )
