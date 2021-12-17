import discord
from discord.ext import commands
from main import p
import os
import asyncio
from dotenv import load_dotenv
import requests
import json
import traceback
import sys
import time
import subprocess
import re
import textwrap
import io
import signal
import py_compile

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
		start = time.process_time()
		e = code.lower()
		code = code.replace('```py', '```')
		code = code.replace('open("images/', 'open("pp_iz_lubnbhvgsfdty678d9soewrt56kl7uyitydg7f8s904w5ijyjhgdufd7sa8de9rtuy/')
		code = code.replace("open('images/", "open('pp_iz_lubnbhvgsfdty678d9soewrt56kl7uyitydg7f8s904w5ijyjhgdufd7sa8de9rtuy/")
		arg = code
		arg = arg.split('```')

		param = arg[2]
		f = open('inputs.txt', 'w')
		f.write(param)
		f.close()

		arg=arg[1]
		
		t = textwrap.indent(arg, '\t')
		f = open("output.py", "w")
		f.write(
f'''
import traceback; import sys; sys.modules['os']=None; sys.modules['sys']=None; del sys
try:
	{t}
except:
	print(traceback.format_exc())
'''
		)
		f.close()

		res = ''
		error = False	
		try:
			with open("check.py", "w") as check:
				check.write(arg[1:])

			py_compile.compile('check.py', doraise=True)
			print(f'[CODE]\n{arg[1:]}')
		except py_compile.PyCompileError as se:
			
			res = str(se)
			res = res.replace("check.py", "file.py")
			res = res[1:]
			error = True

		os.remove('check.py')		

		if error == False:
			res = subprocess.Popen("python3 output.py < inputs.txt", shell=True, stdout=subprocess.PIPE, preexec_fn=os.setsid)

			await asyncio.sleep(1.9)
			os.killpg(os.getpgid(res.pid), signal.SIGTERM)

			o = ''
			for line in io.TextIOWrapper(res.stdout, encoding="utf-8"):
				if (time.process_time() - start) > 2:
					break
				o += line
			
			with open('o.txt', 'w') as file:
				file.write(o)

			output = ""
			try:
				with open("o.txt", "r") as file:
					for i in range(51):
						line = next(file).strip()
						output += line + '\n'
				output += "#Length limit reached"
			except:
				f = open("o.txt", "r")
				output = f.read()
				f.close()
		else:
			output = res
		try:
			os.remove("o.txt")
		except:
			pass
		os.remove("output.py")
		os.remove("inputs.txt")


		''''
		if 'import' in e:
			embed = discord.Embed(description='**You cannot import modules.**', color=discord.Color.gold())
		'''
		if 'exec(' in e or 'eval(' in e:
			embed = discord.Embed(description='**Use of `eval()` and `exec()` is restricted.**', color=discord.Color.gold())
		elif output== '':
			embed = discord.Embed(color=discord.Color.gold())
			embed.add_field(name='Program Output', value='```css\nNo Output\n```')
			embed.add_field(name='Time Taken', value=f'```\n{str(time.process_time() - start)[:12]}\n```', inline=False)
			print("[OUTPUT]\nNo Output")
		else:
			if error == False:
				if '  File "output.py", line ' in output:
					output = output.replace('  File "output.py", line ', '  File "file.py", line ')
					output = output.replace("pp_iz_lubnbhvgsfdty678d9soewrt56kl7uyitydg7f8s904w5ijyjhgdufd7sa8de9rtuy/", "images/")

					o = output
					try:
						num = str(int(o[58:61]) - 4)
						n = 62
					except:
						try:
							num = str(int(o[58:60]) - 4)
							n = 61
						except:
							num = str(int(o[58]) - 4)
							n = 59

					o = output[:58] + num + output[n:]
					output = o

			embed = discord.Embed(color=discord.Color.gold())
			if len(output) <= 980:
				embed.add_field(name="Program Output", value=f'```yaml\n{output}\n```')
				
				if "Traceback" in output or "SyntaxError:" in output:
					print(f'[ERROR]\n{output}')
				else:
					print(f'[OUTPUT]\n{output}')
			else:
				embed.add_field(name="Program Output", value=f'```yaml\n{output[:980]} #Size limit reached\n```')
				print(f'[OUTPUT]\n{output[:980]}')
			embed.add_field(name='Time Taken', value=f'```\n{str(time.process_time() - start)[:12]}\n```', inline=False)

		await ctx.send(embed=embed)

		with open('webserver.py', 'w') as w:
			w.write('''
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Normal Bot : ONLINE"

def run():
  app.run(host='0.0.0.0',port=8080)

def webserver():
    t = Thread(target=run)
    t.start()
			''')

def setup(client):
	client.add_cog(Code(client))
