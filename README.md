# 🤖 Gemini 1.5 Telegram Chatbot

A smart AI-powered Telegram bot built with Python and Google’s Gemini 1.5 Flash model. This bot can respond to user messages, provide intelligent replies, and includes interactive inline buttons — all running on Telegram.

---

## 🚀 Features

- Chat with Gemini 1.5 Flash using Google Generative AI API
- Telegram bot with async support
- Interactive commands and inline buttons
- Clean, modular code for easy customization

---

## 🧠 Powered By

- **Google Generative AI (Gemini 1.5 Flash)**
- **python-telegram-bot v20+**
- **AsyncIO / Asynchronous Python**

---

## 📂 Project Structure

```
telegram-chatbot/
│
├── main.py              # Main bot code
├── requirements.txt     # Python dependencies
├── README.md            # This file
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/jitendra-2004/telegram-chatbot.git
cd telegram-chatbot
```

### 2. Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Your API Keys

Open `main.py` and set the following:

```python
TELEGRAM_BOT_TOKEN = "your-telegram-bot-token"
GEMINI_API_KEY = "your-google-generativeai-api-key"
```

---

## ▶️ Run the Bot

```bash
python main.py
```

If everything is set up correctly, the bot will start running and respond to your messages on Telegram.

---

## 📦 requirements.txt

```txt
python-telegram-bot==20.7
google-generativeai==0.5.2
```

> You can generate this file by running:
```bash
pip freeze > requirements.txt
```

---

## 🙌 Credits

Built with passion by [@jitendra-2004](https://github.com/jitendra-2004)  

---

## 📜 License

This project is licensed under the MIT License. Feel free to use, fork, and enhance it!

---

## 📬 Connect With Me

- GitHub: [jitendra-2004](https://github.com/jitendra-2004)
- LinkedIn: [www.linkedin.com/in/jitendra-bairwa-039a3a357]
- Telegram Bot: [t.me/NewTestingJeetBot]
