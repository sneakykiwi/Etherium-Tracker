import json
import time
import requests

def shapeshift():
    print('Getting ETH info for [Shapeshift.io]')
    eth_pairs = open("shapeshiftpairs.txt","r")
    time.sleep(1)
    for pair in eth_pairs:
        pair = pair.split('"')[1]
        pair = pair.split('"')[0]
        current_pair = pair.split('ETH')
        current_pair = pair.split('_')
        if current_pair[0] == 'ETH':
            #print(current_pair[0])
            final_pair = current_pair[1]
            url = 'https://www.ShapeShift.io/limit/' + pair
            info = requests.get(url=url)
            json_data = json.loads(info.text)
            print(final_pair,'has a rate of', '1 ETH = ','[', json_data['rate'], final_pair, ']', '| Inverse Rate is ','1 ', final_pair, '=','[', float(1/json_data['rate']),'ETH ]')
            jsondata = open('shapeshiftdata.json', 'a')
            jsondata.write(str(json_data))
#shapeshift()
def coinstwitch():
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    url2 = "https://api.coinswitch.co/v2/coins"
    headers2 = {'x-api-key': "Yllz4CvDVh7wz8kmzNz2a8oJ8SgpdheTa74UgqHT",'x-user-ip': "78.87.9.46"}
    coins = requests.request("GET", url2, headers=headers2)
    json_coins = json.loads(coins.text)
    coinswitchdata = open('coinstwitchdata.json', 'a')
    url = "https://api.coinswitch.co/v2/rate"
    for section in json_coins['data']:
        coinswitchdata.write(section['symbol'] + '\n')
        symbol = section['symbol']
        payload_dict = {"depositCoin":"eth", "destinationCoin": symbol}
        #print(str(payload_dict))
        #print(payload_dict['destinationCoin'])
        headers = {'content-type': 'application/json', 'x-api-key': 'Yllz4CvDVh7wz8kmzNz2a8oJ8SgpdheTa74UgqHT','x-user-ip': '78.87.9.46'}
        info = requests.request("POST", url, json=payload_dict, headers=headers)
        #if info.text['msg'].split('eth')[0] != 'Invalid trade pair':
        try:
            symbol = symbol.upper()
            json_data = json.loads(info.text)
            #print(json_data['data']['rate'])
            print(symbol, 'has a rate of', '1 ETH = ', '[', json_data['data']['rate'], symbol, ']', '| Inverse Rate is ', '1 ', symbol, '=', '[', float(1 / json_data['data']['rate']), 'ETH ]')
        except:
            json_data = json.loads(info.text)
            if json_data['msg'][18:] == 'Invalid trade pair':
                print('Invalid Trade Pair', 'ETH - ', symbol)
            elif json_data['msg'] == 'unable to provide offers for pair currently':
                print('Unable to provide offers for the current pair.')
            elif json_data['msg'][35:] == 'deposit_coin_amount must be between':
                print('Deposit amount must be between ', json_data['msg'][:35])
#coinstwitch()
def flyp():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    flypdata = open('flypdata.json', 'a')
    url = 'https://flyp.me/api/v1/data/exchange_rates'
    rates = requests.get(url=url)
    json_data = json.loads(rates.text)
    for i in json_data:
        if i[:3] == 'ETH':
            target_coin = i[4:]
            time.sleep(1)
            print(target_coin, 'has a rate of', '1 ETH = ', '[', json_data[i], target_coin, ']','| Inverse Rate is ', '1 ', target_coin, '=', '[', float(1 / float(json_data[i])), 'ETH ]')
#flyp()
def simpleswamp():
    url1 = 'https://api.simpleswap.io/fixed/get_all_pairs'
    pairsgrab = requests.get(url=url1)
    pairs_datajson = json.loads(pairsgrab.text)
    simpleswap = open('simpleswap.json', 'a')
    for pair in pairs_datajson['eos']:
        url2 = 'https://api.simpleswap.io/fixed/get_estimated?currency_from=eth&currency_to=' + pair['symbol'] + '&amount=1'
        symbol = pair['symbol'].upper()
        rate = requests.get(url=url2)
        rate_info = json.loads(rate.text)
        if rate_info != None:
            print(symbol, 'has a rate of', '1 ETH = ', '[', rate_info, ']', symbol, '| Inverse Rate is ', symbol, '=', '[', 1 / float(rate_info), ']', 'ETH')
        else:
            print('Invalid Trade Pair ETH -', symbol)
#simpleswamp()
def godex():
    url1 = 'https://api.godex.io/api/v1/coins'
    symbolsreq = requests.get(url=url1)
    symbols = json.loads(symbolsreq.text)
    godextext = open('godex.json', 'a')
    #print(str(symbols))
    for x in symbols:
        coin = x['code']
        if coin != 'ETH':
            godextext.write(coin + '\n')
            url2 = 'https://api.godex.io/api/v1/info'
            params = {"from": "ETH", "to": coin, "amount": 1}
            headers = {'content-type': 'application/json'}
            rates_request = requests.post(url=url2, data=params)
            rate = json.loads(rates_request.text)['rate']
            print(coin, 'has a rate of', '1 ETH = ', '[', rate, coin,']','| Inverse Rate is ', '1 ', coin, '=', '[',float(1 / float(rate)), 'ETH ]')

#godex()
#~~~~~~Service Unavailable~~~~~~~
def nexchange():
    url1 = 'https://api.nexchange.io/en/api/v1/pair/'
    pairs_request = requests.get(url=url1)
    print(pairs_request)
#nexchange()

