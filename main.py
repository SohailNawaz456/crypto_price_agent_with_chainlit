import chainlit as cl
import requests

@cl.on_message
async def main(message: cl.Message):
    user_input = message.content.strip().lower()

    if user_input == "top10":
        await show_top_10_prices()
    else:
        await show_specific_coin_price(user_input)

async def show_top_10_prices():
    url = "https://api.binance.com/api/v3/ticker/price"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        content = "🔟 **Top 10 Crypto Coin Prices on Binance:**\n\n"
        for coin in data[:10]:
            content += f"🔷 `{coin['symbol']}`: **{coin['price']}** USDT\n"

        await cl.Message(content=content).send()

    except requests.exceptions.RequestException as e:
        await cl.Message(content=f"❌ Error fetching top 10 coin prices: {e}").send()

async def show_specific_coin_price(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol.upper()}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        await cl.Message(
            content=f"💰 `{data['symbol']}` price is **{data['price']}** USDT"
        ).send()
    except requests.exceptions.RequestException as e:
        await cl.Message(content=f"❌ Error fetching coin price: {e}").send()
