
import discord
from discord.ext import commands
from main import p
from PIL import Image
from io import BytesIO
import os

class Images(commands.Cog):
	global p

	def __init__(self, client):
		self.client = client

	# When the cog is loaded
	@commands.Cog.listener()
	async def on_ready(self):
		print(f'[LOGS] {self.__class__.__name__} cog has been loaded.\n')

	# Wanted command
	@commands.command(name='wanted', aliases=['Wanted', 'WANTED'], description='Generates a wanted poster of the given user.')
	async def wanted(self, ctx, user_: discord.Member=None):
		user = user_
		if user == None:
			user = ctx.author

		wanted = Image.open('images/wanted.jpg')
		asset = user.avatar_url_as(size=128)
		data = BytesIO(await asset.read())
		pfp = Image.open(data)
		pfp = pfp.resize((177, 177))
		wanted.paste(pfp, (120, 212))
		# Creates a 'wanted_output.jpg' which gets sent as output
		wanted.save('wanted_output.jpg')

		await ctx.send(file = discord.File('wanted_output.jpg'))
		print(f'[LOGS] Command used: {p}wanted')

		# Deletes the saved image file
		os.remove('wanted_output.jpg')

def setup(client):
	client.add_cog(Images(client))
