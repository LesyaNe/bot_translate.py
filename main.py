import telebot
from googletrans import Translator


bot = telebot.TeleBot('5927677920:AAHMktLf6_RRoc9piTA3mP5pzkRmBjGTmq4')  # токен


@bot.message_handler(commands=['start'])
def to_start(message):
    bot.send_message(message.chat.id,
                     "Привет, я бот-переводчик английского языка. Напиши слово, и я переведу")

@bot.message_handler(content_types='text')  # текст пользователя
# @bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_text1(message):
    bot.send_message(message.chat.id, 'Перевожу')

def do_translate(content_types):
    translator = Translator()
    txt = translator.translate(content_types)
    if txt[0] == 'ru':
        transed = translator.translate(txt ='en')
        bot.send_message(message.chat.id, transed)

    elif txt[0] == 'en':  # если язык английский
        transed = translator.translate(message.text,
                                       txt ='ru')
        bot.send_message(message.chat.id, transed)

    else:
        bot.send_message(message.chat.id, 'Я вас не понял')


if __name__ == '__main__':

    bot.polling(none_stop=True)

