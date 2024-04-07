from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

#################################################################

FIRST_MAIN = InlineKeyboardBuilder()\

FIRST_MAIN.add(types.InlineKeyboardButton(
    text="Продолжить",
    callback_data="Admin_continue")
)

FIRST_MAIN.add(types.InlineKeyboardButton(
    text="Обучение",
    callback_data="Admin_tutorial")
)

FIRST_MAIN.adjust(2)

#################################################################

MAIN = InlineKeyboardBuilder()\

MAIN.add(types.InlineKeyboardButton(
    text="Администрация",
    callback_data="Admin_add")
)

MAIN.add(types.InlineKeyboardButton(
    text="Просмотр групп",
    callback_data="Admin_groups_control")
)

MAIN.add(types.InlineKeyboardButton(
    text="Преподователи",
    callback_data="Admin_add_teacher")
)

MAIN.adjust(2)

#################################################################

ADMIN_CONTROL = InlineKeyboardBuilder()\

ADMIN_CONTROL.add(types.InlineKeyboardButton(
    text="Добавить админа",
    callback_data="Admin_add_1")
)

ADMIN_CONTROL.add(types.InlineKeyboardButton(
    text="Удалить админа",
    callback_data="Admin_delete_1")
)

ADMIN_CONTROL.add(types.InlineKeyboardButton(
    text="Главное меню",
    callback_data="Admin_continue")
)

ADMIN_CONTROL.adjust(2)

#################################################################

GROUPS_CHECK = InlineKeyboardBuilder()\

GROUPS_CHECK.add(types.InlineKeyboardButton(
    text="Создать группу",
    callback_data="Create_group")
)

GROUPS_CHECK.add(types.InlineKeyboardButton(
    text="Главное меню",
    callback_data="Admin_continue")
)

GROUPS_CHECK.adjust(2)

#################################################################

CREATE_GROUP_5 = InlineKeyboardBuilder()\

CREATE_GROUP_5.add(types.InlineKeyboardButton(
    text=">>>",
    callback_data="Next_admin")
)

CREATE_GROUP_5.adjust(2)

#################################################################

CREATED_GROUP = InlineKeyboardBuilder()\

CREATED_GROUP.add(types.InlineKeyboardButton(
    text="Главное меню",
    callback_data="Admin_continue")
)

CREATED_GROUP.adjust(2)

#################################################################

TEACHER_SETTINGS = InlineKeyboardBuilder()\

TEACHER_SETTINGS.add(types.InlineKeyboardButton(
    text="Добавить предмет",
    callback_data="Add_teacher")
)

TEACHER_SETTINGS.add(types.InlineKeyboardButton(
    text=">>>",
    callback_data="Next_admin_2")
)

TEACHER_SETTINGS.add(types.InlineKeyboardButton(
    text="Главное меню",
    callback_data="Admin_continue")
)

TEACHER_SETTINGS.adjust(2)

#################################################################

CREATED_TEACHER = InlineKeyboardBuilder()\

CREATED_TEACHER.add(types.InlineKeyboardButton(
    text="Вернуться",
    callback_data="Admin_add_teacher")
)

CREATED_TEACHER.add(types.InlineKeyboardButton(
    text="Главное меню",
    callback_data="Admin_continue")
)

CREATED_TEACHER.adjust(2)
