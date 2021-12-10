import discord
from discord.ext import commands
from main import p
import os
from dotenv import load_dotenv
import requests
import json
import traceback
import sys
import time
import subprocess
import re
import textwrap

class Code(commands.Cog):
	global p

	def __init__(self, client):
		self.client = client

	# When the cog is loaded
	@commands.Cog.listener()
	async def on_ready(self):
		print(f'[LOGS] {self.__class__.__name__} cog has been loaded.\n')

	# Python command
	@commands.command(name='python', aliases=['Python', 'PYTHON', 'py', 'Py', 'pY', 'PY'], description='Executes Python code(you cannot import modules).')
	async def code(self, ctx, *, code):
		e = code.lower()
		#code = code.replace('import', '')
		code = code.replace('```py', '```')

		start = time.process_time()
		arg = code

		arg = arg.split('```')
		print(arg)

		param = arg[2]
		f = open('inputs.txt', 'w')
		f.write(param)
		f.close()

		arg=arg[1]
		t = textwrap.indent(arg, '\t')
		f = open("output.py", "w")
		f.write(
f'''
import traceback
try:
	{t}
except:
	print(traceback.format_exc())
'''
		)
		f.close()

		error = False
		try:
			res = subprocess.check_output("python3 output.py < inputs.txt", shell=True)
		except subprocess.CalledProcessError as e:
			res = 'Syntax Error'
			error = True

		time_taken = str(time.process_time() - start)
		'''
		if 'import' in e:
			embed = discord.Embed(description='**You cannot import modules.**', color=discord.Color.gold())'''
		if error == False:
			if res.decode('UTF-8') == '':
				embed = discord.Embed(color=discord.Color.gold())
				embed.add_field(name='Program Output', value=f'```css\nNo Output\n```')
			else:
				embed = discord.Embed(color=discord.Color.gold())
				embed.add_field(name="Program Output", value=f'```yaml\n{res.decode("UTF-8")}\n```')
		elif error:
			embed = discord.Embed(color=discord.Color.gold())
			embed.add_field(name='Program Output', value=f'```arm\n{res}\n```')

		await ctx.send(embed=embed)

		os.remove("output.py")
		os.remove("inputs.txt")

def setup(client):
	client.add_cog(Code(client))

'''
Traceback (most recent call last):
  File "output.py", line 5, in <module>
    u
NameError: name 'u' is not defined
'''
