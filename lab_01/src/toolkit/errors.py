class ToolkitError(Exception):
    """Ошибка, возникающая при некорректной работе с toolkit."""


class CalculatorError(ToolkitError):
    """Ошибка, возникающая при некорректной работе калькулятора."""


class ConverterError(ToolkitError):
    """Ошибка, возникающая при некорректной работе конвертера."""


class DivByZeroError(CalculatorError):
    """Ошибка, возникающая при делении на ноль."""


class EmptyExpressionError(CalculatorError):
    """Ошибка, возникающая при вводе пустого выражения."""


class InvalidCharacterError(CalculatorError):
    """Ошибка, возникающая при вводе недопустимого символа."""


class MissingOperandError(CalculatorError):
    """Ошибка, возникающая при пропуске операнда."""


class MissingOperatorError(CalculatorError):
    """Ошибка при отсутствии оператора между операндами."""


class TwoBinOperatorsError(CalculatorError):
    """Ошибка, возникающая при вводе двух операторов подряд."""


class UnknownUnitError(ConverterError):
    """Ошибка, возникающая при вводе неизвестной единицы."""


class IncompatibleUnitsError(ConverterError):
    """Ошибка, возникающая при вводе несовместимых единиц."""


class InvalidNumericValueError(ConverterError):
    """Ошибка, возникающая при вводе неверного числового значения."""


class IncorrectParenthesisExpressionError(CalculatorError):
    """Ошибка, возникающая при вводе некорректной скобочной последовательности."""
