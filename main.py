# Import Discord module stated in the documentation
import discord

token = 'YOUR_DISCORD_BOT_TOKEN_HERE'

client = discord.Client()

@client.event
async def on_message(message):

    # Koetsu needs to know that only user's messages are readable
    if message.author == client.user:
        return

    # Stupid input command and output
    if message.content.startswith('.hello'):
        msg = 'Hello {0.author.mention}!'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('.ping'):
        msg = 'Pong!'.format(message)
        await client.send_message(message.channel, msg)

# Koetsu's output on IDE or console when it starts correctly
@client.event
async def on_ready():
    print('I\'m online!')

    # Set bot status in what you want
    await client.change_presence(game=discord.Game(name="Helping people to have fun!"))

client.run(token)
