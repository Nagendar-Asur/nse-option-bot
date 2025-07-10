from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)
import datetime
import os
from scraper import fetch_nse_option_chain
from predictor import get_suggestions

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome! Use /trending to get tomorrow’s top option picks.")

async def trending(update: Update, context: ContextTypes.DEFAULT_TYPE):
    stocks = ["RELIANCE", "INFY", "HDFCBANK", "TCS", "ICICIBANK"]
    message = "📊 Top Option Picks for Tomorrow ({}):\n".format(
        (datetime.date.today() + datetime.timedelta(days=1)).strftime("%d-%b-%Y")
    )

    for symbol in stocks:
        chain = fetch_nse_option_chain(symbol)
        suggestion = get_suggestions(symbol, chain)
        if suggestion:
            message += f"\n🔹 {symbol}: {suggestion}"

    await update.message.reply_text(message)

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("trending", trending))
    app.run_polling()
