# Koetsu
A "do-everything" Discord bot (not now).

# Getting started

**DISCLAIMER** You need to work in a environment with Python 3.4.2 or newer (NOT 3.7+), since the main Discord module doesn't work below or above these Python versions.

### Python

Let's start with some requirements, shall we?
* `AioHTTP` library
* `websockets` library
* `PyNaCl` library (optional, you can install it if you want to try to use the voice)
* `libffi` library, necessary if use Linux. You can install it on Debian based distro by writing `sudo apt-get install libffi-dev`.

The Discord API module that you need to install is discord.py, downloadable with this command:

`python -m pip install discord.py`

### Discord Bot

In order to make a working Discord Bot, you need to create an application on [Discord Developers page](https://discordapp.com/developers/applications/ "Discord Developers") first.

After you specified the name of the application, you need to go in Bot section, available under Settings in the sidebar on the left.

Now, press the Add Bot button, and... congratulations! You created the bot. But there's one step left. You need to reveal the token, which is like your bot's password, so you **need** to keep this really secret, because a bad person can use it to make bad things. And we don't this to happen, right?

We are almost at the end of the bot's setup! Go into the repo's `main.py` file, and on the 4th line, replace `YOUR_DISCORD_BOT_TOKEN_HERE` with the token you've generated. And now, you did it! A basic Discord bot is now working.
