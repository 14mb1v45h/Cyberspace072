# AI Trading Assistant for Binance

## Overview
This project is a Python-based AI Trading Assistant designed to automate trading on the Binance cryptocurrency exchange. It uses a simple moving average crossover strategy to generate buy and sell signals for a specified trading pair (e.g., BTC/USDT) and places market orders via the Binance API. The assistant is intended for educational purposes and should be tested thoroughly on the Binance Testnet before use with real funds.

## Features
- Fetches real-time market data using Binance API.
- Implements a moving average crossover strategy (10-period and 50-period).
- Places automated market orders based on trading signals.
- Configurable trading parameters (symbol, quantity, interval).
- Error handling for robust operation.
- Uses Binance Testnet for safe testing.

## Prerequisites
- Python 3.8+
- Binance account with API keys (Testnet or Live)
- Installed dependencies:
  - `python-binance`
  - `pandas`
  - `ta` (technical analysis library)
  - `python-dotenv`

## Installation
1. **Clone the Repository** (or download the script):
   ```bash
   git clone <repository_url>
   cd ai-trading-assistant
   ```
2. **Install Dependencies**:
   ```bash
   pip install python-binance pandas ta python-dotenv
   ```
3. **Set Up Environment Variables**:
   - Create a `.env` file in the project root:
     ```plaintext
     BINANCE_API_KEY=your_api_key
     BINANCE_API_SECRET=your_api_secret
     ```
   - Replace `your_api_key` and `your_api_secret` with your Binance Testnet API credentials (sign up at https://testnet.binance.vision/) or live API keys.

## Usage
1. **Configure Trading Parameters**:
   - Open `ai_trading_assistant.py` and modify the following variables as needed:
     - `SYMBOL`: Trading pair (e.g., "BTCUSDT").
     - `QUANTITY`: Trade size (e.g., 0.001 BTC).
     - `INTERVAL`: Candlestick interval (e.g., "1h" for 1-hour).
     - `SHORT_MA` and `LONG_MA`: Moving average periods.
     - `CHECK_INTERVAL`: Time between checks (in seconds).
   - Ensure `testnet=True` in the Binance client for testing.
2. **Run the Script**:
   ```bash
   python ai_trading_assistant.py
   ```
   The assistant will start monitoring the market, generating signals, and placing trades based on the strategy.

## Strategy
The assistant uses a **Moving Average Crossover Strategy**:
- **Buy Signal**: When the 10-period simple moving average (SMA) crosses above the 50-period SMA.
- **Sell Signal**: When the 10-period SMA crosses below the 50-period SMA.
- Trades are executed as market orders with a fixed quantity.

## Testing
- Use the Binance Testnet (set `testnet=True` in the script) to test without risking real funds.
- Obtain Testnet API keys from https://testnet.binance.vision/.
- Verify sufficient test funds for the trading pair (e.g., BTC/USDT).

## Risk Warning
- **Financial Risk**: Automated trading carries significant risks. Losses may exceed initial investments.
- **Testing**: Always test on the Binance Testnet before deploying with real funds.
- **API Limits**: Be aware of Binance API rate limits (see https://binance-docs.github.io/apidocs/spot/en/).
- **Security**: Never hardcode API keys or share them publicly.

## Potential Enhancements
- Add risk management (stop-loss, take-profit, dynamic position sizing).
- Implement advanced strategies (e.g., RSI, MACD, or machine learning models).
- Add logging for trade history and performance tracking.
- Integrate notifications (e.g., email, Telegram) for trade alerts.
- Enhance error handling for API rate limits and network issues.

## Dependencies
- `python-binance`: For Binance API interaction.
- `pandas`: For data manipulation.
- `ta`: For technical analysis indicators.
- `python-dotenv`: For secure API key management.

## License
This project is for educational purposes and provided as-is. Use at your own risk.

## Resources
- Binance API Documentation: https://binance-docs.github.io/apidocs/spot/en/
- Binance Testnet: https://testnet.binance.vision/
- Python-Binance Library: https://python-binance.readthedocs.io/