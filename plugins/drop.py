from bot import Bot
# from os import environ
from config import Api_key
import aiohttp
from pyrogram import Client, filters

@client.on_message(filters.command('api') & filters.private)
async def start(client, message):
    await message.reply(
        f"**Hi {message.chat.first_name}! Send Your Api Here 😉**\n\n"
        "Some Went Worng contact 👉 <a href=\"https://t.me/groupdcbots\">@Groupdcbots</a>.")


@client.on_message(filters.regex(r'https?://[^\s]+') & filters.private)
async def link_handler(client, message):
    links = message.text
    links = links.split("\n")
    for num in range(len(links)):
      try:
        short_link = await get_shortlink(links[num])
        await message.reply(f'**🔱 Long URL:** {links[num]}\n**⚜️ Shortened URL:** {short_link}\n\n〽️ Powered by <a href="https://t.me/groupdcbots\">@Groupdcbots</a>', quote=True, disable_web_page_preview=True)
      except Exception as e:
        await message.reply(f'Error: {e}', quote=True)


async def get_shortlink(link):
    url = 'https://urlshortx.com/api'
    params = {'api': Api_key, 'url': link}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, raise_for_status=True) as response:
            data = await response.json()
            return data["shortenedUrl"]


bot.run()
