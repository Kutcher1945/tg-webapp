# keyboards/menu.py

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

main_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📥 Создать задачу", web_app=WebAppInfo(url="https://your-deployed-webapp.com"))],
    [InlineKeyboardButton(text="👨‍💻 Специалисты", callback_data="specialists")],
    [InlineKeyboardButton(text="📝 Текущие задачи", callback_data="current_tasks")],
    [InlineKeyboardButton(text="✅ Завершённые задачи", callback_data="completed_tasks")],
])
