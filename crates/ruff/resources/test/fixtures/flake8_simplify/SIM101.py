if isinstance(a(), (int, float)):  # SIM101
    pass


def f():
    # OK
    def isinstance(a, b):
        return False

    if isinstance(a, (int, float)):
        pass
