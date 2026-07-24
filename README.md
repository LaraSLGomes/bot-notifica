# 🎟️ Ticketmaster Telegram Notification Bot

A lightweight Python script that monitors ticket availability for events on Ticketmaster and sends real-time notifications directly to your Telegram chat.

---

## ✨ Features

- **Automated Monitoring:** Checks ticket availability at customizable time intervals.
- **Instant Alerts:** Sends a Telegram notification with a direct link as soon as tickets are detected.
- **Duplicate Prevention:** Tracks notification state to avoid spamming your chat while tickets remain available.
- **Secure Configuration:** Uses environment variables (`.env`) to keep your Telegram bot token and credentials safe.

---

## 📋 Prerequisites

- **Python 3.9+**
- A **Telegram Bot Token** (obtained via [@BotFather](https://t.me/BotFather))
- Your **Telegram Chat ID** (obtained via [@userinfobot](https://t.me/userinfobot))

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name
```

### 2. Set Up a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuration

1. Create a `.env` file in the root directory of the project:

   ```bash
   touch .env
   ```

2. Add your Telegram credentials to the `.env` file:

   ```env
   TELEGRAM_TOKEN=your_bot_token_here
   CHAT_ID=your_chat_id_here
   ```

3. Update the event URL in `main.py`:

   ```python
   URL_EVENTO = "[https://www.ticketmaster.com.br/event/your-event-link](https://www.ticketmaster.com.br/event/your-event-link)"
   ```

---

## 🏃 Usage

Run the bot script:

```bash
python main.py
```

---

## 📁 Project Structure

```text
├── .env                  # Environment variables (git-ignored)
├── .env.example          # Template for environment variables
├── .gitignore            # Git ignore rules
├── main.py               # Main bot application logic
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## ⚠️ Disclaimer

This project is intended for personal and educational use only. Please respect Ticketmaster's terms of service and avoid setting aggressively low polling intervals to prevent rate limiting or IP blocks.