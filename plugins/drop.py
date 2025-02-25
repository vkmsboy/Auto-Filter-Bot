from bot import Bot
# from os import environ

import aiohttp
from pyrogram import Client, filters

API_KEY = "e3eddb3e7c5513eee187120fce788ddc4a1a643b"

@Client.on_message(filters.command('api') & filters.private)
async def start(Client, message):
    await message.reply(
        f"**Hi {message.chat.first_name}! Send Your Api Here 😉**\n\n"
        "Some Went Worng contact 👉 <a href=\"https://t.me/groupdcbots\">@Groupdcbots</a>.")


@Client.on_message(filters.regex(r'https?://[^\s]+') & filters.private)
async def link_handler(Client, message):
    links = message.text
    links = links.split("\n")
    for num in range(len(links)):
      try:
        short_link = await get_shortlink(links[num])
        await message.reply(f'**🔱 Long URL:** {links[num]}\n**⚜️ Shortened URL:** {short_link}\n\n〽️ Powered by <a href="https://t.me/groupdcbots\">@Groupdcbots</a>', quote=True, disable_web_page_preview=True)
      except Exception as e:
        await message.reply(f'Error: {e}', quote=True)


async def get_shortlink(link):
    url = 'https://droplink.co/api'
    params = {'api': API_KEY, 'url': link}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, raise_for_status=True) as response:
            data = await response.json()
            return data["shortenedUrl"]
