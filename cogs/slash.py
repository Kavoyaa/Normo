import discord
from discord.ext import commands
from discord.commands import slash_command, Option, SlashCommandGroup
import requests
import os
import random
from PIL import Image
import PIL.ImageOps  
from io import BytesIO
from pyston import PystonClient, File

async def run_code(ctx, language, codeblock_type, msg, comment, color, auto_detect):
	code = msg.content
	
	if code.count('`') < 6:
		await ctx.respond(f"**The code must be inside a codeblock.**\n\nHow to make a codeblock:\n\`\`\`{codeblock_type}\n[code]\n\`\`\`", ephemeral=True)
		return

	await msg.add_reaction("<a:colorfulloading:921304808256860171>")

	url = msg.jump_url

	code = code.split('```')
	code = code[1]
	code = code.splitlines(keepends=True)
	code = code[1:]

	co = ''
	for item in code:
		co += item

	pyston = PystonClient()
	output = await pyston.execute(language, [File(co)])
	success = output.success
	output = str(output)

	if output == "":
		output = "```\nNo Output\n```" 
	else:
		if len(output) > 980:
			output = output[:980]
			output = output + f"\n{comment} Size limit reached"
		
		if output.count('\n') > 51:
			o = output.split('\n')
			o = o[:51]
			
			result = ''
			for item in o:
				result += item + '\n'
			
			output = result + f'{comment} Length limit reached'

		output = f"```yaml\n{output}\n```"	
	
	click = f'Click [here]({url}) to see the code.'

	if auto_detect:
		embed = discord.Embed(color = color if success else discord.Color.red())
		embed.add_field(name='Program Output', value=output, inline=False)
		embed.add_field(name='Lang chosen by Auto-Detect:', value=f'```fix\n{language.capitalize()}\n```{click}', inline=False)
	elif not auto_detect:
		embed = discord.Embed(color = color if success else discord.Color.red())
		embed.add_field(name='Program Output', value=output+click, inline=False)

	embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)

	await ctx.respond(embed=embed)
	await msg.clear_reaction("<a:colorfulloading:921304808256860171>")

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
		'''Shows a random meme from Reddit'''
		def give_meme():
			response = requests.get("https://reddit-meme-api.herokuapp.com")
			res = response.json()

			post = res['post_link']
			title = res['title']
			url = res['url']
			ups = res['ups']
			nsfw = res['nsfw']

			if nsfw: return discord.Embed(description='An unknown error occured. Please try again.', color=discord.Color.red())

			embed = discord.Embed(description=f'**[{title}]({post})**', color=discord.Color.random())
			embed.set_image(url=url)
			embed.set_footer(text=f'👍 {ups}')

			return embed

		await ctx.respond(embed=give_meme())

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
			except:
				await ctx.respond(f"**{r[0]['word']}**\n/{r[0]['phonetic']}/\n\n**{partOfSpeech0}**\n{definition0}")
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
	@slash_command(name='convert', description='Converts ASCII binary to text.')
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

	# /execute
	@slash_command(name='execute', description='Runs the code of the given langauge.')
	async def slashExecute(self, ctx, language: Option(str, "The language you want to run.", choices=['Auto-Detect', 'Python', 'JavaScript', 'C#', 'Java', 'C++', 'Rust', 'C', 'PHP']), message_id: Option(str, 'ID of the message with the code. You may need to type the message beforehand.')):
		try:
			msg = await ctx.fetch_message(int(message_id))
		except:
			await ctx.respond('**Invalid message ID.**\n\n**How to get message ID?**\nTurn on "Devloper Mode" then right click/hold a message and click/tap "Copy ID"\n\n**How to turn on "Devloper Mode"?**\n__Desktop:__\nSettings Area -> Under User Settings -> Advanced -> Devloper Mode\n\n__Mobile:__\nSettings Area -> Under App Settings -> Behaviour -> Devloper Mode', ephemeral=True)
			return

		auto = False
		if language == 'Auto-Detect':
			auto = True

			m = msg.content
			m = m.split('```')
			m = m[1]
			m = m.splitlines(keepends=True)[0]
			m = m.replace('\n', '')

			if m == 'cs' or m == 'csharp':
				language = "C#"
			elif m == 'py' or m == 'python':
				language = 'Python'
			elif m == 'js' or m == 'javascript':
				language = "JavaScript"
			elif m == 'java':
				language = 'Java'
			elif m == 'cpp' or m == 'c++':
				language = 'C++'
			elif m == 'c':
				language = 'C'
			elif m == 'rs' or m == 'rust':
				language = 'Rust'
			elif m == 'php':
				language = 'PHP'
			else:
				await ctx.respond('Auto-detect failed. Please manually select the language.', ephemeral=True)
				return

		if language == "C#":
			await run_code(ctx, "csharp", "cs", msg, "//", discord.Color.purple(), auto_detect=auto)
		elif language == "Python":
			await run_code(ctx, "python", "py", msg, "#", discord.Color.gold(), auto_detect=auto)
		elif language == "JavaScript":
			await run_code(ctx, "javascript", "js", msg, "//", 0xFFF200, auto_detect=auto)
		elif language == "Java":
			await run_code(ctx, "java", "java", msg, "//", 0x178DC9, auto_detect=auto)
		elif language == "C++":
			await run_code(ctx, "c++", "cpp", msg, "//", 0x1F6ABD, auto_detect=auto)
		elif language == "C":
			await run_code(ctx, "c", "c", msg, "//", 0x1F6ABD, auto_detect=auto)
		elif language == "Rust":
			await run_code(ctx, "rust", "rs", msg, "//", discord.Color.orange(), auto_detect=auto)
		elif language == 'PHP':
			await run_code(ctx, "php", "php", msg, "//", 0x787CB4, auto_detect=auto)

def setup(client):
	client.add_cog(Slash(client))
