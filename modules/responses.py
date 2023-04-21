import random
import pyjokes


def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'help':
        return '`Available commands: !help !roll !jokes and hello`'

    if p_message == 'hello':
        return 'Hello there!'

    if p_message == 'roll':
        return str(random.randint(1, 100))

    if p_message == 'joke':
        return pyjokes.get_joke()

    else:
        return None
