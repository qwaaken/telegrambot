import telebot
from config import token
from logic_ai import get_class 

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Добро пожаловать в бота по определению dog breed . \n Просто отправь фото и узнаешь что на нём")

@bot.message_handler(content_types=['photo'])
def photo(message):
    file_info = bot.get_file(message.photo[-1].file_id)
    file_name = file_info.file_path.split('/')[-1]
    downloaded_file = bot.download_file(file_info.file_path)
    with open("images/"+file_name, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.send_message(message.chat.id, "Work in progress it might take some time")
    class_name, score = get_class("images/"+file_name)
    if score >= 0.9:
        bot.reply_to(message, f"La race de chien présente sur votre image est un {class_name}")
    else:
        bot.reply_to(message,"Sorry but I probably don't know this breed ")

bot.polling()
