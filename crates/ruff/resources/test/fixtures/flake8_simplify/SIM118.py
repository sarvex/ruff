key in obj.keys()  # SIM118

foo["bar"] in obj.keys()  # SIM118

foo['bar'] in obj.keys()  # SIM118

foo() in obj.keys()  # SIM118

for key in obj.keys():  # SIM118
    pass

for key in list(obj.keys()):
    if some_property(key):
        del obj[key]

list(obj.keys())

set(obj.keys())

{k: k for k in obj.keys()}  # SIM118

iter(obj.keys())

key in (obj or {}).keys()  # SIM118
