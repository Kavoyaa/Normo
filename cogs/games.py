import discord
from discord.ext import commands
from main import p
import random

# Variables for Tictactoe and Place comamnds
ttc_player1 = ""
ttc_player2 = ""
ttc_turn = ""
ttc_gameOver = True
ttc_board_emoji = "⬜"

ttc_BOARD = []

ttc_winningConditions = [
	[0, 1, 2],
	[3, 4, 5],
	[6, 7, 8],
	[0, 3, 6],
	[1, 4, 7],
	[2, 5, 8],
	[0, 4, 8],
	[2, 4, 6]
]

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
		global count
		global ttc_player1
		global ttc_player2
		global ttc_turn
		global ttc_gameOver
		global ttc_board_emoji

		if ttc_gameOver:
			global ttc_BOARD

			ttc_BOARD = [
				ttc_board_emoji,
				ttc_board_emoji,
				ttc_board_emoji,
				ttc_board_emoji,
				ttc_board_emoji,
				ttc_board_emoji,
				ttc_board_emoji,
				ttc_board_emoji,
				ttc_board_emoji
			]
			ttc_turn = ''
			ttc_gameOver = False
			count = 0

			ttc_player1 = user
			ttc_player2 = ctx.author

			# Displaying the board
			line = ''
			output = []
			for x in range(len(ttc_BOARD)):
				if x == 2 or x == 5 or x == 8:
					line += ' ' + ttc_BOARD[x]
					output.append(line)
					line = ''
				else:
					line += ' ' + ttc_BOARD[x]

			ttc_board = f"{output[0]}\n{output[1]}\n{output[2]}"

			embed = discord.Embed(title='Tic-Tac-Toe', colour=0x808080)

			embed.add_field(name='Player One ❮🇽❯', value=f'<@{str(ttc_player1.id)}>', inline=True)

			embed.add_field(name='Player Two ❮🅾️❯', value=f'<@{str(ttc_player2.id)}>', inline=True)

			embed.add_field(name=chr(173), value=chr(173), inline=True) # Empty field

			embed.add_field(name='Board', value=ttc_board.replace(' ', ''), inline=True)

			embed.add_field(name='Help', value=f'-`{p}place <1-9>` to mark\n a tile.\n-`{p}endttc` to end game.', inline=True)

			embed.add_field(name=chr(173), value=chr(173), inline=True) # Empty field

			await ctx.send(embed=embed)

			# Randomizing who goes first
			num = random.randint(1, 2)

			if num == 1:
				ttc_turn = ttc_player1
				await ctx.send(f'> It is <@{str(ttc_player1.id)}>\'s turn.')
			elif num == 2:
				ttc_turn = ttc_player2
				await ctx.send(f'> It is <@{str(ttc_player2.id)}>\'s turn.')
		else:
			await ctx.send(f'A game is already in progress! There can only be one game going on at a time. Use `{p}endttc` to end game.')

		print(f'[LOGS] Command used: {p}tictactoe')
	
	# Place command
	@commands.command(name='place', aliases=['PLACE', 'Place'], description='Used to mark a tile in Tic-Tac-Toe.')
	async def place(self, ctx, position: int):
		global ttc_turn
		global ttc_player1
		global ttc_player2
		global count
		global ttc_gameOver
		global ttc_board_emoji

		def checkWinner(winningConditions, mark):
			global ttc_gameOver
			for condition in winningConditions:
				if ttc_BOARD[condition[0]] == mark and ttc_BOARD[condition[1]] == mark and ttc_BOARD[condition[2]] == mark:
					ttc_gameOver = True

		if not ttc_gameOver:
			mark = ''
			if ttc_turn == ctx.author:
				if ttc_turn == ttc_player1:
					mark = '🇽'
				elif ttc_turn == ttc_player2:
					mark = '🅾️'
			
				if 0 < position < 10 and ttc_BOARD[position - 1] == ttc_board_emoji :
					ttc_BOARD[position - 1] = mark
					count += 1

					# Displaying the board
					line = ''
					output = []
					for x in range(len(ttc_BOARD)):
						if x == 2 or x == 5 or x == 8:
							line += ' ' + ttc_BOARD[x]
							output.append(line)
							line = ''
						else:
							line += ' ' + ttc_BOARD[x]
					
					ttc_board = f'{output[0]}\n{output[1]}\n{output[2]}'

					embed = discord.Embed(title='Tic-Tac-Toe', colour=0x808080)

					embed.add_field(name='Player One ❮🇽❯', value=f'<@{str(ttc_player1.id)}>', inline=True)

					embed.add_field(name='Player Two ❮🅾️❯', value=f'<@{str(ttc_player2.id)}>', inline=True)

					embed.add_field(name=chr(173), value=chr(173), inline=True) # Empty field

					embed.add_field(name='Board', value=ttc_board.replace(' ', ''), inline=True)

					embed.add_field(name='Help', value=f'-`{p}place <1-9>` to mark\n a tile.\n-`{p}endttc` to end game.', inline=True)

					embed.add_field(name=chr(173), value=chr(173), inline=True) # Empty field

					await ctx.send(embed=embed)

					checkWinner(ttc_winningConditions, mark)
					if ttc_gameOver == True:
						await ctx.send(f'{mark} wins! GG.')
					elif count >= 9:
						ttc_gameOver = True

						await ctx.send('It\'s a draw!')
					
					# Switching turns
					if ttc_turn == ttc_player1:
						ttc_turn = ttc_player2
					elif ttc_turn == ttc_player2:
						ttc_turn = ttc_player1
				else:
					await ctx.send('Make sure you **choose a number between 1 and 9** and **an empty tile**.')
			else:
				await ctx.send('It is not your turn!')
		else:
			await ctx.send(f'Start start a new game using the `{p}tictactoe` command.')


	# In case of error in tictactoe command
	@tictactoe.error
	async def tictactoe_error(self, ctx, error):
		print(error)
		# If the error is MissingRequiredArgument, which means one or more required arguments weren't given.
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send('Mention 2 players to use command.')
		# If the error is BadArgument, which means one or more arguments were invalid.
		elif isinstance(error, commands.BadArgument):
			await ctx.send('Make sure to mention/ping the players.')

	# In case of error in place command
	@place.error
	async def place_error(self, ctx, error):
		# If the error is MissingRequiredArgument, which means one or more required arguments weren't given.
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send('Enter a position you would like to mark.')
		# If the error is BadArgument, which means one or more arguments were invalid.
		elif isinstance(error, commands.BadArgument):
			await ctx.send('Make sure to enter a **number** between 1 to 9.')

	# Endttc command
	@commands.command(name='endttc', aliases=['EndTTC', 'ENDTTC', 'endTtc', 'ENDttc', 'Endttc', 'endTTC', 'endtictactoe', 'Endtictactoe', 'ENDTICTACTOE', 'EndTicTacToe', 'EndTic-Tac-Toe', 'endTicTacToe'], description='Ends an ongoing Tic-Tac-Toe game.')
	async def endttc(self, ctx):
		global ttc_gameOver

		if ttc_gameOver:
			await ctx.send(f'There is no ongoing game to end! Use `{p}tictactoe` to start a new game.')
		else:
			if ctx.author == ttc_player1 or ctx.author == ttc_player2:
				ttc_gameOver = True
				await ctx.send('The game has ended.')
			else:
				await ctx.send('You must be a participant in the game to use this command.')

def setup(client):
	client.add_cog(Games(client))
