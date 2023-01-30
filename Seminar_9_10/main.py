from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

app = ApplicationBuilder().token("5971721023:AAH1mfMYNbx1YM6oQKCpZVI3CghY76594es").build()

app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("sub", sub_command))
app.add_handler(CommandHandler("mult", mult_command))
app.add_handler(CommandHandler("div", div_command))

print('Server start')

app.run_polling()