"""Diagram #2."""


def main() -> None:
    """Entrypoint of a program."""
    xs: list[str] = ['a', 'b', 'c']
    f(xs)
    xs = g(xs)
    print(xs)


def f(kaki: list[str]) -> None:
    """Yeehaw."""
    kaki.append('kaki')


def g(l: list[str]) -> list[str]:
    """Function."""
    copy: list[str] = []
    for item in l:
        copy.append(item)
    l.pop(3)
    return copy


if __name__ == "__main__":
    main()