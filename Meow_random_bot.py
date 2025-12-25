#pip install pyTelegramBotAPI в терминал

from telebot import TeleBot, types
import random

TOKEN = ""  #https://telegram.me/BotFather для получения TOKEN создаем бота и вставляем в скобки
bot = TeleBot(TOKEN)

meow = [
    "Мяу!",
    "Мяяяууу!",
    "Мяв",
    "Мур!",
    "Мряв!",
    "Мрр",
    "Мрр мяу",
    "Муррр"
]

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(types.KeyboardButton("Давай поговорим"))

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.send_message(message.chat.id, "Мяу", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == "Давай поговорим")
def random_mewing(message):
    count = random.randint(1, len(meow))
    words = random.sample(meow, count)
    text = " ".join(words)
    bot.send_message(message.chat.id, text, reply_markup=keyboard)

bot.infinity_polling()