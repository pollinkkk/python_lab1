ABSOLUTE_ZERO_VALUES: dict[str, float] = {
    "k": 0.0,
    "c": -273.15,
    "f": -459.67,
}

LENGTH_FACTORS: dict[str, float] = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1.0,
    "km": 1000.0,
}

MASS_FACTORS: dict[str, float] = {
    "g": 0.001,
    "kg": 1.0,
}

OPERATOR_PRIORITY: dict[str, int] = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
    "//": 2,
    "%": 2,
    "u+": 3,
    "u-": 3,
}
