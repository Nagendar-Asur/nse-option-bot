import requests
import time

def fetch_nse_option_chain(symbol):
    url = f"https://www.nseindia.com/api/option-chain-equities?symbol={symbol.upper()}"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json",
        "Referer": "https://www.nseindia.com/option-chain",
    }

    session = requests.Session()
    try:
        session.get("https://www.nseindia.com", headers=headers, timeout=5)
        time.sleep(1)
        response = session.get(url, headers=headers, timeout=10)
        data = response.json()
        return data['records']['data']
    except Exception as e:
        print("Error fetching NSE data:", e)
        return []