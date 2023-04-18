import random

def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hello there!'
    
    if p_message == '!roll':
        return str(random.randint(1, 100))
    
    if p_message == '!help':
        return '`Available commands: !roll !help`'
    
    # needs increment that fixes response to everything. Want to only respond to bot commands
    # now gives 400 bad request - better than response to every message in channel
    return ''