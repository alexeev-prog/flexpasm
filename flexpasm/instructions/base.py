from abc import ABC, abstractmethod


class BaseMnemonic(ABC):
	@abstractmethod
	def generate(self, syntax: str, indentation: str = '') -> str:
		raise NotImplementedError

	@abstractmethod
	def comment(self) -> str:
		raise NotImplementedError


class BaseRegister(ABC):
	@abstractmethod
	def __str__(self) -> str:
		raise NotImplementedError
