# SIM102
if a and b:
    c

    if c:
        d

# SIM102
if a:
    pass
elif b:
    if c:
        d

if a:
    if b:
        c

        # Fixable due to placement of this comment.
        c

        c
    else:
        d

# OK
if __name__ == "__main__" and foo():
    ...

# OK
if a:
    d
    if b:
        c

while x > 0:
    # SIM102
    if y > 0 and z > 0:
        """this
is valid"""

        """the indentation on
            this line is significant"""

                    "this is" \
        "allowed too"

                    ("so is"
        "this for some reason")


# SIM102
if x > 0 and y > 0:
    """this
is valid"""

    """the indentation on
        this line is significant"""

            "this is" \
    "allowed too"

            ("so is"
    "this for some reason")

while x > 0:
    # SIM102
    if node.module and (
        node.module == "multiprocessing"
        or node.module.startswith("multiprocessing.")
    ):
        print("Bad module!")

# SIM102
if node.module and (
    node.module == "multiprocessing"
    or node.module.startswith("multiprocessing.")
):
    print("Bad module!")


# OK
if a:
    if b:
        print("foo")
else:
    print("bar")

# OK
if a and b and c:
    print("foo")
elif a and b or not a:
    print("bar")
# OK
if a:
    # SIM 102
    if b and c:
        print("foo")
else:
    print("bar")


# OK
if a:
    if b:
        if c:
            print("foo")
        print("baz")
else:
    print("bar")
