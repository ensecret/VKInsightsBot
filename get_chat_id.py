from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TELEGRAM_TOKEN = '7554028626:AAHP7iEcgXrNmM9UwkNTM4TJly4NRpCAc_I'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await update.message.reply_text(f"Ваш Chat ID: {chat_id}")
    # Сохраняем chat_id в файл
    with open("chat_id.txt", "w") as f:
        f.write(str(chat_id))
    print(f"Chat ID {chat_id} сохранен в chat_id.txt")


def main():
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    start_handler = CommandHandler("start", start)
    application.add_handler(start_handler)

    print("Запустите скрипт и отправьте команду /start вашему боту в Telegram.")
    application.run_polling()

if __name__ == '__main__':
    main()
