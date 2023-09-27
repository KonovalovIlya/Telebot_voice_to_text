import os
import telebot
import speech_recognition
from pydub import AudioSegment


TOKEN = ''
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def hello(message):
    """Функция отправляющая приветствие в ответ на комманду / start"""
    bot.send_message(message.chat.id, 'Привет '+message.chat.first_name)


#@bot.message_handler(content_types=['audio', 'voice'])


if __name__ == "__main__":
    bot.polling()
