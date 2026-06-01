from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
from urllib.parse import quote

TOKEN = "8863865830:AAGHRVy-MgesNn-thoEx4_3XicqBBI6Vh6k"

async def search_music(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    query = quote(text)
    url = f"https://www.youtube.com/results?search_query={query}"

    await update.message.reply_text(
        f"🎵 نتیجه سرچ:\n{url}"
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT, search_music))

print("Bot Started...")
app.run_polling(drop_pending_updates=True)
