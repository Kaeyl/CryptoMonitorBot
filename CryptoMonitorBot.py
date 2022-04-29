import json
import requests
# import datetime
import time

key_binance = "https://api.binance.com/api/v3/ticker/price?symbol="
key_binance_refresh = "https://api.binance.com/api/v3/ticker/price?symbol="


currencies_binance = ["APEAUD"]
coin_at_begin_time = 0
coin_at_end_time = 0
# begin_time = datetime.datetime.now()
# end_time = datetime.datetime(2022, 4, 29, 14, 0, 0) This is for the sleep section later in the program
# Its purpose is so set an alocated time that the next part of the code will run. Currently running on a sleep time of
# (insert) number of seconds

j = 0
k = 0

def check_currencies():
    global currencies_binance
    global coin_at_begin_time
    global j

    for i in currencies_binance:
        # completing API for request
        url1 = key_binance_refresh + currencies_binance[j]
        data = requests.get(url1)
        data = data.json()
        j = j + 1
        print(f"{data['symbol']} price is {data['price']}")
        if data['symbol'] == "APEAUD":
            coin_at_begin_time = data['price']
            coin_at_begin_time = float(coin_at_begin_time)
            coin_at_begin_time = float("{:.3f}".format(coin_at_begin_time))
            print(coin_at_begin_time)

def check_currencies_at_end():
    global key_binance_refresh
    global currencies_binance
    global coin_at_end_time
    global k

    for i in currencies_binance:
        # completing API for request
        url2 = key_binance_refresh + currencies_binance[k]
        data = requests.get(url2)
        data = data.json()
        k = k + 1
        print(f"{data['symbol']} price is {data['price']}")
        if data['symbol'] == "APEAUD":
            coin_at_end_time = data['price']
            coin_at_end_time = float(coin_at_end_time)
            coin_at_end_time = float("{:.3f}".format(coin_at_end_time))

def monitor_ape():
    global time_delay
    global name_coin_value_at_end_time
    global coin_at_begin_time
    global coin_at_end_time
    print(coin_at_begin_time)
    print(coin_at_end_time)
    if float(name_coin_value_at_end_time) > float(coin_at_begin_time):
        print("Value has increased by " + str(name_coin_value_at_end_time))
    if float(name_coin_value_at_end_time) < float(coin_at_begin_time):
        print("Value has decreased by " + str(name_coin_value_at_end_time))
    else:
        print('Nothing has changed')

check_currencies()
time.sleep(120) # Time delay before running next function
check_currencies_at_end()


# print(begin_time)
# while datetime.datetime.now()  < end_time:
#     time.sleep(1)
# print(end_time)
name_coin_value_at_end_time = coin_at_end_time - coin_at_begin_time

time.sleep(5)
monitor_ape()

