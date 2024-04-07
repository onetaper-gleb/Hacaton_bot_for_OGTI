from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

#################################################################

WELCOMING_MESSAGE_TEACHER = InlineKeyboardBuilder()\

WELCOMING_MESSAGE_TEACHER.add(types.InlineKeyboardButton(
    text="Продолжить",
    callback_data="Teacher_continue")
)

WELCOMING_MESSAGE_TEACHER.add(types.InlineKeyboardButton(
    text="Обучение",
    callback_data="Teacher_tutorial")
)

WELCOMING_MESSAGE_TEACHER.adjust(2)

#################################################################

REGISTRATION_TEACHER = InlineKeyboardBuilder()\

REGISTRATION_TEACHER.add(types.InlineKeyboardButton(
    text="Зарегитрироваться",
    callback_data="Teacher_registrate")
)

REGISTRATION_TEACHER.add(types.InlineKeyboardButton(
    text="Назад",
    callback_data="Teacher_back")
)

REGISTRATION_TEACHER.adjust(2)