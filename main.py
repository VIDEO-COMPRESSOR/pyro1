from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid
import requests
import json
import subprocess
from pyrogram import Client, filters
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait
from pyromod import listen
from pyrogram.types import Message
import pyrogram
import tgcrypto
from p_bar import progress_bar
#from details import api_id, api_hash, bot_token
from subprocess import getstatusoutput
import helper
import logging
import time
import glob
import aiohttp
import asyncio
import aiofiles
from pyrogram.types import User, Message
#import progressor
#from progressor import progress_for_pyrogram
#import sys
import re
import os
import io
#import pycurl

res = "NA"


bot = Client("bot",
             bot_token=os.environ.get("BOT_TOKEN","5696138411:AAE2hRzQZeWwtBUqz6Lvt-KWyj6FBc4Y860"),
             #bot_token=os.environ.get("BOT_TOKEN","5436870859:AAFJxvm5CuWMCUyqoN7VHHNR5QLKxS0wd1U"),
             api_id=int(os.environ.get("API_ID","952608")),
             api_hash=os.environ.get("API_HASH","8d8d0ad8e3d4bcd54420190f57da78ad"))
auth_users = [
    int(chat) for chat in os.environ.get("AUTH_USERS","818269274").split(",") if chat != '']
sudo_users = auth_users
sudo_groups = [
    int(chat) for chat in os.environ.get("GROUPS","-1001476904215").split(",") if chat != '']



keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="Devloper",
                url="https://pornhub.com/",
            ),
            InlineKeyboardButton(
                text="Repo",
                url="https://lund-chushLoo.com/repo",
            ),
        ],
    ]
)


@bot.on_message(filters.command(["pyro"]))
async def account_login(bot: Client, m: Message):

 editable = await m.reply_text("**Hi Press**\n**Text** = /pro_txt\n**Top** = /pro_top\n**Vision** = /pro_vision\n**Jw** = /pro_jw\n**Olive** = /pro_olive\n**Addapdf** = /adda_pdf")


@bot.on_message(filters.command(["cancel"]))
async def cancel(_, m):
    editable = await m.reply_text("Canceling All process Plz wait\n🚦🚦 Last Process Stopped 🚦🚦")
    global cancel
    cancel = True
    await editable.edit("cancled")
    return


@bot.on_message(filters.command("restart"))
async def restart_handler(_, m):
    await m.reply_text("Restarted!", True)
    os.execl(sys.executable, sys.executable, *sys.argv)


@bot.on_message(filters.command(["pro"]))
async def account_login(bot: Client, m: Message):
    user = m.from_user.id if m.from_user is not None else None
    if user is not None and user not in sudo_users:
        await m.reply("**bhag bhosadi ke", quote=True)
        return
    else:
        editable = await m.reply_text(
            "Hello Bruh **I am Text Downloader Bot**. I can download videos from **text** file one by one.**\n\nDeveloper** : NAAM TO SUNA HOGA**\nLanguage** : Python**\nFramework** : Pyrogram\n\nSend **TXT** File {Name : Link}")
    #input: Message = await bot.listen(editable.chat.id)
    #x = await input.download()
    #await input.delete(True)
    
    path = f"./downloads/{m.chat.id}"

    try:
        with open("NTT.txt", "r") as f:
            content = f.read()
        content = content.split("\n")
        links = []
        for i in content:
            links.append(i.split(":", 1))
        #os.remove(x)
        # print(len(links))
        
    except:
        await m.reply_text("Invalid file input.")
        #os.remove(x)
        return
    
    editable = await m.reply_text(
        f"Total links found are **{len(links)}**"
    )
    #input1: Message = await bot.listen(editable.chat.id)
    raw_text = "0"

    try:
        arg = int(raw_text)
    except:
        arg = 0

    #editable = await m.reply_text("**Enter Title**")
    #input0: Message = await bot.listen(editable.chat.id)
    raw_text0 = "CLASSPLUS"

    #await m.reply_text("**Enter resolution**")
    #input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = "0"

    #editable4 = await m.reply_text(
    #    "Now send the **Thumb url**\nEg : ```https://telegra.ph/file/d9e24878bd4aba05049a1.jpg```\n\nor Send **no**"
   # )
   # input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = "no"

    thumb = "no"
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"

    if raw_text == '0':
        count = 1
    else:
        count = int(raw_text)

    try:
        for i in range(arg, len(links)):
            await m.reply_text("**Now in Top Loop ✅**")
            url = links[i][1]
            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/","").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").strip()

            cmd = f'yt-dlp -F "{url}"'
            k = await helper.run(cmd)
            out = helper.vid_info(str(k))
            if '256x144' in out:
                ytf = f"{out['256x144']}"
            elif '320x180' in out:
                ytf = out['320x180']
            elif 'unknown' in out:
                ytf = out["unknown"]
            else:
                 for data1 in out:
                     ytf = out[data1]
                     await m.reply_text("** I think it's Looks like Error 😆**")
            
            name = f'{str(count).zfill(3)}) {name1} {res}'
            if "acecwply" in url:
                cmd = f'yt-dlp -o "{name}.%(ext)s" -f "bestvideo[height<={raw_text2}]+bestaudio" --hls-prefer-ffmpeg --no-keep-video --remux-video mkv --no-warning "{url}"'
            elif "youtu" in url:
                cmd = f'yt-dlp -i -f "bestvideo[height<={raw_text2}]+bestaudio" --no-keep-video --remux-video mkv --no-warning "{url}" -o "{name}.%(ext)s"'
            elif "player.vimeo" in url:
                cmd = f'yt-dlp -f "{ytf}+bestaudio" --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s"'
            elif "m3u8" or "livestream" in url:
                cmd = f'yt-dlp -f "{ytf}" --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s"'
                await m.reply_text("**link m3u8 ✅**")
            elif ytf == "0" or "unknown" in out:
                cmd = f'yt-dlp -f "{ytf}" --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s"'
                await m.reply_text("** link unknown based✅**")
            elif ".pdf" or "download" in url:
                cmd = "pdf"
            else:
                cmd = f'yt-dlp -f "{ytf}+bestaudio" --hls-prefer-ffmpeg --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s"'
                await m.reply_text("** link not detected ✅**")

            try:
                Show = f"**Downloading:-**\n\n**Name :-** `{name}\nQuality - {raw_text2}`\n\n**Url :-** `{url}`"
                prog = await m.reply_text(Show)
                cc = f"**Name »** {name1} {res}.mp4\n**Batch »** {raw_text0}\n**Index »** {str(count).zfill(3)}"
                cc1 = f"**Name »** ** {name1} {res}.pdf\n**Batch »** {raw_text0}\n**Index »** {str(count).zfill(3)}"
                
                if cmd == "pdf" or ".pdf" in url or ".pdf" in name:
                    await m.reply_text("**link pdf check ✅**")
                    try:
                        ka = await helper.aio(url, name)
                        await prog.delete(True)
                        
                        reply = await m.reply_text(f"Uploading - ```{name}```")
                        
                        start_time = time.time()
                        await m.reply_document(
                            ka,
                            caption=
                            f"**Name »** {name1} {res}.pdf\n**Batch »** {raw_text0}\n**Index »** {str(count).zfill(3)}"
                        )
                        count += 1
                        
                        await reply.delete(True)
                       
                        os.remove(ka)
                       
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                else:
                    await m.reply_text("**Now in Last Portion ✅**")
                    res_file = await helper.download_video(url, cmd, name)
                    await m.reply_text("**Now in Last Portion 1 ✅**")
                    filename = res_file
                    await m.reply_text("**Now in Last Portion 2 ✅**")
                    await helper.send_vid(bot, m, cc, filename, thumb, name,
                                          prog)
                    await m.reply_text("**Now in Last Portion 3 ✅**")
                    count += 1
                   
                    await m.reply_text("**Now in Last Portion 4 ✅**")
            except Exception as e:
                await m.reply_text(
                    f"**downloading failed ❌**\n{str(e)}\n**Name** - {name}\n**Link** - `{url}`"
                )
                continue

    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("Done")

bot.run()
