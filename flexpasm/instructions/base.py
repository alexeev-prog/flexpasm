from abc import ABC, abstractmethod


class BaseRegister(ABC):
	@abstractmethod
	def __str__(self) -> str:
		raise NotImplementedError
