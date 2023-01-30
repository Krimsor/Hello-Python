from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import time
from spy import *


async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'Текущие дата и время: {time.strftime("%d.%m.%Y г. %H:%M", time.localtime())}')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'/time - время\n/sum - сумма двух чисел\n/sub - разность двух чисел\n/mult - умножение двух чисел\n/div - деление двух чисел\n/help - список команд')

# Пример ввода команды: /sum 1 3
async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x + y}')

# Пример ввода команды: /sub 3 1
async def sub_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} - {y} = {x - y}')

# Пример ввода команды: /mult 3 3
async def mult_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} * {y} = {x * y}')

# Пример ввода команды: /div 12 4
async def div_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} / {y} = {x / y}')
