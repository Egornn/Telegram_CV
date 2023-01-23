import os
import telebot
# from telegram.ext import Updater
# from telegram.ext import CommandHandler, CallbackQueryHandler
# from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup
# import asyncio
import core.key as key


bot = telebot.TeleBot(key.BOT_TOKEN) 

@bot.message_handler(commands= ['start', 'hello'])
def hello_user (message):
    bot.send_message(message.chat.id, 'Hello, this is a bot by Egor Nazdriukhin that contains relevant information and /contacts including /CV, /LinkedIn and /GitHub')

@bot.message_handler(commands= ['CV'])
def cv_user (message):
    bot.send_message(message.chat.id,  "https://drive.google.com/file/d/1Drnop43gCaGtQV4PXW-7yuOPgzv2Y5A9/view?usp=share_link")

@bot.message_handler(commands= ['LinkedIn'])
def linkedin_profile (message):
    bot.send_message(message.chat.id, 'https://www.linkedin.com/in/egor-nazdriukhin-288101255')

@bot.message_handler(commands= ['GitHub'])
def git_link (message):
    bot.send_message(message.chat.id, 'https://github.com/Egornn?tab=repositories')

@bot.message_handler(commands= ['contacts'])
def contacts (message):
    
    bot.send_message(message.chat.id, 'address: 907 Watkins House, 3 Thomas Layton Way, Brentford, London, UK')
    bot.send_message(message.chat.id, 'email: enazdryuhin@nes.ru')
    bot.send_message(message.chat.id, 'tel: +44 7469 637234')
    


bot.infinity_polling()
