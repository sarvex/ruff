# Errors
if a or c:
    b
if x in [1, 2]:
    for _ in range(20):
        print("hello")
if x in [1, 2]:
    for _ in range(20):
        print("hello")
if x in [1, 2]:
    for _ in range(20):
        print("hello")
if result.eofs in ["F", "E"]:
    errors = 1
elif result.eofs == "S":
    skipped = 1


# OK
def complicated_calc(*arg, **kwargs):
    return 42


def foo(p):
    if p == 2:
        return complicated_calc(microsecond=0)
    elif p == 3:
        return complicated_calc(microsecond=0, second=0)
    return None


a = False
b = True
c = True

if a or not b and c:
    z = 1
elif b:
    z = 2
errors = 1
