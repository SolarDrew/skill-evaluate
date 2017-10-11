from opsdroid import match_regex

def setup(opsdroid):
    logging.debug("Loaded evaluate module")

@match_regex('hi')
async def hello(opsdroid, config, message):
    await message.respond('Hey')
