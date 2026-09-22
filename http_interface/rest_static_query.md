> [English](./rest_static_query.md) | [中文](./rest_static_query_cn.md)

## POST Product information query

## POST /v1/stock-info

### Interface description

This interface only supports batch requests for basic information on US, HK, and A-share products.

### Request Frequency

| Plan          | Individual request                                | Request multiple HTTP interfaces                                                                                                                                                                      |
| ------------- | ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Free          | Once every 10 seconds, only 1 request can be made | 1、One request per second.2、/batch-kline needs 10-second intervals.3、Total of 10 requests per minute (every 6 seconds).4、Max 1000 daily requests; excess resets at midnight.                           |
| Basic         | Only 1 request per second                         | 1、One request per second.2、/batch-kline: 1 request every 3 seconds.3、Total of 60 requests per minute (1 request per second).4、Max 86400 daily requests; excess resets at midnight.                    |
| Premium       | Up to 10 requests per second                      | 1、Combined interfaces: 10 requests/second.2、/batch-kline: 1 request/2 seconds.3、Total: 600 requests/minute (10/second).4、Daily limit: 864,000 requests; reset daily at midnight if exceeded.          |
| Professional  | Up to 20 requests per second                      | 1、Combined interfaces: 20 requests/second.2、/batch-kline: 1 request/second interval.3、Total: 1200 requests/minute (20/second).4、Daily limit: 1,728,000 requests; reset daily at midnight if exceeded. |
| All HK Stocks | Up to 20 requests per second                      | 1、Combined interfaces: 20 requests/second.2、/batch-kline: 1 request/second interval.3、Total: 1200 requests/minute (20/second).4、Daily limit: 1,728,000 requests; reset daily at midnight if exceeded. |
| All CN Stocks | Up to 20 requests per second                      | 1、Combined interfaces: 20 requests/second.2、/batch-kline: 1 request/second interval.3、Total: 1200 requests/minute (20/second).4、Daily limit: 1,728,000 requests; reset daily at midnight if exceeded. |

### Interface Limitations

- 1、Please be sure to read:[HTTP Interface Limitations](https://github.com/alltick/alltick-realtime-forex-crypto-stock-tick-finance-websocket-api/blob/main/http_interface/interface_limitation_cn.md)
- 2、Please be sure to read:[Error Code Descriptions](https://github.com/alltick/alltick-realtime-forex-crypto-stock-tick-finance-websocket-api/blob/main/error_code_description_cn.md)

### **Interface Address**

- **Base Path:** `/quote-stock-b-api/v1/stock-info`
- **Full URL:** `https://quote.alltick.co/quote-stock-b-api/static-info`

<br />

### Request Parameters

| Name  | Position | Type   | Required | Description                                  |
| ----- | -------- | ------ | -------- | -------------------------------------------- |
| X-API-Key | header   | string | Yes      | Your token                                   |
| query | body     | string | Yes      | See explanation for query request parameters |

> Query Request Parameters

Assign the following JSON to the body

```json
{
  "trace": "edd5df80-df7f-4acf-8f67-68fd2f096426",
  "data": {
    "symbol_list": [
      {
        "code": "857.HK"
      },
      {
        "code": "UNH.US"
      }
    ]
  }
}
```

### Query Request Parameters

| Name           | Type      | Required | Description                                                                                                                                                                                                                                                                                         |
| -------------- | --------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| trace          | string    | Yes      | <br />                                                                                                                                                                                                                                                                                              |
| data           | object    | Yes      | <br />                                                                                                                                                                                                                                                                                              |
| » symbol\_list | \[object] | Yes      | <br />                                                                                                                                                                                                                                                                                              |
| » » code       | string    | No       | Refer to the code list and select the code you want to query：[Click on the code list](https://docs.google.com/spreadsheets/d/1avkeR1heZSj6gXIkDeBt8X3nv4EzJetw4yFuKjSDYtA/edit?gid=495387863#gid=495387863)  Note: The case of the code value must be consistent with the code in the product list. |

> Response Example

> OK

```json
{
  "ret": 200,
  "msg": "ok",
  "trace": "edd5df80-df7f-4acf-8f67-68fd2f096426",
  "data": {
    "static_info_list": [
      {
        "board": "HKEquity",
        "bps": "101.7577888985738336",
        "circulating_shares": "9267359712",
        "currency": "HKD",
        "dividend_yield": "3.4558141358352833",
        "eps": "13.7190213011686429",
        "eps_ttm": "18.0567016900844671",
        "exchange": "SEHK",
        "hk_shares": "9267359712",
        "lot_size": "100",
        "name_cn": "腾讯控股",
        "name_en": "TENCENT",
        "name_hk": "騰訊控股",
        "symbol": "700.HK",
        "total_shares": "9267359712"
      }
    ]
  }
}
```

### Response Result

| Status Code | Status Meaning | Description | Data Model |
| ----------- | -------------- | ----------- | ---------- |
| 200         | OK             | OK          | Inline     |

### Response Data Structure

Status Code **200**

| Name                    | Type      | Required | Constraints | Chinese Name | Description                                            |
| ----------------------- | --------- | -------- | ----------- | ------------ | ------------------------------------------------------ |
| » ret                   | integer   | true     | <br />      | <br />       | Return code                                            |
| » msg                   | string    | true     | <br />      | <br />       | Message corresponding to the return code               |
| » trace                 | string    | true     | <br />      | <br />       | Request trace                                          |
| » data                  | object    | true     | <br />      | <br />       | <br />                                                 |
| »» static\_info\_list   | \[object] | true     | <br />      | <br />       | <br />                                                 |
| »»» board               | string    | false    | <br />      | <br />       | The sector to which the stock belongs                  |
| »»» bps                 | string    | false    | <br />      | <br />       | Net assets per share                                   |
| »»» circulating\_shares | string    | false    | <br />      | <br />       | circulating capital                                    |
| »»» currency            | string    | false    | <br />      | <br />       | Transaction currency                                   |
| »»» dividend\_yield     | string    | false    | <br />      | <br />       | dividends                                              |
| »»» eps                 | string    | false    | <br />      | <br />       | earnings per share                                     |
| »»» eps\_ttm            | string    | false    | <br />      | <br />       | earnings per share (TTM)                               |
| »»» exchange            | string    | false    | <br />      | <br />       | The exchange to which the product belongs              |
| »»» hk\_shares          | string    | false    | <br />      | <br />       | Hong Kong stocks share capital (Hong Kong stocks only) |
| »»» lot\_size           | string    | false    | <br />      | <br />       | Number of shares per lot                               |
| »»» name\_cn            | string    | false    | <br />      | <br />       | Product name in simplified Chinese                     |
| »»» name\_en            | string    | false    | <br />      | <br />       | English product name                                   |
| »»» name\_hk            | string    | false    | <br />      | <br />       | Product name in traditional Chinese                    |
| »»» symbol              | string    | false    | <br />      | <br />       | Product code                                           |
| »»» total\_shares       | string    | false    | <br />      | <br />       | total share capital                                    |

