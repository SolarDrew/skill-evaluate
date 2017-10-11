from opsdroid.matchers import match_regex
import logging

def setup(opsdroid):
    logging.debug("Loaded evaluate module")

@match_regex('=')
async def hello(opsdroid, config, message):
    text = message.text.replace('=', '')
    response = str(eval(text))
    await message.respond(response)
