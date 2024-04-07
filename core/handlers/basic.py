import pygame
from aiogram.types import Message
from core.keyboards.reply import START_KEYBOARD
from core.middlewares.Classes import User

users = pygame.sprite.Group()


async def choice(message: Message):
    await message.delete()
    await message.answer(f'''Здравствуйте! 👋 
Вы запустили бота ОГТИ! 🤖 
Для начала работы с ботом, пожалуйста, выберите, кем вы являетесь! 👇''', reply_markup=START_KEYBOARD.as_markup())
    id_us = message.chat.id
    name = message.from_user.username
    for i in users:
        if i.id == id_us:
            pass
    else:
        User(message.from_user.id, name, id_us, users)
