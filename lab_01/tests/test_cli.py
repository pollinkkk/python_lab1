import builtins
import subprocess
import sys

from toolkit.calculator import calculate


def test_cli_calc_success() -> None:
    """Проверяет успешный запуск калькулятора через CLI."""
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "toolkit",
            "calc",
            "2 + 3 * 4",
        ],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0
    assert result.stdout.strip() == "14.0"


def test_cli_convert_success() -> None:
    """Проверяет успешный запуск конвертера через CLI."""
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "toolkit",
            "convert",
            "100",
            "--from",
            "cm",
            "--to",
            "m",
        ],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0
    assert result.stdout.strip() == "1.0"


def test_cli_calc_error() -> None:
    """Проверяет ошибку калькулятора через CLI."""
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "toolkit",
            "calc",
            "3 +",
        ],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 2
    assert result.stderr.strip() == "Пропущен операнд"


def test_help_exit_code() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "toolkit", "--help"],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0


def test_user_error_goes_to_stderr_and_returns_code_2() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "toolkit", "calc", "10 / 0"],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 2
    assert "деление на ноль" in result.stderr.lower()


def test_calculator_does_not_use_input_or_print(monkeypatch) -> None:
    def forbidden(*args, **kwargs):
        raise AssertionError("input() or print() must not be used")

    monkeypatch.setattr(builtins, "input", forbidden)
    monkeypatch.setattr(builtins, "print", forbidden)

    result = calculate("2 + 3")

    assert result == 5
