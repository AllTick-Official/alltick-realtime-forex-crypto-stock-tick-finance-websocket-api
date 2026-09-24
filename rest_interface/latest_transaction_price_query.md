> [English](./latest_transaction_price_query.md) | [中文](./latest_transaction_price_query_cn.md)

## GET Latest Trade Tick Query

## GET /v1/quote

### Interface Description

This interface supports batch requests for the latest trade prices (latest tick data) but does not support requests for historical trade prices (historical tick data).

### Request Frequency

| Text          | Text                                                                                      | Text                                                                                                                                                                                                  |
| ------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Free          | 1、Once every 10 seconds, only 1 request can be made 2、5 products per batch max            | 1、One request per second.2、/batch-kline needs 10-second intervals.3、Total of 10 requests per minute (every 6 seconds).4、Max 1000 daily requests; excess resets at midnight.                           |
| Basic         | 1、Only 1 request per second 2、Suggest 50 code requests max due to GET URL length limit    | 1、One request per second.2、/batch-kline: 1 request every 3 seconds.3、Total of 60 requests per minute (1 request per second).4、Max 86400 daily requests; excess resets at midnight.                    |
| Premium       | 1、Up to 10 requests per second 2、Suggest 50 code requests max due to GET URL length limit | 1、Combined interfaces: 10 requests/second.2、/batch-kline: 1 request/2 seconds.3、Total: 600 requests/minute (10/second).4、Daily limit: 864,000 requests; reset daily at midnight if exceeded.          |
| Professional  | 1、Up to 20 requests per second 2、Suggest 50 code requests max due to GET URL length limit | 1、Combined interfaces: 20 requests/second.2、/batch-kline: 1 request/second interval.3、Total: 1200 requests/minute (20/second).4、Daily limit: 1,728,000 requests; reset daily at midnight if exceeded. |
| All HK Stocks | 1、Up to 20 requests per second 2、Suggest 50 code requests max due to GET URL length limit | 1、Combined interfaces: 20 requests/second.2、/batch-kline: 1 request/second interval.3、Total: 1200 requests/minute (20/second).4、Daily limit: 1,728,000 requests; reset daily at midnight if exceeded. |
| All CN Stocks | 1、Up to 20 requests per second 2、Suggest 50 code requests max due to GET URL length limit | 1、Combined interfaces: 20 requests/second.2、/batch-kline: 1 request/second interval.3、Total: 1200 requests/minute (20/second).4、Daily limit: 1,728,000 requests; reset daily at midnight if exceeded. |

### Interface Limitations

- 1、Please be sure to read:[HTTP Interface Limitations](https://github.com/alltick/alltick-realtime-forex-crypto-stock-tick-finance-websocket-api/blob/main/http_interface/interface_limitation_cn.md)
- 2、Please be sure to read:[Error Code Descriptions](https://github.com/alltick/alltick-realtime-forex-crypto-stock-tick-finance-websocket-api/blob/main/error_code_description_cn.md)

### API Endpoints

**1、US Stocks, Hong Kong Stocks, A Shares, Major Index Data API Endpoints:**

- **Base Path:** `/quote-stock-b-api/v1/quote`
- **Full URL:** `https://quote.alltick.co/quote-stock-b-api/v1/quote/{query}`

**2、Forex, Precious Metals, Cryptocurrencies, Commodities API Endpoints:**

- **Base Path:** `/quote-b-api/v1/quote`
- **Full URL:** `https://quote.alltick.co/quote-b-api/v1/quote/{query}`

### Request Parameters

| Name      | Position | Type   | Required | Description                                       |
| --------- | -------- | ------ | -------- | ------------------------------------------------- |
| X-API-Key | header   | string | Yes      | Your token                                        |
| query     | path     | string | Yes      | See explanation of query request parameters below |

> Query Request Parameters

The following JSON should be URL-encoded and assigned to the `query` query string in the URL.

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

| Name           | Type      | Required | Description                                                                                                                                                                                                                                                                                          |
| -------------- | --------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| trace          | string    | Yes      | <br />                                                                                                                                                                                                                                                                                               |
| data           | object    | Yes      | <br />                                                                                                                                                                                                                                                                                               |
| » symbol\_list | \[object] | Yes      | <br />                                                                                                                                                                                                                                                                                               |
| »» code        | string    | No       | Refer to the code list and select the code you want to query：[Click on the code list](https://docs.google.com/spreadsheets/d/1avkeR1heZSj6gXIkDeBt8X3nv4EzJetw4yFuKjSDYtA/edit?gid=495387863#gid=495387863)   Note: The case of the code value must be consistent with the code in the product list. |

> Response Example

> OK

```json
{
  "ret": 200,
  "msg": "ok",
  "trace": "edd5df80-df7f-4acf-8f67-68fd2f096426",
  "data": {
    "tick_list": [
      {
        "code": "857.HK",
        "seq": "30841439",
        "tick_time": "1677831545217",
        "price": "136.302",
        "volume": "0",
        "turnover": "0",
        "trade_direction": 0
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

| Name                 | Type      | Required | Constraint | Chinese Name | Description                                             |
| -------------------- | --------- | -------- | ---------- | ------------ | ------------------------------------------------------- |
| » ret                | integer   | true     | <br />     | <br />       | Return code                                             |
| » msg                | string    | true     | <br />     | <br />       | Message corresponding to the return code                |
| » trace              | string    | true     | <br />     | <br />       | Request trace                                           |
| » data               | object    | true     | <br />     | <br />       | <br />                                                  |
| »» tick\_list        | \[object] | true     | <br />     | <br />       | <br />                                                  |
| »»» code             | string    | false    | <br />     | <br />       | Code                                                    |
| »»» seq              | string    | false    | <br />     | <br />       | Sequence                                                |
| »»» tick\_time       | string    | false    | <br />     | <br />       | Timestamp                                               |
| »»» price            | string    | false    | <br />     | <br />       | Price                                                   |
| »»» volume           | string    | false    | <br />     | <br />       | Volume                                                  |
| »»» turnover         | string    | false    | <br />     | <br />       | Turnover                                                |
| »»» trade\_direction | integer   | false    | <br />     | <br />       | Trading direction, 0 for default, 1 for BUY, 2 for SELL |

