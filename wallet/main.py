"""
                .__  .__          __
__  _  _______  |  | |  |   _____/  |_
\ \/ \/ /\__  \ |  | |  | _/ __ \   __\
 \     /  / __ \|  |_|  |_\  ___/|  |
  \/\_/  (____  /____/____/\___  >__|
              \/               \/
                                     by Commit404 & salobchyanskiy
"""


# Импорты / Imports
import requests
import time
import copy
import random
import os
import json
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from keyboards import inline_kb1, inline_btn_1, \
    inline_kb2, inline_btn_2, \
    inline_kb3, inline_btn_3, \
    inline_kb4, inline_btn_4, \
    inline_kb5, inline_btn_5, \
    inline_kb6, inline_btn_6 # импортируем из клавиатуры кнопки
from config import config # импортируем конфиг



client = Bot(token=config.token)
dp = Dispatcher(client)

# Приветствие / Welcome
@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("👋 Привет, {message.from_user.full_name}! я *Crimson Coalition Wallet* - Мультивалютный криптокошелек в Telegram. Покупайте, продавайте, храните и платите криптовалютой когда хотите. Подписывайтесь на наш канал @CrimsonCoalition. 💰.\nВаш мультивалютный кошелек создан и вы можете начать пользование системой 🛠. ")

 # Wallet / Кошелек
@dp.message_handler(commands=["wallet"])
async def wallet_command(message: types.Message):
    await message.reply("{0.first_name}, это ваш счет:", reply_markup=inline_kb1)
    
# Settings / Настройки
@dp.message_handler(commands=["settings"])
async def settings_command(message: types.Message):
    await message.reply("{0.first_name}, Добро пожаловать в настройки:", reply_markup=inline_kb4)
                      
# Donate / Донат
@dp.message_handler(commands=["donate"])
async def donate_command(message: types.Message):
    await message.reply("{0.first_name}, мы постоянно занимаемся развитием этого проекта и стараемся делать регулярные обновления, если тебе нравится этот кошелек - отправь любую сумму пожертвования разработчикам на коффе:", reply_markup=inline_kb6)
 
# Admin / Админка
@dp.message_handler(commands=["admin"])                      
async def adm_start_command(message: types.Message):
    await message.reply("{0.first_name}, ты не админ")
                      
# Делаем так, чтобы бот работал постоянно
if __name__ == '__main__':
    executor.start_polling(dp)
