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

	# Fact command
	@commands.command(name='fact', description='Show a random fact!')
	async def fact(self, ctx):
		'''Sends a random fact.'''

		res = requests.get('https://uselessfacts.jsph.pl/random.json?language=en')
		r = res.json()
		fact = r['text']

		embed = discord.Embed(title='Random Fact', description=f'{fact}', color=discord.Color.blue())

		await ctx.send(embed=embed)
	
	# Emojify command
	@commands.command(name='emojify', description='Make the bot say whatever you want with emojis!')
	async def emojify(self, ctx, *, text):
		'''Converts the given text into emojis.'''
		text = text.lower()
		output = ''
		for char in text:
			if char == " ":
				output += "      "
			if char in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '!', '?', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '*', '#']:
				if char == '1':
					char = ":one:"
				elif char == "2":
					char = ":two:"
				elif char == "3":
					char = ":three:"
				elif char == "4":
					char = ":four:"
				elif char == "5":
					char = ":five:"
				elif char == "6":
					char = ":six:"
				elif char == "7":
					char = ":seven:"
				elif char == "8":
					char = ":eight:"
				elif char == "9":
					char = ":nine:"
				elif char == "0":
					char = ":zero:"
				elif char == "!":
					char = ":grey_exclamation:"
				elif char == "?":
					char = ":grey_question:"
				elif char == "#":
					char = ":hash:"
				elif char == "*":
					char = ":asterisk:"
				else:
					char = char.replace(char, f":regional_indicator_{char}:")
				output += char
			else:
				output += char
		
		await ctx.send(output)

	# 8ball command
	@commands.command(name='8ball', aliases=['magicball', 'magic8ball'], description='Ask the magic 8-ball a question!')
	async def eightball(self, ctx, *, question):
		'''Sends an embed with a randoom image from the list below'''
		responses = [
		'as_i_see_it_yes',
		'ask_again_later',
		'better_not_tell_you_now',
		'cannot_predict_now',
		'concentrate_and_ask_again',
		'dont_count_on_it.',
		'it_is_certain',
		'it_is_decidely_so',
		'most_likely',
		'my_reply_is_no',
		'no',
		'outlook_good',
		'reply_hazy_try_again',
		'signs_point_to_yes',
		'very_doubtful',
		'without_a_doubt',
		'yes_definitely',
		'yes',
		'you_may_rely_on_it',
		]

		img = random.choice(responses)
		file = discord.File(f'images/8ball/{img}.png')

		embed = discord.Embed(color=0x000099)
		embed.set_image(url=f'attachment://{img}.png')
		embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)

		await ctx.send(f'*\🎱"{question}"\🎱*', file=file, embed=embed)
		print(f'[LOGS] Command used: {p}8ball')

	#Coinflip command
	@commands.command(name='coinflip', description='Flips a coin!')
	async def coinflip(self, ctx):
		'''Says either heads or tails.'''
		responses = ['Heads!', 'Tails!']

		await ctx.reply(random.choice(responses), mention_author=False)
		print(f'[LOGS] Command used: {p}coinflip')

	#Choose command
	@commands.command(name='choose', description='Chooses a random item from the given input.\n**Example for usage:**\n`.choose apple mango`\n**Output:** `apple`\nYou can put as many items as you like.')
	async def choose(self, ctx, *, items):
		'''Chooses a random item from the given input'''
		output = items.split()

		await ctx.reply(random.choice(output), mention_author=False)
		print(f'[LOGS] Command used: {p}choose')

	# Kill command
	@commands.command(name='kill', aliases=['keel', 'keal'], description='Kill your enemies!')
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

		embed.set_author(name=f'{ctx.author.name} is killing {user.name}!', icon_url=ctx.author.avatar.url)

		embed.set_image(url=random.choice(gifs))

		embed.set_footer(text=f'{ctx.author.name} killed {user.name}. RIP💀')

		await ctx.send(embed=embed)
		print(f'[LOGS] Command used: {p}kill')

	# Inspire command
	@commands.command(name='inspire', aliases=['motivate'], description='Shows a random inspirational quote.')
	async def inspire(self, ctx):
		'''Shows random inspirational quote'''
		response = requests.get('https://api.quotable.io/random')
		res = response.json()
		content = res['content']
		author = res['author']

		embed = discord.Embed(description=f'**"{content}"**\n-{author}', colour=0x00FF00)

		await ctx.reply(embed=embed, mention_author=False)
		print(f'[LOGS] Command used: {p}inspire')

	# Hello command
	@commands.command(name='hello', description='Feeling lonely? Have the bot say hello to you!')
	async def hello(self, ctx):
		'''Says hello'''
		await ctx.reply(f'Hello {ctx.author.mention}!')
		print(f'[LOGS] Command used: {p}hello')

	# Afk command
	@commands.command(name='afk', description='Tells people that you are AFK.')
	async def afk(self, ctx):
		'''Says <ctx.author> is AFK'''
		await ctx.send(f'{ctx.author.mention} is AFK!')
		print(f'[LOGS] Command used: {p}afk')

	# Bye command
	@commands.command(name='bye', description='Says bye. Yep, that\'s it. Bye.')
	async def bye(self, ctx):
		'''Says bye'''
		await ctx.reply(f'Bye-bye {ctx.author.mention}!')
		print(f'[LOGS] Command used: {p}bye')

	# Joke command
	@commands.command(name='joke', description='Shows a random joke.')
	async def joke(self, ctx):
		'''Shows a random joke.'''

		'''
		def joke1():
			res = requests.get('https://v2.jokeapi.dev/joke/Miscellaneous,Dark,Pun,Spooky,Christmas?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=twopart')
			r = res.json()
			setup = r['setup']
			punchline = r['delivery']

			return f'**{setup}**\n\n||{punchline}||'


		def joke2():
			res = requests.get('https://official-joke-api.appspot.com/random_joke')
			r = res.json()
			setup = r['setup']
			punchline = r['punchline']

			return f'**{setup}**\n\n||{punchline}||'

		randomNum = random.randint(1, 2)

		if randomNum == 1:
			await ctx.send(joke1())
			print(f'[LOGS] Command used: {p}joke')
		elif randomNum == 2:
			await ctx.send(joke2())
			print(f'[LOGS] Command used: {p}joke')
		'''

		await ctx.reply('All the APIs used for this command died so the command is temporarily disabled. Sadge.')

	# Meme command
	@commands.command(name='meme', description='Shows a random meme from Reddit.')
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

			res = requests.get(random.choice(links))
			r = res.json()
			title = r['title']
			url = r['url']
			nsfw = r['nsfw']
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

			await ctx.reply(embed=embed, mention_author=False)
		else:
			embed = discord.Embed(description=f'**[{title}]({url})**', color=discord.Color.random())

			embed.set_image(url=url)

			await ctx.reply(embed=embed, mention_author=False)

	# Yomama command
	@commands.command(name='yomama', aliases=['yomomma', 'yomoma'], description='Tells a yomama joke.\nYo mama so fat I couldn\'t fit the entire joke about her here.')
	async def yomama(self, ctx):
		res = requests.get("https://api.yomomma.info/")
		r = res.json()
		joke = r['joke']

		await ctx.reply(joke, mention_author=False)

	# Uwu command
	@commands.command(name='uwu', description='UwU.')
	async def uwu(self, ctx):
		await ctx.send('**UwU**')

	# Owo command
	@commands.command(name='owo', description='OwO.')
	async def owo(self, ctx):
		await ctx.send('**OwO**')

	# Say command
	@commands.command(name='say', description='Have the bot say something!')
	async def say(self, ctx, *, message):
		await ctx.send(message)

def setup(client):
	client.add_cog(Fun(client))
