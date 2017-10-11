from opsdroid import match_regex

@match_regex('hi')
async def hello(opsdroid, config, message):
    await message.respond('Hey')
