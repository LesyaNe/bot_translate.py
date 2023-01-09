import telebot
from googletrans import Translator
import os

bot = telebot.TeleBot('5927677920:AAHMktLf6_RRoc9piTA3mP5pzkRmBjGTmq4')  # токен


@bot.message_handler(commands=['start'])
def to_start(message):  # обращаемся к переводчику
    bot.send_message(message.chat.id,
                     "Привет, я бот-переводчик английского языка. Напиши слово, и я переведу")  # сообщение \start


# @bot.message_handler(content_types='text')  # текст пользователя
@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_text1(message):
    bot.send_message(message.chat.id, 'Перевожу')

def do_translate(message):
    translator = Translator()
    txt = translator.detect(message.text)  # определяем язык
    if txt[0] == 'ru':  # если язык русский
        transed = translator.translate(message.text,
                                       txt_tgt='en')  # переводим с русского на анг.
        bot.send_message(message.chat.id, transed)  # отправляем перевод

    elif txt[0] == 'en':  # если язык английский
        transed = translator.translate(message.text,
                                       txt_tgt='ru')  # переводит с английского на русский
        bot.send_message(message.chat.id, transed)  # отправляем перевод

    else:
        bot.send_message(message.chat.id, 'Я вас не понял')  # если пользователь ввел некорректный текс


if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)  # запускаем бота
        except Exception as e:  # если ошибка
            print('error: ' + str(e))  # выводим ее в терминал
