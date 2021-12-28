import discord
from discord.ext import commands
from typing import List
from main import p
import random


class Games(commands.Cog):
	global p

	def __init__(self, client):
		self.client = client

	# When the cog is loaded
	@commands.Cog.listener()
	async def on_ready(self):
		print(f'[LOGS] {self.__class__.__name__} cog has been loaded.\n')
	
	@commands.command(name='tictactoe')
	async def tic(self, ctx):
		await ctx.send('coming soon xd')

	
	
def setup(client):
	client.add_cog(Games(client))
