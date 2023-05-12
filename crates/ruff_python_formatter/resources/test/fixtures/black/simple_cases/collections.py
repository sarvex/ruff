import core, time, a

from . import A, B, C

# keeps existing trailing comma
from foo import (
    bar,
)

# also keeps existing structure
from foo import (
    baz,
    qux,
)

# `as` works as well
from foo import (
    xyzzy as magic,
)

a = {1,2,3,}
b = {
1,2,
     3}
c = {
    1,
    2,
    3,
}
x = 1,
y = narf(),
nested = {(1,2,3),(4,5,6),}
nested_no_trailing_comma = {(1,2,3),(4,5,6)}
nested_long_lines = ["aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb", "cccccccccccccccccccccccccccccccccccccccc", (1, 2, 3), "dddddddddddddddddddddddddddddddddddddddd"]
{"oneple": (1,),}
{"oneple": (1,)}
['ls', f'lsoneple/{foo}']
x = {"oneple": (1,)}
y = {"oneple": (1,),}
assert (
    False
), f"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa wraps {bar}"

[1, 2, 3,]

division_result_tuple = (6/2,)
print("foo %r", (foo.bar,))

IGNORED_TYPES_FOR_ATTRIBUTE_CHECKING = (
    Config.IGNORED_TYPES_FOR_ATTRIBUTE_CHECKING
    | {pylons.controllers.WSGIController}
)

ec2client.get_waiter('instance_stopped').wait(
    InstanceIds=[instance.id],
    WaiterConfig={
        'Delay': 5,
    })
ec2client.get_waiter("instance_stopped").wait(
    InstanceIds=[instance.id],
    WaiterConfig={"Delay": 5,},
)
ec2client.get_waiter("instance_stopped").wait(
    InstanceIds=[instance.id], WaiterConfig={"Delay": 5,},
)
