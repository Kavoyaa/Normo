import discord
from discord.ext import commands
import os
import dotenv

# Set this to prefix of your choice
p = "."
client = commands.Bot(command_prefix = p)

# Removes the default 'help' command
client.remove_command("help")

@client.event
async def on_ready():
    print("[BOT ONLINE]\nLogged in as {0.user}.\n".format(client))

for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')

dotenv.load_dotenv()
client.run(os.environ.get("TOKEN"))
