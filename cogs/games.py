import nextcord as discord
from nextcord.ext import commands
from main import p
import random

class Games(commands.Cog):
	global p

	def __init__(self, client):
		self.client = client

	# When the cog is loaded
	@commands.Cog.listener()
	async def on_ready(self):
		print(f'[LOGS] {self.__class__.__name__} cog has been loaded.\n')

	# Tictactoe command
	@commands.command(name='tictactoe', aliases=['Tictactoe', 'TICTACTOE', 'TicTacToe', 'tic-tac-toe', 'Tic-tac-toe', 'TIC-TAC-TOE', 'ttc', 'Ttc', 'TTC', 't-t-c', 'T-t-c', 'T-T-C'], description='Play Tic-Tac-Toe with your friends!')
	async def tictactoe(self, ctx, user: discord.Member):
		reactions = ['1️⃣', '1️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '❌']

def setup(client):
	client.add_cog(Games(client))
