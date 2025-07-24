import pytest

from src.decorators import log


@log
def successful_function(x, y):
    return x + y


@log
def failing_function(x, y):
    return x / y


def test_successful_function(capsys):
    result = successful_function(1, 2)
    captured = capsys.readouterr()

    assert result == 3
    assert "successful_function ok" in captured.out


def test_failing_function(capsys):
    with pytest.raises(ZeroDivisionError):
        failing_function(1, 0)

    captured = capsys.readouterr()
    assert "failing_function error: ZeroDivisionError. Inputs: (1, 0), {}" in captured.out
