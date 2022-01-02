import discord
from discord.ext import commands
from main import p

class Moderation(commands.Cog):
	global p

	def __init__(self, client):
		self.client = client

	# When the cog is loaded
	@commands.Cog.listener()
	async def on_ready(self):
		print(f'[LOGS] {self.__class__.__name__} cog has been loaded.\n')

	# Kick command
	@commands.command(name='kick', description='Kicks the mentioned user.\nRequired perm(s): Kick members')
	@commands.has_permissions(kick_members=True)
	async def kick(self, ctx, user: discord.Member, *, reason=None):
		'''Kicks the mentioned user'''

		if user == ctx.author:
			await ctx.send('You can\'t kick yourself!')
		else:
			# Embed which will be sent when a person is kicked
			embed = discord.Embed(colour=discord.Color.red())

			embed.set_author(name=f'User Kicked | {user}', icon_url=user.avatar.url)

			embed.add_field(name='User', value=f'{user.mention}', inline=True)
			embed.add_field(name='Moderator',value=f'{ctx.author.mention}', inline=True)
			embed.add_field(name='Reason', value=f'{reason}', inline=True)


			# Embed which will be DMed to the person who was kicked
			embed2 = discord.Embed(description=f'**You were kicked from {ctx.guild.name}**', colour=discord.Color.red())

			embed2.add_field(name='Reason', value=f'{reason}', inline=True)
			embed2.add_field(name='Moderator', value=f'{ctx.author.name}', inline=True)

			if user.bot:
				pass
			else:
				await user.send(embed=embed2) # DM

			await user.kick(reason=reason) # Kicks the user
			await ctx.send(embed=embed)

	# Softban command
	@commands.command(name='softban', description='Softbans the mention user.\nRequired perm(s): Kick members')
	@commands.has_permissions(kick_members=True)
	async def softban(self, ctx, user: discord.Member, reason=None):
		'''
		Softbans the mentioned user.
		A softban bans then immediately unbans the mentioned user to act asa kick which also deletes messages of the kicked user.
		'''

		if user == ctx.author:
			await ctx.send('You can\'t softban yourself!')
		else:
			# Embed which will be sent when a person is softbanned
			embed = discord.Embed(colour=discord.Color.red())

			embed.set_author(name=f'User Softbanned | {user}', icon_url=user.avatar.url)

			embed.add_field(name='User', value=f'{user.mention}', inline=True)
			embed.add_field(name='Moderator',value=f'{ctx.author.mention}', inline=True)
			embed.add_field(name='Reason', value=f'{reason}', inline=True)


			# Embed which will be DMed to the person who was kicked
			embed2 = discord.Embed(description=f'**You were softbanned from {ctx.guild.name}**', colour=discord.Color.red())

			embed2.add_field(name='Reason', value=f'{reason}', inline=True)
			embed2.add_field(name='Moderator', value=f'{ctx.author.name}', inline=True)

			if user.bot:
				pass
			else:
				await user.send(embed=embed2) # DM

			await user.ban(reason=f'[SOFTBAN] {reason}') # Bans the user
			await ctx.send(embed=embed)
			await user.unban(reason='The ban was a softban.')

	# Ban command
	@commands.command(name='ban', description='Bans the mentioned user.\nRequired perm(s): Ban members')
	@commands.has_permissions(ban_members=True)
	async def ban(self, ctx, user: discord.Member, *, reason=None):
		'''Bans the mentioned user'''
		
		if user == ctx.author:
			await ctx.send('You can\'t ban yourself!')
		else:
			# Embed which will be sent when a person is banned
			embed = discord.Embed(colour=discord.Color.red())

			embed.set_author(name=f'User Banned | {user}', icon_url=user.avatar.url)

			embed.add_field(name='User', value=f'{user.mention}', inline=True)
			embed.add_field(name='Moderator',value=f'{ctx.author.mention}', inline=True)
			embed.add_field(name='Reason', value=f'{reason}', inline=True)


			# Embed which will be DMed to the person who was banned
			embed2 = discord.Embed(description=f'**You were banned from {ctx.guild.name}**', colour=discord.Color.red())

			embed2.add_field(name='Reason', value=f'{reason}', inline=True)
			embed2.add_field(name='Moderator', value=f'{ctx.author.name}', inline=True)

			if user.bot:
				pass
			else:
				await user.send(embed=embed2) # DM

			await user.ban(reason=reason) # Bans the user
			await ctx.send(embed=embed)

	# Purge command
	@commands.command(name='purge', aliases=['clear'], description='Deletes the given amount of messages.\nRequired perm(s): Manage messages')
	@commands.has_permissions(manage_messages=True)
	async def purge(self, ctx, amount: int):
		await ctx.channel.purge(limit=amount + 1)

		if amount == 1:
			embed = discord.Embed(title=f'**Sucessfully deleted {str(amount)} message.**')
		else:
			embed = discord.Embed(title=f'**Sucessfully deleted {str(amount)} messages.**')

		embed.set_footer(text='This message will be deleted in 10 seconds.')

		await ctx.send(embed=embed, delete_after=10)

	# Embed command
	@commands.command(name='embed', aliases=['embedify'], description='Make your own embeds!\n`.help embed`(coming soon) to see how to use.\nRequited perm(s): Administrator')
	async def embed(self, ctx, *, input):
		code = input
		title = ''
		desc = ''

		if '<title>' in code:
			_title = code.split('<title>')
			title = _title[1]

		if '<desc>' in code:
			_desc = code.split('<desc>')
			desc = _desc[1]

		if '<colour>' in code:
			colour = code.split('<colour>')
			hexVal = colour[1].replace('#', '0x')
			convertedHex = int(hexVal, 16)

			embed = discord.Embed(title=title, description=desc, colour=convertedHex)
		elif not '<colour>' in code:
			embed = discord.Embed(title=title, description=desc)

		if '<img>' in code:
			img = code.split('<img>')
			embed.set_image(url=img[1])

		if '<thumbnail>' in code:
			thumbnail = code.split('<thumbnail>')
			embed.set_thumbnail(url=thumbnail[1])

		if '<footer>' in code:
			footer = code.split('<footer>')
			embed.set_footer(text=footer[1])

		if '<author>' in code:
			author = code.split('<author>')

			if '<name>' in author[1]:
				name = author[1].split('<name>')

				if '<icon>' in author[1]:
					authorIcon = author[1].split('<icon>')
					embed.set_author(name=name[1], icon_url=authorIcon[1])
				else:
					embed.set_author(name=name[1])

		if '<fields>' in code:
			field = code.split('<fields>')

			for i in range(100):
				try:
					if i % 2 !=0:
						name = field[1].split('<name>')
						value = field[1].split('<value>')
						inline = field[1].split('<inline>')

						if value[i]:
							if name[i]:
								if inline[i]:
									if inline[i] == 'False' or inline[i] == 'false':
										embed.add_field(name=name[i], value=value[i], inline=False)
									elif inline[i] == 'True' or inline[i] == 'true':
										embed.add_field(name=name[i], value=value[i], inline=True)
				except:
					pass

		await ctx.send(embed=embed)

def setup(client):
	client.add_cog(Moderation(client))
