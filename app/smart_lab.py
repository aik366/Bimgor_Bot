import json
import asyncio
import httpx


async def get_price_async(ticker: str):
    """Асинхронно получить текущую цену и изменение за день в %."""
    url = f"https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR/securities/{ticker}.json"

    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(url)
            response.raise_for_status()
            data = response.json()
    except httpx.RequestError:
        return None

    if "marketdata" not in data:
        return None

    columns = data["marketdata"]["columns"]
    rows = data["marketdata"]["data"]

    last_col = None
    last_to_prev_col = None
    for i, col in enumerate(columns):
        if col == "LAST":
            last_col = i
        elif col == "LASTTOPREVPRICE":
            last_to_prev_col = i

    if last_col is None or not rows:
        return None

    price = rows[0][last_col]
    # LASTTOPREVPRICE — готовый процент изменения
    change_pct = rows[0][last_to_prev_col] if last_to_prev_col else 0

    return (float(price), float(change_pct)) if price else None


async def get_index_async():
    """Асинхронно получить значение индекса IMOEX и изменение за день в %."""
    url = "https://iss.moex.com/iss/engines/stock/markets/index/securities/IMOEX.json?boardid=INDEX"

    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(url)
            response.raise_for_status()
            data = response.json()
    except httpx.RequestError:
        return None

    if "marketdata" not in data:
        return None

    columns = data["marketdata"]["columns"]
    rows = data["marketdata"]["data"]

    last_value_col = None
    change_pct_col = None
    for i, col in enumerate(columns):
        if col == "CURRENTVALUE":
            last_value_col = i
        elif col == "LASTCHANGEPRC":
            change_pct_col = i

    if last_value_col is None or not rows:
        return None
    print(columns, rows)
    value = rows[0][last_value_col]
    change_pct = rows[0][change_pct_col] if change_pct_col else 0

    return (float(value), float(change_pct)) if value else None


def load_portfolio_json(filepath: str = "DATA/ticker_json.json") -> dict:
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def get_portfolio_from_json(filepath: str = "DATA/ticker_json.json") -> dict:
    """Загрузить PORTFOLIO {ticker: quantity} из JSON файла."""
    data = load_portfolio_json(filepath)
    portfolio = {}
    for ticker, values in data.items():
        if ticker != "IMOEX":
            portfolio[ticker] = values[0]  # количество
    return portfolio


# # Ваши акции: тикер -> количество штук (загружается из ticker_json.json)
# PORTFOLIO = get_portfolio_from_json()


async def save_portfolio_json_async(filepath: str = "DATA/ticker_json.json") -> None:
    """
    Сохранить портфель в JSON файл.

    Формат: {ticker: [quantity, price, change_pct, day_value, value], ...}
    """
    stocks = []

    for ticker, quantity in get_portfolio_from_json().items():
        price_data = await get_price_async(ticker)
        if price_data:
            price, change_pct = price_data
            value = price * quantity
            day_value = value * (change_pct / 100)
            stocks.append((ticker, [
                quantity,
                round(price, 2),
                round(change_pct, 2),
                round(day_value, 2),
                round(value, 2),
            ]))
        else:
            stocks.append((ticker, [quantity, None, None, None, None]))

    # Сортируем по стоимости (value) по убыванию
    stocks.sort(key=lambda x: x[1][4] if x[1][4] is not None else 0, reverse=True)

    portfolio = dict(stocks)

    # Добавляем индекс IMOEX
    index_data = await get_index_async()
    if index_data:
        index_value, index_change = index_data
        portfolio["IMOEX"] = [
            round(index_value, 2),
            round(index_change, 2),
        ]

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(portfolio, f, indent=2, ensure_ascii=False)


async def viev_ticers(filepath: str = "DATA/ticker_json.json") -> None:
    """Вывести портфель из JSON файла в консоль."""
    await save_portfolio_json_async()
    portfolio = load_portfolio_json(filepath)
    moex_str, investment, dividends, comisions, profit = "", 0.0, 0.0, 0.0, 0.0

    if "IMOEX" in portfolio:
        index_value, index_change = portfolio["IMOEX"]
        sign = "+" if index_change >= 0 else ""
        moex_str += f"IMOEX: {index_value:.2f} ({sign}{index_change:.2f}%)\n\n"
    if "INVESTMENT" in portfolio:
        investment = portfolio["INVESTMENT"][0]
        # moex_str += f"INVESTMENT: {investment:_.0f}\n"
    if "DIVIDENDS" in portfolio:
        dividends = portfolio["DIVIDENDS"][0]
        # moex_str += f"DIVIDENDS: {dividends:_.0f}\n"
    if "COMISIONS" in portfolio:
        comisions = portfolio["COMISIONS"][0]
        # moex_str += f"COMISIONS: {portfolio['COMISIONS'][0]:_.0f}\n"
    if "PROFIT" in portfolio:
        profit = portfolio["PROFIT"][0]
        # moex_str += f"PROFIT: {portfolio['PROFIT'][0]:_.0f}\n\n"
        
    total = 0.0
    total_day_change = 0.0
    for ticker, data in portfolio.items():
        if ticker in ("IMOEX", "INVESTMENT", "DIVIDENDS", "COMISIONS", "PROFIT"):
            continue
        quantity, price, change_pct, day_value, value = data
        if price is not None:
            sign = "+" if change_pct >= 0 else ""
            moex_str += f"{ticker}: {quantity}|{price}|{sign}{change_pct}%|{day_value:.0f}|{value:.0f}\n"
            total += value
            total_day_change += day_value
        else:
            moex_str += f"{ticker}: {quantity}|N/A|N/A|N/A|N/A\n"

    # Доход/убыток за день
    day_sign = "+" if total_day_change >= 0 else ""
    moex_str += f"\nЗа день: {day_sign}{total_day_change:_.0f}\n"
    moex_str += f"Итого: {total:_.0f}\n\n"
    
    my_portfolio = total - investment - comisions + dividends 
    portfolio_sign = "+" if my_portfolio >= 0 else ""
    moex_str += f"Ваш портфель: {portfolio_sign}{my_portfolio:_.0f}\n"

    return moex_str


def read_json_file(filename):
    with open(filename, encoding='utf-8') as file:
        return json.load(file)


def write_to_json_file(filename, collection):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(collection, file, ensure_ascii=False, indent=2)


def update_json_file(ticker, volume):
    my_json = read_json_file("DATA/ticker_json.json")
    my_json[ticker] = [int(volume)]
    write_to_json_file("DATA/ticker_json.json", my_json)


def delete_json_file(ticker):
    my_json = read_json_file("DATA/ticker_json.json")
    if ticker in my_json:
        del my_json[ticker]
        write_to_json_file("DATA/ticker_json.json", my_json)




    # value_sorted = dict(sorted(my_dict.items(), key=lambda x: x[1][3], reverse=True))
    # for ticker, v in value_sorted.items():
    #     my_tickers += f"{ticker} = {v[0]}({v[1]}) {v[2]} ({v[3]:,})\n"
    # return f"{my_tickers}\nИтого: {int(summ):,} ({(int(summ) - my_nested):,})"


# Пример использования
if __name__ == "__main__":
    print(viev_ticers())
