import yfinance as yf
import pandas as pd


def get_price_data(tickers, start, end):

    data = yf.download(
        tickers,
        start=start,
        end=end,
        group_by="ticker",
        auto_adjust=True
    )

    frames = []

    for t in tickers:
        df = data[t][["Close"]].copy()
        df["ticker"] = t
        df = df.reset_index()
        frames.append(df)

    return pd.concat(frames)


def add_returns(df):

    df = df.sort_values(["ticker", "Date"])

    df["ret_1d"] = df.groupby("ticker")["Close"].pct_change()
    df["ret_21d"] = df.groupby("ticker")["Close"].pct_change(21)

    return df
