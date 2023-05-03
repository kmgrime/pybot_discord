# Discord Bot with Responses

[![Size](https://img.shields.io/github/languages/code-size/kmgrime/pybot_discord)](https://github.com/kmgrime/pybot_discord)
[![Downloads](https://img.shields.io/github/downloads/kmgrime/pybot_discord/total)](https://github.com/kmgrime/pybot_discord)
[![License](https://img.shields.io/github/license/kmgrime/pybot_discord)](https://github.com/kmgrime/pybot_discord/blob/main/LICENSE)

This is a Python script for a basic Discord bot that responds to specific commands or messages. The bot will respond to messages with certain keywords or commands, such as "hello" or "!roll". It also includes PyJokes package to add some humor to its responses.

## Installation

1. Clone this repository to your local machine.
2. Install the necessary Python packages by running the following command:

```sh
pip install -r requirements.txt
```

1. Create a new Discord bot and obtain its token. You can follow the steps [here](https://discordpy.readthedocs.io/en/stable/discord.html) to create a bot and obtain its token.
2. Replace the `TOKEN` variable in the code with your bot's token.

## Usage

To start the bot, run the following command in your terminal or command prompt:

```sh
python bot.py
```

The bot will now be online and listening for messages in the Discord server it's been added to. The bot responds to the following commands:

- `!roll`: Generates a random number between 1 and 100.
- `!help`: Displays the available commands.
- `!joke`: Returns a random joke using the PyJokes package.
- `hello`: Responds with "Hello there!".

The bot also logs messages it receives, printing the author's username, message content, and channel it was sent in.

## Docker

#### Prerequisites

- Docker

To run the bot in a container you simply clone the repository and build the image with the following commands

```
docker build -t discordpybot:0.0.1 .
```

```
docker run 'imageID'
```

Then you can check if the container is up and running by typing:

```
docker ps
```

---

## Contributing

If you have any suggestions for improvements or new features to add to the bot, feel free to open an issue or submit a pull request.

## Credits

This bot uses the following Python packages:

- `discord.py`: For creating the bot and interacting with the Discord API.
- `pyjokes`: For generating random jokes to include in the bot's responses.

## License

This project is licensed under the [MIT License](https://github.com/kmgrime/pybot_discord/blob/main/LICENSE).
