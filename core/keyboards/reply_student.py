from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

#################################################################

FIRST_MAIN = InlineKeyboardBuilder()\

FIRST_MAIN.add(types.InlineKeyboardButton(
    text="Продолжить",
    callback_data="Student_continue")
)

FIRST_MAIN.add(types.InlineKeyboardButton(
    text="Обучение",
    callback_data="Student_tutorial")
)

FIRST_MAIN.adjust(2)

#################################################################

ID_ENTER_1 = InlineKeyboardBuilder()\

ID_ENTER_1.add(types.InlineKeyboardButton(
    text="Введите ID группы",
    callback_data="Enter_ID_Student")
)

ID_ENTER_1.add(types.InlineKeyboardButton(
    text="Назад",
    callback_data="Back")
)

ID_ENTER_1.adjust(1)

#################################################################

ID_ENTER_2 = InlineKeyboardBuilder()\

ID_ENTER_2.add(types.InlineKeyboardButton(
    text="Вводите",
    callback_data="Enter_ID_Student_2")
)

ID_ENTER_2.adjust(1)

#################################################################

TO_REGISTRATE = InlineKeyboardBuilder()\

TO_REGISTRATE.add(types.InlineKeyboardButton(
    text="Зарегистрироваться",
    callback_data="To_registrate")
)

TO_REGISTRATE.adjust(1)

#################################################################

REGISTRATION_SUCCESS = InlineKeyboardBuilder()\

REGISTRATION_SUCCESS.add(types.InlineKeyboardButton(
    text="Меню курса",
    callback_data="Registration-success")
)

REGISTRATION_SUCCESS.adjust(1)

#################################################################

LOBBY_MARKUP = InlineKeyboardBuilder()\

LOBBY_MARKUP.add(types.InlineKeyboardButton(
    text="Дедлайны",
    callback_data="Deadlines")
)

LOBBY_MARKUP.add(types.InlineKeyboardButton(
    text="Выбрать предмет",
    callback_data="Choose_subject")
)

LOBBY_MARKUP.add(types.InlineKeyboardButton(
    text="Профиль",
    callback_data="Profile")
)

LOBBY_MARKUP.add(types.InlineKeyboardButton(
    text="Расписание",
    callback_data="Schedule")
)

LOBBY_MARKUP.adjust(2)

#################################################################

PROFILE_STUDENT = InlineKeyboardBuilder()\

PROFILE_STUDENT.add(types.InlineKeyboardButton(
    text="Назад",
    callback_data="Back")
)

PROFILE_STUDENT.adjust(1)

#################################################################

SUBJECT = InlineKeyboardBuilder()\

SUBJECT.add(types.InlineKeyboardButton(
    text="Лекции",
    callback_data="Lectures")
)

SUBJECT.add(types.InlineKeyboardButton(
    text="Работы",
    callback_data="Works")
)

SUBJECT.add(types.InlineKeyboardButton(
    text="Преподаватель",
    callback_data="Teacher_conts")
)

SUBJECT.add(types.InlineKeyboardButton(
    text="Назад",
    callback_data="Back")
)

SUBJECT.add(types.InlineKeyboardButton(
    text="Главное меню",
    callback_data="Main_screen")
)

SUBJECT.adjust(2)