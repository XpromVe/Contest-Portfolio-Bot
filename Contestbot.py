from email.mime import message
import sys
import random
import telebot  # Install with: pip install pyTelegramBotAPI
import logging
#настройка логирования
logging.basicConfig(filename='logs.txt', level=logging.INFO, format='%(asctime)s - %(message)s')
def log_action(message):
    logging.info(f"User: {message.chat.first_name} (ID: {message.chat.id}) - Text: {message.text}")

from colorama import init, Fore
init(autoreset=True)

from telebot import types

# Если при запуске передать токен в консоль (python Contestbot.py ТОКЕН), 
# бот возьмет его. Иначе берет твой токен по умолчанию.
if len(sys.argv) > 1:
    TOKEN = sys.argv[1]
else:
    TOKEN = "YOUR_DEFAULT_TOKEN"

bot = telebot.TeleBot(TOKEN)

def get_main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    markup.add(
        types.KeyboardButton("👤 Обо мне"),
        types.KeyboardButton("🎯 Моя цель"),
        types.KeyboardButton("🏫 Мои курсы"),
        types.KeyboardButton("📈 Путь А → Б"),
        types.KeyboardButton("🎮 Мои хобби"),
        types.KeyboardButton("💻 Лучшие работы"),
        types.KeyboardButton("🛠 Технологии"),
        types.KeyboardButton("📞 Связь"),
        types.KeyboardButton("🏆 Достижения")
    )
    return markup

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        "Привет! 👋 Это мое интерактивное портфолио для конкурса CapEducation.\n\n"
        "Жми на кнопки ниже, чтобы узнать обо мне больше!"
    )
    bot.send_message(message.chat.id, welcome_text, reply_markup=get_main_menu())

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "👤 Обо мне":
        log_action(message)
        text = "👤 *КТО Я?*\n    Привет! Меня зовут Артур. Мне 13 лет, я учусь в 7 классе в Астане. \n    Я увлекаюсь программированием, созданием игр и изучением технологий.\n    Этот бот — мой проект, в котором я делюсь тем, что умею!"
        bot.send_message(message.chat.id, text, parse_mode='Markdown')

    elif message.text == "🎯 Моя цель":
        log_action(message)
        text = "🎯 *МОЯ ЦЕЛЬ*\n   Создавать качественные проекты, разбираться в сложных алгоритмах и стать профессиональным разработчиком. \nВ будущем планирую развиваться в GameDev и автоматизации.\n"
        bot.send_message(message.chat.id, text, parse_mode='Markdown')

    elif message.text == "🏫 Мои курсы":
        log_action(message)
        text = (
            "  🏫 *МОИ КУРСЫ*\n"
            "Я учусь в CapEducation. Мой ментор — Аида тичер. Благодаря курсам я прокачал логику и понимание кода."
        )
        bot.send_message(message.chat.id, text, parse_mode='Markdown')
        
    elif message.text == "📈 Путь А → Б":
        log_action(message)
        text = "🗺 *ПУТЬ А → Б*\n   В начале пути я писал только самые базовые вещи, а сейчас уверенно работаю со сложными словарями, циклами, ООП и создаю собственных Telegram-ботов."
        bot.send_message(message.chat.id, text, parse_mode='Markdown')
        
    elif message.text == "🎮 Мои хобби":
        log_action(message)
        text = (
            "🎮 *МОИ ХОББИ*\n"
            "Я очень разносторонний человек:\n"
            "• Вхожу в топ-10 000 игроков региона в Osu!\n"
            "• Разбираюсь в сложной механике триггеров Geometry Dash 2.2.\n"
            "• Занимаюсь воркаутом на турниках.\n"
            "• Обожаю кататься на велике по Зеленому поясу Астаны."
        )
        bot.send_message(message.chat.id, text, parse_mode='Markdown')
        
    elif message.text == "💻 Лучшие работы":
        log_action(message)
        text = (
            "💻 *ЛУЧШИЕ РАБОТЫ*\n"
            "Горжусь своими проектами:\n"
            "1. Игры на базе библиотеки Pygame.\n"
            "2. Концепты игр во вселенной Countryballs.\n"
            "3. Масштабный архитектурный архив города в Minecraft с использованием модов."
        )
        bot.send_message(message.chat.id, text, parse_mode='Markdown')
        
    elif message.text == "🛠 Технологии":
        log_action(message)
        text = (
            "🚀 *МОЙ СТЕК ТЕХНОЛОГИЙ:*\n"
            "🔹 *Язык:* Python\n"
            "🔹 *Инструменты:* Pygame, TeleBot\n"
            "🔹 *Архитектура:* SQL/JSON логирование"
        )
        bot.send_message(message.chat.id, text, parse_mode='Markdown')

    elif message.text == "📞 Связь":
        log_action(message)
        text = "📞 *СВЯЗЬ*\n    Мой GitHub: https://github.com/XpromVe\nРад любым вопросам и предложениям!"
        bot.send_message(message.chat.id, text, parse_mode='Markdown')
        
    elif message.text == "🏆 Достижения":
        log_action(message)
        photos = ['d1.jpeg', 'd2.jpeg', 'd3.jpeg', 'd4.jpeg']
        photos_path=random.choice(photos)
        with open(photos_path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo)

    else:
        log_action(message)
        bot.reply_to(message, "Используй кнопки меню, чтобы перемещаться по моему портфолио ⬇️", reply_markup=get_main_menu())
@bot.message_handler(content_types=['sticker'])
def handle_sticker(message):
    bot.send_dice(message.chat.id)
    bot.reply_to(message, "🎲!")
@bot.message_handler(func=lambda message: True)
def handle_unknown(message):
    bot.reply_to(message, "Я пока учусь понимать другие фразы. Лучше нажми на кнопку в меню 👾")

if __name__ == '__main__':
    print(Fore.GREEN + "Бот запущен! Ждем сообщений...")
    bot.infinity_polling()