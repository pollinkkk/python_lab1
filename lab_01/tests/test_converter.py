import pytest

from toolkit.converter import convert
from toolkit.errors import (
    IncompatibleUnitsError,
    InvalidNumericValueError,
    UnknownUnitError,
)


def test_convert_milimeters_to_meters() -> None:
    """Проверяет перевод миллиметров в метры."""
    result = convert(1000, "mm", "m")

    assert result == 1.0


def test_convert_kilometers_to_meters() -> None:
    """Проверяет перевод километров в метры."""
    result = convert(2.0, "km", "m")

    assert result == 2000.0


def test_convert_kilograms_to_grams() -> None:
    """Проверяет перевод граммов в килограммы."""
    result = convert(1.5, "kg", "g")

    assert result == 1500.0


def test_convert_celsius_to_fahrenheit() -> None:
    """Проверяет перевод градусов Цельсия в Фаренгейты."""
    result = convert(0.0, "c", "f")

    assert result == pytest.approx(32.0)


def test_convert_fahrenheit_to_celsius() -> None:
    """Проверяет перевод градусов Фаренгейтов в Цельсия."""
    result = convert(32, "f", "c")

    assert result == pytest.approx(0.0)


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
