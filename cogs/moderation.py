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
	@commands.command(name='kick', aliases=['Kick', 'KICK'], description='Kicks the mentioned user.\nRequired perm(s): Kick members')
	@commands.has_permissions(kick_members=True)
	async def kick(self, ctx, user: discord.Member, *, reason_=None):
		'''Kicks the mentioned user'''
		reason = reason_
		if user == ctx.author:
			await ctx.send('You can\'t kick yourself!')
		else:
			# Embed which will be sent when a person is kicked
			embed = discord.Embed(colour=0xFF0000)

			embed.set_author(name=f'User Kicked | {user}', icon_url=user.avatar_url)

			embed.add_field(name='User', value=f'{user.mention}', inline=True)
			embed.add_field(name='Moderator',value=f'{ctx.author.mention}', inline=True)
			embed.add_field(name='Reason', value=f'{reason}', inline=True)


			# Embed which will be DMed to the person who was kicked
			embed2 = discord.Embed(description=f'**You were kicked from {ctx.guild.name}**', colour=0xFF0000)

			embed2.add_field(name='Reason', value=f'{reason}', inline=True)
			embed2.add_field(name='Moderator', value=f'{ctx.author.name}', inline=True)

			if user.bot:
				pass
			else:
				await user.send(embed=embed2) # DM

			await user.kick(reason=reason) # Kicks the user
			await ctx.send(embed=embed)
			print(f'[LOGS] Command used: {p}kick')

	# Softban command
	@commands.command(name='softban', aliases=['Softban', 'SOFTBAN', 'softBan', 'SoftBan'], description='Softbans the mention user.\nRequired perm(s): Kick members')
	@commands.has_permissions(kick_members=True)
	async def softban(self, ctx, user: discord.Member, reason_=None):
		'''
		Softbans the mentioned user.
		A softban bans then immediately unbans the mentioned user to act asa kick which also deletes messages of the kicked user.
		'''

		if user == ctx.author:
			await ctx.send('You can\'t softban yourself!')
		else:
			# Embed which will be sent when a person is softbanned
			embed = discord.Embed(colour=0xFF0000)

			embed.set_author(name=f'User Softbanned | {user}', icon_url=member.avatar_url)

			embed.add_field(name='User', value=f'{user.mention}', inline=True)
			embed.add_field(name='Moderator',value=f'{ctx.author.mention}', inline=True)
			embed.add_field(name='Reason', value=f'{reason}', inline=True)


			# Embed which will be DMed to the person who was kicked
			embed2 = discord.Embed(description=f'**You were softbanned from {ctx.guild.name}**', colour=0xFF0000)

			embed2.add_field(name='Reason', value=f'{reason}', inline=True)
			embed2.add_field(name='Moderator', value=f'{ctx.author.name}', inline=True)

			if user.bot:
				pass
			else:
				await user.send(embed=embed2) # DM

			await user.ban(reason=f'[SOFTBAN] {reason}') # Bans the user
			await ctx.send(embed=embed)
			await user.unban(reason='The ban was a softban.')
			print(f'[LOGS] Command used: {p}softban')

	# Ban command
	@commands.command(name='ban', aliases=['Ban', 'BAN'], description='Bans the mentioned user.\nRequired perm(s): Ban members')
	@commands.has_permissions(ban_members=True)
	async def ban(self, ctx, user: discord.Member, *, reason_=None):
		'''Bans the mentioned user'''
		reason = reason_
		if user == ctx.author:
			await ctx.send('You can\'t ban yourself!')
		else:
			# Embed which will be sent when a person is banned
			embed = discord.Embed(colour=0xFF0000)

			embed.set_author(name=f'User Banned | {user}', icon_url=user.avatar_url)

			embed.add_field(name='User', value=f'{user.mention}', inline=True)
			embed.add_field(name='Moderator',value=f'{ctx.author.mention}', inline=True)
			embed.add_field(name='Reason', value=f'{reason}', inline=True)


			# Embed which will be DMed to the person who was banned
			embed2 = discord.Embed(description=f'**You were banned from {ctx.guild.name}**', colour=0xFF0000)

			embed2.add_field(name='Reason', value=f'{reason}', inline=True)
			embed2.add_field(name='Moderator', value=f'{ctx.author.name}', inline=True)

			if user.bot:
				pass
			else:
				await user.send(embed=embed2) # DM

			await user.ban(reason=reason) # Bans the user
			await ctx.send(embed=embed)
			print(f'[LOGS] Command used: {p}ban')

def setup(client):
	client.add_cog(Moderation(client))
