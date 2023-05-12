try:
    y = 6 + "7"
except TypeError:
    # RSE102
    raise ValueError()

try:
    x = 1 / 0
except ZeroDivisionError:
    raise

# RSE102
raise TypeError()
