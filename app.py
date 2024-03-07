import os, json, requests
from resend import Resend

def get_gas_price():
    url = 'https://api.etherscan.io/api'
    params = {
        'module': 'gastracker',
        'action': 'gasoracle',
        'apikey': os.environ.get("ETHERSCAN_API_KEY")
    }

    response = requests.get(url, params=params)
    response_json = response.json()
    gas_price = response_json['result']['SafeGasPrice']
    return gas_price

def send_email(price):
    client = Resend(api_key=os.environ.get("RESEND_API_KEY"))
    client.send_email(
        to=os.environ.get("EMAIL_TO"), 
        sender=os.environ.get("EMAIL_FROM"), 
        subject=f"Ethereum Gas Price: {price} gwei", 
        text=f"The current Ethereum gas price is {price} gwei."
        )

def main():
    threshold = os.environ.get('PRICE_THRESHOLD')
    while True:
        price = get_gas_price()
        if price < threshold:
            send_email(price)

if __name__ == '__main__':
    main()
