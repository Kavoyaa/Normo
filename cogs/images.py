import nextcord as discord
from nextcord.ext import commands
from main import p
from PIL import Image
import PIL.ImageOps  
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

	# Avatar command
	@commands.command(name='avatar', aliases=['Avatar', 'AVATAR', 'av', 'Av', 'aV', 'AV'], description="Sends the mentioned user's avatar(sends the command user's avatar if no one is mentioned).")
	async def avatar(self, ctx, user_: discord.Member=None):
		if user_ == None:
			av = ctx.author.avatar.url
			heading = f"{ctx.author}'s avatar:"
		else:
			av = user_.avatar.url
			heading = f"{user_}'s avatar:"
		
		embed = discord.Embed(title= heading, color=discord.Color.random())
		embed.set_image(url=av)

		await ctx.reply(embed=embed)
	
	# Invert command
	@commands.command(name='invert', aliases=['Invert', 'INVERT'], description='Sends colo(u)r inverted version of the mentioned user\'s profile picture!')
	async def invert(self, ctx, user_: discord.Member=None):
		user = user_
		if user == None:
			user = ctx.author

		avatar = user.display_avatar
		data = BytesIO(await avatar.read())
		pfp = Image.open(data)

		inverted_image = PIL.ImageOps.invert(pfp.convert('RGB'))
		inverted_image.save('inverted.jpg')

		await ctx.send(file = discord.File('inverted.jpg'))
		os.remove('inverted.jpg')

	# Wanted command
	@commands.command(name='wanted', aliases=['Wanted', 'WANTED'], description='Generates a wanted poster of the given user!')
	async def wanted(self, ctx, user_: discord.Member=None):
		user = user_
		if user == None:
			user = ctx.author

		wanted = Image.open('images/wanted.jpg')
		asset = user.display_avatar.with_size(128)
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

	# Cmon command
	@commands.command(name='cmon', aliases=['Cmon', 'CMON'], description='Generates a "C\'mon do something" meme with the profile picture of the given user!')
	async def dosomething(self, ctx, user_: discord.Member=None):
		user = user_
		if user == None:
			user = ctx.author

		wanted = Image.open('images/cmon.jpg')
		asset = user.display_avatar.with_size(128)
		data = BytesIO(await asset.read())
		pfp = Image.open(data)
		pfp = pfp.resize((177, 177))
		wanted.paste(pfp, (120, 212))
		# Creates a 'cmon_output.jpg' which gets sent as output
		wanted.save('cmon_output.jpg')

		await ctx.send(file = discord.File('cmon_output.jpg'))

		# Deletes the saved image file
		os.remove('cmon_output.jpg')
	
	# Grayscale command
	@commands.command(name='grayscale', aliases=['Grayscale', 'GRAYSCALE', 'greyscale', 'Greyscale', 'GREYSCALE'])
	async def gray(self, ctx, user_: discord.Member=None):
		user = user_
		if user == None:
			user = ctx.author

		avatar = user.display_avatar
		data = BytesIO(await avatar.read())
		pfp = Image.open(data)
		inverted_image = PIL.ImageOps.grayscale(pfp.convert('RGB'))
		inverted_image.save('grayscaled.jpg')

		await ctx.send(file = discord.File('grayscaled.jpg'))
		os.remove('grayscaled.jpg')

def setup(client):
	client.add_cog(Images(client))

