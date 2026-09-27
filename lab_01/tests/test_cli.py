import subprocess
import sys


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