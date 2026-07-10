#║██       ╔═███   ╔██         ██ ╔█████
#║██      ╔╝██ ██  ╚╗██       ██  ║█ 
#║██      ║██    ██ ╚╗██      ██  ║█████
#║██      ║██   ██   ╚╗██    ██   ║█
#║██████╗╚╗██ ██     ╚╗██ ██     ║█████╗
#╚══════╝ ╚═███        ╚═██       ╚═════╝
# © americaboys_official 2024-2025
# this file - unofficial module for Hikka Userbot
#  /\_/\   This module was loaded through https://t.me/hikka_gmod
# ( o.o )   Licensed under the GNU AGPLv3.
#  > ^ <  
# ------------------------------------------------
# Name: irisStat
# meta developer: @americaboys_official
# Description: накрутка сообщений в статистике ириса
# Commands: .inn | .инн
# Thanks: me
# ------------------------------------------------
# Licensed under the GNU AGPLv3
# https://www.gnu.org/licenses/agpl-3.0.html
# channel: https://t.me/hikka_gmod
from telethon import events
from telethon.tl.types import PeerChannel
from asyncio import sleep
from .. import loader, utils

@loader.tds
class Irisizm(loader.Module):
    """накрутка сообщений в стате ириса, использовать только в чате где есть ирис!!"""
    strings = {'name': 'irisStat'}
    
    @loader.command()
    async def инн(self, message):
        """[количество] - включить накрутку сообщений"""

        await message.edit("<b>Накрутка активирована!</b>")

        args = message.text.split(maxsplit=1)
        if len(args) < 2:
            return await message.reply('<b>Используйте</b>: <code>.инн [количество]</code>')

        try:
            count = int(args[1])
        except ValueError:
            return await message.edit('</b>Используйте целое число</b>')

        if count <= 0:
            return await message.edit('<b>Количество должно быть больше 0</b>')
        if count > 5000:
            return await message.edit('<b>Количество не должно превышать 5000 сообщений!</b>')

        for _ in range(count):
            sent_message = await message.reply("<b>BesedaBloody топ</b> 😈")
            await sleep(0.05)
            await sent_message.delete()
