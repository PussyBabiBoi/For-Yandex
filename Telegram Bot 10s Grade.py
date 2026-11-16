import telebot
from telebot import types

bot = telebot.TeleBot('6431073684:AAHEWJhYUPRWnQe5_1pIVeeHz49dT0tUj8o')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Привет {message.from_user.username}, Меня зовут Alex и я могу помочь тебе подготовиться к ЕГЭ по профильной математике! \nПросто нажми на /tasks и выбери нужное тебе задание')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, '/start - Начать бота \n/help - Список всех команд \n/tasks - Выбрать задание')


@bot.message_handler(commands=['tasks'])
def task(message):
    task_markup = types.InlineKeyboardMarkup()
    task1 = types.InlineKeyboardButton('Расстояние между скрещивающимися прямыми', callback_data='first')
    task_markup.row(task1)
    task2 = types.InlineKeyboardButton('Расстояние от точки до плоскости', callback_data='second')
    task_markup.row(task2)
    task3 = types.InlineKeyboardButton('Угол между прямой и плоскостью', callback_data='third')
    task_markup.row(task3)
    task4 = types.InlineKeyboardButton('Угол между скрещивающимися прямыми', callback_data='fourth')
    task_markup.row(task4)
    task5 = types.InlineKeyboardButton('Угол между плоскостями', callback_data='fifth')
    task_markup.row(task5)
    task6 = types.InlineKeyboardButton('К заданиям', callback_data='sixth')
    task_markup.row(task6)
    bot.reply_to(message, 'Какое задание ты хочешь разобрать?', reply_markup=task_markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'first':
        back_markup = types.InlineKeyboardMarkup()
        back_markup.add(types.InlineKeyboardButton('Назад', callback_data='back'))
        file1 = open('1st task.jpg', 'rb')
        bot.send_photo(callback.message.chat.id, file1, reply_markup=back_markup)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
    elif callback.data == 'second':
        back_markup = types.InlineKeyboardMarkup()
        back_markup.add(types.InlineKeyboardButton('Назад', callback_data='back'))
        file2 = open('2nd task.jpg', 'rb')
        bot.send_photo(callback.message.chat.id, file2, reply_markup=back_markup)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
    elif callback.data == 'third':
        back_markup = types.InlineKeyboardMarkup()
        back_markup.add(types.InlineKeyboardButton('Назад', callback_data='back'))
        file3 = open('3d task.jpg', 'rb')
        bot.send_photo(callback.message.chat.id, file3, reply_markup=back_markup)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
    elif callback.data == 'fourth':
        back_markup = types.InlineKeyboardMarkup()
        back_markup.add(types.InlineKeyboardButton('Назад', callback_data='back'))
        file4 = open('4th task.jpg', 'rb')
        bot.send_photo(callback.message.chat.id, file4, reply_markup=back_markup)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
    elif callback.data == 'fifth':
        back_markup = types.InlineKeyboardMarkup()
        back_markup.add(types.InlineKeyboardButton('Назад', callback_data='back'))
        file5 = open('5th task.jpg', 'rb')
        bot.send_photo(callback.message.chat.id, file5, reply_markup=back_markup)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
    elif callback.data == 'sixth':
        practicing(callback.message)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
    elif callback.data == 'back':
        task(callback.message)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)


@bot.message_handler(commands=['practice'])
def practicing(message):
    bot.send_message(message.chat.id, 'Теперь, после обучения ты можешь попрактиковаться, применив полученные знания.')
    practice_markup = types.InlineKeyboardMarkup()
    practice1 = types.InlineKeyboardButton('Задача на расстояние между скрещивающимися прямыми', callback_data='prctce 1')
    practice_markup.row(practice1)
    practice2 = types.InlineKeyboardButton('Задача на расстояние от точки до плоскости', callback_data='prctce 2')
    practice_markup.row(practice2)
    practice3 = types.InlineKeyboardButton('Задача на угол между прямой и плоскостью', callback_data='prctce 3')
    practice_markup.row(practice3)
    practice4 = types.InlineKeyboardButton('Задача на угол между скрещивающимися прямыми', callback_data='prctce 4')
    practice_markup.row(practice4)
    practice5 = types.InlineKeyboardButton('Задача на угол между плоскостями', callback_data='prctce 5')
    practice_markup.row(practice5)
    bot.reply_to(message, 'По какой теме ты хочешь решить задачу?', reply_markup=practice_markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message1(callback):
    if callback.data == 'prctce 1':
        one = open('pc 1.png', 'rb')
        back_markup = types.InlineKeyboardMarkup()
        back_markup.add(types.InlineKeyboardButton('Назад', callback_data='back'))
        bot.send_photo(callback.message.chat.id, one)
        bot.send_message(callback.message.chat.id, 'В кубе ABCDA1B1C1D1 найдите расстояние между прямыми AB1 и BC1. Длина ребра куба равна 3.')
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'prctce 2':
        two = open('pc 2.png', 'rb')
        back_markup = types.InlineKeyboardMarkup()
        back_markup.add(types.InlineKeyboardButton('Назад', callback_data='back'))
        bot.send_photo(callback.message.chat.id, two)
        bot.send_message(callback.message.chat.id, 'В правильной треугольной призме ABCA1B1C1 сторона основания равна 2, а боковое ребро равно 1. Найдите расстояние от точки B1 до плоскости ABC1')
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'prctce 3':
        three = open('pc 3.png', 'rb')
        back_markup = types.InlineKeyboardMarkup()
        back_markup.add(types.InlineKeyboardButton('Назад', callback_data='back'))
        bot.send_photo(callback.message.chat.id, three)
        bot.send_message(callback.message.chat.id, 'Дан куб ABCDA1B1C1D1. Найдите угол между прямой A1C1 и плоскостью (A1D1C). Ответ дайте в градусах.')
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'prctce 4':
        four = open('pc 4.png', 'rb')
        back_markup = types.InlineKeyboardMarkup()
        back_markup.add(types.InlineKeyboardButton('Назад', callback_data='back'))
        bot.send_photo(callback.message.chat.id, four)
        bot.send_message(callback.message.chat.id, 'В кубе ABCDA1B1C1D1 найти угол между прямыми: а) A1C1 и BD; б) A1B и B1C.')
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'prctce 5':
        back_markup = types.InlineKeyboardMarkup()
        back_markup.add(types.InlineKeyboardButton('Назад', callback_data='back'))
        bot.send_message(callback.message.chat.id, 'В правильной четырёхугольной призме ABCDA1B1C1D1 сторона основания равна 2, а высота равна √2. Найдите угол между плоскостями ABC и AB1C.')
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'back':
        practicing(callback.message)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)


bot.infinity_polling()