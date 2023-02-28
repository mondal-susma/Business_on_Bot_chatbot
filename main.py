import os
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Load environment variables from .env file
load_dotenv()

# Define basic math operations functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

# Define command handlers
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a math bot! Type /help to see what I can do.")

def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I can perform basic math operations. Here are the commands you can use:\n/add num1 num2\n/subtract num1 num2\n/multiply num1 num2\n/divide num1 num2")

def handle_math(update, context):
    command = update.message.text.split()[0]
    if command == "/add":
        num1 = float(update.message.text.split()[1])
        num2 = float(update.message.text.split()[2])
        result = add(num1, num2)
        context.bot.send_message(chat_id=update.effective_chat.id, text=result)
    elif command == "/subtract":
        num1 = float(update.message.text.split()[1])
        num2 = float(update.message.text.split()[2])
        result = subtract(num1, num2)
        context.bot.send_message(chat_id=update.effective_chat.id, text=result)
    elif command == "/multiply":
        num1 = float(update.message.text.split()[1])
        num2 = float(update.message.text.split()[2])
        result = multiply(num1, num2)
        context.bot.send_message(chat_id=update.effective_chat.id, text=result)
    elif command == "/divide":
        num1 = float(update.message.text.split()[1])
        num2 = float(update.message.text.split()[2])
        result = divide(num1, num2)
        context.bot.send_message(chat_id=update.effective_chat.id, text=result)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="I'm sorry, I don't understand that command. Type /help to see what I can do.")

# Set up the updater and dispatcher
updater = Updater(token=os.getenv("TELEGRAM_BOT_TOKEN"), use_context=True)
dispatcher = updater.dispatcher

# Add command and message handlers
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("help", help))
dispatcher.add_handler(MessageHandler(Filters.text & (Filters.command("/add") | Filters.command("/subtract") | Filters.command("/multiply") | Filters.command("/divide")), handle_math))

# Start the bot
updater.start_polling()
