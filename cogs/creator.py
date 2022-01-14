import discord
from discord.ext import commands

class Creator(commands.Cog):
	global p

	def __init__(self, client):
		self.client = client

	# When the cog is loaded
	@commands.Cog.listener()
	async def on_ready(self):
		print(f'[LOGS] {self.__class__.__name__} cog has been loaded.\n')

	@commands.command()
	async def inv(self, ctx, user: discord.Member=None):
		
		
		await ctx.send(f'success\n```\n{ctx.author.guild.vanity_invite}')

def setup(client):
	client.add_cog(Creator(client))
