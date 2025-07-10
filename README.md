# NSE Option Chain Telegram Bot

This is a Telegram bot that fetches live NSE option chain data and gives suggestions for trending call options.

### 🔧 Commands

- `/start` – Welcome message
- `/trending` – Shows top picks based on Open Interest

### 🛠 How to Deploy on Render

1. Fork/upload this repo to your GitHub
2. Go to [https://render.com](https://render.com)
3. Click "New Web Service"
4. Fill in:
   - Build command: `pip install -r requirements.txt`
   - Start command: `python main.py`
5. Add environment variable:
   - Key: `TELEGRAM_BOT_TOKEN`
   - Value: (your token from @BotFather)

Click "Create Web Service" and your bot is live!