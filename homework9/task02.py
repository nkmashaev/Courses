from contextlib import contextmanager
from types import TracebackType


class Suppressor:
    def __init__(self, exception: Exception):
        self.suppressed_exception = exception

    def __enter__(self):
        pass

    def __exit__(self, exctype, excinst, exctb):
        return exctype is not None and issubclass(self.suppressed_exception, exctype)


@contextmanager
def suppressor(ex: Exception):
    try:
        yield
    except ex:
        pass
    except Exception as some_ex:
        if not issubclass(ex, type(some_ex)):
            raise (some_ex)
