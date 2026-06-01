from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = "8863865830:AAGHRVy-MgesNn-thoEx4_3XicqBBI6Vh6k"

songs = {
    "mockingbird": "https://t.me/YourChannel/25",
    "lose yourself": "https://t.me/YourChannel/30",
    "eminem":"https://t.me/music_b_rooz"
}

async def search_music(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if text in songs:
        await update.message.reply_text(
            f"🎵 لینک آهنگ:\n{songs[text]}"
        )
    else:
        await update.message.reply_text(
            "❌ آهنگ پیدا نشد"
        )

app = Application.builder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT, search_music))

print("Bot Started...")
app.run_polling()
