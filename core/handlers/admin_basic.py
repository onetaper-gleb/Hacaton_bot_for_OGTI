import asyncio

import pygame
from aiogram import Bot
from aiogram.types import CallbackQuery, Message
from core.handlers.basic import users
from core.keyboards.reply import START_KEYBOARD
from core.keyboards.reply_admins import FIRST_MAIN, MAIN, ADMIN_CONTROL, GROUPS_CHECK, CREATE_GROUP_5, CREATED_GROUP, \
    TEACHER_SETTINGS, CREATED_TEACHER
from core.middlewares.Classes import Admin
from core.middlewares.functions_admin import checker, checker_2, add_admin_to_bd, groups_to_see, get_subs, \
    create_group_bd, schedule_add, create_teacher_bd

admins = pygame.sprite.Group()


def start_admin(spisok):
    if spisok:
        for i in spisok:
            Admin(int(i[1]), i[0], int(i[2]), admins)
            print(i)


async def delete_message(message: Message):
    await message.delete()


async def welcoming_message_ad(call: CallbackQuery):
    id_us = call.message.chat.id
    for i in users:
        if i.chat_id == id_us:
            if checker(i.username):
                for j in admins:
                    print(j.username)
                    if str(j.chat_id) == str(id_us):
                        break
                else:
                    Admin(i.id, i.username, i.chat_id, admins, add=True)
                    for j in admins:
                        if j.chat_id == id_us:
                            j.previous_actions.append((welcoming_message_ad, call.message))
                            break
                await call.message.delete()
                await call.message.answer(f'''Отлично! 👍
                
Перед началом работы с ботом, советуем пройти обучение 👨‍🎓

Если вы уже прошли обучение или хотите его пропустить, нажмите кнопку «Продолжить» ➡️''', reply_markup=FIRST_MAIN.as_markup())
            else:
                await call.message.edit_text(f'''Извините, вы не являетесь админом, если это не так, обратитесь к действующим админам
Для начала работы с ботом, пожалуйста, выберите, кем вы являетесь! 👇''', reply_markup=START_KEYBOARD.as_markup())


async def main_menu_admin(call: CallbackQuery):
    for j in admins:
        if str(j.chat_id) == str(call.message.chat.id):
            try:
                if j.previous_actions[-1][0] == teacher_settings:
                    j.page = 0
            except:
                pass
            await delete_message(call.message)
            j.previous_actions.append((main_menu_admin, call.message))
            break
    await call.message.answer(f'''Вы находитесь в главном меню администратора! ✅
Выберите действие, которое вы хотите выполнить, нажав одну из кнопок ниже👇''', reply_markup=MAIN.as_markup())


async def admin_control(call: CallbackQuery):
    for j in admins:
        if str(j.chat_id) == str(call.message.chat.id):
            await delete_message(call.message)
            j.previous_actions.append((admin_control, call.message))
            break
    adminers = checker_2()
    ret = []
    for i in range(len(adminers)):
        ret.append(f'{str(i + 1)}. @{adminers[i][0]}')
    ret = '\n'.join(ret)
    await call.message.answer(f'''Вы перешли в раздел "Администрация" 👀
Здесь вы можете назначить или удалить администратора 🎖
    
{ret}''', reply_markup=ADMIN_CONTROL.as_markup())


async def admin_delete(call: CallbackQuery):
    for j in admins:
        if str(j.chat_id) == str(call.message.chat.id):
            j.previous_actions.append((admin_delete, call.message))
            break
    adminers = checker_2()
    ret = []
    for i in range(len(adminers)):
        ret.append(f'{str(i + 1)}. @{adminers[i][0]}')
    ret = '\n'.join(ret)
    await call.message.edit_text(f'''Выберите из списка администратора, которого вы хотите удалить

{ret}''')


async def admin_add_1(call: CallbackQuery):
    for j in admins:
        if str(j.chat_id) == str(call.message.chat.id):
            await delete_message(call.message)
            j.previous_actions.append((admin_add_1, await call.message.answer(f'''Введите тег пользователя без @
Пример: Hleb_sin''')))
            break


async def admin_message_register(message: Message):
    for j in admins:
        print(message.from_user.username, j.username)
        if j.chat_id == message.chat.id:
            print("SUCCESS")
            if j.previous_actions[-1][0] == admin_add_1:
                add_admin_to_bd(message.text)
                await asyncio.create_task(admin_control_2(message))
            elif j.previous_actions[-1][0] == admin_delete:
                add_admin_to_bd(message.text, add=False)
                await asyncio.create_task(admin_control_2(message))
            elif j.previous_actions[-1][0] == groups_check:
                await asyncio.create_task(group_check(message))
                print('Hey')
            elif j.previous_actions[-1][0] == create_group_1:
                await asyncio.create_task(create_group_2(message))
                print('Hey')
            elif j.previous_actions[-1][0] == create_group_2:
                await asyncio.create_task(create_group_3(message))
            elif j.previous_actions[-1][0] == create_group_3:
                await asyncio.create_task(create_group_5(message))
            elif j.previous_actions[-1][0] == create_group_5:
                await asyncio.create_task(group_created(message))
            elif j.previous_actions[-1][0] == create_teacher_1:
                await asyncio.create_task(create_teacher_2(message))
            elif j.previous_actions[-1][0] == create_teacher_2:
                await asyncio.create_task(create_teacher_3(message))
            elif j.previous_actions[-1][0] == create_teacher_3:
                await asyncio.create_task(created_teacher(message))
            break


async def admin_control_2(message: Message):
    for j in admins:
        if str(j.chat_id) == str(message.chat.id):
            await delete_message(message)
            await delete_message(j.previous_actions[-1][1])
            j.previous_actions.append((admin_control, message))
            break
    adminers = checker_2()
    ret = []
    for i in range(len(adminers)):
        ret.append(f'{str(i + 1)}. @{adminers[i][0]}')
    ret = '\n'.join(ret)
    await message.answer(f'''Вы перешли в раздел "Администрация" 👀
Здесь вы можете назначить или удалить администратора 🎖
    
{ret}''', reply_markup=ADMIN_CONTROL.as_markup())


async def groups_check(call: CallbackQuery):
    for j in admins:
        if str(j.chat_id) == str(call.message.chat.id):
            res = groups_to_see()
            ans = []
            if res:
                for i in range(len(res)):
                    ans.append(f'{i + 1}. {res[i][0]} {res[i][1]}')
                ans = "\n".join(ans)
                await call.message.edit_text(f'''Выберите группу, которую хотите просмортеть

{ans}''', reply_markup=GROUPS_CHECK.as_markup())
            else:
                await call.message.edit_text(f'''Пока что не создано ни одной группы курса, самое время начать.''',
                                             reply_markup=GROUPS_CHECK.as_markup())
            j.previous_actions.append((groups_check, call.message))
            break


async def group_check(message: Message):
    for j in admins:
        if str(j.chat_id) == str(message.chat.id):
            await asyncio.create_task(delete_message(message))
            await asyncio.create_task(delete_message(j.previous_actions[-1][1]))
            res = groups_to_see(one=message.text)
            ans = []
            ans_1 = []
            if res:
                ans.append(f'{res[0][0][0]} - {res[0][0][1]} \n \n {res[0][0][2]}')
                ans.append('\n\nСписок учеников: \n')
                for i in range(len(res[1])):
                    ans.append(
                        f'\n {i + 1}. {res[1][i][0]} {res[1][i][1]} {res[1][i][2]} {res[1][i][3]} {res[1][i][4]}')
                ans.append('\n\nСписок предметов: \n')
                for i in range(len(res[2])):
                    ans.append(f'\n {i + 1}. {res[2][i]}')
                ans = "\n".join(ans)
                j.previous_actions.append((groups_check, await message.answer(f'''Вот данные группы:

            {ans}''', reply_markup=GROUPS_CHECK.as_markup())))
            else:
                res = groups_to_see()
                ans = []
                if res:
                    for i in range(len(res)):
                        ans.append(f'{i + 1}. {res[i][0]} {res[i][1]}')
                    ans = "\n".join(ans)
                    j.previous_actions.append((groups_check, await message.answer(f'''Убедитесь, что вы ввели номер коректно

            {ans}''', reply_markup=GROUPS_CHECK.as_markup())))
            break


async def create_group_1(call: CallbackQuery):
    for j in admins:
        if str(j.chat_id) == str(call.message.chat.id):
            await asyncio.create_task(delete_message(call.message))
            j.previous_actions.append((create_group_1, await call.message.answer('Введите название курса')))
            break

async def create_group_2(message: Message):
    for j in admins:
        if str(j.chat_id) == str(message.chat.id):
            await asyncio.create_task(delete_message(message))
            await asyncio.create_task(delete_message(j.previous_actions[-1][1]))
            j.new_cours.append(message.text)
            j.previous_actions.append((create_group_2, await message.answer('Введите описание курса')))
            break


async def create_group_3(message: Message):
    for j in admins:
        if str(j.chat_id) == str(message.chat.id):
            await asyncio.create_task(delete_message(message))
            await asyncio.create_task(delete_message(j.previous_actions[-1][1]))
            j.new_cours.append(message.text)
            j.previous_actions.append((create_group_3, await message.answer('Введите количество учеников курса')))
            break


async def create_group_5(message: Message):
    for j in admins:
        if str(j.chat_id) == str(message.chat.id):
            await asyncio.create_task(delete_message(message))
            await asyncio.create_task(delete_message(j.previous_actions[-1][1]))
            j.new_cours.append(message.text)
            subs = get_subs(j.page)
            subs = '\n'.join(subs)
            j.previous_actions.append((create_group_5, await message.answer(f'''Введите номера предметов из списка и запишите через пробел
            
{subs}''', reply_markup=CREATE_GROUP_5.as_markup())))
            break


async def create_group_5_2(call: CallbackQuery):
    for j in admins:
        if str(j.chat_id) == str(call.message.chat.id):
            j.page += 1
            subs = get_subs(j.page)
            subs = '\n'.join(subs)
            j.previous_actions.append((create_group_5, call.message))
            await call.message.edit_text(f'''Введите номера предметов из списка и запишите через пробел

{subs}''', reply_markup=CREATE_GROUP_5.as_markup())
            break


async def group_created(message: Message):
    for j in admins:
        if str(j.chat_id) == str(message.chat.id):
            await asyncio.create_task(delete_message(message))
            await asyncio.create_task(delete_message(j.previous_actions[-1][1]))
            j.new_cours.append(message.text)
            passes, password = create_group_bd(j.new_cours)
            passes = "\n".join(passes)
            j.previous_actions.append((group_created, await message.answer(f'''Вы успешно создали новую группу курса {j.new_cours[0]}, её пароль: {password}

Пароли учеников:

{passes}

Добавьте расписание к группе в формате pdf''')))
            j.new_cours = []
            j.page = 0
            break


async def get_pdf(message: Message, bot: Bot):
    for j in admins:
        if j.chat_id == message.chat.id:
            if j.previous_actions[-1][0] == group_created:
                await asyncio.create_task(pdf_load_to_bd(message, bot))


async def pdf_load_to_bd(message: Message, bot: Bot):
    file_id = message.document.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    await bot.download_file(file_path, f"schedules/{schedule_add()}")
    await message.answer("Поздравляем с успешной регистрацией", reply_markup=CREATED_GROUP.as_markup())


async def teacher_settings(call: CallbackQuery):
    for j in admins:
        if j.chat_id == call.message.chat.id:
            j.previous_actions.append((teacher_settings, call.message))
            subs = get_subs(j.page, id=True)
            subs = '\n'.join(subs)
            await call.message.edit_text(f'''Введите номера предметов из списка и запишите через пробел

{subs}''', reply_markup=TEACHER_SETTINGS.as_markup())
            break


async def teacher_settings_2(call: CallbackQuery):
    for j in admins:
        if j.chat_id == call.message.chat.id:
            j.previous_actions.append((teacher_settings, call.message))
            j.page += 1
            subs = get_subs(j.page, id=True)
            subs = '\n'.join(subs)
            await call.message.edit_text(f'''Введите номера предметов из списка и запишите через пробел

{subs}''', reply_markup=TEACHER_SETTINGS.as_markup())
            break


async def create_teacher_1(call: CallbackQuery):
    for j in admins:
        if str(j.chat_id) == str(call.message.chat.id):
            await asyncio.create_task(delete_message(call.message))
            j.previous_actions.append((create_teacher_1, await call.message.answer('Введите предмет')))
            break


async def create_teacher_2(message: Message):
    for j in admins:
        if str(j.chat_id) == str(message.chat.id):
            await asyncio.create_task(delete_message(message))
            await asyncio.create_task(delete_message(j.previous_actions[-1][1]))
            j.new_cours.append(message.text)
            j.previous_actions.append((create_teacher_2, await message.answer('Введите ФИО учителя')))
            break


async def create_teacher_3(message: Message):
    for j in admins:
        if str(j.chat_id) == str(message.chat.id):
            await asyncio.create_task(delete_message(message))
            await asyncio.create_task(delete_message(j.previous_actions[-1][1]))
            j.new_cours.append(message.text)
            j.previous_actions.append((create_teacher_3, await message.answer('Введите телеграм тег учителя по примеру: Hleb_sin')))
            break


async def created_teacher(message: Message):
    for j in admins:
        if str(j.chat_id) == str(message.chat.id):
            await asyncio.create_task(delete_message(message))
            await asyncio.create_task(delete_message(j.previous_actions[-1][1]))
            j.new_cours.append(message.text)
            create_teacher_bd(j.new_cours)
            j.new_cours = []
            j.previous_actions.append((create_teacher_3, await message.answer('Вы добавили новый предмет, нажмите вернуться, чтобы вернуться к списку учителей', reply_markup=CREATED_TEACHER.as_markup())))
            break


