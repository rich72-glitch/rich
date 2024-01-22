import yfinance as yf

def get_low_pe_stocks(threshold=10, num_stocks=10):
    # Get a list of S&P 500 symbols
    sp500_symbols = yf.Ticker("^GSPC").history(period="1d")['Close'].index.tolist()

    low_pe_stocks = []

    for symbol in sp500_symbols:
        try:
            # Get stock information
            stock = yf.Ticker(symbol)

            # Get P/E ratio
            pe_ratio = stock.info.get('trailingPE', None)

            # If P/E ratio is available and below the threshold, add to the list
            if pe_ratio is not None and pe_ratio < threshold:
                low_pe_stocks.append((symbol, pe_ratio))

            # Break the loop if we have enough stocks
            if len(low_pe_stocks) >= num_stocks:
                break
        except Exception as e:
            print(f"Error processing {symbol}: {e}")

    return low_pe_stocks

if __name__ == "__main__":
    # Set the P/E ratio threshold and the number of stocks to retrieve
    pe_threshold = 10
    num_stocks_to_retrieve = 5

    # Get low P/E ratio stocks
    low_pe_stocks = get_low_pe_stocks(pe_threshold, num_stocks_to_retrieve)

    # Print the results
    print(f"Stocks with P/E ratio below {pe_threshold}:")
    for symbol, pe_ratio in low_pe_stocks:
        print(f"{symbol}: P/E Ratio - {pe_ratio}")
