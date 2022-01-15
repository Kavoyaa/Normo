import discord
from discord.ext import commands
from main import p
import statistics as stat
import math

async def average(ctx, type_of_average, values):
	toa = type_of_average.lower()
	values = values.replace(" ", "")
	v = values.split(',')
	
	data = []
	for item in v:
		data.append(int(item))
	
	if toa == 'mean':
		output = stat.mean(data)
	elif toa == 'median':
		output = stat.median(data)
	elif toa == 'mode':
		output = stat.median(data)

	await ctx.reply(f'{toa.capitalize()} of: `{values.replace(",", ", ")}`\n**{output}**', mention_author=False)

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

		e = i.replace('^', '**')
		output = eval(e, {'__builtins__':{}})

		await ctx.reply(f'`{i}`\n**{output}**')

	# Mean command
	@commands.command(name='mean', description='Tells the mean of the given values! Seprate the values by a `,`(comma).')
	async def mean(self, ctx, *, values):
		await average(ctx, "mean", values)

	# Median command
	@commands.command(name='median', description='Tells the median of the given values! Seprate the values by a `,`(comma).')
	async def median(self, ctx, *, values):
		await average(ctx, "median", values)
	
	# Mode command
	@commands.command(name='mode', description='Tells the mode of the given values! Seprate the values by a `,`(comma).')
	async def mode(self, ctx, *, values):
		await average(ctx, "mode", values)

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
