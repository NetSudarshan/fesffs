import asyncio
from aiogram import Bot, Dispatcher, types
from bot_manager import start_all_bots
from database import add_bot
from config import ADMIN_ID

ADMIN_BOT_TOKEN = "PASTE_ADMIN_BOT_TOKEN"

bot = Bot(token=ADMIN_BOT_TOKEN)
dp = Dispatcher()

@dp.message(commands=["addbot"])
async def addbot(msg: types.Message):
    if msg.from_user.id != ADMIN_ID:
        return
    token = msg.text.split(" ", 1)[1]
    if add_bot(token):
        await msg.answer("✅ Bot added. Restarting soon.")
    else:
        await msg.answer("❌ Invalid or duplicate token")

async def main():
    asyncio.create_task(start_all_bots())
    await dp.start_polling(bot)

asyncio.run(main())
