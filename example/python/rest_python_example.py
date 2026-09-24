import time
import requests
import json
from urllib.parse import quote

# Extra headers
test_headers = {
    'Content-Type': 'application/json'
}

# Replace with your own token
token = 'testtoken'
test_headers['X-API-Key'] = token

'''
# Special Note:
# GitHub: https://github.com/alltick/realtime-forex-crypto-stock-tick-finance-websocket-api
# Token Application: https://alltick.co
# Replace "testtoken" in the URL below with your own token
# API addresses for forex, cryptocurrencies, and precious metals:
# https://quote.alltick.co/quote-b-ws-api
# Stock API address:
# https://quote.alltick.co/quote-stock-b-ws-api
Encode the following JSON and put it in the URL path (not as a query string parameter)
{"trace": "python_http_test1", "data": {"code": "700.HK", "kline_type": 1, "kline_timestamp_end": 0, "query_kline_num": 2, "adjust_type": 0}}
{"trace": "python_http_test2", "data": {"symbol_list": [{"code": "700.HK"}, {"code": "UNH.US"}]}}
{"trace": "python_http_test3", "data": {"symbol_list": [{"code": "700.HK"}, {"code": "UNH.US"}]}}
'''

# Build params as JSON strings
params1 = '{"trace": "python_http_test1", "data": {"code": "700.HK", "kline_type": 1, "kline_timestamp_end": 0, "query_kline_num": 2, "adjust_type": 0}}'
params2 = '{"trace": "python_http_test2", "data": {"symbol_list": [{"code": "700.HK"}, {"code": "UNH.US"}]}}'
params3 = '{"trace": "python_http_test3", "data": {"symbol_list": [{"code": "700.HK"}, {"code": "UNH.US"}]}}'

# Build URLs with the encoded query in the path
# Format: https://quote.alltick.co/quote-stock-b-api/v1/{endpoint}/{query}
test_url1 = 'https://quote.alltick.co/quote-stock-b-api/v1/kline/' + quote(params1, safe='')
test_url2 = 'https://quote.alltick.co/quote-stock-b-api/v1/depth/' + quote(params2, safe='')
test_url3 = 'https://quote.alltick.co/quote-stock-b-api/v1/quote/' + quote(params3, safe='')

resp1 = requests.get(url=test_url1, headers=test_headers)
time.sleep(1)
resp2 = requests.get(url=test_url2, headers=test_headers)
time.sleep(1)
resp3 = requests.get(url=test_url3, headers=test_headers)

# Decoded text returned by the request
text1 = resp1.text
print(text1)

text2 = resp2.text
print(text2)

text3 = resp3.text
print(text3)
