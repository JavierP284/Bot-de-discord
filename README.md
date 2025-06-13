# Bot-de-discord

Este es un bot de Discord multifuncional desarrollado en Python. El bot incluye comandos para reproducir música en canales de voz, buscar información en Wikipedia, obtener imágenes de Pokémon y responder a mensajes en el chat. Utiliza la librería `discord.py` junto con otras herramientas como `yt-dlp` para la reproducción de música desde YouTube y `wikipedia` para búsquedas rápidas.

## Características principales

- **Reproducción de música:** Usa comandos de barra (`$play`, `$pause`, `$resume`, `$skip`, `$stop`) para buscar y reproducir canciones de YouTube directamente en un canal de voz.
- **Búsqueda en Wikipedia:** Consulta rápida de resúmenes de Wikipedia en español usando el comando `$wiki`.
- **Pokémon:** Obtén la imagen de cualquier Pokémon usando el comando `$poke`.
- **Respuestas automáticas:** El bot puede responder a ciertos mensajes en el chat de texto.
- **Soporte para comandos tradicionales y slash commands:** Puedes usar tanto comandos con prefijo (`$`) como comandos de barra (`/`).

## Instalación

1. Clona este repositorio.
2. Instala las dependencias con:
   ```
   pip install -r requirements.txt
   ```
3. Crea un archivo `.env` en la raíz del proyecto y agrega tu token de bot de Discord:
   ```
   TOKEN=tu_token_aqui
   ```
4. Asegúrate de tener `ffmpeg` instalado y agregado al PATH de tu sistema.
5. Ejecuta el bot con:
   ```
   python main.py
   ```

## Uso
- Para mostrar los comandos:
  Escribe `$info`  
- Para reproducir música:  
  Escribe `$play <nombre de la canción o URL de YouTube>` en un canal de texto.
- Para pausar, reanudar, saltar o detener la música:  
  Usa `$pause`, `$resume`, `$skip`, `$stop`.
- Para buscar en Wikipedia:  
  Escribe `$wiki <consulta>`.
- Para obtener la imagen de un Pokémon:  
  Escribe `$poke <nombre_del_pokemon>`.
  
Basado en `discord.py`, `yt-dlp`, `wikipedia` y otras librerías de código abierto.
