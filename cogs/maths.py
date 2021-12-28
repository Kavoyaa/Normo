import discord
from discord.ext import commands
from main import p
import statistics as stat
import math

class Maths(commands.Cog):
	global p

	def __init__(self, client):
		self.client = client

	# When the cog is loaded
	@commands.Cog.listener()
	async def on_ready(self):
		print(f'[LOGS] {self.__class__.__name__} cog has been loaded.\n')

	# Calculate command
	@commands.command(name='calculate', aliases=['calc', 'c'], description='Calculate the given input(numbers only)!')
	async def calculate(self, ctx, *, input):
		i = ''
		for item in input:
			if item not in ['+', '-', '/', '*', '=', '^', '(', ')', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']:
				pass
			else:
				i += item
		i = i.replace('^', '**')
		await ctx.reply(eval(i, {'__builtins__':{}}))
	
	# Average command
	@commands.command(name='average', aliases=['avg'], description='Tells the average of the given values! If the type of average(mean, median or mode) is not mentioned, command shows the mean of the given values. Seprate the values by a `,`(comma).')
	async def mean(self, ctx, typeOfAverage: None, *, values):
		if typeOfAverage == None:
			toa = 'mean'
		else:
			toa = typeOfAverage.lower()
		if toa == "mean" or toa == "median" or toa == "mode":
			values = values.replace(" ", "")
			values = values.split(',')
			
			data = []
			for item in values:
				data.append(int(item))

			if toa == 'mean':
				await ctx.reply(stat.mean(data))
			elif toa == 'median':
				await ctx.reply(stat.median(data))
			elif toa == 'mode':
				await ctx.reply(stat.mode(data))
		else:
			embed = discord.Embed(color=discord.Color.red())
			embed.add_field(name='Command Error:', value=f"typeOfAverage must be 'mean', 'median' or 'mode', not '{typeOfAverage}'")
			await ctx.send(embed=embed)
	
	# Squareroot command
	@commands.command(name='squareroot', aliases=['sqrt'], description='Gives the square root of the given number!')
	async def squareroot(self, ctx, number: int):
		await ctx.reply(f'**Square root of {number}:**\n`{math.sqrt(number)}`')
	
	# Cos command
	@commands.command(name='cos', aliases=['cosine'], description='Gives the cosine of the given number!')
	async def cosine(self, ctx, number: int):
		await ctx.reply(f'**Cosine of {number}:**\n`{math.cos(number)}`')

	# Sin command
	@commands.command(name='sin', aliases=['sine'], description='Gives the sine of the given number!')
	async def sine(self, ctx, number: int):
		await ctx.reply(f'**Sine of {number}:**\n`{math.sin(number)}`')

	# Tan command
	@commands.command(name='tan', aliases=['tangent'], description='Gives the tangent of the given number!')
	async def tangent(self, ctx, number: int):
		await ctx.reply(f'**Tangent of {number}:**\n`{math.tan(number)}`')

def setup(client):
	client.add_cog(Maths(client))
