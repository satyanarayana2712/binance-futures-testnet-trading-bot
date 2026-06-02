# Binance Futures Testnet Trading Bot

## Overview

A Python CLI application that places Market and Limit orders on Binance Futures Testnet (USDT-M).

## Features

* Place MARKET orders
* Place LIMIT orders
* BUY and SELL support
* Input validation
* Logging of requests, responses, and errors
* Structured project architecture
* Binance Futures Testnet integration

## Project Structure

trading_bot/

├── bot/

│ ├── client.py

│ ├── orders.py

│ ├── validators.py

│ └── logging_config.py

├── logs/

├── cli.py

├── .env

├── requirements.txt

└── README.md

## Installation

Create virtual environment:

python -m venv venv

Activate:

Windows:

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

## Environment Variables

Create a .env file:

API_KEY=your_api_key

API_SECRET=your_secret_key

## Usage

### Market Order

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

### Limit Order

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 200000

## Validation Examples

Invalid Side:

python cli.py --symbol BTCUSDT --side ABC --type MARKET --quantity 0.001

Output:

FAILED

Side must be BUY or SELL

## Logging

Logs are stored in:

logs/trading.log

## Assumptions

* Binance Futures Testnet account is active.
* API credentials are valid.
* Internet connection is available.
## Screenshots

See the screenshots folder for:
- Market Order Success
- Limit Order Success
- Validation Example
- Logging Output
- Project Structure

## Author

Satyanarayana Alla
