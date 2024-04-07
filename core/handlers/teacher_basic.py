import asyncio

import pygame
from aiogram.types import CallbackQuery, Message

from core.handlers.basic import users
from core.keyboards.reply import START_KEYBOARD
from core.keyboards.reply_teacher import WELCOMING_MESSAGE_TEACHER
from core.middlewares.Classes import Teacher
from core.middlewares.functions_teacher import checker_teach

teachers = pygame.sprite.Group()


async def delete_message(message: Message):
    await message.delete()


async def welcoming_message_teacher(call: CallbackQuery):
    id_us = call.message.chat.id
    for i in users:
        if i.chat_id == id_us:
            if checker_teach(i.username):
                for j in teachers:
                    if str(j.chat_id) == str(id_us):
                        break
                else:
                    Teacher(i.id, i.username, i.chat_id, teachers, add=True)
                    for j in teachers:
                        if j.chat_id == id_us:
                            j.previous_actions.append((welcoming_message_teacher, call.message))
                            break
                await call.message.delete()
                await call.message.answer(f'''Отлично! 👍

Перед началом работы с ботом, советуем пройти обучение 👨‍🎓

Если вы уже прошли обучение или хотите его пропустить, нажмите кнопку «Продолжить» ➡️''',
                                          reply_markup=WELCOMING_MESSAGE_TEACHER.as_markup())
            else:
                await call.message.edit_text(f'''Извините, вы не являетесь админом, если это не так, обратитесь к действующим админам
Для начала работы с ботом, пожалуйста, выберите, кем вы являетесь! 👇''', reply_markup=START_KEYBOARD.as_markup())


async def registered_message(message: Message):
    for j in teachers:
        if j.chat_id == message.chat.id:
            if j.previous_actions[-1][0] == registration_step_2:
                await asyncio.create_task(registration_step_3(message))
            elif j.previous_actions[-1][0] == registration_step_3:
                await asyncio.create_task(registration_step_4(message))
            elif j.previous_actions[-1][0] == registration_step_4:
                await asyncio.create_task(registration_step_5(message))
            elif j.previous_actions[-1][0] == registration_step_5:
                await asyncio.create_task(registration_step_6(message))
            elif j.previous_actions[-1][0] == registration_step_6:
                await asyncio.create_task(registration_step_7(message))


async def registration_teacher(call: CallbackQuery):
    id_us = call.message.chat.id
    for j in teachers:
        if j.chat_id == id_us:
            await call.message.edit_text('Пройдите пожалуйста регистрацию')


async def registration_step_2(call: CallbackQuery):
    for j in teachers:
        if j.chat_id == call.message.chat.id:
            await asyncio.create_task(delete_message(call.message))
            j.previous_actions.append(
                (registration_step_2, await call.message.answer("Введите свою Фамилию")))
            break


async def registration_step_3(message: Message):
    for j in teachers:
        if j.chat_id == message.chat.id:
            await asyncio.create_task(delete_message(j.previous_actions[-1][1]))
            await asyncio.create_task(delete_message(message))
            j.registration_list.append(message.text)
            j.previous_actions.append((registration_step_3, await message.answer("Введите своё имя")))
            break


async def registration_step_4(message: Message):
    for j in teachers:
        if j.chat_id == message.chat.id:
            await asyncio.create_task(delete_message(j.previous_actions[-1][1]))
            await asyncio.create_task(delete_message(message))
            j.registration_list.append(message.text)
            j.previous_actions.append((registration_step_4, await message.answer("Введите своё отчество")))
            break


async def registration_step_5(message: Message):
    for j in teachers:
        if j.chat_id == message.chat.id:
            await asyncio.create_task(delete_message(j.previous_actions[-1][1]))
            await asyncio.create_task(delete_message(message))
            j.registration_list.append(message.text)
            j.previous_actions.append((registration_step_5, await message.answer("Введите контактный телефон")))
            break


async def registration_step_6(message: Message):
    for j in teachers:
        if j.chat_id == message.chat.id:
            await asyncio.create_task(delete_message(j.previous_actions[-1][1]))
            await asyncio.create_task(delete_message(message))
            j.registration_list.append(message.text)
            j.previous_actions.append((registration_step_6, await message.answer("Введите свою почту")))
            break


async def registration_step_7(message: Message):
    for j in teachers:
        if j.chat_id == message.chat.id:
            await asyncio.create_task(delete_message(j.previous_actions[-1][1]))
            await asyncio.create_task(delete_message(message))
            j.registration_list.append(message.text)
            j.previous_actions.append((registration_step_7, message))
            await message.answer(f'Вы успешно вошли в группу курса {j.group_name}. ✅', reply_markup=REGISTRATION_SUCCESS.as_markup())
            break