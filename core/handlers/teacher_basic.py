import asyncio

import pygame
from aiogram import Bot
from aiogram.types import CallbackQuery, Message

from core.handlers.basic import users
from core.keyboards.reply import START_KEYBOARD
from core.keyboards.reply_teacher import WELCOMING_MESSAGE_TEACHER, REGISTRATION_TEACHER, REGISTRATION_SUCCESS_TEACHER, \
    MAIN_LOBBY_TEACHER, LESSONS_TEACHER, CREATE_LESSON, LESSON_PDF_CONV
from core.middlewares.Classes import Teacher
from core.middlewares.extra_gen import append_all_2
from core.middlewares.functions_teacher import checker_teach, lecture_add

teachers = pygame.sprite.Group()


async def delete_message(message: Message):
    await message.delete()


def start_teacher(spisok):
    if spisok:
        for i in spisok:
            Teacher(int(i[1]), i[0], int(i[2]), teachers)


async def welcoming_message_teacher(call: CallbackQuery):
    id_us = call.message.chat.id
    for i in users:
        if i.chat_id == id_us:
            m = checker_teach(i.username)
            if m:
                for j in teachers:
                    if str(j.chat_id) == str(id_us):
                        j.subs = m
                else:
                    Teacher(i.id, i.username, i.chat_id, teachers, add=True)
                    for j in teachers:
                        if j.chat_id == id_us:
                            j.subs = m
                            j.previous_actions.append((welcoming_message_teacher, call.message))
                            break
                await call.message.delete()
                await call.message.answer(f'''Отлично! 👍

Перед началом работы с ботом, советуем пройти обучение 👨‍🎓

Если вы уже прошли обучение или хотите его пропустить, нажмите кнопку «Продолжить» ➡️''',
                                          reply_markup=WELCOMING_MESSAGE_TEACHER.as_markup())
            else:
                await call.message.edit_text(f'''Извините, вы не являетесь учителем, если это не так, обратитесь к действующим админам
Для начала работы с ботом, пожалуйста, выберите, кем вы являетесь! 👇''', reply_markup=START_KEYBOARD.as_markup())
            break


async def registered_message(message: Message):
    for j in teachers:
        if j.chat_id == message.chat.id:
            if j.previous_actions[-1][0] == registration_step_2_teach:
                await asyncio.create_task(registration_step_3_teach(message))
            elif j.previous_actions[-1][0] == registration_step_3_teach:
                await asyncio.create_task(registration_step_4_teach(message))
            elif j.previous_actions[-1][0] == registration_step_4_teach:
                await asyncio.create_task(registration_step_5_teach(message))
            elif j.previous_actions[-1][0] == registration_step_5_teach:
                await asyncio.create_task(registration_step_6_teach(message))
            elif j.previous_actions[-1][0] == registration_step_6_teach:
                await asyncio.create_task(registration_step_7_teach(message))



async def registration_teacher(call: CallbackQuery):
    id_us = call.message.chat.id
    for j in teachers:
        if j.chat_id == id_us:
            await call.message.edit_text('Пройдите пожалуйста регистрацию', reply_markup=REGISTRATION_TEACHER.as_markup())


async def registration_step_2_teach(call: CallbackQuery):
    for j in teachers:
        if j.chat_id == call.message.chat.id:
            await asyncio.create_task(delete_message(call.message))
            j.previous_actions.append(
                (registration_step_2_teach, await call.message.answer("Введите свою Фамилию")))
            break


async def registration_step_3_teach(message: Message):
    for j in teachers:
        if j.chat_id == message.chat.id:
            await asyncio.create_task(delete_message(j.previous_actions[-1][1]))
            await asyncio.create_task(delete_message(message))
            j.registration_list.append(message.text)
            j.previous_actions.append((registration_step_3_teach, await message.answer("Введите своё имя")))
            break


async def registration_step_4_teach(message: Message):
    for j in teachers:
        if j.chat_id == message.chat.id:
            await asyncio.create_task(delete_message(j.previous_actions[-1][1]))
            await asyncio.create_task(delete_message(message))
            j.registration_list.append(message.text)
            j.previous_actions.append((registration_step_4_teach, await message.answer("Введите своё отчество")))
            break


async def registration_step_5_teach(message: Message):
    for j in teachers:
        if j.chat_id == message.chat.id:
            await asyncio.create_task(delete_message(j.previous_actions[-1][1]))
            await asyncio.create_task(delete_message(message))
            j.registration_list.append(message.text)
            j.previous_actions.append((registration_step_5_teach, await message.answer("Введите контактный телефон")))
            break


async def registration_step_6_teach(message: Message):
    for j in teachers:
        if j.chat_id == message.chat.id:
            await asyncio.create_task(delete_message(j.previous_actions[-1][1]))
            await asyncio.create_task(delete_message(message))
            j.registration_list.append(message.text)
            j.previous_actions.append((registration_step_6_teach, await message.answer("Введите свою почту")))
            break


async def registration_step_7_teach(message: Message):
    for j in teachers:
        if j.chat_id == message.chat.id:
            await asyncio.create_task(delete_message(j.previous_actions[-1][1]))
            await asyncio.create_task(delete_message(message))
            j.registration_list.append(message.text)
            j.previous_actions.append((registration_step_7_teach, message))
            append_all_2(j.registration_list, j.id)
            await message.answer(f'Вы успешно зарегистрировались. ✅', reply_markup=REGISTRATION_SUCCESS_TEACHER.as_markup())
            break


async def main_lobby_teacher(call: CallbackQuery):
    for j in teachers:
        if j.chat_id == call.message.chat.id:
            await asyncio.create_task(delete_message(call.message))
            j.previous_actions.append((main_lobby_teacher, call.message))
            await call.message.answer(f'Описание',
                                 reply_markup=MAIN_LOBBY_TEACHER.as_markup())
            break


async def Lessons_teacher(call: CallbackQuery):
    for j in teachers:
        if j.chat_id == call.message.chat.id:
            j.previous_actions.append((Lessons_teacher, call.message))
            await call.message.edit_text(f'''Вы перешли в раздел "Уроки" 👀
Здесь вы можете создать новый уроки или взаимодействовать со старыми''',
                                      reply_markup=LESSONS_TEACHER.as_markup())
            break


async def Create_lesson(call: CallbackQuery):
    for j in teachers:
        if j.chat_id == call.message.chat.id:
            j.previous_actions.append((Create_lesson, call.message))
            await call.message.edit_text(f'''Вы захотели создать новый урок! 👨‍🏫
 Выберите, что хотите добавить''',
                                         reply_markup=CREATE_LESSON.as_markup())
            break


async def Create_lecture(call: CallbackQuery):
    for j in teachers:
        if j.chat_id == call.message.chat.id:
            j.previous_actions.append((Create_lecture, call.message))
            await call.message.edit_text(f'''Вы захотели добавить "лекцию"✍️
Скиньте файл с лекцией в формате PDF''')
            break


async def Create_test(call: CallbackQuery):
    for j in teachers:
        if j.chat_id == call.message.chat.id:
            j.previous_actions.append((Create_test, call.message))
            await call.message.edit_text(f'''Вы захотели добавить "Тест"✍️
Скиньте файл с тестом в формате PDF''')
            break


async def Create_lab(call: CallbackQuery):
    for j in teachers:
        if j.chat_id == call.message.chat.id:
            j.previous_actions.append((Create_lab, call.message))
            await call.message.edit_text(f'''Вы захотели добавить "лабораторную работу"✍️
Скиньте файл с лабораторной работой в формате PDF''')
            break



async def get_pdf_teach(message: Message, bot: Bot):
    for j in teachers:
        if j.chat_id == message.chat.id and j.previous_actions:
            if j.previous_actions[-1][0] == Create_lecture:
                await asyncio.create_task(pdf_load_to_bd(message, bot, 'lecture'))
            elif j.previous_actions[-1][0] == Create_lab:
                await asyncio.create_task(pdf_load_to_bd(message, bot, 'lab'))
            elif j.previous_actions[-1][0] == Create_test:
                await asyncio.create_task(pdf_load_to_bd(message, bot, 'test'))
            break


async def pdf_load_to_bd(message: Message, bot: Bot, typ):
    file_id = message.document.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    for j in teachers:
        if j.chat_id == message.chat.id:
            if typ == 'lecture':
                await bot.download_file(file_path, f"lectures/{lecture_add(file_id[1:10], j.subs)}")
                await message.answer("Лекция добавлена, пора назначить её кому-нибудь", reply_markup=LESSON_PDF_CONV.as_markup())
            elif typ == 'lab':
                await bot.download_file(file_path, f"lectures/{lecture_add(file_id[1:10], j.subs)}")
                await message.answer("Лабораторная добавлена, пора назначить её кому-нибудь", reply_markup=LESSON_PDF_CONV.as_markup())
            elif typ == 'test':
                await bot.download_file(file_path, f"lectures/{lecture_add(file_id[1:10], j.subs)}")
                await message.answer("Тест добавлена, пора назначить его кому-нибудь", reply_markup=LESSON_PDF_CONV.as_markup())
