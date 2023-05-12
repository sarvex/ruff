import sys

if sys.platform in ["linus", "win32", "cygwin"]:
    ...  # OK
    ...  # OK
elif sys.platform not in ["linux", "darwin"]:
    ...  # OK

...  # OK
