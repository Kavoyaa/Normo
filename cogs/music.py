import discord
from discord.ext import commands
from main import p
import requests

class Music(commands.Cog):
	global p

	def __init__(self, client):
		self.client = client

	# When the cog is loaded
	@commands.Cog.listener()
	async def on_ready(self):
		print(f'[LOGS] {self.__class__.__name__} cog has been loaded.\n')

	# Lyrics command
	@commands.command(name='lyrics', aliases=['lyric'], description='Shows the lyrics of the inputted song!')
	async def afk(self, ctx, *, song):
		'''Returns lyrics of the inputted song.'''
		try:
			s = song.replace(" ", "_")

			res = requests.get(f"https://some-random-api.ml/lyrics?title={s}")
			r = res.json()

			title = r['title']
			author = r['author']
			thumbnail = r['thumbnail']['genius']
			lyrics = r['lyrics']

			embed = discord.Embed(description=lyrics, color=discord.Color.blue())
			embed.set_author(name=f'"{title}" by {author}')
			embed.set_thumbnail(url=thumbnail)
			embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
			
			await ctx.send(embed=embed)
		except:
			embed = discord.Embed(color=discord.Color.red())
			embed.add_field(name='Command Error:', value='Song not found. Try typing the name of the artist along with the song name.')
			await ctx.send(embed=embed)

def setup(client):
	client.add_cog(Music(client))
