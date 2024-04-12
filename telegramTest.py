# pip install python-telegram-bot

import telegram
import asyncio

bot = telegram.Bot(token="7023720766:AAE71lDhMh7bHxfDpxL8FxDewGkHp-Xkg_0")
chat_id = "5093226994"

asyncio.run(bot.sendMessage(chat_id=chat_id, text="안녕하세요!!파이썬 텔레그램 테스트!!!"))
