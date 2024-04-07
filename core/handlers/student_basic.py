import asyncio

import pygame
from aiogram.types import Message, CallbackQuery, FSInputFile

from core.handlers.admin_basic import admin_message_register
from core.keyboards.reply_student import FIRST_MAIN, ID_ENTER_1, ID_ENTER_2, TO_REGISTRATE, REGISTRATION_SUCCESS, \
    LOBBY_MARKUP, PROFILE_STUDENT, SUBJECT
from core.handlers.basic import users
from core.middlewares.Classes import Student
from core.middlewares.extra_gen import generate_password, exists, existing_id, append_all
from core.middlewares.functions_student import subjects_student_choose, get_schedule

students = pygame.sprite.Group()


def start_students(spisok, spisok2):
    if spisok:
        for i in spisok:
            Student(int(i[1]), i[0], int(i[2]), students)
    for j in students:
        for i in spisok2:
            j.group_name = i[0]
            j.group_description = i[1]


async def return_back(call: CallbackQuery):
    for j in students:
        if str(j.chat_id) == str(call.message.chat.id):
            await asyncio.create_task(j.previous_actions[-1][0](call))
            break


async def delete_message(message: Message):
    await message.delete()


async def welcoming_message(call: CallbackQuery):
    id_us = call.message.chat.id
    for i in users:
        if i.chat_id == id_us:
            for j in students:
                if str(j.chat_id) == str(id_us):
                    break
            else:
                Student(i.id, i.username, i.chat_id, students, add=True)

                for j in students:
                    if j.chat_id == id_us:
                        j.previous_actions.append((welcoming_message, call.message))
                break
    await call.message.delete()
    await call.message.answer(f'''Теперь, для того чтобы понять, как работает бот ОГТИ, мы предлагаем пройти вам обучение.  
Для этого нажмите на кнопку «Обучение» 👨‍🎓 

Если вы уже прошли обучение или хотите его пропустить, нажмите кнопку «Продолжить» ➡️''', reply_markup=FIRST_MAIN.as_markup())


async def id_wait(call: CallbackQuery):
    for j in students:
        if j.chat_id == call.message.chat.id:
            j.previous_actions.append((welcoming_message, call.message))
            break
    await call.message.delete()
    await call.message.answer(f'''Теперь, введите ID вашей группы, чтобы ваши учителя могли присылать вам уроки!👨‍🏫''', reply_markup=ID_ENTER_1.as_markup())\


async def id_wait_2(message: Message):
    for j in students:
        if j.chat_id == message.chat.id:
            await asyncio.create_task(delete_message(j.previous_actions[-1][1]))
            await asyncio.create_task(delete_message(message))
            j.previous_actions.append((welcoming_message, message))
            break
    await message.answer('К сожалению такого ID не существует, попробуйте снова.', reply_markup=ID_ENTER_1.as_markup())


async def id_wait_change(call: CallbackQuery):
    for j in students:
        if j.chat_id == call.message.chat.id:
            j.previous_actions.append((id_wait, call.message))
            break
    await call.message.edit_text('Вводите:')


async def group_exists(message: Message):
    for j in students:
        if j.chat_id == message.chat.id:
            await asyncio.create_task(delete_message(j.previous_actions[-1][1]))
            await asyncio.create_task(delete_message(message))
            j.previous_actions.append((group_exists, message))
            await message.answer(f'''Вы вошли в группу {j.group_name} 😄 

Теперь, чтобы учитель смог понять, кто зашел в группу и мог получить ваши контактные данные, пожалуйста, пройдите регистрацию! ✅"''',
                                 reply_markup=TO_REGISTRATE.as_markup())
            break


async def registered_message(message: Message):
    for j in students:
        if j.chat_id == message.chat.id:
            if j.previous_actions[-1][0] == id_wait:
                exist, group_name, group_description = exists(message, j.id)
                if exist:
                    j.group_name = group_name
                    j.group_description = group_description
                    await asyncio.create_task(group_exists(message))
                else:
                    await asyncio.create_task(id_wait_2(message))
            elif j.previous_actions[-1][0] == registration_step_1:
                exist = existing_id(message, j.id)
                if exist:
                    await asyncio.create_task(registration_step_2(message))
            elif j.previous_actions[-1][0] == registration_step_2:
                await asyncio.create_task(registration_step_3(message))
            elif j.previous_actions[-1][0] == registration_step_3:
                await asyncio.create_task(registration_step_4(message))
            elif j.previous_actions[-1][0] == registration_step_4:
                await asyncio.create_task(registration_step_5(message))
            elif j.previous_actions[-1][0] == registration_step_5:
                await asyncio.create_task(registration_step_6(message))
            elif j.previous_actions[-1][0] == registration_step_6:
                await asyncio.create_task(registration_step_7(message))
            elif j.previous_actions[-1][0] == choose_subject:
                await asyncio.create_task(subject_menu(message))
            break
    else:
        await asyncio.create_task(admin_message_register(message))


async def registration_step_1(call: CallbackQuery):
    for j in students:
        if j.chat_id == call.message.chat.id:
            await asyncio.create_task(delete_message(call.message))
            j.previous_actions.append((registration_step_1, await call.message.answer("Введите свой персональный пароль")))
            break


async def registration_step_2(message: Message):
    for j in students:
        if j.chat_id == message.chat.id:
            await asyncio.create_task(delete_message(j.previous_actions[-1][1]))
            await asyncio.create_task(delete_message(message))
            j.registration_list.append(message.text)
            j.previous_actions.append((registration_step_2, await message.answer("Введите свою фамилию")))
            break


async def registration_step_3(message: Message):
    for j in students:
        if j.chat_id == message.chat.id:
            await asyncio.create_task(delete_message(j.previous_actions[-1][1]))
            await asyncio.create_task(delete_message(message))
            j.registration_list.append(message.text)
            j.previous_actions.append((registration_step_3, await message.answer("Введите своё имя")))
            break


async def registration_step_4(message: Message):
    for j in students:
        if j.chat_id == message.chat.id:
            await asyncio.create_task(delete_message(j.previous_actions[-1][1]))
            await asyncio.create_task(delete_message(message))
            j.registration_list.append(message.text)
            j.previous_actions.append((registration_step_4, await message.answer("Введите своё отчество")))
            break


async def registration_step_5(message: Message):
    for j in students:
        if j.chat_id == message.chat.id:
            await asyncio.create_task(delete_message(j.previous_actions[-1][1]))
            await asyncio.create_task(delete_message(message))
            j.registration_list.append(message.text)
            j.previous_actions.append((registration_step_5, await message.answer("Введите контактный телефон")))
            break


async def registration_step_6(message: Message):
    for j in students:
        if j.chat_id == message.chat.id:
            await asyncio.create_task(delete_message(j.previous_actions[-1][1]))
            await asyncio.create_task(delete_message(message))
            j.registration_list.append(message.text)
            j.previous_actions.append((registration_step_6, await message.answer("Введите свою почту")))
            break


async def registration_step_7(message: Message):
    for j in students:
        if j.chat_id == message.chat.id:
            await asyncio.create_task(delete_message(j.previous_actions[-1][1]))
            await asyncio.create_task(delete_message(message))
            j.registration_list.append(message.text)
            append_all(j.registration_list, j.id)
            j.previous_actions.append((registration_step_7, message))
            await message.answer(f'Вы успешно вошли в группу курса {j.group_name}. ✅', reply_markup=REGISTRATION_SUCCESS.as_markup())
            break


async def lobby_student(call: CallbackQuery):
    for j in students:
        if j.chat_id == call.message.chat.id:
            await asyncio.create_task(delete_message(call.message))
            j.previous_actions.append((lobby_student, call.message))
            await call.message.answer(f"""Добро пожаловать на главную страницу группы {j.group_name}!👏 
            
{j.group_description}""", reply_markup=LOBBY_MARKUP.as_markup())
            break


async def profile_student(call: CallbackQuery):
    for j in students:
        if j.chat_id == call.message.chat.id:
            await asyncio.create_task(delete_message(call.message))
            await call.message.answer(f"""Вы перешли в раздел "Профиль" 👀
 Здесь вы можете увидеть вашу статистику, изменить информацию о вас ✍️
 Нажмите на одну из кнопок ниже, чтобы выбрать действие 👇""", reply_markup=PROFILE_STUDENT.as_markup())
            break


async def choose_subject(call: CallbackQuery):
    for j in students:
        if j.chat_id == call.message.chat.id:
            await asyncio.create_task(delete_message(call.message))
            subs = subjects_student_choose(j.group_name)
            strok = '\n'.join(subs)
            j.previous_actions.append((choose_subject, await call.message.answer(f"""Вы перешли в раздел "Выбрать предмет" 👀
Выберите предмет, по которому вы хотите пройти урок👨‍🏫\n\n{strok}""")))
            break


async def subject_menu(message: Message):
    for j in students:
        if j.chat_id == message.chat.id:
            await asyncio.create_task(delete_message(message))
            await asyncio.create_task(delete_message(j.previous_actions[-1][1]))
            j.previous_actions.append((choose_subject, message))
            subs = subjects_student_choose(j.group_name)
            for i in subs:
                if i.startswith(message.text):
                    strok = i[3:].split(' - ')
                    break
            await message.answer(f"""{strok[0]}

Для выбора действия, нажмите на одну из кнопок ниже👇""", reply_markup=SUBJECT.as_markup())
            break


async def send_schedule(call: CallbackQuery):
    for j in students:
        if j.chat_id == call.message.chat.id:
            sch = get_schedule(j.group_name)
            file = FSInputFile(path=sch)
            await call.message.answer_document(file)
