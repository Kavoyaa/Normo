import discord
from discord.ext import commands
from main import p
from PIL import Image, ImageFont, ImageDraw
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
	@commands.command(name='avatar', aliases=['av'], description="Sends the mentioned user's avatar(sends the command user's avatar if no one is mentioned).")
	async def avatar(self, ctx, user: discord.Member=None):
		if user == None:
			av = ctx.author.avatar.url
			heading = f"{ctx.author}'s avatar:"
		else:
			av = user.avatar.url
			heading = f"{user}'s avatar:"
		
		embed = discord.Embed(title= heading, color=discord.Color.random())
		embed.set_image(url=av)

		await ctx.reply(embed=embed)
	
	# Invert command
	@commands.command(name='invert', description='Sends colo(u)r inverted version of the mentioned user\'s profile picture!')
	async def invert(self, ctx, user: discord.Member=None):
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
	@commands.command(name='wanted', description='Generates a wanted poster of the given user!')
	async def wanted(self, ctx, user: discord.Member=None):
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

		# Deletes the saved image file
		os.remove('wanted_output.jpg')

	# Cmon command
	@commands.command(name='cmon', aliases=['comeon'], description='Generates a "C\'mon do something" meme with the profile picture of the given user!')
	async def dosomething(self, ctx, user: discord.Member=None):
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
	
	# Delete command
	@commands.command(name='delete', aliases=['deletememe'], description='"deletes" the given user :)')
	async def delete(self, ctx, user: discord.Member=None):
		if user == None:
			user = ctx.author

		wanted = Image.open('images/delete.jpg')
		asset = user.display_avatar.with_size(128)
		data = BytesIO(await asset.read())
		pfp = Image.open(data)
		pfp = pfp.resize((195, 195))
		wanted.paste(pfp, (120, 135))

		# Creates a 'delete_output.jpg' which gets sent as output
		wanted.save('delete_output.jpg')

		await ctx.send(file = discord.File('delete_output.jpg'))

		# Deletes the saved image file
		os.remove('delete_output.jpg')
	
	# Grayscale command
	@commands.command(name='grayscale', description='Grayscales the PFP of the given user.')
	async def gray(self, ctx, user: discord.Member=None):
		if user == None:
			user = ctx.author

		avatar = user.display_avatar
		data = BytesIO(await avatar.read())
		pfp = Image.open(data)
		inverted_image = PIL.ImageOps.grayscale(pfp.convert('RGB'))
		inverted_image.save('grayscaled.jpg')

		await ctx.send(file = discord.File('grayscaled.jpg'))
		os.remove('grayscaled.jpg')
	
	# What command
	@commands.command(name='what')
	async def what(self, ctx, *, text):
		image = Image.open("images/what.png")
		font = ImageFont.truetype("fonts/arial.ttf", 75)
		draw = ImageDraw.Draw(image)

		draw.text((5, 5), text, (0, 0, 0), font=font)
		image.save("what_output.png")
		
		await ctx.send(file=discord.File("what_output.png"))
		os.remove("what_output.png")
	
	# What command
	@commands.command(name='changeMyMind', aliases=['change_my_mind'], description='Generates a "Change My Mind" meme/')
	async def change_my_mind(self, ctx, *, text):
		image = Image.open("images/change_my_mind.jpeg")
		font = ImageFont.truetype("fonts/arial.ttf", 40)
		draw = ImageDraw.Draw(image)

		draw.text((300, 550), text, (0, 0, 0), font=font)
		image.save("change_my_mind_output.jpeg")
		
		await ctx.send(file=discord.File("change_my_mind_output.jpeg"))
		os.remove("change_my_mind_output.jpeg")

def setup(client):
	client.add_cog(Images(client))

