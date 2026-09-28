import argparse
import sys

from .calculator import calculate
from .converter import convert
from .errors import ToolkitError


def create_parser() -> argparse.ArgumentParser:
    """Создаёт парсер аргументов командной строки."""
    parser = argparse.ArgumentParser(
        prog="toolkit",
        description="Набор консольных утилит.",
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    calc_parser = subparsers.add_parser("calc")
    calc_parser.add_argument("expression")

    convert_parser = subparsers.add_parser("convert")
    convert_parser.add_argument("value", type=float)
    convert_parser.add_argument("--from", dest="from_unit", required=True)
    convert_parser.add_argument("--to", dest="to_unit", required=True)

    return parser


def main() -> int:
    """Запускает консольное приложение toolkit."""
    parser = create_parser()
    args = parser.parse_args()

    try:
        if args.command == "calc":
            result = calculate(args.expression)

        elif args.command == "convert":
            result = convert(
                args.value,
                args.from_unit,
                args.to_unit,
            )

        print(result)
        return 0

    except ToolkitError as error:
        print(error, file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
