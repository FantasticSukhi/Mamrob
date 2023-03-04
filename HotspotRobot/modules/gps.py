from geopy.geocoders import Nominatim
from telethon import *
from telethon.tl import *

from HotspotRobot import *
from HotspotRobot import telethn
from HotspotRobot.events import register

GMAPS_LOC = "https://maps.googleapis.com/maps/api/geocode/json"


@register(pattern="^/gps (.*)")
async def _(event):
    args = event.pattern_match.group(1)

    try:
        geolocator = Nominatim(user_agent="SkittBot")
        location = args
        geoloc = geolocator.geocode(location)
        longitude = geoloc.longitude
        latitude = geoloc.latitude
        gm = "https://www.google.com/maps/search/{},{}".format(latitude, longitude)
        await telethn.send_file(
            event.chat_id,
            file=types.InputMediaGeoPoint(
                types.InputGeoPoint(float(latitude), float(longitude))
            ),
        )
        await event.reply(
            "» ᴏᴘᴇɴ ᴡɪᴛʜ: [🌏ɢᴏᴏɢʟᴇ ᴍᴀᴘꜱ]({})".format(gm),
            link_preview=False,
        )
    except Exception as e:
        print(e)
        await event.reply("I can't find that")


__help__ = """
‣ ꜱᴇɴᴅꜱ ʏᴏᴜ ᴛʜᴇ ɢᴘꜱ ʟᴏᴄᴀᴛɪᴏɴ ᴏꜰ ᴛʜᴇ ɢɪᴠᴇɴ Qᴜᴇʀʏ...

  ➲ /gps <location>: ɢᴇᴛ ɢᴘꜱ ʟᴏᴄᴀᴛɪᴏɴ.
"""

__mod_name__ = "Gᴘs"
