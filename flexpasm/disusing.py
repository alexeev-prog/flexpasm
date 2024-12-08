import dis
from typing import Callable
from rich import print


def get_function_bytecode(function: Callable, printing: bool = True):
	result = dis.dis(function)

	if printing:
		print(result)

	return result


def get_function_info(function: Callable, printing: bool = True):
	result = dis.code_info(function)

	if printing:
		print(result)

	return result


def get_function_instructions(function: Callable, printing: bool = True):
	result = dis.get_instructons(function)

	if printing:
		print(result)

	return result
