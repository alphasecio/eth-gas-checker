# eth-gas-checker
This app runs on [Railway](https://railway.app/?referralCode=alphasec), checks Ethereum gas price every hour using the [Etherscan](https://etherscan.io/) API, and sends email via [Resend](https://resend.com) if the price crosses your pre-defined threshold. Set up the following environment variables before deploying the service:
* `ETHERSCAN_API_KEY`: Etherscan API key to check Ethereum gas price; get it [here](https://etherscan.io/myapikey).
* `RESEND_API_KEY`: Resend API key to send email notifications; get it [here](https://resend.com/api-keys).
* `EMAIL_FROM`: Email address to send alert from, as configured in Resend.
* `EMAIL_TO`: Email address to send alert to, as configured in Resend.
* `PRICE_THRESHOLD`: Send email if Ethereum gas price drops below this threshold (gwei).

To deploy on [Railway](https://railway.app/?referralCode=alphasec) using a one-click template, click the button below. The template does not allow cron schedule to be defined, so set up the hourly run (`0 * * * *`) in the service settings once it's deployed.

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template/pDebYY?referralCode=alphasec)
