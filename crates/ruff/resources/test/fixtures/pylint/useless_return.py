import sys


def print_python_version():
    print(sys.version)
    return None  # [useless-return]


def print_python_version():
    print(sys.version)
    return None  # [useless-return]


def print_python_version():
    print(sys.version)
    return None  # [useless-return]


class SomeClass:
    def print_python_version(self):
        print(sys.version)
        return None  # [useless-return]


def print_python_version():
    return


def print_python_version():
    return None


def print_python_version():
    return None


def print_python_version():
    """This function returns None."""
    return None


def print_python_version():
    """This function returns None."""
    print(sys.version)
    return None  # [useless-return]


class BaseCache:
    def get(self, key: str) -> str | None:
        print(f"{key} not found")
        return None

    def get(self, key: str) -> None:
        print(f"{key} not found")
        return None
