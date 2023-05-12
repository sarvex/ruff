a = bool(b)

a = b != c

a = bool(b + c)

a = not b

def f():
    # OK
    def bool():
        return False

    a = bool(b)
