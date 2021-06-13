import discord
from discord.ext import commands
import json
import requests

client = commands.Bot(command_prefix=';')
client.remove_command('help')

@client.command()
async def hi(ctx):
    await ctx.send('Hello!')

@client.command()
async def say(ctx, *, text):
    await ctx.send(text)
    await ctx.message.delete()

@client.command()
async def help(ctx):
    embed = discord.Embed(
        title = '**All commands** </>',
        description = '''Hi! Im bot Hooks Manager! 

`Moderarion`
`ban`, `kick`, `warn`, `say`.

`Utils`
`dm`, `say`, `avatar`, `user`, `server`, `mail`, `cat`, `fox`,`dog`,`wink`,`koala`.

`System`
 `support`, `bot`.

**Prefix: [;]**''',
    colour = discord.Colour.from_rgb(106, 192, 245)
    )


    await ctx.send(embed=embed)



@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason=None):
  await user.kick(reason=reason)
  await ctx.send(f"{user} kicked from this guild.")

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *, reason=None):
  await user.ban(reason=reason)
  await ctx.send(f"{user} banned from this guild.")

@client.command()
async def avatar(ctx, *,  avamember : discord.Member=None):
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)

@client.command()
async def clear(ctx, amount=None):

    await ctx.channel.purge(limit=int(amount))
    embed = discord.Embed(
        description = '<a:679326929895161882:853672921574277120> Success deleted!',
    colour = discord.Colour.from_rgb(106, 192, 245)
    )
    await ctx.send(embed=embed)
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound ):
        await ctx.send(embed = discord.Embed(description = f'** {ctx.author.name}, command not found.**', color=0x0c0c0c))


@client.event
async def on_ready():
    activity = discord.Game(name=";help \\\ шард #5", type=3)
    await client.change_presence(status=discord.Status.idle, activity=activity)
    
@client.command()
async def fox(ctx):
    response = requests.get('https://some-random-api.ml/img/fox') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = 0xff9900, title = 'Random Fox') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    embed.set_footer(text=f"Request by: {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed = embed) # Отправляем Embed

@client.command()
async def cat(ctx):
    response = requests.get('https://some-random-api.ml/img/cat') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = 0xff9900, title = 'Random Cat') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    embed.set_footer(text=f"Request by: {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed = embed) # Отправляем Embed

@client.command()
async def dog(ctx):
    response = requests.get('https://some-random-api.ml/img/dog') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = 0xff9900, title = 'Random Dog') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    embed.set_footer(text=f"Request by: {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed = embed) # Отправляем Embed

@client.command()
async def wink(ctx):
    response = requests.get('https://some-random-api.ml/animu/wink') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = 0xff9900, title = 'Winking ') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    embed.set_footer(text=f"Request by: {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed = embed) # Отправляем Embed

@client.command()
async def koala(ctx):
    response = requests.get('https://some-random-api.ml/img/koala') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = 0xff9900, title = 'Random Koala') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    embed.set_footer(text=f"Request by: {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed = embed) # Отправляем Embed

import discord
from discord.ext import commands
import json
import requests

client = commands.Bot(command_prefix=';')
client.remove_command('help')

@client.command()
async def hi(ctx):
    await ctx.send('Hello!')

@client.command()
async def say(ctx, *, text):
    await ctx.send(text)
    await ctx.message.delete()

@client.command()
async def help(ctx):
    embed = discord.Embed(
        title = '**All commands** </>',
        description = '''Hi! Im bot Hooks Manager! 

`Moderarion`
`ban`, `kick`, `warn`, `say`.

`Utils`
`dm`, `say`, `avatar`, `user`, `server`, `mail`, `cat`, `fox`,`dog`,`wink`,`koala`.

`System`
 `support`, `bot`.

**Prefix: [;]**''',
    colour = discord.Colour.from_rgb(106, 192, 245)
    )


    await ctx.send(embed=embed)



@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason=None):
  await user.kick(reason=reason)
  await ctx.send(f"{user} kicked from this guild.")

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *, reason=None):
  await user.ban(reason=reason)
  await ctx.send(f"{user} banned from this guild.")

@client.command()
async def avatar(ctx, *,  avamember : discord.Member=None):
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)

@client.command()
async def clear(ctx, amount=None):

    await ctx.channel.purge(limit=int(amount))
    embed = discord.Embed(
        description = '<a:679326929895161882:853672921574277120> Success deleted!',
    colour = discord.Colour.from_rgb(106, 192, 245)
    )
    await ctx.send(embed=embed)
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound ):
        await ctx.send(embed = discord.Embed(description = f'** {ctx.author.name}, command not found.**', color=0x0c0c0c))


@client.event
async def on_ready():
    activity = discord.Game(name=";help \\\ шард #5", type=3)
    await client.change_presence(status=discord.Status.idle, activity=activity)
    
@client.command()
async def fox(ctx):
    response = requests.get('https://some-random-api.ml/img/fox') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = 0xff9900, title = 'Random Fox') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    embed.set_footer(text=f"Request by: {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed = embed) # Отправляем Embed

@client.command()
async def cat(ctx):
    response = requests.get('https://some-random-api.ml/img/cat') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = 0xff9900, title = 'Random Cat') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    embed.set_footer(text=f"Request by: {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed = embed) # Отправляем Embed

@client.command()
async def dog(ctx):
    response = requests.get('https://some-random-api.ml/img/dog') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = 0xff9900, title = 'Random Dog') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    embed.set_footer(text=f"Request by: {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed = embed) # Отправляем Embed

@client.command()
async def wink(ctx):
    response = requests.get('https://some-random-api.ml/animu/wink') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = 0xff9900, title = 'Winking ') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    embed.set_footer(text=f"Request by: {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed = embed) # Отправляем Embed

@client.command()
async def koala(ctx):
    response = requests.get('https://some-random-api.ml/img/koala') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = 0xff9900, title = 'Random Koala') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    embed.set_footer(text=f"Request by: {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed = embed) # Отправляем Embed

token = os.environ.get('BOT_TOKEN')

client.run(str(token))
