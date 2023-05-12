# OK
a = "abc"
b = 'ghijkl'

# Errors
c = "def"
d = f"defghi"
e = ("def" + "ghi")
f = 'abcde'
g = f""

# OK
g = f"ghi{123:45}"

# Error
h = 'xyz'

v = 23.234234

# OK
f"{v:0.2f}"
f"{f'{v:0.2f}'}"

# Errors
f"{v:{f'0.2f'}}"
f"{f''}"
f"{{test}}"
f'{{ 40 }}'
f"{{a {{x}}"
f"{{{{x}}}}"

# To be fixed
# Error: f-string: single '}' is not allowed at line 41 column 8
# f"\{{x}}"  
