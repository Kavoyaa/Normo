import discord
from discord.ext import commands
from discord.commands import slash_command, Option, SlashCommandGroup
import requests
import os
import random
from PIL import Image
import PIL.ImageOps  
from io import BytesIO

class Slash(commands.Cog):
	global p

	def __init__(self, client):
		self.client = client

	# When the cog is loaded
	@commands.Cog.listener()
	async def on_ready(self):
		print(f'[LOGS] {self.__class__.__name__} cog has been loaded.\n')
	
	# /cat
	@slash_command(name='cat', description='Shows a random cat picture 😻!')
	async def slashCat(self, ctx):
		key = os.environ['CAT_API_KEY']

		res = requests.get(f'https://api.thecatapi.com/v1/images/search?api_key={key}')
		r = res.json()
		url = r[0]['url']

		embed = discord.Embed(description='**[Meow😻](https://thecatapi.com/)**', color=discord.Color.random())
		embed.set_image(url=url)
		embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)

		await ctx.respond(embed=embed)
	
	# /dog
	@slash_command(name='dog', description='Shows a random dog picture 🐶!')
	async def slashDog(self, ctx):
		'''Sends a random dog picture.'''
		res = requests.get('https://dog.ceo/api/breeds/image/random')
		r = res.json()
		url = r['message']

		embed = discord.Embed(description='**[Woof🐶](https://dog.ceo/)**', color=discord.Color.random())
		embed.set_image(url=url)
		embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)

		await ctx.respond(embed=embed)
	
	# /emojify
	@slash_command(name='emojify', description='Make the bot say whatever you want with emojis!')
	async def slashEmojify(self, ctx, text: Option(str, "The text you want to emojify.")):
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
		
		await ctx.respond(output)
	
	# /8ball
	@slash_command(name='8ball', description='Ask the magic 8-ball a question!')
	async def slashEightBall(self, ctx, question: Option(str, "The question you want to ask the magic 8ball.")):
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

		await ctx.respond(f'*\🎱"{question}"\🎱*', file=file, embed=embed)

	# /meme
	@slash_command(name='meme', description='Shows a random meme from Reddit.')
	async def slashMeme(self, ctx):
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

			await ctx.respond(embed=embed)
			print(f'[LOGS] Command used: {p}meme | NSFW error')
		else:
			embed = discord.Embed(description=f'**[{title}]({url})**', color=discord.Color.random())

			embed.set_image(url=url)

			await ctx.respond(embed=embed)
	
	# /dictionary
	@slash_command(name='dictionary', description='Gets the dictionary information about a word.')
	async def slashDictionary(self, ctx, word: Option(str, 'The word you want dictionary information about.')):
		try:
			res = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word.lower()}")
			r = res.json()
		
			meanings = r[0]['meanings']
			partOfSpeech0 = meanings[0]['partOfSpeech']
			definition0 = meanings[0]['definitions'][0]['definition']

			try:
				partOfSpeech1 = meanings[1]['partOfSpeech']
				definition1 = meanings[1]['definitions'][0]['definition']
			except:
				pass

			try:
				await ctx.respond(f"**{r[0]['word']}**\n/{r[0]['phonetic']}/\n\n**{partOfSpeech0}**\n{definition0}\n\n**{partOfSpeech1}**\n{definition1}")
				print(f'[LOGS] Command used: {p}dictionary')
			except:
				await ctx.respond(f"**{r[0]['word']}**\n/{r[0]['phonetic']}/\n\n**{partOfSpeech0}**\n{definition0}")
				print(f'[LOGS] Command used: {p}dictionary')
		except:
			embed = discord.Embed(color=discord.Color.red())
			embed.add_field(name='Command Error:', value=f"Word '{word.lower()} not found.")
			await ctx.respond(embed=embed)
	
	# /inspire
	@slash_command(name='inspire', description='Sends a random inspirational quote.')
	async def slashInspire(self, ctx):
		'''Shows random inspirational quote'''
		response = requests.get('https://api.quotable.io/random')
		res = response.json()
		content = res['content']
		author = res['author']

		embed = discord.Embed(description=f'**"{content}"**\n-{author}', colour=0x00FF00)

		await ctx.respond(embed=embed)
	
	# /say
	@slash_command(name='say', description='Have the bot say something!')
	async def slashSay(self, ctx, message: Option(str, "The message the bot will say.")):
		await ctx.respond(message)
	
	# /binary
	@slash_command(name='binary', description='Converts the given input to ASCII binary.')
	async def slashBinary(self, ctx, input: Option(str, "The text to be converted to binary.")):
		res = ''.join(format(ord(i), '08b') for i in input)
		output = str(res)

		await ctx.respond(output)

	# /convert
	@slash_command(name='convert', description='Converts the given input to ASCII binary.')
	async def slashConvert(self, ctx, input: Option(str, "The binary code which will be converted to text(make sure it's ASCII binary).")):
		try:
			if " " in input:
				input = input.replace(" ", "")
			binary_int = int(input, 2)
			byte_number = binary_int.bit_length() + 7 // 8
			binary_array = binary_int.to_bytes(byte_number, "big")
			converted_text = binary_array.decode()

			await ctx.respond(converted_text)
		except:
			embed = discord.Embed(color=discord.Color.red())
			embed.add_field(name='Command Error:', value="The given binary code is either not valid or it isn't ASCII binary.")
			await ctx.respond(embed=embed, ephemeral=True)
	
	# /image group
	images = SlashCommandGroup("image", "Image commands.")

	# /image wanted
	@images.command(name='wanted', description='Creates a wanted poster of the given user!')
	async def slashWanted(self, ctx, user: Option(discord.Member, "The user you want to use the command with.", required=False, default=None)):
		if user == None:
			user = ctx.author

		wanted = Image.open('images/wanted.jpg')
		asset = user.display_avatar.with_size(128)
		data = BytesIO(await asset.read())
		pfp = Image.open(data)
		pfp = pfp.resize((177, 177))
		wanted.paste(pfp, (120, 212))
		# Creates a 'slash_wanted_output.jpg' which gets sent as output
		wanted.save('slash_wanted_output.jpg')

		await ctx.respond(file = discord.File('slash_wanted_output.jpg'))

		# Deletes the saved image file
		os.remove('slash_wanted_output.jpg')

	# /image cmon
	@images.command(name="cmon", description='Generates a "C\'mon do something" meme with the profile picture of the given user!')
	async def slashCmon(self, ctx, user: Option(discord.Member, "The user you want to use the command with.", required=False, default=None)):
		if user == None:
			user = ctx.author

		wanted = Image.open('images/cmon.jpg')
		asset = user.display_avatar.with_size(128)
		data = BytesIO(await asset.read())
		pfp = Image.open(data)
		pfp = pfp.resize((177, 177))
		wanted.paste(pfp, (120, 212))
		# Creates a 'slash_cmon_output.jpg' which gets sent as output
		wanted.save('slash_cmon_output.jpg')

		await ctx.respond(file = discord.File('slash_cmon_output.jpg'))

		# Deletes the saved image file
		os.remove('slash_cmon_output.jpg')

	# /image delete
	@images.command(name="delete", description='"deletes" the given user :)')
	async def slashDelete(self, ctx, user: Option(discord.Member, "The user you want to use the command with.", required=False, default=None)):
		if user == None:
			user = ctx.author

		wanted = Image.open('images/delete.jpg')
		asset = user.display_avatar.with_size(128)
		data = BytesIO(await asset.read())
		pfp = Image.open(data)
		pfp = pfp.resize((195, 195))
		wanted.paste(pfp, (120, 135))
		# Creates a 'slash_delete_output.jpg' which gets sent as output
		wanted.save('slash_delete_output.jpg')

		await ctx.respond(file = discord.File('slash_delete_output.jpg'))

		# Deletes the saved image file
		os.remove('slash_delete_output.jpg')

def setup(client):
	client.add_cog(Slash(client))
	