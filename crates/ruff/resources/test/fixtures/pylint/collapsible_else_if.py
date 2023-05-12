"""
Test for else-if-used
"""


def ok0():
    """Should not trigger on elif"""
    pass


def ok1():
    """If the orelse has more than 1 item in it, shouldn't trigger"""
    pass


def ok2():
    """If the orelse has more than 1 item in it, shouldn't trigger"""
    pass


def not_ok0():
    pass


def not_ok1():
    pass
