import discord
from discord.ext import commands
from main import p

class Info(commands.Cog):
	global p
	module_name = 'info'

	def __init__(self, client):
		self.client = client

	# When the cog is loaded
	@commands.Cog.listener()
	async def on_ready(self):
		print(f'[LOGS] {self.__class__.__name__} cog has been loaded.\n')

	# help command
	@commands.command(name='help', aliases=['Help', 'HELP'], description='Shows a list of all command modules.', module=module_name)
	async def help(self, ctx, category=None):
		# (There is probably a better, more efficient way to make commands other than if-elif-else statements.)

		if category != None:
			c = category.lower()
		# help
		if category == None:
			embed = discord.Embed(title='Normal Bot\'s Command List', description=f'Use `{p}help [module]` for more info on a module.\nUse `{p}help all` for a list of all commands.', color=discord.Color.random())

			embed.add_field(name='🛠️Utility', value=f'`{p}help utility`')
			embed.add_field(name='😄Fun', value=f'`{p}help fun`')
			embed.add_field(name='ℹ️Info', value=f'`{p}help info`')
			embed.add_field(name='🐶Animals', value=f'`{p}help animals`')
			embed.add_field(name='🎲Games', value=f'`{p}help games`')
			embed.add_field(name='❗Moderation', value=f'`{p}help moderation`')

			await ctx.reply(embed=embed)
			print(f'[LOGS] Command used: {p}help')
		# help all
		elif c == 'all':
			embed = discord.Embed(title='List of all commands:', description=f'The bot prefix is `{p}`.', color=discord.Color.random())

			for command in self.client.walk_commands():
				embed.add_field(name=p + command.name, value=command.description)

			await ctx.reply(embed=embed)
			print(f'[LOGS] Command used: {p}help all')
		# help utility
		elif c == 'utility':
			embed = discord.Embed(description='**🛠️Utility Commands**', color=discord.Color.random())

			for command in self.client.walk_commands():
				if command.module == 'cogs.utility':
					embed.add_field(name=p + command.name, value=command.description)

			await ctx.reply(embed=embed)
			print(f'[LOGS] Command used: {p}help utility')
		# help fun
		elif c == 'fun':
			embed = discord.Embed(description='**😄Fun Commands**', color=discord.Color.random())

			for command in self.client.walk_commands():
				if command.module == 'cogs.fun':
					embed.add_field(name=p + command.name, value=command.description)

			await ctx.reply(embed=embed)
			print(f'[LOGS] Command used: {p}help fun')
		# help info
		elif c == 'info':
			embed = discord.Embed(description='**ℹ️Info Commands**', color=discord.Color.random())

			for command in self.client.walk_commands():
				if command.module == 'cogs.info':
					embed.add_field(name=p + command.name, value=command.description)

			await ctx.reply(embed=embed)
			print(f'[LOGS] Command used: {p}help info')
		# help animal/animals
		elif c == 'animal' or c =='animals':
			embed = discord.Embed(description='**🐶Animals Commands**', color=discord.Color.random())

			for command in self.client.walk_commands():
				if command.module == 'cogs.animals':
					embed.add_field(name=p + command.name, value=command.description)

			await ctx.reply(embed=embed)
			print(f'[LOGS] Command used: {p}help animal(s)')
		# help game/games
		elif c == 'game' or c =='games':
				embed = discord.Embed(description='**🎲Game Commands**', color=discord.Color.random())

				for command in self.client.walk_commands():
					if command.module == 'cogs.games':
						embed.add_field(name=p + command.name, value=command.description)

				await ctx.reply(embed=embed)
				print(f'[LOGS] Command used: {p}help game(s)')
		# help moderation
		elif c == 'moderation' or c =='mod':
					embed = discord.Embed(description='**❗Moderation Commands**', color=discord.Color.random())

					for command in self.client.walk_commands():
						if command.module == 'cogs.moderation':
							embed.add_field(name=p + command.name, value=command.description)

					await ctx.reply(embed=embed)
					print(f'[LOGS] Command used: {p}help moderation')

def setup(client):
	client.add_cog(Info(client))
