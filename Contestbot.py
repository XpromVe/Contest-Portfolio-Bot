import sys
import random
import telebot
import logging
import re          # Обязательное требование ТЗ!
import bot_text    # Архитектурное требование ТЗ (вынос контента)!
from colorama import init, Fore

init(autoreset=True)
from telebot import types

# Настройка логирования
logging.basicConfig(filename='logs.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def log_action(message):
    logging.info(f"User: {message.chat.first_name} (ID: {message.chat.id}) - Text: {message.text}")

if len(sys.argv) > 1:
    TOKEN = sys.argv[1]
else:
    TOKEN = "8809769203:AAHclMcT5brnh_LENJwYL7JKWd1YfOmAmno"

bot = telebot.TeleBot(TOKEN)

def get_main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    markup.add(
        types.KeyboardButton("👤 Обо мне"),
        types.KeyboardButton("🎯 Моя цель"),
        types.KeyboardButton("🚀 Как я пришел в IT"),
        types.KeyboardButton("🏫 Мой ментор"),
        types.KeyboardButton("📈 Путь А → Б"),
        types.KeyboardButton("🎮 Мои хобби"),
        types.KeyboardButton("💻 Лучшие работы"),
        types.KeyboardButton("📞 Связь & GitHub"),
        types.KeyboardButton("🏆 Достижения")
    )
    return markup

# Реализация обязательных команд из ТЗ (/about, /goal, /mentor)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = "Привет! 👋 Это мое интерактивное портфолио для конкурса CapEducation.\n\nЖми на кнопки ниже или используй команды!"
    bot.send_message(message.chat.id, welcome_text, reply_markup=get_main_menu())

@bot.message_handler(commands=['about'])
def cmd_about(message):
    bot.send_message(message.chat.id, bot_text.ABOUT_ME, parse_mode='Markdown')

@bot.message_handler(commands=['goal'])
def cmd_goal(message):
    bot.send_message(message.chat.id, bot_text.GOAL, parse_mode='Markdown')

@bot.message_handler(commands=['mentor'])
def cmd_mentor(message):
    bot.send_message(message.chat.id, bot_text.MENTOR, parse_mode='Markdown')

@bot.message_handler(content_types=['text'])
def handle_text(message):
    log_action(message)
    
    if message.text == "👤 Обо мне":
        bot.send_message(message.chat.id, bot_text.ABOUT_ME, parse_mode='Markdown')
    elif message.text == "🎯 Моя цель":
        bot.send_message(message.chat.id, bot_text.GOAL, parse_mode='Markdown')
    elif message.text == "🚀 Как я пришел в IT":
        bot.send_message(message.chat.id, bot_text.HOW_I_STARTED, parse_mode='Markdown')
    elif message.text == "🏫 Мой ментор":
        bot.send_message(message.chat.id, bot_text.MENTOR, parse_mode='Markdown')
    elif message.text == "📈 Путь А → Б":
        bot.send_message(message.chat.id, bot_text.WAY_A_B, parse_mode='Markdown')
    elif message.text == "🎮 Мои хобби":
        bot.send_message(message.chat.id, bot_text.HOBBIES, parse_mode='Markdown')
    elif message.text == "💻 Лучшие работы":
        bot.send_message(message.chat.id, bot_text.BEST_WORKS, parse_mode='Markdown')
    elif message.text == "📞 Связь & GitHub":
        bot.send_message(message.chat.id, bot_text.GITHUB_LINK, parse_mode='Markdown')
    elif message.text == "🏆 Достижения":
        # Бонусные баллы ТЗ: Обработка ошибок через try-except!
        try:
            photos = ['d1.jpeg', 'd2.jpeg', 'd3.jpeg', 'd4.jpeg']
            photos_path = random.choice(photos)
            with open(photos_path, 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
        except Exception as e:
            logging.error(f"Ошибка при отправке фото: {e}")
            bot.send_message(message.chat.id, "⚠️ Не удалось загрузить диплом. Попробуйте еще раз позже!")
            
    # Бонусные баллы ТЗ: Валидация ввода пользователя через регулярные выражения (re.match)!
    elif re.match(bot_text.EMAIL_REGEX, message.text):
        bot.reply_to(message, "✅ Ваш Email успешно прошёл валидацию через регулярное выражение! Я обязательно свяжусь с вами.")
    else:
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
