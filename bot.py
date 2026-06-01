from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = "8863865830:AAGHRVy-MgesNn-thoEx4_3XicqBBI6Vh6k"

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text(f"تو گفتی: {text}")

app = Application.builder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT, reply))

print("Bot Started...")
app.run_polling(drop_pending_updates=True)
