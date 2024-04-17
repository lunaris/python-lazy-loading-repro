import sys
import types

class Foo(types.ModuleType):
    @property
    def bar(self) -> str:
        return "Hello from foo.bar"

sys.modules[__name__].__class__ = Foo
