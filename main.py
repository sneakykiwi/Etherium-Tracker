import json
import time
import requests
import _thread
import queue
def menu():
    print(''' 
 _______ .___________.__    __   _______ .______      __   __    __  .___  ___.    .___________.______          ___       ______  __  ___  _______ .______      
|   ____||           |  |  |  | |   ____||   _  \    |  | |  |  |  | |   \/   |    |           |   _  \        /   \     /      ||  |/  / |   ____||   _  \     
|  |__   `---|  |----|  |__|  | |  |__   |  |_)  |   |  | |  |  |  | |  \  /  |    `---|  |----|  |_)  |      /  ^  \   |  ,----'|  '  /  |  |__   |  |_)  |    
|   __|      |  |    |   __   | |   __|  |      /    |  | |  |  |  | |  |\/|  |        |  |    |      /      /  /_\  \  |  |     |    <   |   __|  |      /     
|  |____     |  |    |  |  |  | |  |____ |  |\  \----|  | |  `--'  | |  |  |  |        |  |    |  |\  \----./  _____  \ |  `----.|  .  \  |  |____ |  |\  \----.
|_______|    |__|    |__|  |__| |_______|| _| `._____|__|  \______/  |__|  |__|        |__|    | _| `._____/__/     \__\ \______||__|\__\ |_______|| _| `._____|
                                                                                                                                                                
    by SneakyKiwi                                                                                                                                 
                                                                                                                                       ''')
    print('Select one of the options below!')
    print("[1] Shapeshift")
    print('[2] Coinswitch')
    print('[3] Flyp.io')
    print('[4] Simpleswap')
    print('[5] Godex')
    print('[6] All of the above')
    choice = input('Type a number: ')
    if choice == '1':
        print('~~~~~~~~~~~Starting [Shapeshift]~~~~~~~~~~~')
        shapeshift()
        menu()
    elif choice == '2':
        x = False
        coinstwitch(x)
        menu()
    elif choice == '3':
        print('~~~~~~~~~~~Starting [Flyp.io]~~~~~~~~~~~')
        flyp()
        menu()
    elif choice == '4':
        print('~~~~~~~~~~~Starting [Simpleswap]~~~~~~~~~~~')
        simpleswamp()
        menu()
    elif choice == '5':
        print('~~~~~~~~~~~Starting [Godex]~~~~~~~~~~~')
        godex()
        menu()
    elif choice == '6':
        x = True
        #_thread.start_new_thread(coinstwitch(x))
        _thread.start_new_thread(shapeshift())
        print('~~~~~~~~~~~Starting [Shapeshift]~~~~~~~~~~~')
        print('~~~~~~~~~~~Starting [Flyp.io]~~~~~~~~~~~')
        flyp()
        print('~~~~~~~~~~~Starting [Godex]~~~~~~~~~~~')
        godex()
        print('~~~~~~~~~~~Starting [Simpleswap]~~~~~~~~~~~')
        simpleswamp()
        print('~~~~~~~~~~~Starting [Coinswitch]~~~~~~~~~~~')
        coinstwitch(x)
        menu()
    else:
        print('Please enter a value between 1 and 6.')
        menu()
def shapeshift():
    print('Shapeshift')
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
            print(final_pair,'has a rate of', '1 ETH = ','[', float(json_data['rate']), final_pair, ']', '| Inverse Rate is ','1 ', final_pair, '=','[', float(1/float(json_data['rate'])),'ETH ]')
            jsondata = open('shapeshiftdata.json', 'a')
            jsondata.write(str(json_data))
#shapeshift()
def coinstwitch(threadlogic):
    print('Coinswitch')
    url2 = "https://api.coinswitch.co/v2/coins"
    headers2 = {'x-api-key': "Yllz4CvDVh7wz8kmzNz2a8oJ8SgpdheTa74UgqHT",'x-user-ip': "78.87.9.46"}
    coins = requests.request("GET", url2, headers=headers2)
    json_coins = json.loads(coins.text)
    coinswitchdata = open('coinstwitchdata.json', 'a')
    url = "https://api.coinswitch.co/v2/rate"
    log = [' ']
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
            print(symbol, 'has a rate of', '1 ETH = ', '[', float(json_data['data']['rate']), symbol, ']', '| Inverse Rate is ', '1 ', symbol, '=', '[', float(1 / float(json_data['data']['rate'])), 'ETH ]')
        except:
            json_data = json.loads(info.text)
            if json_data['msg'][18:] == 'Invalid trade pair':
                print('Invalid Trade Pair', 'ETH - ', symbol)
            elif json_data['msg'] == 'unable to provide offers for pair currently':
                print('Unable to provide offers for the current pair.', 'ETH - ', symbol)
            elif json_data['msg'][35:] == 'deposit_coin_amount must be between':
                print('Deposit amount must be between ', json_data['msg'][:35])
#coinstwitch()
def flyp():
    print('Flyp')
    flypdata = open('flypdata.json', 'a')
    url = 'https://flyp.me/api/v1/data/exchange_rates'
    rates = requests.get(url=url)
    json_data = json.loads(rates.text)
    for i in json_data:
        if i[:3] == 'ETH':
            target_coin = i[4:]
            time.sleep(1)
            print(target_coin, 'has a rate of', '1 ETH = ', '[', float(json_data[i]), target_coin, ']','| Inverse Rate is ', '1 ', target_coin, '=', '[', float(1 / float(json_data[i])), 'ETH ]')
#flyp()
def simpleswamp():
    print('Simpleswap')
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
            print(symbol, 'has a rate of', '1 ETH = ', '[', float(rate_info), ']', symbol, '| Inverse Rate is 1 ', symbol, '=', '[', float(1 / float(rate_info)), 'ETH ]')
        else:
            print('Invalid Trade Pair ETH -', symbol)
#simpleswamp()
def godex():
    print('Godex')
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
            print(coin, 'has a rate of', '1 ETH = ', '[', float(rate), coin,']','| Inverse Rate is ', '1 ', coin, '=', '[',float(1 / float(rate)), 'ETH ]')

#godex()
#~~~~~~Service Unavailable~~~~~~~
def nexchange():
    url1 = 'https://api.nexchange.io/en/api/v1/pair/'
    pairs_request = requests.get(url=url1)
    print(pairs_request)
#nexchange()


menu()
