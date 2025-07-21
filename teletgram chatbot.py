from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, CommandHandler, ContextTypes,
    MessageHandler, filters, CallbackQueryHandler
)
import google.generativeai as genai

# === CONFIGURATION ===
TELEGRAM_BOT_TOKEN = "enter TELEGRAM_BOT token"
GEMINI_API_KEY = "enter GEMINI_API_KEY"

# === Gemini 1.5 Setup ===
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# === COMMAND HANDLERS ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("Say Hello 👋", callback_data='hello')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "👋 Hi! I'm your Smart Telegram Bot.\nType anything or use commands:\n/help /hello",
        reply_markup=reply_markup
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛠 Available commands:\n/start - Welcome\n/help - Show help\n/hello - Say hello\nYou can also send me any question!"
    )

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.effective_user.first_name
    await update.message.reply_text(f"Hello {name}! How can I assist you today? 😊")

# === INLINE BUTTON CALLBACK ===
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "hello":
        await query.edit_message_text(text="👋 Hello from your smart bot!")

# === CHAT WITH GEMINI 1.5 ===
async def chat_with_gemini_15(user_input):
    try:
        convo = model.start_chat(history=[])
        response = convo.send_message(user_input)
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Gemini Error: {str(e)}"

# === HANDLE USER MESSAGES ===
async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_msg = update.message.text
    await update.message.reply_text("🤖 Thinking...")
    reply = await chat_with_gemini_15(user_msg)
    await update.message.reply_text(reply)

# === MAIN FUNCTION ===
if __name__ == '__main__':
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    # Register commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("hello", hello))

    # Register message handler for non-command texts
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    # Inline buttons
    app.add_handler(CallbackQueryHandler(button_handler))

    print("✅ Bot is running using Gemini 1.5...")
    app.run_polling()
