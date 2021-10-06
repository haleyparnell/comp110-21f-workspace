"""Tracing Example."""

x: int = 1


def main() -> None:
    """Entrypoint of a program."""
    x: int = 1
    f()
    x += g(4)


def f() -> None:
    """Procedure."""
    global x
    x += 1


def g(x: int) -> int:
    """Function."""
    return x ** 2 % 3


if __name__ == "__main__":
    main()