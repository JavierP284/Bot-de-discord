import discord
from discord.ext import commands
import requests
import wikipedia
import os
from dotenv import load_dotenv
from datetime import datetime
import yt_dlp
import asyncio

from music import play, pause, resume, skip, stop  # Importa los comandos de música

load_dotenv()
token = os.getenv("TOKEN")
print(f"Token cargado: {token}")  # Solo para depuración, luego bórralo

SONG_QUEUES = {}

def buscar_wikipedia(consulta):
    try:
        wikipedia.set_lang("es")
        resultado = wikipedia.summary(consulta, sentences=4)
        return resultado
    except wikipedia.exceptions.DisambiguationError as e:
        return f'La busqueda "{consulta}" es ambigua, por favor especifica más.'
    except wikipedia.exceptions.PageError as e:
        return f'No se encontro informacion relacionada con "{consulta}".'

intents = discord.Intents.all()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='$', intents=intents)

# REGISTRA LOS COMANDOS DE MÚSICA
bot.add_command(play)
bot.add_command(pause)
bot.add_command(resume)
bot.add_command(skip)
bot.add_command(stop)

@bot.command()
async def info(ctx):
    mensaje = (
        "**Comandos disponibles:**\n"
        "🎵 `$play <canción o url>` — Reproduce música de YouTube en tu canal de voz\n"
        "⏸️ `$pause` — Pausa la música\n"
        "▶️ `$resume` — Reanuda la música\n"
        "⏭️ `$skip` — Salta la canción actual\n"
        "⏹️ `$stop` — Detiene la música y desconecta\n"
        "📚 `$wiki <consulta>` — Busca un resumen en Wikipedia\n"
        "🕹️ `$poke <nombre_pokemon>` — Muestra la imagen de un Pokémon\n"
        "ℹ️ `$info` — Muestra este mensaje de ayuda\n"
    )
    await ctx.send(mensaje)

@bot.command()
async def poke(ctx, arg):
    try:
        pokemon = arg.split(" ",1)[0].lower()
        result = requests.get("https://pokeapi.co/api/v2/pokemon/"+pokemon)
        if result.text == "Not Found":
            await ctx.send("Pokemon no encontrado!")
        else:
            image_url = result.json()['sprites']['front_default']
            print(image_url)
            await ctx.send(image_url)

    except Exception as e:
        print(f"Error: ", e)

@poke.error
async def poke_error(ctx, error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send("Proporciona el noombre de un Pokemon")

@bot.command()
async def wiki(ctx, *, consulta):
    try:
        resultado= buscar_wikipedia(consulta)
        await ctx.send(resultado)
    except Exception as e:
        await ctx.send(f"Error al buscar en Wikipedia: {e}")

@bot.event
async def on_message(message):
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")

    if "hola" in message.content.lower():
        await message.channel.send(f"Hola! {message.author.name}!")
    
    # Esto permite que los comandos funcionen
    await bot.process_commands(message)

@bot.event
async def on_ready():
    print(f"Estamos dentro! {bot.user}")

bot.run(token)