from abc import ABC, abstractmethod


class BaseRegister(ABC):
    @abstractmethod
    def __str__(self) -> str:
        raise NotImplementedError


class BaseMnemonic(ABC):
    @abstractmethod
    def generate(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def comment(self) -> str:
        raise NotImplementedError


class MnemonicTemplate(ABC):
    @abstractmethod
    def generate(self, syntax: str, indentation: str = "") -> str:
        raise NotImplementedError

    @abstractmethod
    def comment(self) -> str:
        raise NotImplementedError
