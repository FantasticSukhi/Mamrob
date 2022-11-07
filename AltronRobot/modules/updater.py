import sys
from git import Repo
from os import system, execle, environ
from git.exc import InvalidGitRepositoryError
from AltronRobot.events import register
from AltronRobot import telethn as tbot
from AltronRobot import DRAGONS


UPSTREAM_REPO = "https://github.com/ItZxSTaR/Altron"

def gen_chlog(repo, diff):
    upstream_repo_url = Repo().remotes[0].config_reader.get("url").replace(".git", "")
    ac_br = repo.active_branch.name
    ch_log = ""
    ch = f"<b>updates for <a href={upstream_repo_url}/tree/{ac_br}>[{ac_br}]</a>:</b>"
    d_form = "%d/%m/%y || %H:%M"
    for c in repo.iter_commits(diff):
        ch_log += (
            f"\n\n💬 <b>{c.count()}</b> 🗓 <b>[{c.committed_datetime.strftime(d_form)}]</b>\n<b>"
            f"<a href={upstream_repo_url.rstrip('/')}/commit/{c}>[{c.summary}]</a></b> 👨‍💻 <code>{c.author}</code>"
        )
    if ch_log:
        return str(ch + ch_log)
    return ch_log


def updater():
    try:
        repo = Repo()
    except InvalidGitRepositoryError:
        repo = Repo.init()
        origin = repo.create_remote("upstream", UPSTREAM_REPO)
        origin.fetch()
        repo.create_head("main", origin.refs.main)
        repo.heads.main.set_tracking_branch(origin.refs.main)
        repo.heads.main.checkout(True)
    ac_br = repo.active_branch.name
    if "upstream" in repo.remotes:
        ups_rem = repo.remote("upstream")
    else:
        ups_rem = repo.create_remote("upstream", UPSTREAM_REPO)
    ups_rem.fetch(ac_br)
    changelog = gen_chlog(repo, f"HEAD..upstream/{ac_br}")
    return bool(changelog)


@register(pattern=("/update"))
async def update_bot(event):
    if int(event.sender.id) in DRAGONS:
        msg = await tbot.reply("» ᴄʜᴇᴄᴋɪɴɢ ᴜᴘᴅᴀᴛᴇs...", parse_mode=None, link_preview=None)
        update_avail = updater()
        if update_avail:
            await msg.edit("»__ ᴜᴘᴅᴀᴛᴇ ғɪɴɪsʜᴇᴅ __\n» __ʙᴏᴛ ʀᴇsᴛᴀʀᴛɪɴɢ, ʙᴀᴄᴋ ᴀᴄᴛɪᴠᴇ ᴀɢᴀɪɴ ɪɴ 𝟹𝟶s __.")
            system("git pull -f && pip3 install -U -r requirements.txt")
            execle(sys.executable, sys.executable, "main.py", environ)
            return
        await msg.edit(f"__» ᴀʟʀᴇᴀᴅʏ ᴜᴘᴅᴀᴛᴇᴅ ʙʏ ᴀʟᴛʀᴏɴ __")
