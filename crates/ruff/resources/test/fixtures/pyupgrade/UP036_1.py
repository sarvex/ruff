import sys

if sys.version_info == 2:
    2
else:
    3

if sys.version_info < (3,):
    2
else:
    3

if sys.version_info < (3,0):
    2
else:
    3

if sys.version_info == 3:
    3
else:
    2

if sys.version_info > (3,):
    3
else:
    2

if sys.version_info >= (3,):
    3
else:
    2

from sys import version_info

if version_info > (3,):
    3
else:
    2

print(1)
print(1)
print(1)

def f():
    print(1)

print(1)

def f():
    print(1)
