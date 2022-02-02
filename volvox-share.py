# -*- coding: utf8 -*-
import telebot
import os

print("Coded and designed by Krylov Vladimir")

bot = telebot.TeleBot('your token here')
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Загрузить файл', 'О проекте', 'Просмотр файлов', 'О компьютере')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Добро пожаловать в Volvox Share', reply_markup=keyboard1)
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'загрузить файл':
        bot.send_message(message.chat.id, 'Отправьте фотографию как документ')
        
        @bot.message_handler(content_types=['document'])
        def handle_docs_photo(message):
            try:
                chat_id = message.chat.id

                file_info = bot.get_file(message.document.file_id)
                downloaded_file = bot.download_file(file_info.file_path)

                src = 'C:/Volvox Share/' + message.document.file_name;
                with open(src, 'wb') as new_file:
                    new_file.write(downloaded_file)
                    bot.reply_to(message, "Фотография сохранена")
    
            except Exception as e:
                bot.reply_to(message, e)        
        
    elif message.text.lower() == 'о проекте':
        bot.send_message(message.chat.id, 'Volvox Share это самый быстрый способ по передаче файлов между устройствами! ')
            
    elif message.text.lower() == 'просмотр файлов':
        bot.send_message(message.chat.id, 'Volvox Share это самый быстрый способ по передаче файлов между устройствами! ')
        
    elif message.text.lower() == 'о компьютере':
        bot.send_message(message.chat.id, 'Выберите пункт управления пк')
        keyboard1 = telebot.types.ReplyKeyboardMarkup()
        keyboard1.row('Скриншот')
        @bot.message_handler(content_types=['text'])
        def send_text(message):
            if message.text.lower() == 'скриншот':
                pg.screenshot("yourPic.png")
bot.polling()