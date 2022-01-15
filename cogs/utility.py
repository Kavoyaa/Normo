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
from discord.ui import Button, View


class Utility(commands.Cog):
	global p

	def __init__(self, client):
		self.client = client

	# When the cog is loaded
	@commands.Cog.listener()
	async def on_ready(self):
		print(f'[LOGS] {self.__class__.__name__} cog has been loaded.\n')

	# Google command
	@commands.command(name='google', description='Shows Google search results of the given input.')
	async def test(self, ctx, *, input):
		search = input
		if "#" in search:
			search = search.replace("#", "%23")
	
		url = "https://www.google.com/search?q=" + search
		button = Button(label="Search Results", url=url)
		view = View()
		view.add_item(button)

		embed = discord.Embed(color=0xdb0085)
		embed.set_author(name='Google', icon_url='https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Google_%22G%22_Logo.svg/2000px-Google_%22G%22_Logo.svg.png')
		embed.add_field(name='Searched for:', value=input)
		embed.set_footer(text=f'Searched by {ctx.author}', icon_url=ctx.author.avatar.url)

		await ctx.send(view=view, embed=embed)

	# Count command
	@commands.command(name='count', description='Counts the number of words in the given `text`.')
	async def count(self, ctx, *, text):
		words = text.split()
		number_of_words = len(words)

		if number_of_words == 1:
			await ctx.reply(f'There is {number_of_words} word in this text.\n*smh you can count that much yourself, why use me?*')
		else:
			await ctx.reply(f'There are {number_of_words} words in this text.')

	# Binary command
	@commands.command(name='binary', description='Converts the given `input` to ASCII binary.')
	async def binary(self, ctx, *, input):
		res = ''.join(format(ord(i), '08b') for i in input)
		output = str(res)

		await ctx.send(output)

	# Convert command
	@commands.command(name='convert', description='Converts the given `input`(which would/must be ASCII binary) to text.')
	async def convert(self, ctx, *, input):
		try:
			if " " in input:
				input = input.replace(" ", "")
			binary_int = int(input, 2)
			byte_number = binary_int.bit_length() + 7 // 8
			binary_array = binary_int.to_bytes(byte_number, "big")
			converted_text = binary_array.decode()

			await ctx.send(converted_text)
		except:
			embed = discord.Embed(color=discord.Color.red())
			embed.add_field(name='Command Error:', value="The given binary code is either not valid or it isn't ASCII binary.")
			await ctx.send(embed=embed)

	# Reverse command
	@commands.command(name='reverse', aliases=['esrever', 'r'], description='Reverses the given text.')
	async def reverse(self, ctx, *, text):
		'''Reverses the given input(text).'''
		reversedString = ''

		for letter in text:
			reversedString = letter + reversedString

		await ctx.send(reversedString)

	# Dictionary command
	@commands.command(name='dictionary', aliases=['dict'], description='Gets the dictionary information about a word.')
	async def dictionary(self, ctx, word):
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
				await ctx.send(f"**{r[0]['word']}**\n/{r[0]['phonetic']}/\n\n**{partOfSpeech0}**\n{definition0}\n\n**{partOfSpeech1}**\n{definition1}")
			except:
				await ctx.send(f"**{r[0]['word']}**\n/{r[0]['phonetic']}/\n\n**{partOfSpeech0}**\n{definition0}")
		except:
			embed = discord.Embed(color=discord.Color.red())
			embed.add_field(name='Command Error:', value=f"Word '{word.lower()} not found.")
			await ctx.send(embed=embed)

	# Uppercase command
	@commands.command(name='uppercase', aliases=['upper'], description='Converts the given text to UPPERCASE.')
	async def uppercase(slef, ctx, *, text):
		'''Converts given input to uppercase'''
		await ctx.reply(text.upper())

	# Lowercase command
	@commands.command(name='lowercase', aliases=['lower'], description='Converts the given text to lowercase.')
	async def lowercase(slef, ctx, *, text):
		'''Converts given input to lowercase'''
		await ctx.reply(text.lower())

	# Hexcode command
	@commands.command(name='hexcode', aliases=['hex'], description='Tells the hex code of the given colour.')
	async def hexcode(self, ctx, *, colour):
		colourName = colour.replace(' ', '')
		await ctx.reply(matplotlib.colors.cnames[colourName])

def setup(client):
	client.add_cog(Utility(client))
