import typing
from typing import cast

# With -> for, variable reused
with None as i:
    pass
# For -> with, variable reused
for i in []:
    with None as i:  # error
        pass

# With -> with, variable reused
with None as i:
    with None as i:  # error
        pass

# With -> with, different variable
with None as i:
    with None as j:  # ok
        pass

# For -> assignment
for i in []:
    # ignore typing cast
    i = cast(int, i)
    i = typing.cast(int, i)
    i = 5  # error

# For -> augmented assignment
for i in []:
    i += 5  # error

# For -> annotated assignment
for i in []:
    i: int = 5  # error

# For -> annotated assignment without value
for i in []:
    i: int  # no error

# Async for -> for, variable reused
async for i in []:
    pass
# For -> async for, variable reused
for i in []:
    async for i in []:  # error
        pass

# For -> function definition
for i in []:
    def f():
        i = 2  # no error

# For -> class definition
for i in []:
    class A:
        i = 2  # no error

# For -> function definition -> for -> assignment
for i in []:
    def f():
        for i in []:  # no error
            i = 2  # error

# For -> class definition -> for -> for
for _ in []:


    class A:
        pass

# For -> use in assignment target without actual assignment; subscript
for i in []:
    a[i] = 2  # no error
    i[a] = 2  # no error

# For -> use in assignment target without actual assignment; attribute
for i in []:
    a.i = 2  # no error
    i.a = 2  # no error

# For target with subscript -> assignment
for a[0] in []:
    a[0] = 2  # error
    a[1] = 2  # no error

# For target with subscript -> assignment
for a['i'] in []:
    a['i'] = 2  # error
    a['j'] = 2  # no error

# For target with attribute -> assignment
for a.i in []:
    a.i = 2  # error
    a.j = 2  # no error

a.j.i = 2  # no error

# For target with double nested attribute -> assignment
for a.i.j in []:
    a.i.j = 2  # error
# For target with attribute -> assignment with different spacing
for a.i in []:
    a. i = 2  # error
for a. i in []:
    a.i = 2  # error
