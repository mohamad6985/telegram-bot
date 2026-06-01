from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, MessageHandler, filters, ContextTypes
import yt_dlp
import os

TOKEN = "8863865830:AAGHRVy-MgesNn-thoEx4_3XicqBBI6Vh6k"

CHANNEL = "https://t.me/music_b_rooz"
async def download_music(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text

    await update.message.reply_text("⏳ درحال پیدا کردن آهنگ...")

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'music.%(ext)s',
        'noplaylist': True,
        'quiet': True
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch1:{query}", download=True)

            video = info['entries'][0]

            title = video['title']
            duration = video['duration']

            file_name = "music.webm"

            keyboard = [
                [InlineKeyboardButton("📢 کانال موزیک", url=CHANNEL)]
            ]

            reply_markup = InlineKeyboardMarkup(keyboard)

            await update.message.reply_audio(
                audio=open(file_name, 'rb'),
                title=title,
                performer="Music Bot",
                caption=f"🎵 {title}\n⏱ {duration} ثانیه",
                reply_markup=reply_markup
            )

            os.remove(file_name)

    except Exception as e:
        await update.message.reply_text(f"❌ خطا:\n{e}")
      app = Application.builder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT, download_music))

print("Bot Started...")
app.run_polling(drop_pending_updates=True)
