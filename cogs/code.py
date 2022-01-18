import discord
from discord.ext import commands
from pyston import PystonClient, File

async def run_code(ctx, language, codeblock_type, code, comment, color):
	if code.count('`') < 6:
		await ctx.reply(f"**The code must be inside a codeblock.**\n\nHow to make a codeblock:\n\`\`\`{codeblock_type}\n[code]\n\`\`\`", mention_author=False)
		return

	await ctx.message.add_reaction("<a:colorfulloading:921304808256860171>")

	co = code.splitlines(keepends=True)
	co = co[1:-1]

	c = ''
	for item in co:
		c += item

	pyston = PystonClient()
	output = await pyston.execute(language, [File(c)])
	success = output.success
	output = str(output)

	if output == "":
		output = "```\nNo Output\n```" 
	else:
		if len(output) > 980:
			output = output[:980]
			output = output + f"\n{comment} Size limit reached"
		
		if output.count('\n') > 51:
			o = output.split('\n')
			o = o[:51]
			
			result = ''
			for item in o:
				result += item + '\n'
			
			output = result + f'{comment} Length limit reached'

		output = f"```yaml\n{output}\n```"	

	embed = discord.Embed(color = color if success else discord.Color.red())
	embed.add_field(name='Program Output', value=output)
	embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)

	await ctx.send(embed=embed)
	await ctx.message.clear_reaction("<a:colorfulloading:921304808256860171>")

class Code(commands.Cog):
	global p

	def __init__(self, client):
		self.client = client

	# When the cog is loaded
	@commands.Cog.listener()
	async def on_ready(self):
		print(f'[LOGS] {self.__class__.__name__} cog has been loaded.\n')

	# Python command
	@commands.command(name='python', aliases=['py'], description='Executes Python code!')
	@commands.cooldown(1, 6, commands.BucketType.user)
	async def python(self, ctx, *, code):
		await run_code(ctx, "python", "py", code, "#", discord.Color.gold())

	# Javascript command
	@commands.command(name='javascript', aliases=['js'], description='Executes JavaScript code(Node.js)!')
	@commands.cooldown(1, 6, commands.BucketType.user)
	async def javascript(self, ctx, *, code):
		await run_code(ctx, "javascript", "js", code, "//", 0xFFF200)
	
	# Java command
	@commands.command(name='java', description='Executes Java code!')
	@commands.cooldown(1, 6, commands.BucketType.user)
	async def java(self, ctx, *, code):
		await run_code(ctx, "java", "java", code, "//", 0x178DC9)

	# C++ command
	@commands.command(name='c++', aliases=['cpp', 'cplusplus'], description='Executes C++ code!')
	@commands.cooldown(1, 6, commands.BucketType.user)
	async def cpp(self, ctx, *, code):
		await run_code(ctx, "c++", "cpp", code, "//", 0x1F6ABD)
	
	# C command
	@commands.command(name='c', description='Executes C code!')
	@commands.cooldown(1, 6, commands.BucketType.user)
	async def c(self, ctx, *, code):
		await run_code(ctx, "c", "c", code, "//", 0x1F6ABD)

	# Rust command
	@commands.command(name='rust', aliases=['rs'], description='Executes Rust code!')
	@commands.cooldown(1, 6, commands.BucketType.user)
	async def rust(self, ctx, *, code):
		await run_code(ctx, "rust", "rs", code, "//", discord.Color.orange())

	# C# command
	@commands.command(name='c#', aliases=['csharp', 'cs'], description='Executes C# code!')
	@commands.cooldown(1, 6, commands.BucketType.user)
	async def csharp(self, ctx, *, code):
		await run_code(ctx, "csharp", "cs", code, "//", discord.Color.purple())

	# Php command
	@commands.command(name='php', description='Executes PHP code!')
	@commands.cooldown(1, 6, commands.BucketType.user)
	async def php(self, ctx, *, code):
		await run_code(ctx, "php", "php", code, "//", 0x787CB4)

def setup(client):
	client.add_cog(Code(client))
