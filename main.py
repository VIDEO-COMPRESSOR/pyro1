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
from subprocess import getstatusoutput
import helper
import logging
import time
import glob
import aiohttp
import asyncio
import aiofiles
from pyrogram.types import User, Message
import re
import os
import io

res = "NA"


bot = Client("bot",
             #bot_token=os.environ.get("BOT_TOKEN","5696138411:AAE2hRzQZeWwtBUqz6Lvt-KWyj6FBc4Y860"),
             bot_token=os.environ.get("BOT_TOKEN","5436870859:AAFJxvm5CuWMCUyqoN7VHHNR5QLKxS0wd1U"),
             api_id=int(os.environ.get("API_ID","952608")),
             api_hash=os.environ.get("API_HASH","8d8d0ad8e3d4bcd54420190f57da78ad"))
auth_users = [
    int(chat) for chat in os.environ.get("AUTH_USERS","818269274").split(",") if chat != '']
sudo_users = auth_users
sudo_groups = [
    int(chat) for chat in os.environ.get("GROUPS","-1001476904215").split(",") if chat != '']



async def decc(bot: Client, m: Message) :
      




@bot.on_message(filters.command(["start"]))
async def login(bot: Client, m: Message):
    editable = await m.reply_text(
            "Hello Bruh **I am Text Downloader Bot**.  **TXT** 👉{Name : Link}")
   
    path = f"./downloads/"

    try:
        with open("NTT.txt", "r") as f:
            content = f.read()
        content = content.split("\n")
        global links
        links = []
        for i in content:
            links.append(i.split(":", 1))
        
    except:
        await m.reply_text("Invalid file input.")
        return
    
    editable = await m.reply_text(
        f"Total links found are **{len(links)}**"
    )
    global count
    global arg
    global raw_text0
    global thumb
    global raw_text2
    count = 1
    arg = 0
    raw_text0 = "CLASSPLUS" #batch name
    raw_text2 = "0" #resolution
    thumb = "no"
    await m.reply_text("Succesfully Bot Loaded 😍🥰.")


@bot.on_message(filters.command(["pro"]))
async def account_login(bot: Client, m: Message):


    try:
        for i in range(arg, len(links)):
            await m.reply_text("**Now in Top Loop ✅**")
            url = links[i][1]
            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/","").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").strip()

            cmd = f'yt-dlp -F "{url}"'
            k = await helper.run(cmd)
            out = helper.vid_info(str(k))
            if '2567x1449' in out:
                ytf = f"{out['2566x1447']}"
            elif 'unknown' in out:
                ytf = out["unknown"]
            else:
                 for data1 in out:
                     ytf = out[data1]
                     await m.reply_text("** I think it's Looks like Error 😆**")
            
            name = f'{str(count).zfill(3)}) {name1} {res}'
            if "m3u8" or "livestream" in url:
                cmd = f'yt-dlp -f "{ytf}" --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s"'
                await m.reply_text("**link m3u8 ✅**")
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
                        
                        reply = await m.reply_text(f"Uploading Pdfs - ```{name}```")
                        
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
                    await m.reply_text("**Now in Downloading ✅*")
                    res_file = await helper.download_video(url, cmd, name)
                    filename = res_file
                    await m.reply_text("**Now in uploading ✅**")
                    await helper.send_vid(bot, m, cc, filename, thumb, name,
                                            prog)
                    await m.reply_text("**Done video✅**")
                    count += 1
                   
                    
            except Exception as e:
                await m.reply_text(
                    f"**downloading failed ❌**\n{str(e)}\n**Name** - {name}\n**Link** - `{url}`"
                )
                continue

    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("Done")

bot.run()
