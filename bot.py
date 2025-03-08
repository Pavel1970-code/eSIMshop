import telebot
from telebot import types

# 🔹 Тестовый API-токен бота
BOT_TOKEN = "7914550293:AAHrekx5TYwyZ-t2X1gzCrqhjS6crSSWOrU"

# 🔹 Ссылка на WebApp (Telegram Mini App) – исправленная!
APP_URL = "https://t.me/globesimbot/GlobeSimBotApp"

# 🔹 Создаём бота
bot = telebot.TeleBot(BOT_TOKEN)

# 📌 Обработчик команды /start
@bot.message_handler(commands=["start"])
def start_command(message: types.Message):
    # 🔹 WebApp внутри Telegram (правильный формат!)
    web_app_info = types.WebAppInfo(url=APP_URL)

    # 🔹 Клавиатура с кнопкой для открытия WebApp
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu_button = types.KeyboardButton(text="🛒 Перейти в магазин", web_app=web_app_info)
    markup.add(menu_button)

    # 🔹 Отправляем сообщение с кнопкой
    bot.send_message(
        message.chat.id,
        "👋 Добро пожаловать в eSIM-магазин!\n\nНажмите кнопку ниже, чтобы открыть магазин прямо в Telegram.",
        reply_markup=markup
    )

# 🚀 Запуск бота
bot.polling()
