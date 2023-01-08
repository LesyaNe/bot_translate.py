import telebot
from googletrans import Translator

bot = telebot.TeleBot('')  # токен


@bot.message_handler(commands=['start'])
def send_start(message):
    bot.reply_to(message, 'Привет, я бот-переводчик английского языка. Напиши слово, и я переведу')  # сообщение \start


@bot.message_handler(content_types='text')  # текст пользователя
def do_translate(message):
    translator = Translator()  # обращяемся к переводчику
    lang = translator.detect(message.text)  # определяем язык

    if lang[0] == 'ru':  # если язык русский
        transed = translator.translate(message.text, lang_tgt='en')  # переводим с русского на анг.
        bot.reply_to(message, transed)  # отправляем перевод

    elif lang[0] == 'en':  # если язык английский
        transed = translator.translate(message.text, lang_tgt='ru')  # переводит с английского на русский
        bot.reply_to(message, transed)

    else:
        bot.reply_to(message, 'Я вас не понял')  # если пользователь ввел некорректный текс


if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)  # запускаем бота
        except Exception as e:  # если ошибка
            print('error: ' + str(e))  # выводим ее в терминал
