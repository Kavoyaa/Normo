import discord
from discord.ext import commands
from main import p
import os
import dotenv
import requests

class Animals(commands.Cog):
	global p

	def __init__(self, client):
		self.client = client

	# When the cog is loaded
	@commands.Cog.listener()
	async def on_ready(self):
		print(f'[LOGS] {self.__class__.__name__} cog has been loaded.\n')

	@commands.command(name='cat', aliases=['Cat', 'CAT'], description='Shows a random cute cat picture 😻!')
	async def cat(self, ctx):
		'''
		Gets the environment variable 'TOKEN' from a '.env' file.
		This is to hide the cat API's key.
		If you want do the same, make a file called '.env' and put "CAT_API_KEY = <your_catAPI_key>" in it.
		'''
		dotenv.load_dotenv()
		key = os.environ.get('CAT_API_KEY')

		res = requests.get(f'https://api.thecatapi.com/v1/images/search?api_key={key}')
		r = res.json()
		url = r[0]['url']

		embed = discord.Embed(description=f'[Meow😻]({url})', color=discord.Color.random())

		embed.set_image(url=url)

		await ctx.reply(embed=embed)
		print(f'[LOGS] Command used: {p}cat')

def setup(client):
	client.add_cog(Animals(client))
