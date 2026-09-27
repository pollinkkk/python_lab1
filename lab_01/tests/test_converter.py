import pytest
from toolkit.converter import convert
from toolkit.errors import (
    IncompatibleUnitsError,
    InvalidNumericValueError,
    UnknownUnitError,
)


def test_convert_kilometers_to_meters() -> None:
    """Проверяет перевод километров в метры."""
    result = convert(2.0, "km", "m")

    assert result == 2000.0

def test_convert_grams_to_kilograms() -> None:
    """Проверяет перевод граммов в килограммы."""
    result = convert(5000.0, "g", "kg")

    assert result == 5.0


def test_convert_celsius_to_fahrenheit() -> None:
    """Проверяет перевод градусов Цельсия в Фаренгейты."""
    result = convert(100.0, "c", "f")

    assert result == pytest.approx(212.0)

def test_convert_units_case_insensitive() -> None:
    """Проверяет, что регистр единиц измерения не имеет значения."""
    result = convert(2.0, "KM", "M")

    assert result == 2000.0

def test_convert_incompatible_units() -> None:
    """Проверяет ошибку при конвертации несовместимых единиц."""
    with pytest.raises(IncompatibleUnitsError):
        convert(10.0, "kg", "m")

def test_convert_unknown_unit() -> None:
    """Проверяет ошибку при неизвестной единице измерения."""
    with pytest.raises(UnknownUnitError):
        convert(10.0, "banana", "m")

def test_temperature_below_absolute_zero() -> None:
    """Проверяет ошибку при температуре ниже абсолютного нуля."""
    with pytest.raises(InvalidNumericValueError):
        convert(-274.0, "c", "f")

def test_temperature_at_absolute_zero() -> None:
    """Проверяет конвертацию температуры на границе абсолютного нуля."""
    result = convert(-273.15, "c", "k")

    assert result == pytest.approx(0.0)