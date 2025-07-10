import os
import time
import pandas as pd
import ta
from binance.client import Client
from binance.enums import *
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

# Initialize Binance client
client = Client(API_KEY, API_SECRET, testnet=True)  # Use testnet=True for testing

# Trading parameters
SYMBOL = "BTCUSDT"
QUANTITY = 0.001  # Trade size (e.g., 0.001 BTC)
INTERVAL = "1h"  # 1-hour candlestick
SHORT_MA = 10  # Short moving average period
LONG_MA = 50   # Long moving average period
CHECK_INTERVAL = 60  # Check every 60 seconds

def get_historical_data(symbol, interval, limit=100):
    """Fetch historical candlestick data from Binance."""
    klines = client.get_klines(symbol=symbol, interval=interval, limit=limit)
    df = pd.DataFrame(klines, columns=[
        'timestamp', 'open', 'high', 'low', 'close', 'volume',
        'close_time', 'quote_asset_volume', 'trades', 'taker_buy_base',
        'taker_buy_quote', 'ignored'
    ])
    df['close'] = df['close'].astype(float)
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    return df

def calculate_indicators(df):
    """Calculate moving averages for trading signals."""
    df['short_ma'] = ta.trend.sma_indicator(df['close'], window=SHORT_MA)
    df['long_ma'] = ta.trend.sma_indicator(df['close'], window=LONG_MA)
    return df

def trading_strategy(df):
    """Implement a simple moving average crossover strategy."""
    last_row = df.iloc[-1]
    prev_row = df.iloc[-2]
    
    # Buy signal: Short MA crosses above Long MA
    if (prev_row['short_ma'] < prev_row['long_ma'] and 
        last_row['short_ma'] > last_row['long_ma']):
        return "BUY"
    # Sell signal: Short MA crosses below Long MA
    elif (prev_row['short_ma'] > prev_row['long_ma'] and 
          last_row['short_ma'] < last_row['long_ma']):
        return "SELL"
    return None

def place_order(symbol, quantity, side):
    """Place a market order on Binance."""
    try:
        order = client.create_order(
            symbol=symbol,
            side=side,
            type=ORDER_TYPE_MARKET,
            quantity=quantity
        )
        print(f"Order placed: {side} {quantity} {symbol}")
        return order
    except Exception as e:
        print(f"Error placing order: {e}")
        return None

def main():
    print(f"Starting AI Trading Assistant for {SYMBOL}")
    while True:
        try:
            # Fetch and prepare data
            df = get_historical_data(SYMBOL, INTERVAL)
            df = calculate_indicators(df)
            
            # Get trading signal
            signal = trading_strategy(df)
            
            # Execute trades based on signal
            if signal == "BUY":
                print("Buy signal detected")
                place_order(SYMBOL, QUANTITY, SIDE_BUY)
            elif signal == "SELL":
                print("Sell signal detected")
                place_order(SYMBOL, QUANTITY, SIDE_SELL)
            
            # Wait before next check
            time.sleep(CHECK_INTERVAL)
            
        except Exception as e:
            print(f"Error in main loop: {e}")
            time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()