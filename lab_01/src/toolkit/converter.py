from .constants import (
    ABSOLUTE_ZERO_VALUES,
    LENGTH_FACTORS,
    MASS_FACTORS,
)
from .errors import (
    IncompatibleUnitsError,
    InvalidNumericValueError,
    UnknownUnitError,
)


def define_unit_group(unit: str) -> str:
    """Определяет к какой группе относится единица измерения."""
    unit = unit.lower()

    if unit in LENGTH_FACTORS:
        return "length"
    elif unit in MASS_FACTORS:
        return "mass"
    elif unit in ("c", "k", "f"):
        return "temperature"
    
    raise UnknownUnitError(f"Неизвестная единица измерения: {unit}") 

def define_unit_factors(group: str) -> dict[str, float]:
    """Определяет коэфицент перевода единицы измерения по ее группе."""
    return LENGTH_FACTORS if group == 'length' else MASS_FACTORS

def convert_with_factor(
        value: float,
        from_unit: str,
        to_unit: str,
        factors: dict[str, float],
) -> float:
    """Конвертирует значение с помощью коэффициентов."""
    base_unit = value * factors[from_unit]
    return base_unit / factors[to_unit]

def convert_temperature(
        value: float,
        from_unit: str,
        to_unit: str,
) -> float:
    """Конвертирует значения температур."""
    if from_unit == to_unit: 
        return value
    
    if from_unit == "c":
        if to_unit == "f":
            return (value * 1.8) + 32
        return value + 273.15
    elif from_unit == "f":
        if to_unit == "c":
            return (value - 32) / 1.8
        return (value - 32) / 1.8 + 273.15
    else:
        if to_unit == "c":
            return value - 273.15
        return ((value - 273.15) * 1.8) + 32

def check_temperature_value(value: float, unit: str) -> None:
    """Проверяет, что температура не ниже абсолютного нуля."""
    if value < ABSOLUTE_ZERO_VALUES[unit]:
        raise InvalidNumericValueError("Температура ниже абсолютного нуля")

def convert(
        value: float,
        from_unit: str,
        to_unit: str,
) -> float:
    """Конвертирует значение из одной единицы измерения в другую."""
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    from_group, to_group = define_unit_group(from_unit), define_unit_group(to_unit)

    if from_group != to_group:
        raise IncompatibleUnitsError(
            f"Единицы измерения {from_unit} и {to_unit} несовместимы"
        )

    if from_group == "temperature":
        check_temperature_value(value, from_unit)
        result_value = convert_temperature(value, from_unit, to_unit)
        check_temperature_value(result_value, to_unit)
        return result_value
    
    return convert_with_factor(
            value, 
            from_unit, 
            to_unit, 
            define_unit_factors(from_group)
        )
    
