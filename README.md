# Discord Bot with Responses

[![Size](https://img.shields.io/github/languages/code-size/kmgrime/pybot_discord)](https://github.com/kmgrime/pybot_discord)
[![License](https://img.shields.io/github/license/kmgrime/pybot_discord)](https://github.com/kmgrime/pybot_discord/blob/main/LICENSE)

This is a Python script for a basic Discord bot that responds to specific commands or messages. The bot will respond to messages with certain keywords or commands, such as "hello" or "!roll". It also includes PyJokes package to add some humor to its responses.

## Installation

1. **Clone this repository to your local machine**
Open your terminal or command prompt and run the following command:

```sh
git clone https://github.com/kmgrime/pybot_discord.git
```
2. **Install the necessary Python packages**
Navigate to the project directory and run:
```sh
pip install -r requirements.txt
```
3. **Create a New Discord Bot and Obtain its Token**
Follow the steps [here](https://discordpy.readthedocs.io/en/stable/discord.html) to create a bot and obtain its token.
4. **Replace the TOKEN Variable**
Open bot.py in a text editor, find the `TOKEN` variable, and replace it with your bot's token.


## Usage
1. **Starting the Bot**
Run the following command in your terminal or command prompt:
The bot will now be online and actively listening for messages in the Discord server to which it has been added.
```sh
python bot.py
```

2. **Available Commands**
- `!roll`: Generates a random number between 1 and 100.
- `!help`: Displays the available commands.
- `!joke`: Returns a random joke using the PyJokes package.
- `hello`: Responds with "Hello there!".
3. **Message Logging**
The bot logs messages it receives, displaying the author's username, message content, and the channel it was sent in.

## Docker

#### Prerequisites
**Docker**
**Building and Running the Image**
1. **Build the image:**
```
docker build -t discordpybot:0.0.1 .
```

2. **List the images to fetch image ID**
```
docker image list
```
3. **Build and run the image in a container**
```
docker run 'imageID'
```
4. **Verify if the container is up and running:**
```
docker ps
```

---

## Contributing
If you have any suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## Credits

This bot uses the following Python packages:

- `discord.py`: For creating the bot and interacting with the Discord API.
- `pyjokes`: For generating random jokes to include in the bot's responses.

## License

This project is licensed under the [MIT License](https://github.com/kmgrime/pybot_discord/blob/main/LICENSE).
