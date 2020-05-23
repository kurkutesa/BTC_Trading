# BTC_Trading
This script will notify the user whether to `purchase` or `sale` bitcoins via automatically sending messages.
The script runs in the background after every two minutes.

**Set Limits for Trading**
- set the `lower limit` for purchasing  and `upper limit` for saling. 
> `coin_threshold_purchase, coin_threshold_sale = get_limit_value(12500,13500)`

**Run Script**
- python submit_process.py &
- disown
