import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from handlers.handlers import router

# Загрузка переменных окружения из .env
load_dotenv()

# Получение токена из переменной окружения
token = os.getenv("BOT_TOKEN")

if not token:
    raise ValueError("No BOT_TOKEN provided")

bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# Включаем роутер
dp.include_router(router)

async def main():
    await dp.start_polling(bot)

# Проверка имени главного модуля
if __name__ == '__main__':
    asyncio.run(main())
