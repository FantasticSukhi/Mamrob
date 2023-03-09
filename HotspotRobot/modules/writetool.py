import requests

from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

from HotspotRobot import BOT_NAME, BOT_USERNAME, pbot as hotspot


@hotspot.on_message(filters.command("write"))
async def handwrite(_, message: Message):
    if message.reply_to_message:
        if message.reply_to_message.text:
          text = message.reply_to_message.text
        else:
          text = message.reply_to_message.caption

    else:
        text = message.text.split(" ", 1)
        if len(text) == 1:
            await message.reply_text("ɢɪᴠᴇ ᴍᴇ ᴀ ᴛᴇxᴛ ᴡʀɪᴛᴇ.")
            return
        text = text[1]

    m = await message.reply_text("ᴡʀɪᴛɪɴɢ ʏᴏᴜʀ ᴛᴇxᴛ...")
    API = f"https://api.sdbots.tk/write?text={text}"
    req = requests.get(API).url
    caption = f"""
ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴡʀɪᴛᴛᴇɴ ᴛᴇxᴛ 💘

✨ **ᴡʀɪᴛᴛᴇɴ ʙʏ :**
**•**  [{BOT_NAME}](https://t.me/{BOT_USERNAME})
🥀 **ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ :**
**•**  {message.from_user.mention}
"""

    await m.delete()
    await hotspot.send_photo(
        message.chat.id,
        photo=req,
        caption=caption,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("• ᴛᴇʟᴇɢʀᴀᴩʜ •", url=req)]]
        ),
    )


__mod_name__ = "WʀɪᴛᴇTᴏᴏʟ"
__help__ = """
‣ ᴡʀɪᴛᴇꜱ ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ ᴏɴ ᴡʜɪᴛᴇ ᴘᴀɢᴇ ᴡɪᴛʜ ᴀ ᴘᴇɴ 🖊

 ➲ /write <ᴛᴇxᴛ> or <ʀᴇᴘʟʏ ᴛᴏ ᴛᴇxᴛ> : ᴡʀɪᴛᴇꜱ ᴛʜᴇ ᴛᴇxᴛ.
"""
