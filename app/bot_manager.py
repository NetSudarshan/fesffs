import asyncio
from aiogram import Bot, Dispatcher
from database import get_bots

async def run_bot(token):
    bot = Bot(token=token)
    dp = Dispatcher()

    @dp.message()
    async def alive(msg):
        await msg.answer("🤖 Bot alive on Render (free mode)")

    await dp.start_polling(bot)

async def start_all_bots():
    tasks = []
    for token in get_bots():
        tasks.append(asyncio.create_task(run_bot(token)))
    await asyncio.gather(*tasks)
