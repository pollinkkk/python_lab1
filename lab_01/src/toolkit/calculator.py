from .constants import OPERATOR_PRIORITY
from .errors import (
    DivByZeroError,
    EmptyExpressionError,
    IncorrectParenthesisExpressionError,
    InvalidCharacterError,
    MissingOperandError,
    MissingOperatorError,
    TwoBinOperatorsError,
)


def tokenize(expression: str) -> list[str]:
    """Разбивает математическое выражение на токены."""
    tokens: list[str] = []
    current_number = ""
    index = 0

    while index < len(expression):
        character = expression[index]

        if character.isspace():
            if current_number:
                tokens.append(current_number)
                current_number = ""

            index += 1
            continue

        if character.isdigit() or character == ".":
            current_number += character
            index += 1
            continue

        if (
            character == "/"
            and index + 1 < len(expression)
            and expression[index + 1] == "/"
        ):
            if current_number:
                tokens.append(current_number)
                current_number = ""

            tokens.append("//")
            index += 2
            continue

        if current_number:
            tokens.append(current_number)
            current_number = ""

        tokens.append(character)
        index += 1

    if current_number:
        tokens.append(current_number)

    return tokens


def check_empty_expression(tokens: list[str]) -> None:
    """Проверяет, что выражение не пустое."""
    if not tokens:
        raise EmptyExpressionError("Введена пустая строка.")

    
def validate_and_prepare_tokens(tokens: list[str]) -> list[str]:
    """Находит недопустимые символы и ошибки в строке, проверяет скобки и унарные плюс и минус"""
    stack: list[str] = []
    prepared_tokens: list[str] = []
    expect_operand = True

    for token in tokens:
        is_number = token.replace(".", "", 1).isdigit()

        if not is_number and token not in ("+", "-", "*", "/", "//", "%", "(", ")"):
            raise InvalidCharacterError(f"Недопустимый символ: {token}")

        if is_number:
            if not expect_operand:
                raise MissingOperatorError("Пропущен оператор между операндами")

            prepared_tokens.append(token)
            expect_operand = False
            continue

        if token == "(":
            if not expect_operand:
                raise MissingOperatorError(
                    "Пропущен оператор перед скобкой"
                )
            
            stack.append("(")
            prepared_tokens.append(token)
            expect_operand = True
            continue

        if token == ")":
            if not stack:
                raise IncorrectParenthesisExpressionError(
                    "Неверная скобочная последовательность"
                )

            if expect_operand:
                raise MissingOperandError(
                    "Пропущен операнд перед закрывающей скобкой"
                )
               
            stack.pop()
            prepared_tokens.append(token)
            expect_operand = False
            continue

        if token in "+-":
            if expect_operand: 
                prepared_tokens.append("u" + token)
            else:
                prepared_tokens.append(token)

            expect_operand = True
            continue

        if token in ("*", "/", "//", "%"):
            if expect_operand:
                if not prepared_tokens or prepared_tokens[-1] == "(":
                    raise MissingOperandError(
                        "Пропущен операнд"
                    )
                
                raise TwoBinOperatorsError(
                    "Две бинарные операции подряд"
                )

            prepared_tokens.append(token)
            expect_operand = True

    if stack:
        raise IncorrectParenthesisExpressionError(
            "Неверная скобочная последовательность"
        )

    if expect_operand:
        raise MissingOperandError("Пропущен операнд")
    
    return prepared_tokens


def to_rpn(tokens: list[str]) -> list[str]:
    """Переводит токены в обратную польскую запись."""
    output: list[str] = []
    operators: list[str] = []

    for token in tokens:
        is_number = token.replace(".", "", 1).isdigit()

        if is_number:
            output.append(token)
            continue

        if token == "(":
            operators.append(token)
            continue

        if token == ")":
            while operators and operators[-1] != "(":
                output.append(operators.pop())

            operators.pop()
            continue

        if token in ("u+", "u-"):
            operators.append(token)
            continue

        while (
            operators
            and operators[-1] != "("
            and OPERATOR_PRIORITY[operators[-1]] >= OPERATOR_PRIORITY[token]
        ):
            output.append(operators.pop())

        operators.append(token)

    while operators:
        output.append(operators.pop())

    return output


def evaluate_rpn(tokens: list[str]) -> float:
    """Вычисляет выражение в обратной польской записи."""
    stack: list[float] = []

    for token in tokens:
        is_number = token.replace(".", "", 1).isdigit()

        if is_number:
            stack.append(float(token))
            continue

        if token == "u+":
            continue

        if token == "u-":
            operand = stack.pop()
            stack.append(-operand)
            continue

        right_operand = stack.pop()
        left_operand = stack.pop()

        if token == "+":
            result = left_operand + right_operand
        elif token == "-":
            result = left_operand - right_operand
        elif token == "*":
            result = left_operand * right_operand
        elif token == "/":
            if right_operand == 0:
                raise DivByZeroError("Деление на ноль")
        
            result = left_operand / right_operand
        elif token == "//":
            if right_operand == 0:
                raise DivByZeroError("Деление на ноль")

            result = left_operand // right_operand

        else:
            if right_operand == 0:
                raise DivByZeroError("Деление на ноль")

            result = left_operand % right_operand

        stack.append(result)

    return stack[0]


def calculate(expression: str) -> float:
    """Вычисляет математическое выражение."""
    tokens = tokenize(expression)
    check_empty_expression(tokens)
    prepared_tokens = validate_and_prepare_tokens(tokens)
    rpn_tokens = to_rpn(prepared_tokens)
    return evaluate_rpn(rpn_tokens)


