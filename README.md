# 💱 Crypto Price Bot with Chainlit

A simple interactive chatbot built using **[Chainlit](https://www.chainlit.io/)** and **Binance API** to fetch real-time cryptocurrency prices.

---

## 🚀 Features

- 🔟 Get top 10 crypto prices on Binance
- 💰 Fetch the price of a specific cryptocurrency (e.g., BTC, ETH, SOL)
- 🔄 Auto-corrects to `USDT` pairs (e.g., `BTC` → `BTCUSDT`)
- 🧠 Smart message handling with Chainlit
- 🌓 Dark mode UI built-in

---

## 🛠️ Tech Stack

- [Chainlit](https://www.chainlit.io/)
- Python 3.8+
- [Binance Public API](https://github.com/binance/binance-spot-api-docs)

---

## 🧪 Usage

### 1. Clone the repo
```bash
git clone https://github.com/your-username/chainlit-crypto-bot.git
cd chainlit-crypto-bot
pip install -r requirements.txt
chainlit
requests
chainlit run main.py

