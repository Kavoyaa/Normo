import discord
from discord.ext import commands
from main import p
from main import client
import asyncio

class HelpDropdownView(discord.ui.View):
	def __init__(self, ctx):
		super().__init__(timeout=25)
		self.client = client
		self.ctx = ctx

	# Options that will be presented inside the dropdown
	selectOptions = [
		discord.SelectOption(label="Utility", description="", emoji="🛠️"),
		discord.SelectOption(label="Fun", description="", emoji="😄"),
		discord.SelectOption(label="Info", description="", emoji="ℹ️"),
		discord.SelectOption(label="Animals", description="", emoji="🐶"),
		discord.SelectOption(label="Games", description="", emoji="🎲"),
		discord.SelectOption(label="Images", description="", emoji="🖼️"),
		discord.SelectOption(label="Music", description="", emoji="🎵"),
		discord.SelectOption(label="Code", description="", emoji="💻"),
		discord.SelectOption(label="Maths", description="", emoji="📏"),
		discord.SelectOption(label="Giveaway", description="", emoji="🎉"),
		discord.SelectOption(label="Moderation", description="", emoji="❗"),
		discord.SelectOption(label="All", description='List of all commands', emoji="<:normalbot:926491116516282389>")
	]
	
	@discord.ui.select(placeholder="Select a module", min_values=1, max_values=1, options=selectOptions)
	async def select_callback(self, select, interaction):
	
		switcher = {
			"utility": [0, '🛠️'],
			"fun": [1, '😄'],
			"info": [2, 'ℹ️'],
			"animals": [3, '🐶'],
			"games": [4, '🎲'],
			"images": [5, '🖼️'],
			"music": [6, '🎵'],
			"code": [7, '💻'],
			"maths": [8, '📏'],
			"giveaway": [9, '🎉'],
			"moderation": [10, '❗'],
			"all": [11, '']
		}
	
		emoji = switcher.get(select.values[0].lower())[1]
		i = switcher.get(select.values[0].lower())[0]
		
		select.options[i].default = True

		commands = []
		num_of_commands = 0
		for command in self.client.walk_commands():
			num_of_commands += 1
			if select.values[0].lower() != "all":
				if command.module == f'cogs.{select.values[0].lower()}':
					commands.append(command.name)
			else:
				commands.append(command.name)
		
		c = str(commands)
		c = c.replace('[', '')
		c = c.replace(']', '')
		c = c.replace("'", "`")
		
		if select.values[0].lower() != "all":
			embed = discord.Embed(title=f'{emoji}{select.values[0]} commands:', description=c, color=discord.Color.random())
			embed.set_footer(text=self.ctx.author, icon_url=self.ctx.author.avatar.url)
		else:
			embed = discord.Embed(title='List of all commands:', description=c, color=discord.Color.random())
			embed.set_footer(text=f"Total number of commands: {num_of_commands}")
	
		await interaction.response.edit_message(embed=embed, view=self)
		select.options[i].default = False
	
	async def interaction_check(self, interaction):
		if interaction.user != self.ctx.author:
			await interaction.response.send_message("Only the command user can use that!", ephemeral=True)
			return False
		else:
			return True
	
	async def on_timeout(self):
		self.children[0].disabled = True
		await helpMessage.edit(view=self)

class Info(commands.Cog):
	global p

	def __init__(self, client):
		self.client = client

	# When the cog is loaded
	@commands.Cog.listener()
	async def on_ready(self):
		print(f'[LOGS] {self.__class__.__name__} cog has been loaded.\n')

	# Ping command
	@commands.command(name='ping', description='Shows the bot\'s ping/latency.')
	async def ping(self, ctx):
		'''Tells the latency of the bot'''
		global client
		latency = round(client.latency * 1000)

		await ctx.send(f'🏓 | ...pong! In {latency}ms.')
		print(f'[LOGS] Command used: {p}ping')

	# Aliases command
	@commands.command(name='aliases', aliases = ['alias'], description='Shows alias(es) of the given comamnds.')
	async def aliases(self, ctx, command):
		'''Shows all command aliases'''
		c = command.lower()
		embed = discord.Embed(color=discord.Color.random())

		for cmd in self.client.walk_commands():
			if cmd.name == c:
				a = str(cmd.aliases)
				a = a.replace("'", "`")
				a = a.replace('[', '')
				a = a.replace(']', '')
				embed.add_field(name=f'{p}{cmd.name} aliases:', value=a)

		await ctx.reply(embed=embed)
		print(f'[LOGS] Command used: {p}aliases')

	# help command
	@commands.command(name='help', description=f'Shows help about a module or command. `{p}help all` for a list of all commands.')
	async def help(self, ctx, command_or_module=None):
		'''A fully automatic help command which also shows the parameters needed for a command.'''

		# (There is probably a better, more efficient way to make sub-commands other than if-elif-else statements.)

		if command_or_module != None:
			c = command_or_module.lower()
		# help
		if command_or_module == None:
			embed = discord.Embed(title='Nromal Bot\'s Command List', description=f'Use `{p}help [module]` for more info on a module.\nUse `{p}help [command]` for info on a specific command.\nUse `{p}help all` for a list of all commands.', color=discord.Color.random())

			embed.add_field(name='🛠️Utility', value=f'`{p}help utility`')
			embed.add_field(name='😄Fun', value=f'`{p}help fun`')
			embed.add_field(name='ℹ️Info', value=f'`{p}help info`')
			embed.add_field(name='🐶Animals', value=f'`{p}help animals`')
			embed.add_field(name='🎲Games', value=f'`{p}help games`')
			embed.add_field(name='🖼️Images', value=f'`{p}help images`')
			embed.add_field(name='🎵Music', value=f'`{p}help music`')
			embed.add_field(name='💻Code', value=f'`{p}help code`')
			embed.add_field(name='📏Maths', value=f'`{p}help maths`')
			embed.add_field(name='🎉Giveaway', value=f'`{p}help giveaway`')
			embed.add_field(name='❗Moderation', value=f'`{p}help mod`')
			embed.add_field(name='⚙️Creator', value=f'`{p}help creator`')

			global helpMessage
			helpMessage = await ctx.reply(embed=embed, view=HelpDropdownView(ctx), mention_author=False)

		# help all
		elif c == 'all':
			'''Shows all commands'''

			commands = []
			# Makes a field for every command.
			for command in self.client.walk_commands():
					commands.append(command.name)

			c = str(commands)
			c = c.replace('[', '')
			c = c.replace(']', '')
			c = c.replace("'", "`")

			embed = discord.Embed(title='List of all commands:', description=c, color=discord.Color.random())

			# Number of commands
			i = 0
			for command in self.client.walk_commands():
				i += 1

			embed.set_footer(text=f'Total number of commands: {i}')

			await ctx.reply(embed=embed, mention_author=False)

		# help utility
		elif c == 'utility':
			'''Shows 'utility' commands'''
			commands = []
			# Makes a field for every command.
			for command in self.client.walk_commands():
				if command.module == 'cogs.utility':
					commands.append(command.name)

			c = str(commands)
			c = c.replace('[', '')
			c = c.replace(']', '')
			c = c.replace("'", "`")

			embed = discord.Embed(title='🛠️Utility commands:', description=c, color=discord.Color.random())

			embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)

			await ctx.reply(embed=embed, mention_author=False)

		# help fun
		elif c == 'fun':
			'''Shows 'fun' commands'''
			commands = []
			# Makes a field for every command.
			for command in self.client.walk_commands():
				if command.module == 'cogs.fun':
					commands.append(command.name)

			c = str(commands)
			c = c.replace('[', '')
			c = c.replace(']', '')
			c = c.replace("'", "`")

			embed = discord.Embed(title='😄Fun commands:', description=c, color=discord.Color.random())

			embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)

			await ctx.reply(embed=embed, mention_author=False)

		# help info
		elif c == 'info':
			'''Shows 'info' commands'''
			commands = []
			# Makes a field for every command.
			for command in self.client.walk_commands():
				if command.module == 'cogs.info':
					commands.append(command.name)

			c = str(commands)
			c = c.replace('[', '')
			c = c.replace(']', '')
			c = c.replace("'", "`")

			embed = discord.Embed(title='ℹ️Info commands:', description=c, color=discord.Color.random())

			embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)

			await ctx.reply(embed=embed, mention_author=False)

		# help animal/animals
		elif c == 'animal' or c =='animals':
			'''Shows 'animal' commands'''
			commands = []
			# Makes a field for every command.
			for command in self.client.walk_commands():
				if command.module == 'cogs.animals':
					commands.append(command.name)

			c = str(commands)
			c = c.replace('[', '')
			c = c.replace(']', '')
			c = c.replace("'", "`")

			embed = discord.Embed(title='🐶Animals commands:', description=c, color=discord.Color.random())

			embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)

			await ctx.reply(embed=embed, mention_author=False)

		# help game/games
		elif c == 'game' or c =='games':
			'''Shows 'game' commands'''
			commands = []
			# Makes a field for every command.
			for command in self.client.walk_commands():
				if command.module == 'cogs.games':
					commands.append(command.name)

			c = str(commands)
			c = c.replace('[', '')
			c = c.replace(']', '')
			c = c.replace("'", "`")

			embed = discord.Embed(title='🎲Game commands:', description=c, color=discord.Color.random())

			embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)

			await ctx.reply(embed=embed, mention_author=False)

		# help image/images
		elif c == 'image' or c =='images':
			'''Shows 'image' commands'''
			commands = []
			# Makes a field for every command.
			for command in self.client.walk_commands():
				if command.module == 'cogs.images':
					commands.append(command.name)

			c = str(commands)
			c = c.replace('[', '')
			c = c.replace(']', '')
			c = c.replace("'", "`")

			embed = discord.Embed(title='🖼️Image commands:', description=c, color=discord.Color.random())

			embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)

			await ctx.reply(embed=embed, mention_author=False)

		# help music
		elif c == 'music':
			'''Shows 'music' commands'''
			commands = []
			# Makes a field for every command.
			for command in self.client.walk_commands():
				if command.module == 'cogs.music':
					commands.append(command.name)

			c = str(commands)
			c = c.replace('[', '')
			c = c.replace(']', '')
			c = c.replace("'", "`")

			embed = discord.Embed(title='🎵Music commands:', description=c, color=discord.Color.random())

			embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)

			await ctx.reply(embed=embed, mention_author=False)

		# help code
		elif c == 'code':
			'''Shows 'code' commands'''
			commands = []
			# Makes a field for every command.
			for command in self.client.walk_commands():
				if command.module == 'cogs.code':
					commands.append(command.name)

			c = str(commands)
			c = c.replace('[', '')
			c = c.replace(']', '')
			c = c.replace("'", "`")

			embed = discord.Embed(title='💻Code commands:', description=c, color=discord.Color.random())

			embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)

			await ctx.reply(embed=embed, mention_author=False)

		# help maths
		elif c == 'maths' or c == 'math' or c == 'meth':
			'''Shows 'maths' commands'''
			commands = []
			# Makes a field for every command.
			for command in self.client.walk_commands():
				if command.module == 'cogs.maths':
					commands.append(command.name)

			c = str(commands)
			c = c.replace('[', '')
			c = c.replace(']', '')
			c = c.replace("'", "`")

			embed = discord.Embed(title='📏Math commands:', description=c, color=discord.Color.random())

			embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)

			await ctx.reply(embed=embed, mention_author=False)

		# help moderation
		elif c == 'moderation' or c =='mod':
			'''Shows 'moderation' commands'''
			commands = []
			# Makes a field for every command.
			for command in self.client.walk_commands():
				if command.module == 'cogs.moderation':
					commands.append(command.name)

			c = str(commands)
			c = c.replace('[', '')
			c = c.replace(']', '')
			c = c.replace("'", "`")

			embed = discord.Embed(title='❗Moderation commands:', description=c, color=discord.Color.random())

			embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)

			await ctx.reply(embed=embed, mention_author=False)

		# help giveaway
		elif c == 'giveaway' or c == 'giveaways':
			'''Shows 'giveaway' commands'''
			commands = []
			# Makes a field for every command.
			for command in self.client.walk_commands():
				if command.module == 'cogs.giveaway':
					commands.append(command.name)

			c = str(commands)
			c = c.replace('[', '')
			c = c.replace(']', '')
			c = c.replace("'", "`")

			embed = discord.Embed(title='🎉Giveaway commands:', description=c, color=discord.Color.random())

			embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)

			await ctx.reply(embed=embed, mention_author=False)

		# help hex
		elif c == 'hex':
			'''Gives information about .hex command.'''

			embed = discord.Embed(description=f'**How to use:** To use the command, simply type `{p}hex` followed by the name of the colour you want. If the colour is available, the bot will return the hex code of the colour.\n**Example:** `{p}hex red`\n\nHere are all the colours available in `{p}hex`:-')

			embed.set_image(url='https://cdn.discordapp.com/attachments/878136393858187285/879052476026851398/sphx_glr_named_colors_003.png')

			await ctx.reply(embed=embed, mention_author=False)

		# help python
		elif c == 'python':
			'''Gives information about .python command.'''
			v = '''
```
.python
`​`​`py
[code]
`​``input 1
input 2
input 3
```***NOTE:** Specify the inputs only if there are any.*
'''

			embed = discord.Embed(title=f'**{c}**', description='Executes Python code(you cannot import modules).', color=discord.Color.random())
			embed.add_field(name='Usage:', value=v, inline=False)
			embed.add_field(name='Aliases:', value='`py`')
			embed.add_field(name='Module:', value='code', inline=False)

			await ctx.reply(embed=embed, mention_author=False)

		# help [command]
		else:
			for command in self.client.walk_commands():
				if command.name == c:
					embed = discord.Embed(title=f'**{c}**', description=command.description, color=discord.Color.random())

					parameters = command.params
					usage = f'{p}{c} '
					for key, value in parameters.items():
						if str(key) == "self" or str(key) == "ctx":
							pass
						else:
							if "=" in str(value):
								usage += f'[`{key}`] '
							else: 
								usage += f'<`{key}`> '
					
					embed.add_field(name='Usage:', value=usage)

					for command in self.client.walk_commands():
						if command.name == c:
							a = ''
							commandAliases = command.aliases

							for item in commandAliases:
								a += f'`{item}`, '
							
							if a == '':
								a = 'None'
							else:
								a = a[:-2]
							
							embed.add_field(name=f'Aliases: ', value=a, inline=False)

							module = command.module.split('.')
							embed.add_field(name='Module: ', value=module[1], inline=False)

			await ctx.reply(embed=embed, mention_author=False)

def setup(client):
	client.add_cog(Info(client))
