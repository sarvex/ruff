def f():
    return any(check(x) for x in iterable)


def f():
    return next((True for x in iterable if check(x)), True)


def f():
    for el in [1, 2, 3]:
        if is_true(el):
            return True
    raise Exception


def f():
    return not any(check(x) for x in iterable)


def f():
    return all(x.is_empty() for x in iterable)


def f():
    return next((False for x in iterable if check(x)), False)


def f():
    return next(("foo" for x in iterable if check(x)), "bar")


def f():
    # SIM110
    for x in iterable:
        if check(x):
            return True
    else:
        return False


def f():
    # SIM111
    for x in iterable:
        if check(x):
            return False
    else:
        return True


def f():
    # SIM110
    for x in iterable:
        if check(x):
            return True
    else:
        return False
    return True


def f():
    # SIM111
    for x in iterable:
        if check(x):
            return False
    else:
        return True
    return False


def f():
    for x in iterable:
        if check(x):
            return True
        elif x.is_empty():
            return True
    return False


def f():
    for x in iterable:
        return True if check(x) else True
    return False


def f():
    for x in iterable:
        if check(x):
            return True
        elif x.is_empty():
            return True
    else:
        return True
    return False


def f():
    def any(exp):
        pass

    for x in iterable:
        if check(x):
            return True
    return False


def f():
    def all(exp):
        pass

    for x in iterable:
        if check(x):
            return False
    return True


def f():
    x = 1

    return any(check(x) for x in iterable)


def f():
    x = 1

    return not any(check(x) for x in iterable)


def f():
    return all(x in y for x in iterable)


def f():
    return all(x <= y for x in iterable)
