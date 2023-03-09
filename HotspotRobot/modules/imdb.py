import requests
from requests.exceptions import JSONDecodeError

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from HotspotRobot import pbot, SUPPORT_CHAT


@pbot.on_message(filters.command("imdb"))
async def imdb(client, message):
    text = message.text(" ", 1)
    if len(text) == 1:
        return await message.reply_text("» ɢɪᴠᴇ ᴍᴇ ꜱᴏᴍᴇ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ.\n   ᴇx. /imdb Altron")

    try:
        response = requests.get(f"https://api.safone.me/tmdb?query={text[1]}").json()["results"][0]
    except JSONDecodeError:
        return await message.reply_text(
            f"**Some Error Occured:** ᴘʟᴇᴀꜱᴇ ʀᴇᴘᴏʀᴛ ɪᴛ ᴀᴛ ᴏᴜʀ [ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ](https://t.me/{SUPPORT_CHAT})."
            )

    poster = response["poster"]
    imdb_link = response["imdbLink"]
    title = response["title"]
    rating = response["rating"]
    releasedate = response["releaseDate"]
    description = response["overview"]
    popularity = response["popularity"]
    runtime = response["runtime"]
    status = response["status"]
    await client.send_photo(
        message.chat.id,
        poster,
        caption=f"""**» IMDB Movie Details:**

‣ **Title** = `{title}`
‣ **Description** = `{description}`
‣ **Rating** = `{rating}`
‣ **Release-Date** = `{releasedate}`
‣ **Popularity** = `{popularity}`
‣ **Runtime** = `{runtime}`
‣ **Status** = `{status}`
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="• ɪᴍᴅʙ ʟɪɴᴋ •",
                        url=imdb_link,
                    ),
                ],
            ],
        ),
    )


__help__ = """
  ➲ /imdb <ᴍᴏᴠɪᴇ ɴᴀᴍᴇ>: ɢᴇᴛ ꜰᴜʟʟ ɪɴꜰᴏ ᴀʙᴏᴜᴛ ᴀ ᴍᴏᴠɪᴇ ꜰʀᴏᴍ [imdb.com](https://m.imdb.com)
"""
__mod_name__ = "Iᴍᴅʙ"
