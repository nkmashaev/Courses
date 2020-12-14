from contextlib import contextmanager
from types import TracebackType


class Suppressor:
    def __init__(self, exception: Exception):
        self.suppressed_exception = exception

    def __enter__(self):
        pass

    def __exit__(
        self, exception_type: type, exception_value: Exception, traceback: TracebackType
    ):
        return isinstance(exception_value, self.suppressed_exception)


@contextmanager
def suppressor(supressed_exc: Exception):
    try:
        yield
    except supressed_exc:
        pass
    finally:
        pass
