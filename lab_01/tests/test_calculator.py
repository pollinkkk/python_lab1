import pytest

from toolkit.calculator import calculate
from toolkit.errors import (
    DivByZeroError,
    EmptyExpressionError,
    IncorrectParenthesisExpressionError,
    InvalidCharacterError,
    MissingOperandError,
    MissingOperatorError,
    TwoBinOperatorsError,
)


def test_addition() -> None:
    """Проверяет сложение (с пробелами)."""
    assert calculate("2 + 3") == 5.0


def test_operator_priority() -> None:
    """Проверяет приоритет умножения над сложением."""
    assert calculate("2+ 3*4") == 14.0


def test_division() -> None:
    """Проверяет деление."""
    assert calculate("10/4") == 2.5


def test_negative_numbers() -> None:
    """Проверяет работу с отрицательными числами."""
    assert calculate("-2 * -3") == 6.0


def test_parentheses() -> None:
    """Проверяет вычисление выражения со скобками."""
    assert calculate("(2+3)*4") == 20.0


def test_unary_minus() -> None:
    """Проверяет унарный минус."""
    assert calculate("3 * -2") == -6.0


def test_unary_plus() -> None:
    """Проверяет унарный плюс."""
    assert calculate("3 + +2") == 5.0


def test_float_numbers() -> None:
    """Проверяет вычисления с вещественными числами."""
    assert calculate("2.5*4") == pytest.approx(10.0)


def test_addition_with_a_negative_number() -> None:
    """Проверяет сложение с отрицательным числом."""
    assert calculate("1+-2") == -1.0


def test_two_binary_operators() -> None:
    """Проверяет ошибку двух бинарных операторов подряд."""
    with pytest.raises(TwoBinOperatorsError):
        calculate("2*/3")


def test_invalid_character() -> None:
    """Проверяет ошибку неизвестного символа."""
    with pytest.raises(InvalidCharacterError):
        calculate("2+a")


def test_division_by_zero() -> None:
    """Проверяет ошибку деления на ноль."""
    with pytest.raises(DivByZeroError):
        calculate("1/0")


def test_empty_expression() -> None:
    """Проверяет ошибку пустого выражения."""
    with pytest.raises(EmptyExpressionError):
        calculate("")


def test_missing_operand() -> None:
    """Проверяет ошибку отсутствующего операнда."""
    with pytest.raises(MissingOperandError):
        calculate("3 +")


def test_missing_operator() -> None:
    """Проверяет ошибку отсутствующего оператора."""
    with pytest.raises(MissingOperatorError):
        calculate("2 3")


def test_incorrect_parentheses() -> None:
    """Проверяет ошибку неправильной скобочной последовательности."""
    with pytest.raises(IncorrectParenthesisExpressionError):
        calculate("(2+3")


def test_floor_division() -> None:
    """Проверяет вычисления целочисленного деления."""
    assert calculate("7//2") == 3.0


def test_modulo() -> None:
    """Проверяет вычисления деления с остатком."""
    assert calculate("7%2") == 1.0


def test_negative_floor_division() -> None:
    """Проверяет вычисления целочисленного деления с отрицательным операндом."""
    assert calculate("-7//2") == -4.0


def test_negative_modulo() -> None:
    """Проверяет вычисления деления с остатком с отрицательным операндом."""
    assert calculate("-7%2") == 1.0
