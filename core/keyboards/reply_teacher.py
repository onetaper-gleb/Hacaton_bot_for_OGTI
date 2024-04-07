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

#################################################################

REGISTRATION_SUCCESS_TEACHER = InlineKeyboardBuilder()\

REGISTRATION_SUCCESS_TEACHER.add(types.InlineKeyboardButton(
    text="Продолжить",
    callback_data="Teacher_menu_main")
)

REGISTRATION_SUCCESS_TEACHER.adjust(1)

#################################################################

MAIN_LOBBY_TEACHER = InlineKeyboardBuilder()\

MAIN_LOBBY_TEACHER.add(types.InlineKeyboardButton(
    text="Уроки",
    callback_data="Lessons_teacher")
)

MAIN_LOBBY_TEACHER.add(types.InlineKeyboardButton(
    text="Ваши группы",
    callback_data="Your_groups")
)

MAIN_LOBBY_TEACHER.adjust(2)

#################################################################

LESSONS_TEACHER = InlineKeyboardBuilder()\

LESSONS_TEACHER.add(types.InlineKeyboardButton(
    text="Создать урок",
    callback_data="Create_lesson")
)

LESSONS_TEACHER.add(types.InlineKeyboardButton(
    text="Главное меню",
    callback_data="Teacher_menu_main")
)


LESSONS_TEACHER.adjust(2)

#################################################################

CREATE_LESSON = InlineKeyboardBuilder()\

CREATE_LESSON.add(types.InlineKeyboardButton(
    text="Лекция",
    callback_data="Create_lecture")
)

CREATE_LESSON.add(types.InlineKeyboardButton(
    text="Тест",
    callback_data="Create_test")
)

CREATE_LESSON.add(types.InlineKeyboardButton(
    text="Лабораторная работа",
    callback_data="Create_lab")
)

CREATE_LESSON.add(types.InlineKeyboardButton(
    text="Главное меню",
    callback_data="Teacher_menu_main")
)

CREATE_LESSON.adjust(2)

#################################################################

LESSON_PDF_CONV = InlineKeyboardBuilder()\

LESSON_PDF_CONV.add(types.InlineKeyboardButton(
    text="Продолжить",
    callback_data="Create_lesson")
)

LESSON_PDF_CONV.adjust(1)