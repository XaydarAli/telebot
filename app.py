"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging
import requests
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '7207119497:AAFjb9J2uaXasmN6c8f2fMHdeZ037HYfF18'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("""Hi!\nI'm your assistant fo find your favourite songs!\nPowered by aiogram.
    /songs
    /artists
    /albums
     """)
@dp.message_handler(commands=['songs'])
async def send_songs(message: types.Message):
    songs=requests.get(f'http://127.0.0.1:8000/songs')
    for song in songs.json():
        await message.reply(f"""
        TITlE: {song['title']}
        Artist: {song['album']['artist']}
        Album: {song['album']}
        """

        )

@dp.message_handler(commands=['artists'])
async def send_artists(message: types.Message):
    artists=requests.get(f'http://127.0.0.1:8000/artists')
    for artist in artists.json():
        await message.reply(f"""
        first_name: {artist['first_name']}
        last_name: {artist['last_name']}
        """

        )


@dp.message_handler(commands=['albums'])
async def send_albums(message: types.Message):
    albums=requests.get(f'http://127.0.0.1:8000/albums')
    for album in albums.json():
        await message.reply(f"""
        TITLE: {album['title']}
        """

        )

@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)