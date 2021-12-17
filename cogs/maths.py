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
	@commands.command(name='calculate', aliases=['Calculate', 'CALCULATE', 'c', 'C', 'calc', 'Calc', 'CALC'], description='Calculate the given input(numbers only)!')
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
	@commands.command(name='average', aliases=['Average', 'AVERAGE', 'avg', 'Avg', 'AVG'], description='Tells the average of the given values! Make sure to mention the type of average(mean, median or mode). Seprate the values by a `,`(comma).')
	async def mean(self, ctx, typeOfAverage: str, *, values):
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
			embed = discord.Embed(description=f"**Command Error:**\ntypeOfAverage must be 'mean', 'median' or 'mode', not '{typeOfAverage}'", color = 0xFF0000)
			await ctx.send(embed=embed)
	
	# Squareroot command
	@commands.command(name='squareroot', aliases=['Squareroot', 'SQUAREROOT', 'sqrt', 'Sqrt', 'SQRT'], description='Gives the square root of the given number!')
	async def squareroot(self, ctx, number: int):
		await ctx.reply(f'**Square root of {number}:**\n`{math.sqrt(number)}`')
	
	# Cos command
	@commands.command(name='cos', aliases=['Cos', 'COS', 'cosine', 'Cosine', 'COSINE'], description='Gives the cosine of the given number!')
	async def cosine(self, ctx, number: int):
		await ctx.reply(f'**Cosine of {number}:**\n`{math.cos(number)}`')

	# Sin command
	@commands.command(name='sin', aliases=['Sin', 'SIN', 'sine', 'Sine', 'SINE'], description='Gives the sine of the given number!')
	async def sine(self, ctx, number: int):
		await ctx.reply(f'**Sine of {number}:**\n`{math.sin(number)}`')

	# Tan command
	@commands.command(name='tan', aliases=['Tan', 'TAN', 'tangent', 'Tangent', 'TANGENT'], description='Gives the tangent of the given number!')
	async def tangent(self, ctx, number: int):
		await ctx.reply(f'**Tangent of {number}:**\n`{math.tan(number)}`')

def setup(client):
	client.add_cog(Maths(client))
