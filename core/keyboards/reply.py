from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

START_KEYBOARD = InlineKeyboardBuilder()\

START_KEYBOARD.add(types.InlineKeyboardButton(
    text="Ученик",
    callback_data="Student_start")
)

START_KEYBOARD.add(types.InlineKeyboardButton(
    text="Учитель",
    callback_data="Teacher_start")
)


START_KEYBOARD.add(types.InlineKeyboardButton(
    text="Админ",
    callback_data="Admin_start")
)
START_KEYBOARD.adjust(3)
