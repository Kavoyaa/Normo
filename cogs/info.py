import discord
from discord.ext import commands
from main import p
from main import client

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
	@commands.command(name='help', aliases=['Help', 'HELP'], description='**Shows:-**\nList of all modules if `input`=`none`.\nList of all commands if `input`=`all`.\nList of all commands in a module if `input`=`module_name`.\nHelp about a command if `input`=`command_name`\n(only for certain commands).')
	async def help(self, ctx, input_=None):
		# (There is probably a better, more efficient way to make commands other than if-elif-else statements.)

		if input_ != None:
			c = input_.lower()
		# help
		if input_ == None:
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

			# Makes a field for every command.
			for command in self.client.walk_commands():
					parameters = list(command.params.keys())
					try:
						if parameters[2]:
							if parameters[3]:
								if parameters[4]:
									pm1 = parameters[2].replace('_', ' (optional)')
									pm2 = parameters[3].replace('_', ' (optional)')
									pm3 = parameters[4].replace('_', ' (optional)')

									embed.add_field(name=f'{p}{command.name} <`{pm1}`> <`{pm2}`> <`{pm3}`>', value=command.description)
								else:
									pm1 = parameters[2].replace('_', ' (optional)')
									pm2 = parameters[3].replace('_', ' (optional)')

									embed.add_field(name=f'{p}{command.name} <`{pm1}`> <`{pm2}`>', value=command.description)
							else:
								pm1 = parameters[2].replace('_', ' (optional)')

								embed.add_field(name=f'{p}{command.name} <`{pm1}`>', value=command.description)
						else:
							embed.add_field(name=p + command.name, value=command.description)
					except:
						try:
							if parameters[2]:
								if parameters[3]:
									pm1 = parameters[2].replace('_', ' (optional)')
									pm2 = parameters[3].replace('_', ' (optional)')

									embed.add_field(name=f'{p}{command.name} <`{pm1}`> <`{pm2}`>', value=command.description)
								else:
									pm1 = parameters[2].replace('_', ' (optional)')

									embed.add_field(name=f'{p}{command.name} <`{pm1}`>', value=command.description)
							else:
								embed.add_field(name=p + command.name, value=command.description)
						except:
							try:
								if parameters[2]:
									pm1 = parameters[2].replace('_', ' (optional)')

									embed.add_field(name=f'{p}{command.name} <`{pm1}`>', value=command.description)
								else:
									embed.add_field(name=p + command.name, value=command.description)
							except:
								embed.add_field(name=p + command.name, value=command.description)

			await ctx.reply(embed=embed)
			print(f'[LOGS] Command used: {p}help all')
		# help utility
		elif c == 'utility':
			embed = discord.Embed(description='**🛠️Utility Commands**', color=discord.Color.random())

			# Makes a field for every command in 'utility' module.
			for command in self.client.walk_commands():
				if command.module == 'cogs.utility':
					parameters = list(command.params.keys())
					try:
						if parameters[2]:
							if parameters[3]:
								if parameters[4]:
									pm1 = parameters[2].replace('_', ' (optional)')
									pm2 = parameters[3].replace('_', ' (optional)')
									pm3 = parameters[4].replace('_', ' (optional)')

									embed.add_field(name=f'{p}{command.name} `<{pm1}`> <`{pm2}`> <`{pm3}`>', value=command.description)
								else:
									pm1 = parameters[2].replace('_', ' (optional)')
									pm2 = parameters[3].replace('_', ' (optional)')

									embed.add_field(name=f'{p}{command.name} <`{pm1}`> <`{pm2}`>', value=command.description)
							else:
								pm1 = parameters[2].replace('_', ' (optional)')

								embed.add_field(name=f'{p}{command.name} <`{pm1}`>', value=command.description)
						else:
							embed.add_field(name=p + command.name, value=command.description)
					except:
						try:
							if parameters[2]:
								if parameters[3]:
									pm1 = parameters[2].replace('_', ' (optional)')
									pm2 = parameters[3].replace('_', ' (optional)')

									embed.add_field(name=f'{p}{command.name} <`{pm1}`> <`{pm2}`>', value=command.description)
								else:
									pm1 = parameters[2].replace('_', ' (optional)')

									embed.add_field(name=f'{p}{command.name} <`{pm1}`>', value=command.description)
							else:
								embed.add_field(name=p + command.name, value=command.description)
						except:
							try:
								if parameters[2]:
									pm1 = parameters[2].replace('_', ' (optional)')

									embed.add_field(name=f'{p}{command.name} <`{pm1}`>', value=command.description)
								else:
									embed.add_field(name=p + command.name, value=command.description)
							except:
								embed.add_field(name=p + command.name, value=command.description)

			await ctx.reply(embed=embed)
			print(f'[LOGS] Command used: {p}help utility')
		# help fun
		elif c == 'fun':
			embed = discord.Embed(description='**😄Fun Commands**', color=discord.Color.random())

			# Makes a field for every command in 'fun' module.
			for command in self.client.walk_commands():
				if command.module == 'cogs.fun':
					parameters = list(command.params.keys())
					try:
						if parameters[2]:
							if parameters[3]:
								if parameters[4]:
									pm1 = parameters[2].replace('_', ' (optional)')
									pm2 = parameters[3].replace('_', ' (optional)')
									pm3 = parameters[4].replace('_', ' (optional)')

									embed.add_field(name=f'{p}{command.name} `<{pm1}`> <`{pm2}`> <`{pm3}`>', value=command.description)
								else:
									pm1 = parameters[2].replace('_', ' (optional)')
									pm2 = parameters[3].replace('_', ' (optional)')

									embed.add_field(name=f'{p}{command.name} <`{pm1}`> <`{pm2}`>', value=command.description)
							else:
								pm1 = parameters[2].replace('_', ' (optional)')

								embed.add_field(name=f'{p}{command.name} <`{pm1}`>', value=command.description)
						else:
							embed.add_field(name=p + command.name, value=command.description)
					except:
						try:
							if parameters[2]:
								if parameters[3]:
									pm1 = parameters[2].replace('_', ' (optional)')
									pm2 = parameters[3].replace('_', ' (optional)')

									embed.add_field(name=f'{p}{command.name} <`{pm1}`> <`{pm2}`>', value=command.description)
								else:
									pm1 = parameters[2].replace('_', ' (optional)')

									embed.add_field(name=f'{p}{command.name} <`{pm1}`>', value=command.description)
							else:
								embed.add_field(name=p + command.name, value=command.description)
						except:
							try:
								if parameters[2]:
									pm1 = parameters[2].replace('_', ' (optional)')

									embed.add_field(name=f'{p}{command.name} <`{pm1}`>', value=command.description)
								else:
									embed.add_field(name=p + command.name, value=command.description)
							except:
								embed.add_field(name=p + command.name, value=command.description)

			await ctx.reply(embed=embed)
			print(f'[LOGS] Command used: {p}help fun')
		# help info
		elif c == 'info':
			embed = discord.Embed(description='**ℹ️Info Commands**', color=discord.Color.random())

			# Makes a field for every command in 'info' module.
			for command in self.client.walk_commands():
				if command.module == 'cogs.info':
					parameters = list(command.params.keys())
					try:
						if parameters[2]:
							if parameters[3]:
								if parameters[4]:
									pm1 = parameters[2].replace('_', ' (optional)')
									pm2 = parameters[3].replace('_', ' (optional)')
									pm3 = parameters[4].replace('_', ' (optional)')

									embed.add_field(name=f'{p}{command.name} `<{pm1}`> <`{pm2}`> <`{pm3}`>', value=command.description)
								else:
									pm1 = parameters[2].replace('_', ' (optional)')
									pm2 = parameters[3].replace('_', ' (optional)')

									embed.add_field(name=f'{p}{command.name} <`{pm1}`> <`{pm2}`>', value=command.description)
							else:
								pm1 = parameters[2].replace('_', ' (optional)')

								embed.add_field(name=f'{p}{command.name} <`{pm1}`>', value=command.description)
						else:
							embed.add_field(name=p + command.name, value=command.description)
					except:
						try:
							if parameters[2]:
								if parameters[3]:
									pm1 = parameters[2].replace('_', ' (optional)')
									pm2 = parameters[3].replace('_', ' (optional)')

									embed.add_field(name=f'{p}{command.name} <`{pm1}`> <`{pm2}`>', value=command.description)
								else:
									pm1 = parameters[2].replace('_', ' (optional)')

									embed.add_field(name=f'{p}{command.name} <`{pm1}`>', value=command.description)
							else:
								embed.add_field(name=p + command.name, value=command.description)
						except:
							try:
								if parameters[2]:
									pm1 = parameters[2].replace('_', ' (optional)')

									embed.add_field(name=f'{p}{command.name} <`{pm1}`>', value=command.description)
								else:
									embed.add_field(name=p + command.name, value=command.description)
							except:
								embed.add_field(name=p + command.name, value=command.description)

			await ctx.reply(embed=embed)
			print(f'[LOGS] Command used: {p}help info')
		# help animal/animals
		elif c == 'animal' or c =='animals':
			embed = discord.Embed(description='**🐶Animals Commands**', color=discord.Color.random())

			# Makes a field for every command in 'animal/animals' module.
			for command in self.client.walk_commands():
				if command.module == 'cogs.animals':
					parameters = list(command.params.keys())
					try:
						if parameters[2]:
							if parameters[3]:
								if parameters[4]:
									pm1 = parameters[2].replace('_', ' (optional)')
									pm2 = parameters[3].replace('_', ' (optional)')
									pm3 = parameters[4].replace('_', ' (optional)')

									embed.add_field(name=f'{p}{command.name} `<{pm1}`> <`{pm2}`> <`{pm3}`>', value=command.description)
								else:
									pm1 = parameters[2].replace('_', ' (optional)')
									pm2 = parameters[3].replace('_', ' (optional)')

									embed.add_field(name=f'{p}{command.name} <`{pm1}`> <`{pm2}`>', value=command.description)
							else:
								pm1 = parameters[2].replace('_', ' (optional)')

								embed.add_field(name=f'{p}{command.name} <`{pm1}`>', value=command.description)
						else:
							embed.add_field(name=p + command.name, value=command.description)
					except:
						try:
							if parameters[2]:
								if parameters[3]:
									pm1 = parameters[2].replace('_', ' (optional)')
									pm2 = parameters[3].replace('_', ' (optional)')

									embed.add_field(name=f'{p}{command.name} <`{pm1}`> <`{pm2}`>', value=command.description)
								else:
									pm1 = parameters[2].replace('_', ' (optional)')

									embed.add_field(name=f'{p}{command.name} <`{pm1}`>', value=command.description)
							else:
								embed.add_field(name=p + command.name, value=command.description)
						except:
							try:
								if parameters[2]:
									pm1 = parameters[2].replace('_', ' (optional)')

									embed.add_field(name=f'{p}{command.name} <`{pm1}`>', value=command.description)
								else:
									embed.add_field(name=p + command.name, value=command.description)
							except:
								embed.add_field(name=p + command.name, value=command.description)

			await ctx.reply(embed=embed)
			print(f'[LOGS] Command used: {p}help animal(s)')
		# help game/games
		elif c == 'game' or c =='games':
				embed = discord.Embed(description='**🎲Game Commands**', color=discord.Color.random())

				# Makes a field for every command in 'game/games' module.
				for command in self.client.walk_commands():
					if command.module == 'cogs.games':
						parameters = list(command.params.keys())
						try:
							if parameters[2]:
								if parameters[3]:
									if parameters[4]:
										pm1 = parameters[2].replace('_', ' (optional)')
										pm2 = parameters[3].replace('_', ' (optional)')
										pm3 = parameters[4].replace('_', ' (optional)')

										embed.add_field(name=f'{p}{command.name} `<{pm1}`> <`{pm2}`> <`{pm3}`>', value=command.description)
									else:
										pm1 = parameters[2].replace('_', ' (optional)')
										pm2 = parameters[3].replace('_', ' (optional)')

										embed.add_field(name=f'{p}{command.name} <`{pm1}`> <`{pm2}`>', value=command.description)
								else:
									pm1 = parameters[2].replace('_', ' (optional)')

									embed.add_field(name=f'{p}{command.name} <`{pm1}`>', value=command.description)
							else:
								embed.add_field(name=p + command.name, value=command.description)
						except:
							try:
								if parameters[2]:
									if parameters[3]:
										pm1 = parameters[2].replace('_', ' (optional)')
										pm2 = parameters[3].replace('_', ' (optional)')

										embed.add_field(name=f'{p}{command.name} <`{pm1}`> <`{pm2}`>', value=command.description)
									else:
										pm1 = parameters[2].replace('_', ' (optional)')

										embed.add_field(name=f'{p}{command.name} <`{pm1}`>', value=command.description)
								else:
									embed.add_field(name=p + command.name, value=command.description)
							except:
								try:
									if parameters[2]:
										pm1 = parameters[2].replace('_', ' (optional)')

										embed.add_field(name=f'{p}{command.name} <`{pm1}`>', value=command.description)
									else:
										embed.add_field(name=p + command.name, value=command.description)
								except:
									embed.add_field(name=p + command.name, value=command.description)

				await ctx.reply(embed=embed)
				print(f'[LOGS] Command used: {p}help game(s)')
		# help moderation
		elif c == 'moderation' or c =='mod':
					embed = discord.Embed(description='**❗Moderation Commands**', color=discord.Color.random())

					# Makes a field for every command in 'moderation' module.
					for command in self.client.walk_commands():
						if command.module == 'cogs.moderation':
							parameters = list(command.params.keys())
							try:
								if parameters[2]:
									if parameters[3]:
										if parameters[4]:
											pm1 = parameters[2].replace('_', ' (optional)')
											pm2 = parameters[3].replace('_', ' (optional)')
											pm3 = parameters[4].replace('_', ' (optional)')

											embed.add_field(name=f'{p}{command.name} `<{pm1}`> <`{pm2}`> <`{pm3}`>', value=command.description)
										else:
											pm1 = parameters[2].replace('_', ' (optional)')
											pm2 = parameters[3].replace('_', ' (optional)')

											embed.add_field(name=f'{p}{command.name} <`{pm1}`> <`{pm2}`>', value=command.description)
									else:
										pm1 = parameters[2].replace('_', ' (optional)')

										embed.add_field(name=f'{p}{command.name} <`{pm1}`>', value=command.description)
								else:
									embed.add_field(name=p + command.name, value=command.description)
							except:
								try:
									if parameters[2]:
										if parameters[3]:
											pm1 = parameters[2].replace('_', ' (optional)')
											pm2 = parameters[3].replace('_', ' (optional)')

											embed.add_field(name=f'{p}{command.name} <`{pm1}`> <`{pm2}`>', value=command.description)
										else:
											pm1 = parameters[2].replace('_', ' (optional)')

											embed.add_field(name=f'{p}{command.name} <`{pm1}`>', value=command.description)
									else:
										embed.add_field(name=p + command.name, value=command.description)
								except:
									try:
										if parameters[2]:
											pm1 = parameters[2].replace('_', ' (optional)')

											embed.add_field(name=f'{p}{command.name} <`{pm1}`>', value=command.description)
										else:
											embed.add_field(name=p + command.name, value=command.description)
									except:
										embed.add_field(name=p + command.name, value=command.description)

					await ctx.reply(embed=embed)
					print(f'[LOGS] Command used: {p}help moderation')

	# Ping command
	@commands.command(name='ping', aliases=['Ping', 'PING'], description='Shows the bot\'s ping/latency.')
	async def ping(self, ctx):
		global client
		await ctx.send(f'🏓 | ...pong! In {round(client.latency * 1000)}ms.')

def setup(client):
	client.add_cog(Info(client))
