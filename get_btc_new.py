from pycoingecko import CoinGeckoAPI
import os
cg = CoinGeckoAPI()

def get_limit_value(coin_threshold_purchase,coin_threshold_sale):
    return (coin_threshold_purchase, coin_threshold_sale)


def get_coin_value():
    val = cg.get_price(ids='bitcoin', vs_currencies='cad')
    coin = val['bitcoin']['cad']
    return coin


def trade(coin_threshold_purchase,coin_threshold_sale,coin):
    send_message = """
    osascript -e 'tell application "Messages" to send "You should considering purchasing bitcoin at  %s CAD" to buddy "CONTACT_NAME_TO_SEND_MESSAGE" '""" %coin

    if coin_threshold_purchase >= coin:
        print("purchase BTC !!")
        os.system(send_message)
    elif coin_threshold_sale <= coin:
        print("Sale BTC !!")
        os.system(send_message)
    else:
        print("Stay Put !!")


# Set limits for trading
coin_threshold_purchase, coin_threshold_sale = get_limit_value(12500,13500)
#
coin = get_coin_value()
trade(coin_threshold_purchase,coin_threshold_sale,coin)
