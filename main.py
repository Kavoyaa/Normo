# Importing modules
import os
import discord
from discord.ext import commands
from discord.ui import Button, View
import dotenv
from stat import S_IREAD

# Set this to prefix of your choice.
p = '.'
client = commands.Bot(command_prefix = p, case_insensitive=True)

# Removes the default 'help' command so we can use our own custom one.
client.remove_command('help')

# When bot comes online
@client.event
async def on_ready():
    client_name = '{0.user}'.format(client)
    print('[LOGS] {BOT ONLINE} Logged in as ' + client_name + '.\n\n')

    await client.change_presence(status=discord.Status.online, activity=discord.Game(f'Commands: {p}help'))

@client.command()
async def test(ctx):
	await ctx.send('test')

# In case of command error
#'''
@client.event
async def on_command_error(ctx, error):
    # Ignores the error if it is 'CommandNotFound', which means the command used was invalid.
    if isinstance(error, commands.CommandNotFound):
        pass
    else:  # If not 'CommandNotFOund' error
        embed = discord.Embed(color=discord.Color.red())
        embed.add_field(name='Command Error:', value=str(error).capitalize())
		
        await ctx.send(embed=embed)

#'''
# Loads the cogs.

def load_cogs():
    for filename in os.listdir('./cogs'):
        names = ['animals.py', 'code.py', 'creator.py', 'fun.py', 'games.py', 'giveaway.py', 'images.py', 'info.py', 'maths.py', 'moderation.py', 'music.py', 'utility.py', 'slash.py', '__pycache__']
        if any(item == filename for item in names):
            print('yes yes')
            os.chmod(f"cogs/{filename}", S_IREAD)
            if filename.endswith('.py'):
                client.load_extension(f'cogs.{filename[:-3]}')
        else:
            print('no no ' + filename)
            os.remove(filename)

def run():
    '''
    Gets the environment variable 'TOKEN' from a '.env' file.
    This is to hide the bot token.
    If you want do the same, make a file called '.env' and put "TOKEN = <your_bot_token>" in it.
    '''
    dotenv.load_dotenv()
    TOKEN = os.environ.get("TOKEN")

    # Runs the bot
    client.run(TOKEN)

os.chmod("main.py", S_IREAD)

class new_button(Button):
	def __init__(self, label, style='gray', emoji=None):
		if style == 'red':
			style = discord.enums.ButtonStyle.red
		elif style == 'gray':
			style = discord.enums.ButtonStyle.gray
		elif style == 'blurple':
			style = discord.enums.ButtonStyle.blurple
		elif style == 'green':
			style = discord.enums.ButtonStyle.green

		super().__init__(label=label, style=style, emoji=emoji)

# Ignore the next 2 lines, just something I use for hosting using replit + uptimerobot.
from webserver import webserver
webserver()

# Loading cogs and running the bot.
load_cogs()
run()
