import nextcord as discord
from nextcord.ext import commands
import os
import requests

class Animals(commands.Cog):
	global p

	def __init__(self, client):
		self.client = client

	# When the cog is loaded
	@commands.Cog.listener()
	async def on_ready(self):
		print(f'[LOGS] {self.__class__.__name__} cog has been loaded.\n')

	# Cat command
	@commands.command(name='cat', aliases=['Cat', 'CAT', 'cats', 'Cats', 'CATS'], description='Shows a random cat picture 😻!')
	async def cat(self, ctx):
		'''
		Gets the environment variable 'TOKEN' from a '.env' file.
		This is to hide the cat API's key.
		If you want do the same, make a file called '.env' and put "CAT_API_KEY = <your_catAPI_key>" in it.
		'''
	
		key = os.environ['CAT_API_KEY']

		res = requests.get(f'https://api.thecatapi.com/v1/images/search?api_key={key}')
		r = res.json()
		url = r[0]['url']

		embed = discord.Embed(description='**[Meow😻](https://thecatapi.com/)**', color=discord.Color.random())
		embed.set_image(url=url)
		embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)

		await ctx.reply(embed=embed)

	# Dog command
	@commands.command(name='dog', aliases=['Dog', 'DOG' , 'dogs', 'Dogs', 'DOGS'], description='Shows a random dog picture 🐶!')
	async def dog(self, ctx):
		'''Sends a random dog picture.'''
		res = requests.get('https://dog.ceo/api/breeds/image/random')
		r = res.json()
		url = r['message']

		embed = discord.Embed(description='**[Woof🐶](https://dog.ceo/)**', color=discord.Color.random())
		embed.set_image(url=url)
		embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)

		await ctx.reply(embed=embed)
	
	# Fox command
	@commands.command(name='fox', aliases=['Fox', 'FOX', 'foxs', 'Foxs', 'FOXS', 'foxes', 'Foxes', 'FOXES'], description='Shows a random fox picture 🦊!')
	async def fox(self, ctx):
		'''Sends a random fox picture.'''
		res = requests.get('https://randomfox.ca/floof/')
		r = res.json()
		url = r['image']

		embed = discord.Embed(description='**[Fox🦊](https://randomfox.ca/)**', color=discord.Color.random())
		embed.set_image(url=url)
		embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)

		await ctx.reply(embed=embed)

	# Duck command
	@commands.command(name='duck', aliases=['Duck', 'DUCK', 'ducks', 'Ducks', 'DUCKS', 'ducc', 'Ducc', 'DUCC', 'dick', 'quack', 'Quack', 'QUACK'], description='Shows a random duck picture 🦆!')
	async def duck(self, ctx):
		'''Sends a random duck picture.'''
		res = requests.get('https://random-d.uk/api/v2/quack')
		r = res.json()
		url = r['url']

		embed = discord.Embed(description='**[Quack🦆](https://random-d.uk/)**', color=discord.Color.random())
		embed.set_image(url=url)
		embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)

		await ctx.reply(embed=embed)
	
	# Panda command
	@commands.command(name='panda', aliases=['Panda', 'PANDA', 'pandas', 'Pandas', 'PANDAS'], description='Shows a random panda picture 🐼!')
	async def panda(self, ctx):
		'''Sends a random panda picture.'''
		res = requests.get('https://some-random-api.ml/img/panda')
		r = res.json()
		url = r['link']

		embed = discord.Embed(description='**[Panda🐼](https://some-random-api.ml)**', color=discord.Color.random())
		embed.set_image(url=url)
		embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)

		await ctx.reply(embed=embed)
	
	# Bird command
	@commands.command(name='bird', aliases=['Bird', 'BIRD', 'birds', 'Birds', 'BIRDS', 'birb', 'Birb', 'BIRB'], description='Shows a random bird picture 🐦!')
	async def bird(self, ctx):
		'''Sends a random bird picture.'''
		res = requests.get('https://some-random-api.ml/img/birb')
		r = res.json()
		url = r['link']

		embed = discord.Embed(description='**[Birb🐦](https://some-random-api.ml)**', color=discord.Color.random())
		embed.set_image(url=url)
		embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)

		await ctx.reply(embed=embed)

	# Koala command
	@commands.command(name='koala', aliases=['Koala', 'KOALA', 'koalas', 'Koalas', 'KOALAS'], description='Shows a random koala picture 🐨!')
	async def koala(self, ctx):
		'''Sends a random koala picture.'''
		res = requests.get('https://some-random-api.ml/img/koala')
		r = res.json()
		url = r['link']

		embed = discord.Embed(description='**[Koala🐨](https://some-random-api.ml)**', color=discord.Color.random())
		embed.set_image(url=url)
		embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)

		await ctx.reply(embed=embed)
	
	# Raccoon command
	@commands.command(name='raccoon', aliases=['Raccoon', 'RACCOON', 'racoon', 'Racoon', 'RACOON', 'raccoons', 'Raccoons', 'RACCOONS'], description='Shows a random raccoon picture 🦝!')
	async def raccoon(self, ctx):
		'''Sends a random raccoon picture.'''
		res = requests.get('https://some-random-api.ml/animal/raccoon')
		r = res.json()
		url = r['image']

		embed = discord.Embed(description='**[Raccoooon🦝](https://some-random-api.ml)**', color=discord.Color.random())
		embed.set_image(url=url)
		embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)

		await ctx.reply(embed=embed)

def setup(client):
	client.add_cog(Animals(client))
