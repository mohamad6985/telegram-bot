import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
import yt_dlp

TOKEN = os.getenv("8863865830:AAGHRVy-MgesNn-thoEx4_3XicqBBI6Vh6k")


def get_audio_url(query):
    ydl_opts = {
        "format": "bestaudio/best",
        "noplaylist": True,
        "quiet": True,
        "default_search": "ytsearch1",
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(query, download=False)
        if "entries" in info:
            info = info["entries"][0]

        return info["url"], info.get("title", "audio")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎧 اسم آهنگ رو بفرست")


async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text

    await update.message.reply_text("⏳ در حال پیدا کردن...")

    try:
        url, title = get_audio_url(query)

        await update.message.reply_audio(
            audio=url,
            title=title
        )

    except:
        await update.message.reply_text("❌ خطا دوباره تلاش کن")


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))

app.run_polling()
