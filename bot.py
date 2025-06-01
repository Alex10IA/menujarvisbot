import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

BOT_TOKEN = os.environ["BOT_TOKEN"]
SHEETS_URL = os.environ["SHEETS_URL"]

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    if not text:
        await update.message.reply_text("❌ Não entendi nada.")
        return

    payload = {"input": text}
    try:
        requests.post(SHEETS_URL, json=payload)
        await update.message.reply_text("✅ Registado com sucesso no JARVIS.")
    except Exception as e:
        await update.message.reply_text(f"Erro ao enviar: {e}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))
    app.run_polling()
