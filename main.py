# Importing modules
import discord
from discord.ext import commands
import os
import dotenv

# Set this to prefix of your choice.
p = "."
client = commands.Bot(command_prefix = p)

# Removes the default 'help' command so we can use our own custom one.
client.remove_command("help")

# When bot comes online
@client.event
async def on_ready():
    print("[BOT ONLINE]\nLogged in as {0.user}.\n".format(client))

# Loads the cogs
for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')

'''
Gets the environment variable 'TOKEN' from a '.env' file.
This is to hide the bot token.
If you want do the same, make a file called '.env' and put "TOKEN = <your_bot_token>" in it.
'''
dotenv.load_dotenv()
client.run(os.environ.get("TOKEN"))
