# Ethereum Gas Price Checker
This app checks the Ethereum gas price every hour using the [Etherscan](https://etherscan.io/) API, and sends an email via [Resend](https://resend.com) if the price crosses your pre-defined threshold. 

Deploy the app on [Railway](https://railway.app/?referralCode=alphasec), and set the following environment variables. Once deployed, set an hourly cron schedule (`0 * * * *`) in the service settings.
* `ETHERSCAN_API_KEY`: Etherscan API key to check Ethereum gas price; get it [here](https://etherscan.io/myapikey).
* `RESEND_API_KEY`: Resend API key to send email notifications; get it [here](https://resend.com/api-keys).
* `EMAIL_FROM`: Email address to send alert from, as configured in Resend.
* `EMAIL_TO`: Email address to send alert to, as configured in Resend.
* `PRICE_THRESHOLD`: Send email if Ethereum gas price drops below this threshold (gwei).
