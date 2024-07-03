import resend
import os, json, requests

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
    resend.api_key = os.environ.get("RESEND_API_KEY")
    email = resend.Emails.send({
        "from": os.environ.get("EMAIL_FROM"),
        "to": [os.environ.get("EMAIL_TO")],
        "subject": f"Ethereum Gas Price: {price} gwei",
        "html": f"The current Ethereum gas price is {price} gwei."
    })

def main():
    threshold = os.environ.get('PRICE_THRESHOLD')
    price = get_gas_price()
    if price < threshold:
        send_email(price)

if __name__ == '__main__':
    main()
