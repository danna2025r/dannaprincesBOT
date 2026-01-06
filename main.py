import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Tu token se toma de la variable de entorno BOT_TOKEN
TOKEN = os.environ.get("BOT_TOKEN")

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hola 💖 soy el bot de la señorita Danna 👑✨")

def main():
    # Crea la aplicación del bot
    app = ApplicationBuilder().token(TOKEN).build()
    # Añade el handler del comando /start
    app.add_handler(CommandHandler("start", start))
    # Ejecuta el bot
    app.run_polling()

if __name__ == "__main__":
    main()
