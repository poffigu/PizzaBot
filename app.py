import asyncio
import os

from aiogram import Bot, Dispatcher
from dotenv import find_dotenv, load_dotenv

from handlers.user_private import user_private_router


load_dotenv(find_dotenv())
ALLOWED_UPDATES = ['edited_message, message']
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()
dp.include_router(user_private_router)


async def main() -> None:
    # await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)


try:
    asyncio.run(main())
except KeyboardInterrupt:
    print('Exit')
