import discord
from discord.ext import commands
import os
import asyncio
import time
import subprocess
import textwrap
import io
import signal
import py_compile
import requests
from traceback import print_exc
from pyston import PystonClient, File

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
	@commands.cooldown(1, 5, commands.BucketType.user)
	async def python(self, ctx, *, code):
		await ctx.message.add_reaction("<a:colorfulloading:921304808256860171>")

		code = code.replace('```py', '```')
		code = code.split('```')
		code = code[1][1:]

		pyston = PystonClient()
		output = await pyston.execute("python", [File(code)])
		success = output.success
		output = str(output)

		if output == "":
			output = "```\nNo Output\n```" 
		else:
			if len(output) > 980:
				output = output[:980]
				output = output + "\n# Length limit reached"
			
			if output.count('\n') > 51:
				o = output.split('\n')
				o = o[:51]
				
				result = ''
				for item in o:
					result += item + '\n'
				
				output = result + '# Length limit reached'

			output = f"```yaml\n{output}\n```"	

		embed = discord.Embed(color=discord.Color.gold() if success else discord.Color.red())
		embed.add_field(name='Program Output', value=output)
		embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)

		await ctx.message.clear_reaction("<a:colorfulloading:921304808256860171>")
		await ctx.send(embed=embed)
		
def setup(client):
	client.add_cog(Code(client))
