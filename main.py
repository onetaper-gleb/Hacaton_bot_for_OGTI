import asyncio

from aiogram.types import Message, ContentType
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command

from core.handlers.admin_basic import welcoming_message_ad, main_menu_admin, admin_control, admin_add_1, start_admin, \
    admin_delete, groups_check, create_group_5_2, create_group_1, get_pdf, teacher_settings_2, teacher_settings, \
    create_teacher_1
from core.handlers.basic import choice
from core.handlers.student_basic import welcoming_message, id_wait, id_wait_change, start_students, return_back, \
    registered_message, registration_step_1, lobby_student, profile_student, choose_subject, send_schedule
from core.handlers.teacher_basic import welcoming_message_teacher, registration_step_2_teach, registration_teacher
from core.settings import settings
from core.middlewares.functions import get_spisok
from core.utills.commands import set_commands


async def start_bot(bot: Bot):
    await set_commands(bot)
    sp = get_spisok()
    start_students(sp[0], sp[3])
    start_admin(sp[2])
    await bot.send_message(settings.bots.admin_id, 'Bot has just started working')


async def end_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, "Bot finished it's work")


async def start():
    bot = Bot(token=settings.bots.bot_token)
    logging.basicConfig(level=logging.INFO)

    dp = Dispatcher()

    dp.startup.register(start_bot)
    dp.shutdown.register(end_bot)
    dp.message.register(get_pdf, F.content_type == 'document')
    dp.callback_query.register(registration_teacher, F.data == 'Teacher_continue')
    dp.callback_query.register(registration_step_2_teach, F.data == 'Teacher_registrate')
    dp.callback_query.register(create_teacher_1, F.data == 'Add_teacher')
    dp.callback_query.register(teacher_settings, F.data == 'Admin_add_teacher')
    dp.callback_query.register(create_group_1, F.data == 'Create_group')
    dp.callback_query.register(teacher_settings_2, F.data == 'Next_admin_2')
    dp.callback_query.register(create_group_5_2, F.data == 'Next_admin')
    dp.callback_query.register(groups_check, F.data == 'Admin_groups_control')
    dp.callback_query.register(admin_delete, F.data == 'Admin_delete_1')
    dp.callback_query.register(admin_add_1, F.data == 'Admin_add_1')
    dp.callback_query.register(choose_subject, F.data == 'Choose_subject')
    dp.callback_query.register(lobby_student, F.data == 'Registration-success')
    dp.callback_query.register(profile_student, F.data == 'Profile')
    dp.callback_query.register(return_back, F.data == "Back")
    dp.callback_query.register(registration_step_1, F.data == "To_registrate")
    dp.callback_query.register(id_wait_change, F.data == "Enter_ID_Student")
    dp.callback_query.register(id_wait, F.data == "Student_continue")
    dp.callback_query.register(main_menu_admin, F.data == "Admin_continue")
    dp.callback_query.register(admin_control, F.data == "Admin_add")
    dp.callback_query.register(welcoming_message, F.data == "Student_start")
    dp.callback_query.register(welcoming_message_teacher, F.data == "Teacher_start")
    dp.callback_query.register(lobby_student, F.data == 'Main_screen')
    dp.callback_query.register(send_schedule, F.data == 'Schedule')
    dp.callback_query.register(welcoming_message_ad, F.data == 'Admin_start')
    dp.message.register(choice, Command(commands=['start']))
    dp.message.register(registered_message, F.text)


    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())