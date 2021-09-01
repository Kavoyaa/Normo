import discord
from discord.ext import commands
from main import p
import random
import requests

class Fun(commands.Cog):
	global p

	def __init__(self, client):
		self.client = client

	# When the cog is loaded
	@commands.Cog.listener()
	async def on_ready(self):
		print(f'[LOGS] {self.__class__.__name__} cog has been loaded.\n')

	# Joke command
	@commands.command(name='joke', aliases=['Joke', 'JOKE'], description='Shows a random joke.')
	async def joke(self, ctx):
		'''Shows a random joke.'''
		def joke1():
			res = requests.get('https://official-joke-api.appspot.com/random_joke')
			r = res.json()
			setup = r['setup']
			punchline = r['punchline']

			return f'**{setup}**\n\n||{punchline}||'

		def joke2():
			res = requests.get('https://v2.jokeapi.dev/joke/Miscellaneous,Dark,Pun,Spooky,Christmas?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=twopart')
			r = res.json()
			setup = r['setup']
			punchline = r['delivery']

			return f'**{setup}**\n\n||{punchline}||'

		randomNum = random.randint(1, 2)

		if randomNum == 1:
			await ctx.send(joke1())
			print(f'[LOGS] Command used: {p}joke')
		elif randomNum == 2:
			await ctx.send(joke2())
			print(f'[LOGS] Command used: {p}joke')

	# Meme command
	@commands.command(name='meme', aliases=['Meme', 'MEME'], description='Shows a random meme from Reddit.')
	async def meme(self, ctx):
		'''Shows a random meme from Reddit using 1 of 3 different APIs'''
		randomNum = random.randint(1, 4)

		# API one.
		if randomNum == 1:
			links = [
			'https://meme-api.herokuapp.com/gimme/i_irl',
			'https://meme-api.herokuapp.com/gimme/memes',
			'https://meme-api.herokuapp.com/gimme/me_irl',
			'https://meme-api.herokuapp.com/gimme/dankmemes',
			]

			res = requests.get(random.choice(links))
			r = res.json()
			title = r['title']
			url = r['url']
			nsfw = r['nsfw']
		# Same API as above if statement.
		elif randomNum == 2:
			links=[
			'https://meme-api.herokuapp.com/gimme/bonehurtingjuice',
			'https://meme-api.herokuapp.com/gimme/trippinthroughtime',
			'https://meme-api.herokuapp.com/gimme/technicallythetruth'
			]
		# API two.
		elif randomNum == 3:
			links= [
			'https://reddit-meme-api.herokuapp.com/'
			]

			res = requests.get(random.choice(links))
			r = res.json()
			title = r['title']
			url = r['url']
			nsfw = r['nsfw']
		# API three.
		elif randomNum == 4:
			links = [
			'https://memes.blademaker.tv/api'
			]

			res = requests.get(random.choice(links))
			r = res.json()
			title = r['title']
			url = r['image']
			nsfw = r['nsfw']

		# Checks if the meme is NSFW or not; Dosen't send the meme if it's NSFW.
		if nsfw:
			embed = discord.Embed(description='An error occured, please try again!', color=0xFF0000)

			await ctx.reply(embed=embed)
			print(f'[LOGS] Command used: {p}meme | NSFW error')
		else:
			embed = discord.Embed(description=f'**[{title}]({url})**', color=discord.Color.random())

			embed.set_image(url=url)

			await ctx.reply(embed=embed)
			print(f'[LOGS] Command used: {p}meme')

def setup(client):
	client.add_cog(Fun(client))
