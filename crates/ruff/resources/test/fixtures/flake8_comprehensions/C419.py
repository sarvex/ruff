any(x.id for x in bar)
all(x.id for x in bar)
any(x.id for x in bar)
all(x.id for x in bar)
any({x.id for x in bar})

# OK
all(x.id for x in bar)
all(x.id for x in bar)
any(x.id for x in bar)
all((x.id for x in bar))


async def f() -> bool:
    return all(await use_greeting(greeting) for greeting in await greetings())
