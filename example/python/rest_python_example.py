import time
import requests
from urllib.parse import quote

test_headers = {
    'Content-Type': 'application/json'
}

token = 'testtoken'
test_headers['X-API-Key'] = token

params1 = '{"trace": "python_http_test1", "data": {"code": "700.HK", "kline_type": 1, "kline_timestamp_end": 0, "query_kline_num": 2, "adjust_type": 0}}'
params2 = {"trace": "python_http_test2", "data": {"symbol_list": [{"code": "700.HK"}, {"code": "UNH.US"}]}}
params3 = {"trace": "python_http_test3", "data": {"symbol_list": [{"code": "700.HK"}, {"code": "UNH.US"}]}}

test_url1 = 'https://quote.alltick.co/quote-stock-b-api/v1/kline/' + quote(params1, safe='')
test_url2 = 'https://quote.alltick.co/quote-stock-b-api/v1/depth'
test_url3 = 'https://quote.alltick.co/quote-stock-b-api/v1/quote'

resp1 = requests.get(url=test_url1, headers=test_headers)
time.sleep(1)

resp2 = requests.post(url=test_url2, headers=test_headers, json=params2)
time.sleep(1)

resp3 = requests.post(url=test_url3, headers=test_headers, json=params3)

print(resp1.text)
print(resp2.text)
print(resp3.text)
