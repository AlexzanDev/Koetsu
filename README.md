# Koetsu
A "do-everything" Discord bot (not now).

# Setup

Let's start with some requirements, shall we?
* `AioHTTP` library
* `websockets` library
* `PyNaCl` library (optional, you can install it if you want to try to use the voice)
* `libffi` library, necessary if use Linux. You can install it on Debian based distro by writing `sudo apt-get install libffi-dev`.

The Discord API module that you need to install is discord.py, downloadable with this command:

`python -m pip install discord.py`

**WARNING** This module works only with Python 3.4.2 and newer (NOT 3.7+)
