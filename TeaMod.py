__version__ = (0, 0, 7)
#
#
# _           _            _ _
# | |         | |          (_) |
# | |     ___ | |_ ___  ___ _| | __
# | |    / _ \| __/ _ \/ __| | |/ /
# | |___| (_) | || (_) \__ \ |   <
# \_____/\___/ \__\___/|___/_|_|\_\
#
#              © Copyright 2022
#
# 🔒 Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# meta developer: @userbothikka3
# meta banner: https://i.imgur.com/awltLuz.jpeg


from .. import loader, utils
import asyncio


class TeaUseMod(loader.Module):
    """Автоматизирует работу с @TeaUseBot (автоматический чай )"""

    strings = {"name": "TeaMod"}

    async def teacmd(self, message):
        """Включается команда `/tea`. Чтобы остановить, `чай стоп`."""
        self.set("tea", True)
        while self.get("tea"):
            await message.reply("/tea")
            await asyncio.sleep(0.1)
            await utils.answer(
                message,
                "Следующая команда будет произведена через 1 час и 5 минут.",
            )
            await asyncio.sleep(3960)

    async def watcher(self, message):
        if not getattr(message, "out", False):
            return

        if message.raw_text.lower() == "чай стоп":
            self.set("tea", False)
            await utils.answer(message, "<b>чай остановлен.</b>") 