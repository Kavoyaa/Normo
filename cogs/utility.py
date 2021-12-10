import discord
from discord.ext import commands
from main import p
import requests
import matplotlib

import time
import os
import subprocess
import traceback
import re
import textwrap

class Utility(commands.Cog):
	global p

	def __init__(self, client):
		self.client = client

	# When the cog is loaded
	@commands.Cog.listener()
	async def on_ready(self):
		print(f'[LOGS] {self.__class__.__name__} cog has been loaded.\n')

	# Count command
	@commands.command(name='count', aliases=['Count', 'COUNT'], description='Counts the number of words in the given `text`.')
	async def count(self, ctx, *, text):
		words = text.split()
		number_of_words = len(words)

		if number_of_words == 1:
			await ctx.reply(f'There is {number_of_words} word in this text.\n*smh you can count that much yourself, why use me?*')
		else:
			await ctx.reply(f'There are {number_of_words} words in this text.')
			print(f'[LOGS] Command used: {p}count')

	# Binary command
	@commands.command(name='binary', aliases=['Binary', 'BINARY'], description='Converts the given `input` to ASCII binary.')
	async def binary(self, ctx, *, input):
		res = ''.join(format(ord(i), '08b') for i in input)
		output = str(res)

		await ctx.send(output)
		print(f'[LOGS] Command used: {p}binary')

	# Convert command
	@commands.command(name='convert', aliases=['Convert', 'CONVERT'], description='Converts the given `input`(which would/must be ASCII binary) to text.')
	async def convert(self, ctx, *, input):
		binary_int = int(input, 2)
		byte_number = binary_int.bit_length() + 7 // 8
		binary_array = binary_int.to_bytes(byte_number, "big")
		converted_text = binary_array.decode()

		await ctx.send(converted_text)
		print(f'[LOGS] Command used : {p}convert')

	# Reverse command
	@commands.command(name='reverse', aliases=['r', 'R', 'Reverse', 'REVERSE', 'esrever', 'ESREVER', 'Esrever'], description='Reverses the given text.')
	async def reverse(self, ctx, *, text):
		'''Reverses the given input(text).'''
		reversedString = ''

		for letter in text:
			reversedString = letter + reversedString

		await ctx.send(reversedString)
		print(f'[LOGS] Command used: {p}reverse')

	# Calculate command
	@commands.command(name='calculate', aliases=['Calculate', 'CALCULATE', 'c', 'C', 'calc', 'Calc', 'CALC', 'cal', 'Cal', 'CAL'], description='Evaluates the given input.\n`.help calc` for more info.')
	async def calculate(self, ctx, *, input):
		'''Evaluates the given input'''
		i = input
		if '__' in i:
			pass
		else:
			await ctx.reply(eval(input, {'__builtins__':{}}))
		print(f'[LOGS] Command used: {p}calculate')

	# Dictionary command
	@commands.command(name='dictionary', aliases=['Dictionary', 'DICTIONARY', 'dict', 'Dict', 'DICT'], description='Gets the dictionary information about a word.')
	async def dictionary(self, ctx, word):
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
			await ctx.send(f"**{r[0]['word']}**\n/{r[0]['phonetic']}/\n\n**{partOfSpeech0}**\n{definition0}\n\n**{partOfSpeech1}**\n{definition1}")
			print(f'[LOGS] Command used: {p}dictionary')
		except:
			await ctx.send(f"**{r[0]['word']}**\n/{r[0]['phonetic']}/\n\n**{partOfSpeech0}**\n{definition0}")
			print(f'[LOGS] Command used: {p}dictionary')

	# Uppercase command
	@commands.command(name='uppercase', aliases=['Uppercase', 'UPPERCASE', 'upper', 'Upper', 'UPPER'], description='Converts the given text to UPPERCASE.')
	async def uppercase(slef, ctx, *, text):
		'''Converts given input to uppercase'''
		await ctx.reply(text.upper())
		print(f'[LOGS] Command used: {p}upper')

	# Lowercase command
	@commands.command(name='lowercase', aliases=['Lowercase', 'LOWERCASE', 'lower', 'Lower', 'LOWER'], description='Converts the given text to lowercase.')
	async def lowercase(slef, ctx, *, text):
		'''Converts given input to lowercase'''
		await ctx.reply(text.lower())
		print(f'[LOGS] Command used: {p}lower')

	# Hexcode command
	@commands.command(name='hexcode', aliases=['Hexcode', 'HEXCODE', 'HexCode', 'hexCode', 'hex', 'Hex', 'HEX'], description='Tells the hex code of the given colour.')
	async def hexcode(self, ctx, *, colour):
		colourName = colour.replace(' ', '')
		await ctx.reply(matplotlib.colors.cnames[colourName])

'''
	# Python command
	@commands.command(name='python', aliases=['Python', 'PYTHON', 'py', 'Py', 'pY', 'PY'], description='Executes Python code.')
	async def python(self, ctx, * , code):

		#Executes Python code.

		if 'os' in code.lower():
			await ctx.reply("Due to security reasons, and me being too lazy to make this command secure, the use of 'os' module is not allowed. Even if you're not using the module and the code just happens to have 'os' in it, I'd still not allow it XD. Sorry :)")
		else:
			arg = code
			start = time.process_time()
			arg = arg[6:]
			arg = arg.split("```")

			param = arg[1]
			f = open("inputs.txt", "w")
			f.write(param)
			f.close()

			arg=arg[0]
			t = textwrap.indent(arg, '\t')
			f = open("output.py", "w")
			f.write(
f
import traceback
try:
{t}
except:
	print(traceback.format_exc())

			)
			f.close()

			error = False
			try:
				res = subprocess.check_output("python3 output.py < inputs.txt", shell=True)
			except subprocess.CalledProcessError:
				res = '[ERROR]'
				error = True

			time_taken = str(time.process_time() - start)

			if error == False:
				if res.decode('UTF-8') == '':
					embed = discord.Embed(color=discord.Color.gold())
					embed.add_field(name="Program Output", value=f'```\nNo Output```')
				else:
					embed = discord.Embed(color=discord.Color.gold())
					embed.add_field(name="Program Output", value=f'```yaml\n{res.decode("utf-8")}\n```')
			elif error:
				embed = discord.Embed(color=discord.Color.gold())
				embed.add_field(name="Program Output", value=f'```css\n[ERROR]\nCheck your code and run again.\n```')

			await ctx.send(embed=embed)

			os.remove("output.py")
			os.remove("inputs.txt")
'''

def setup(client):
	client.add_cog(Utility(client))
