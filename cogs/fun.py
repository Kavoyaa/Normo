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

	# 8ball command
	@commands.command(name='8ball', aliases=['8Ball', '8BALL', 'eightball', 'Eightball', 'EIGHTBALL', 'EightBall', 'eightBall'], description='Ask the magic 8-ball a question!')
	async def eightball(self, ctx, question):
		'''Gives a random response from the list below'''
		responses = [
		'https://cdn.discordapp.com/attachments/877916745745195060/887553440924983326/IMG_20210915_092503.png', # Yes.
		'https://cdn.discordapp.com/attachments/877916745745195060/887553441122099200/IMG_20210915_092612.png', # It is certain.
		'https://cdn.discordapp.com/attachments/877916745745195060/887553441319256094/IMG_20210915_092710.png', # Without a doubt.
		'https://cdn.discordapp.com/attachments/877916745745195060/887553441457664041/IMG_20210915_092842.png', # Yes, definetly.
		'https://cdn.discordapp.com/attachments/877916745745195060/887553441667354624/IMG_20210915_093651.png', # You may rely on it.
		'https://cdn.discordapp.com/attachments/877916745745195060/887553442023866398/IMG_20210915_093805.png', # As I see it, yes.
		'https://cdn.discordapp.com/attachments/877916745745195060/887553442376220682/IMG_20210915_093921.png', # Most likely.
		'https://cdn.discordapp.com/attachments/877916745745195060/887553442711760896/IMG_20210915_094026.png', # Outlook good.
		'https://cdn.discordapp.com/attachments/877916745745195060/887553443135381514/IMG_20210915_094154.png', # It is decidely so.
		'https://cdn.discordapp.com/attachments/877916745745195060/887553443546419210/IMG_20210915_094226.png' # Signs point to yes.
		]

		embed = discord.Embed(color=0x000099)
		embed.set_image(url=random.choice(responses))

		await ctx.send(f'"{question}"', embed=embed)
		print(f'[LOGS] Command used: {p}8ball')

	#Coinflip command
	@commands.command(name='coinflip', aliases=['Coinflip', 'COINFLIP', 'CoinFlip', 'coinFlip'], description='Flips a coin!')
	async def coinflip(self, ctx):
		'''Says either heads or tails.'''
		responses = ['Heads!', 'Tails!']

		await ctx.reply(random.choice(responses))
		print(f'[LOGS] Command used: {p}coinflip')

	#Choose command
	@commands.command(name='choose', aliases=['Choose', 'CHOOSE'], description='Chooses a random item from the given input.\n**Example for usage:**\n`.choose apple mango`\n**Output:** `apple`\nYou can put as many items as you like.')
	async def choose(self, ctx, items):
		'''Chooses a random item from the given input'''
		output = items.split()

		await ctx.reply(random.choice(output))
		print(f'[LOGS] Command used: {p}choose')

	# Kill command
	@commands.command(name='kill', aliases=['Kill', 'KILL', 'keel', 'Keel', 'KEEL', 'keal', 'Keal', 'KEAL'], description='Kill your enemies!')
	async def kill(self, ctx, user: discord.Member, *, reason_=''):
		'''Sends a random GIF from the list below'''
		gifs = [
		'https://media1.tenor.com/images/a80b2bf31635899ac0900ea6281a41f6/tenor.gif?itemid=5535365',
		'https://media1.tenor.com/images/bb4b7a7559c709ffa26c5301150e07e4/tenor.gif?itemid=9955653',
		'https://media1.tenor.com/images/eb7fc71c616347e556ab2b4c813700d1/tenor.gif?itemid=5840101',
		'https://media1.tenor.com/images/2c945adbbc31699861f411f86ce8058f/tenor.gif?itemid=5459053',
		'https://media1.tenor.com/images/795bf8203af5b4a5d0713a8a2c2a0bcf/tenor.gif?itemid=18595358'
		]

		embed = discord.Embed(description=reason_, color=discord.Color.random())

		embed.set_author(name=f'{ctx.author.name} is killing {user.name}!', icon_url=ctx.author.avatar_url)

		embed.set_image(url=random.choice(gifs))

		embed.set_footer(text=f'{ctx.author.name} killed {user.name}. RIP💀')

		await ctx.send(embed=embed)
		print(f'[LOGS] Command used: {p}kill')

	# Inspire command
	@commands.command(name='inspire', aliases=['Inspire', 'INSPIRE', 'motivate', 'Motivate', 'MOTIVATE'], description='Shows a random inspirational quote.')
	async def inspire(self, ctx):
		'''Shows random inspirational quote'''
		response = requests.get('https://api.quotable.io/random')
		res = response.json()
		content = res['content']
		author = res['author']

		embed = discord.Embed(description=f'**"{content}"**\n-{author}', colour=0x00FF00)

		await ctx.reply(embed=embed)
		print(f'[LOGS] Command used: {p}inspire')

	# Hello command
	@commands.command(name='hello', aliases=['Hello', 'HELLO'], description='Feeling lonely? Have the bot say hello to you!')
	async def hello(self, ctx):
		'''Says hello'''
		await ctx.reply(f'Hello {ctx.author.mention}!')
		print(f'[LOGS] Command used: {p}hello')

	# Afk command
	@commands.command(name='afk', aliases=['Afk', 'AFK'], description='Tells people that you are AFK.')
	async def afk(self, ctx):
		'''Says <ctx.author> is AFK'''
		await ctx.send(f'{ctx.author.mention} is AFK!')
		print(f'[LOGS] Command used: {p}afk')

	# Bye command
	@commands.command(name='bye', aliases=['Bye', 'BYE'], description='Says bye. Yep, that\'s it. Bye.')
	async def bye(self, ctx):
		'''Says bye'''
		await ctx.reply(f'Bye-bye {ctx.author.mention}!')
		print(f'[LOGS] Command used: {p}bye')

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

	# Yomama command
	@commands.command(name='yomama', aliases=['Yomama', 'YOMAMA', 'YoMama', 'yoMama'], description='Tells a yomama joke.\nYo mama so fat I couldn\'t fit the entire joke about her here.')
	async def yomama(self, ctx):
		res = requests.get("https://api.yomomma.info/")
		r = res.json()
		joke = r['joke']

		await ctx.send(joke)
		print(f'[LOGS] Command used: {p}yomama')

def setup(client):
	client.add_cog(Fun(client))
