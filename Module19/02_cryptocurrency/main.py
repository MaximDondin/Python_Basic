data = {
    "address": "0x544444444444",
    "ETH": {
        "balance": 444,
        "total_in": 444,
        "total_out": 4
    },
    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
            },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 0
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0
        }
    ]
}

#1
print('1) Списки ключей и значений словаря.')
for i_inf in data:
    print(i_inf, ':', data[i_inf])

#2
data['ETH']['total_diff'] = 100
#print('\n2)', data['ETH'])

#3
data['tokens'][0]['fst_token_info']['name'] = 'doge'
#print('\n3)', data['tokens'][0]['fst_token_info'])

#4
count = 0
for i_token_inf in range(len(data['tokens'])):
    count += data['tokens'][i_token_inf].pop('total_out')
data['ETH']['total_out'] = count
#print('\n4)', data['ETH'], '\n', data['tokens'][0].get('total_out'), '\n', data['tokens'][1].get('total_out'))

#5
data['tokens'][1]['sec_token_info']['total_price'] = data['tokens'][1]['sec_token_info'].pop('price')
#print('\n5)', data['tokens'][1]['sec_token_info'])