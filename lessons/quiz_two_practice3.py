"""Tracing Example."""
x: list[int] = [1, 2]


def main() -> None:
    """Entrypoint of a program."""
    y: list[int] = [1]
    g: list[int] = f()
    y = x
    g = [1]


def f() -> list[int]:
    """Yeehaw."""
    return [1, 4]


if __name__ == "__main__":
    main()