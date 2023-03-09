import requests

from HotspotRobot import SUPPORT_CHAT, BOT_USERNAME
from HotspotRobot.events import register
from requests.exceptions import JSONDecodeError, ConnectionError


@register(pattern=f"^/spell|^/spell@{BOT_USERNAME}")
async def _(event):
    text = event.text.split(" ", 1)
    reply_msg = await event.get_reply_message()

    if event.reply_to_msg_id and reply_msg.text:
        text = reply_msg.text
    else:
        if len(text) == 1:
            return await event.reply("» ɢɪᴠᴇ ᴍᴇ ꜱᴏᴍᴇ ꜱᴇɴᴛᴇɴᴄᴇ.\n  ᴇx. /spell Altron   or\n  ᴇx. /spell <ʀᴇᴘʟʏ ᴛᴏ ᴍꜱɢ>")
        text = text[1]

    try:
        response = requests.get(f"https://api.safone.me/spellcheck?text={text}").json()
    except (JSONDecodeError, ConnectionError) as e:
        return await event.reply(
            f"**Some Error Occured:** ᴘʟᴇᴀꜱᴇ ʀᴇᴘᴏʀᴛ ɪᴛ ᴀᴛ ᴏᴜʀ [ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ](https://t.me/{SUPPORT_CHAT})."
            f"\n\n**Error:** {e}"
            )

    TEXT = f"""**Sentence:** `{text}`\n\n**Corrected:** `{response["corrected"]}`\n\n**Corrections:**"""
    for correction in response["corrections"]:
        TEXT += f"""\n  •  `{correction["text"]} - {correction["correct"]}`"""

    await event.reply(TEXT)


@register(pattern=f"^/define|^/define@{BOT_USERNAME}")
async def _(event):
    text = event.text.split(" ", 1)
    if len(text) == 1:
        return await event.reply(f"**Usage:**  /define <ᴡᴏʀᴅ>")
    
    try:
        response = requests.get(f"https://wordsapiv1.p.mashape.com/words/{text[1]}/definitions").json()
    except (JSONDecodeError, ConnectionError) as e:
        return await event.reply(
            f"**Some Error Occured:** ᴘʟᴇᴀꜱᴇ ʀᴇᴘᴏʀᴛ ɪᴛ ᴀᴛ ᴏᴜʀ [ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ](https://t.me/{SUPPORT_CHAT})."
            f"\n\n**Error:** {e}"
            )

    AltPy = f"» ᴍᴇᴀɴɪɴɢꜱ ᴏꜰ {text[1]}:"
    for i in range(5):
        try:
            meaning = response["definitions"][i]["definition"]
            AltPy += f"\n - `{meaning}`"
        except IndexError:
            break

    await event.reply(AltPy)


@register(pattern=f"^/synonyms|^/synonyms@{BOT_USERNAME}")
async def _(event):
    text = event.text.split(" ", 1)
    if len(text) == 1:
        return await event.reply(f"**Usage:**  /synonyms <ᴡᴏʀᴅ>")

    try:
        response = requests.get(f"https://wordsapiv1.p.mashape.com/words/{text[1]}/synonyms")
    except (JSONDecodeError, ConnectionError) as e:
        return await event.reply(
            f"**Some Error Occured:** ᴘʟᴇᴀꜱᴇ ʀᴇᴘᴏʀᴛ ɪᴛ ᴀᴛ ᴏᴜʀ [ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ](https://t.me/{SUPPORT_CHAT})."
            f"\n\n**Error:** {e}"
            )

    AltPy = f"» ꜱʏɴᴏɴʏᴍꜱ ᴏꜰ {text[1]}:\n"
    for i in range(5):
        try:
            Syn = response["synonyms"][i]
            AltPy += f"\n - `{Syn}`"
        except IndexError:
            break

    await event.reply(AltPy)


@register(pattern=f"^/antonyms|^/antonyms@{BOT_USERNAME}")
async def _(event):
    text = event.text.split(" ", 1)
    if len(text) == 1:
        return await event.reply(f"**Usage:**  /antonyms <ᴡᴏʀᴅ>")

    try:
        response = requests.get(f"https://wordsapiv1.p.mashape.com/words/{text[1]}/antonyms")
    except (JSONDecodeError, ConnectionError) as e:
        return await event.reply(
            f"**Some Error Occured:** ᴘʟᴇᴀꜱᴇ ʀᴇᴘᴏʀᴛ ɪᴛ ᴀᴛ ᴏᴜʀ [ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ](https://t.me/{SUPPORT_CHAT})."
            f"\n\n**Error:** {e}"
            )

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
