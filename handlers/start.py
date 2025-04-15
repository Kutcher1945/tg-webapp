# handlers/start.py

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from keyboards.menu import main_menu

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "Привет! Вот что ты можешь сделать:",
        reply_markup=main_menu
    )
