# **Menen Bári Suraidy – Telegram Q&A Bot** 🤖

[![Python](https://img.shields.io/badge/Python-3.11+-blue)](https://www.python.org/)  
[![Telegram](https://img.shields.io/badge/Telegram-Bot-blue)](https://core.telegram.org/bots)  
[![OpenAI](https://img.shields.io/badge/OpenAI-API-red)](https://openai.com/)  

**Menen Bári Suraidy** is a **smart AI-powered Telegram bot** that answers questions in group and private chats. Built with **Telethon** and **OpenAI**, it’s fast, reliable, and user-friendly.

---

## **🚀 Features**
- ✅ **Instant AI-powered answers**  
- ✅ Works in **group chats** and **private chats**  
- ✅ **Easy to setup and run**  
- ✅ Modern and scalable architecture  

---

## **🔧 Requirements**
Before running the bot, you need:  
- **Telegram Bot Token**  
- **Telegram API ID & API Hash** (for Telethon)  
- **OpenAI API Key**  

> Store them in a `.env` file (see example below).

---

## **⚡ Setup**

1. **Clone the repository**  
```bash
git clone https://github.com/beysen-nr/menen-bari-suraid.git
cd MenenBariSuraid
```
2. **Install dependecies**  
```bash
pip install -r requirements.txt
```
3. **Create .env file** in the root of your project and add your credentials
```env
TELEGRAM_API_ID=your_telegram_api_id
TELEGRAM_API_HASH=your_telegram_api_hash
BOT_TOKEN=your_telegram_bot_token
OPENAI_API_KEY=your_openai_api_key
```
> ⚠️ Do not commit .env to GitHub
4. **Run the bot** in the root of your project and add your credentials
```python
python3 main.py
```

---

## **💬 Usage**

● Ask a group chat:
```bash
@menenbarisuraidybot Where does power lie, brother?
```
● Use it by replying:
```bash
@menenbarisuraidybot What's he talking about?
```
● Or to fact-check by replying:
```bash
@menenbarisuraidybot fact-check
```

---

## **🎨 Customization**
● Edit main.py to adjust bot behavior or responses.
● Add features like **multi-language support, logging**, or custom command shortcuts.

---

## **📄 License**

● **MIT License** – free to use, modify, and share.

<img width="600" height="700" alt="image" src="https://github.com/user-attachments/assets/9b95723d-8f07-4d7b-be76-4ca8c84d6c56" />



