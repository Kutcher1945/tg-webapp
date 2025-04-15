import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv
import os

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

dp = Dispatcher(storage=MemoryStorage())

@dp.message(CommandStart())
async def start(message: Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📩 Создать задачу", web_app=WebAppInfo(url="https://your-domain.com/webapp/index.html"))]
    ])
    await message.answer("Привет! Нажмите кнопку ниже, чтобы создать задачу.", reply_markup=keyboard)

@dp.message()
async def handle_web_app_data(message: Message):
    if message.web_app_data:
        data = message.web_app_data.data
        await message.answer(f"Получены данные из Web App: {data}")
    else:
        await message.answer("Пожалуйста, используйте кнопку для запуска Web App.")

async def main():
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
