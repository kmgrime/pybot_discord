# imports
import discord
import logging
from modules import responses

# logging
print('Starting log service...')

# Logging attributes: https://docs.python.org/3/library/logging.html#logrecord-attributes

logging.basicConfig(filename='logs.log',
                    encoding='utf-8',
                    filemode='w',
                    level=logging.DEBUG,
                    format='%(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d [%(filename)s])',
                    datefmt='%d/%m/%Y %I:%M:%S %p')

logging.debug('debug')
logging.info('info')
logging.warning('Warning')
logging.error('Error')
logging.critical('Critical')

print('Logging started')

# response


async def send_message(message, user_message):
    try:
        response = responses.get_response(user_message)
        await message.channel.send(response)

    # bad exception - do better
    except Exception as e:
        print(e)


# remember to change token before pushing code to repo
def run_discord_bot():
    TOKEN = 'YOUR_TOKEN_HERE'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        if user_message[0] == '!':
            print(user_message[0])
            user_message = user_message[1:]
            await send_message(message, user_message)
        elif user_message.lower() == 'hello':
            await send_message(message, user_message)
        else:
            print('No output response')

    client.run(TOKEN)
