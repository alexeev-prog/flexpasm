from dataclasses import dataclass, field
from typing import Any, Callable

from flexpasm.exceptions import MacroNotFound


@dataclass
class Macro:
    name: str
    handler: Callable
    args: dict = field(default_factory=list)
    kwargs: dict = field(default_factory=dict)


class MacroManager:
    def __init__(self):
        self._macros = {}

    def add_macro(self, macro_name: str = None):
        def wrapper(func, *args, **kwargs):
            name = func.__name__ if macro_name is None else macro_name

            self._macros[name] = Macro(
                name=name, handler=func, args=args, kwargs=kwargs
            )
            return func

        return wrapper

    def exec(self, macro_name: str, *args, **kwargs) -> Any:
        macro = self._macros.get(macro_name)

        if macro is None:
            raise MacroNotFound(f'Macro "{macro_name}" not exists')

        print(f"[MACRO] Execute macro-function: {macro.name}")
        result = macro.handler(*args, **kwargs)

        return result
