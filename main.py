import asyncio
import logging
import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.storage.memory import MemoryStorage

# Загрузка токена из .env
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Инициализация диспетчера
dp = Dispatcher(storage=MemoryStorage())

# ✅ Обработчик команды /start
@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        f"Привет, {message.from_user.full_name or 'пользователь'}! 👋\n\n"
        "Я — бот для отслеживания задач Дата Инженеров Ситуационного Центра.\n\n"
        "Используй меню Telegram (внизу), чтобы открыть приложение или отправить команду."
    )

# ✅ Обработка данных из WebApp (если отправляешь через window.Telegram.WebApp.sendData)
@dp.message()
async def handle_web_app_data(message: Message):
    if message.web_app_data:
        await message.answer(f"📥 Получены данные из WebApp:\n<code>{message.web_app_data.data}</code>")
    else:
        await message.answer("Пожалуйста, используй меню Telegram для взаимодействия.")

# 🔁 Запуск бота
async def main():
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
