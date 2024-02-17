# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 22:20:52 2024

@author: ABBOS
"""

from transliterate import to_cyrillic, to_latin
import telebot


TOKEN = '6563601887:AAHLSjiAFKkONPgAnAUi1jd6RacRqOasT_E'
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = "Assalomu alaykum, Xush kelibsiz!"
    javob += "\nMatn kiriting:"
    bot.reply_to(message, javob)
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg) 
    bot.reply_to(message, javob(msg))

bot.polling()


#matn = input("Matn kiriting:")

#if matn.isascii():
 #   print(to_cyrillic(matn))
#else:
 #   print(to_cyrillic(matn))