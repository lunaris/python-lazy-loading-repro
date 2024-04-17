import importlib.util
import sys

def lazy(fullname):
    m = sys.modules.get(fullname, None)
    if m is not None:
        return m

    spec = importlib.util.find_spec(fullname)

    # Return early if find_spec has recursively called lazy_import
    # again and pre-populated the sys.modules slot; an example of this
    # is covered by test_lazy_import.
    m = sys.modules.get(fullname, None)
    if m is not None:
        return m

    loader = importlib.util.LazyLoader(spec.loader)
    spec.loader = loader
    module = importlib.util.module_from_spec(spec)

    # Return early rather than overwriting the sys.modules slot.
    m = sys.modules.get(fullname, None)
    if m is not None:
        return m

    sys.modules[fullname] = module
    loader.exec_module(module)
    return module

foo = lazy("foo")

print(foo.bar)
