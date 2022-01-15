import os
import discord
from discord.ext import commands
import dotenv

p = '.' # Set this to prefix of your choice.
client = commands.Bot(command_prefix=p, case_insensitive=True, intents=discord.Intents.all())

# Removes the default 'help' command.
client.remove_command('help')

# When bot comes online
@client.event
async def on_ready():
    client_name = '{0.user}'.format(client)
    print('[LOGS] {BOT ONLINE} Logged in as ' + client_name + '.\n\n')

    await client.change_presence(status=discord.Status.online, activity=discord.Game(f'Commands: {p}help'))

# In case of command error
#'''
@client.event
async def on_command_error(ctx, error):
    value =str(error).capitalize()
    if isinstance(error, commands.CommandNotFound):
        if '.' in value:
            return
        else:
            pass
    elif isinstance(error, commands.MissingPermissions):
        missing_perms = str(error.missing_permissions)
        missing_perms = missing_perms.replace('[', '')
        missing_perms = missing_perms.replace(']', '')

        value = f'You are missing the following permission(s):\n{missing_perms}'
    elif isinstance(error, commands.BotMissingPermissions):
        bot_missing_perms = str(error.missing_permissions)
        bot_missing_perms = missing_perms.replace('[', '')
        bot_missing_perms = missing_perms.replace(']', '')

        value = f'The bot is missing the following permission(s):\n{bot_missing_perms}'
    elif isinstance(error, commands.MissingRequiredArgument):
        value = str(error).capitalize()
    else:
        raise error
		
    embed = discord.Embed(color=discord.Color.red())
    embed.add_field(name='Command Error:', value=value)
		
    await ctx.send(embed=embed)	
#'''

# Loads the cogs.
def load_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}')

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

# Ignore the next 2 lines, just something I use for hosting using replit + uptimerobot.
from webserver import webserver
webserver()

# Loading cogs and running the bot.
load_cogs()
run()
