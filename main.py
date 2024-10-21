import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from handlers.handlers import router

load_dotenv()  # Загрузка переменных окружения из .env

# Получение токена из переменной окружения
token = os.getenv("BOT_TOKEN")

bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# Включаем роутер
dp.include_router(router)

async def main():
    await dp.start_polling(bot)

# Проверка имени главного модуля
if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
