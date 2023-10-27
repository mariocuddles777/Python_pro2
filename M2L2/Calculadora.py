import discord
from discord.ext import commands
import random
import math

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
    channel_id = 1152369673573244999
    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send('''Hola, soy Mr.Calculator y soy una calculadora.
                    Para poder llamarme deberas usar el prefix &, e introducir alguno de los siguientes comandos.
                    1- add: Con este comando podras sumar dos numeros
                    2- rest: Con este comando podras restar dos numeros
                    3- multi: Con este comando podras multiplicar dos numeros
                    4- divi: Con este comando podras dividir dos numeros
                    5- power: Con este comando podras elevar un numero
                    6- raiz: Con este comando podras sacar la raiz cuadrada de un numero''')

@bot.command()
async def sum(ctx, num1: float, num2: float):
    result = num1 + num2
    await ctx.send(f"La suma de {num1} y {num2} es: {result}")

@bot.command()
async def subtract(ctx, num1: float, num2: float):
    result = num1 - num2
    await ctx.send(f"La resta de {num1} y {num2} es: {result}")

@bot.command()
async def multiply(ctx, num1: float, num2: float):
    result = num1 * num2
    await ctx.send(f"El producto de {num1} y {num2} es: {result}")

@bot.command()
async def divide(ctx, num1: float, num2: float):
    if num2 != 0:
        result = num1 / num2
        await ctx.send(f"La división de {num1} entre {num2} es: {result}")
@bot.command()
async def raiz(ctx, left: int):
    """Adds two numbers together."""
    raiz = math.sqrt(left)
    await ctx.send(raiz)
@bot.command()
async def power(ctx, base: float, exponent: float):
    result = base ** exponent
    await ctx.send(f"{base} elevado a la potencia {exponent} es igual a: {result}")

bot.run('MTE1OTk2OTc3NzU4NzA2NTAyNA.GoyW8n.IJ0PKPYr1ll-65DFFrWPZPyF42HeeJdB8OFSfE')
bot.run('token')