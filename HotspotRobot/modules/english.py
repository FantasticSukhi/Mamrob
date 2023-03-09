import requests

from telethon import *
from telethon.tl.types import *
from requests.exceptions import JSONDecodeError

from HotspotRobot import SUPPORT_CHAT
from HotspotRobot.events import register

API_KEY = "6ae0c3a0-afdc-4532-a810-82ded0054236"
URL = "http://services.gingersoftware.com/Ginger/correct/json/GingerTheText"


@register(pattern="^/spell(?: |$)(.*)")
async def _(event):
    text = event.text.split(" ", 1)
    reply_msg = event.get_reply_message()

    if event.reply_to_msg_id and reply_msg.text:
        text = reply_msg.text
    else:
        if len(text) == 1:
            return await event.reply("» ɢɪᴠᴇ ᴍᴇ ꜱᴏᴍᴇ ꜱᴇɴᴛᴇɴᴄᴇ.\n  ᴇx. /spell Altron   or\n  ᴇx. /spell <ʀᴇᴘʟʏ ᴛᴏ ᴍꜱɢ>")
        text = text[1]

    try:
        response = requests.get(f"https://api.safone.me/spellcheck?text={text}").json()
    except JSONDecodeError:
        return await event.reply(
            f"**Some Error Occured:** ᴘʟᴇᴀꜱᴇ ʀᴇᴘᴏʀᴛ ɪᴛ ᴀᴛ ᴏᴜʀ [ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ](https://t.me/{SUPPORT_CHAT})."
            )

    TEXT = f"""**Sentence:** `{text}`\n\n**Corrected:** `{response["corrected"]}`\n\n**Corrections:**"""
    for correction in response["corrections"]:
        TEXT += f"""\n  •  `{correction["text"]} - {correction["correct"]}`"""

    await event.reply(TEXT)


@register(pattern="^/define")
async def _(event):
    text = event.text.split(" ", 1)
    if len(text) == 1:
        return await event.reply(f"**Usage:**  /define <ᴡᴏʀᴅ>")
    
    response = requests.get(f"https://wordsapiv1.p.mashape.com/words/{text[1]}/definitions")
    AltPy = f"» ᴍᴇᴀɴɪɴɢꜱ ᴏꜰ {text[1]}:"
    for i in range(5):
        try:
            meaning = response["definitions"][i]["definition"]
            AltPy += f"\n - `{meaning}`"
        except IndexError:
            break

    await event.reply(AltPy)


@register(pattern="^/synonyms")
async def _(event):
    text = event.text.split(" ", 1)
    if len(text) == 1:
        return await event.reply(f"**Usage:**  /synonyms <ᴡᴏʀᴅ>")

    response = requests.get(f"https://wordsapiv1.p.mashape.com/words/{text[1]}/synonyms")
    AltPy = f"» ꜱʏɴᴏɴʏᴍꜱ ᴏꜰ {text[1]}:\n"
    for i in range(5):
        try:
            Syn = response["synonyms"][i]
            AltPy += f"\n - `{Syn}`"
        except IndexError:
            break

    await event.reply(AltPy)


@register(pattern="^/antonyms")
async def _(event):
    text = event.text.split(" ", 1)
    if len(text) == 1:
        return await event.reply(f"**Usage:**  /antonyms <ᴡᴏʀᴅ>")

    response = requests.get(f"https://wordsapiv1.p.mashape.com/words/{text[1]}/antonyms")
    AltPy = f"» ᴀɴᴛᴏɴʏᴍꜱ ᴏꜰ {text}:\n"
    for i in range(5):
        try:
            Ant = response["antonyms"][i]
            AltPy += f"\n - {Ant}"
        except IndexError:
            break

    await event.reply(AltPy)


__help__ = f"""
  ➲ /define <text> : ᴛʏᴘᴇ ᴛʜᴇ ᴡᴏʀᴅ ᴏʀ ᴇxᴘʀᴇꜱꜱɪᴏɴ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ꜱᴇᴀʀᴄʜ
     ‣ **For example**: /define kill
  ➲ /spell : ᴡʜɪʟᴇ ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ, ᴡɪʟʟ ʀᴇᴘʟʏ ᴡɪᴛʜ ᴀ ɢʀᴀᴍᴍᴀʀ ᴄᴏʀʀᴇᴄᴛᴇᴅ ᴠᴇʀꜱɪᴏɴ
  ➲ /synonyms <word> : ꜰɪɴᴅ ᴛʜᴇ ꜱʏɴᴏɴʏᴍꜱ ᴏꜰ ᴀ ᴡᴏʀᴅ
  ➲ /antonyms <word> : ꜰɪɴᴅ ᴛʜᴇ ᴀɴᴛᴏɴʏᴍꜱ ᴏꜰ ᴀ ᴡᴏʀᴅ
"""

__mod_name__ = "Eɴɢʟɪsʜ"
