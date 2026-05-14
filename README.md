# Telegram Translator Bot

An asynchronous Telegram translator bot built with Python and `aiogram`. The bot accepts `/translate <text>` and returns a translation via an inline keyboard for target languages.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![aiogram](https://img.shields.io/badge/aiogram-v3.0%2B-blue?style=for-the-badge&logo=telegram)
![aiohttp](https://img.shields.io/badge/aiohttp-async-blue?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

## 🛠️ Tech Stack

- `aiogram` — asynchronous framework for Telegram bots
- `aiohttp` — async HTTP client for translation API calls
- `python-dotenv` — environment variable management via `.env`

## 🚀 Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/telegram-translator-bot.git
cd telegram-translator-bot
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
TOKEN=your_telegram_token_from_botfather
```

> 💡 **How to get a token?**
> 1. Open Telegram and find the **@BotFather** bot
> 2. Send the `/newbot` command
> 3. Follow the instructions and copy your token

### 5. Run the bot

```bash
python main.py
```

## 📱 Usage

1. Open your bot in Telegram
2. Send `/start`
3. Send the command:

```text
/translate Hello, how are you?
```

4. Choose the target language from the inline buttons

## 🏗️ Project structure

```text
telegram-translator-bot/
├── handlers/
│   └── routes.py        # Command handlers and routing logic
├── middleware/
│   └── rate_limit.py    # Rate limiting middleware (if implemented)
├── .env.example         # Example environment file
├── .gitignore           # Git ignore rules
├── main.py              # Main bot file with dispatcher setup
└── requirements.txt     # Project dependencies
```

## 📖 Documentation

- [aiogram Documentation](https://docs.aiogram.dev/)
- [Telegram Bot API](https://core.telegram.org/bots/api)

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
