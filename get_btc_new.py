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
    cmd_trupti = """
    osascript -e 'tell application "Messages" to send "You should considering purchasing bitcoin at  %s CAD" to buddy "Trupti Desale" '""" %coin
    cmd_sopan = """
    osascript -e 'tell application "Messages" to send "You should considering purchasing bitcoin at %s CAD" to buddy "My" '""" %coin

    if coin_threshold_purchase >= coin:
        print("purchase")
        os.system(cmd_trupti)
        os.system(cmd_sopan)
    elif coin_threshold_sale <= coin:
        print("SALE")
        os.system(cmd_trupti)
        os.system(cmd_sopan)
    else:
        print("Stay put !!!")

## Try switch case

coin_threshold_purchase, coin_threshold_sale = get_limit_value(12500,13500)
coin = get_coin_value()
trade(coin_threshold_purchase,coin_threshold_sale,coin)
