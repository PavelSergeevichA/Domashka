import pytest

from src.decorators import log


@log()
def test_function(x=10):
    assert x * 2 == 20

@log("test_log.txt")
def test_function_with_logging(x=1):
    assert x + 1 == 2
