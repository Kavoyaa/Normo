import discord
from discord.ext import commands

class Moderation(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		print(f'[LOGS] {self.__class__.__name__} cog has been loaded.\n')

def setup(client):
	client.add_cog(Moderation(client))
