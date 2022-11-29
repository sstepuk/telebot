import os
import logging

from aiogram import Bot, Dispatcher, executor, types

#from config import TOKEN

logging.basicConfig(level = logging.INFO)

TOKEN = os.getenv('TOKEN')

bot = Bot(token = TOKEN)
dp = Dispatcher(bot)
def strlat(strin):
    trd = {
        ' ': ' ', 
        '-': '-',
        'а': 'a',
        'б': 'b',
        'в': 'v',
        'г': 'g',
        'д': 'd',
        'е': 'e',
        'ё': 'jo',
        'ж': 'zh',
        'з': 'z',
        'и': 'i',
        'й': 'j',
        'к': 'k',
        'л': 'l',
        'м': 'm',
        'н': 'n',
        'о': 'o',
        'п': 'p',
        'р': 'r',
        'с': 's',
        'т': 't',
        'у': 'u',
        'ф': 'f',
        'х': 'h',
        'ц': 'tc',
        'ч': 'ch',
        'ш': 'sh',
        'щ': 'shсh',
        'ъ': 'j',
        'ы': 'u',
        'ь': '',
        'э': 'e',
        'ю': 'ju',
        'я': 'ia',
        'А': 'A',
        'Б': 'B',
        'В': 'V',
        'Г': 'G',
        'Д': 'D',
        'Е': 'E',
        'Ё': 'Jo',
        'Ж': 'Zh',
        'З': 'Z',
        'И': 'I',
        'Й': 'J',
        'К': 'K',
        'Л': 'L',
        'М': 'M',
        'Н': 'N',
        'О': 'O',
        'П': 'P',
        'Р': 'R',
        'С': 'S',
        'Т': 'T',
        'У': 'U',
        'Ф': 'F',
        'Х': 'H',
        'Ц': 'Tc',
        'Ч': 'Ch',
        'Ш': 'Sh',
        'Щ': 'Shсh',
        'Ъ': '',
        'Ы': 'U',
        'Ь': '',
        'Э': 'E',
        'Ю': 'Ju',
        'Я': 'Ia'
    }
    tranout = ''
    for i in range(len(strin)):
        if strin[i] != 'ь':
            tranout+=trd[strin[i]]
    return tranout.upper()

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_name = message.from_user.full_name
    user_id=message.from_user.id
    text = f'Привет, {user_name}! Какое ФИО вы хотите транслитерировать?'
    logging.info(f'{user_name=} {user_id=} sent message: {message.text}')
    await message.reply(text)

@dp.message_handler()
async def translit(message: types.Message):
    user_name = message.from_user.full_name
    user_id=message.from_user.id
    #text = f'Hello, {name}!'
    text = strlat(message.text)
    logging.info(f'{user_name=} {user_id=} sent message: {text}')
    await bot.send_message(user_id, text)
    
if __name__=='__main__':
    executor.start_polling(dp)

