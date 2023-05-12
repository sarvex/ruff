###
# Errors
###
def foo2(x, y, w, z):
    for i in x:
        if i > y or i > w:  # [no-else-break]
            break
        else:
            a = z


def foo5(x, y, z):
    for i in x:
        if i > y:  # [no-else-break]
            if y:
                a = 4
            else:
                b = 2
            break
        elif z:
            c = 2
        else:
            c = 3
        break


def foo1(x, y, z):
    for i in x:
        if i > y:  # [no-else-break]
            break
        else:
            a = z


def foo3(x, y, z):
    for i in x:
        if i > y:
            a = 1
            if z:  # [no-else-break]
                b = 2
            else:
                c = 3
        else:
            d = 4

        break


def foo4(x, y):
    for i in x:
        if i > x:  # [no-else-break]
            if y:
                a = 4
            else:
                b = 2
            break
        else:
            c = 3
        break


def foo6(x, y):
    for i in x:
        if i > x:
            if y:  # [no-else-break]
                a = 4
                break
            else:
                b = 2
        else:
            c = 3
        break


def bar4(x):
    for _ in range(10):
        if x:
            break
        try:
            return
        except ValueError:
            break


###
# Non-errors
###
def bar1(x, y, z):
    for i in x:
        if i > y:
            break
        return z


def bar2(w, x, y, z):
    for i in w:
        if i > x:
            break
        if z < i:
            a = y
        else:
            break
        return


def bar3(x, y, z):
    for i in x:
        if i <= y:
            return z
        if z:
            break
        return None


def nested1(x, y, z):
    for i in x:
        if i > x:
            for j in y:
                if j < z:
                    break
        else:
            a = z


def nested2(x, y, z):
    for i in x:
        if i > x:
            for _ in y:
                break
        else:
            a = z


def elif1(x, y, w, z):
    for i in x:
        if i > y or i <= w:
            a = z
        else:
            break


def elif2(x, y, w, z):
    for i in x:
        if i <= y and i > w:
            break
        else:
            a = z
