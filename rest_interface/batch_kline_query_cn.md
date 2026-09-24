> [English](./batch_kline_query.md) | [中文](./batch_kline_query_cn.md)

## POST 批量查询产品最新2根K线（最高、最低、开盘、收盘价）

## POST /v1/batch-kline

### 接口说明

该接口可以一次性批量查询多个产品，且可批量一次性查询多个k线类型（k线类型指的是1分钟，15分钟，30分钟等），但只能批量查询最新的2根k线。
使用HTTP接口获取K线的客户，建议将/kline和/batch-kline这2个接口结合使用,步骤如下：
1、首先，通过 /kline 接口轮询请求历史数据并存储到本地数据库，后续历史数据可直接从客户的数据库获取，无需再通过接口请求。
2、然后，后续持续使用 /batch-kline 接口批量请求多个产品的最新2根K线，并将数据更新到数据库。
这种方式能够快速更新最新的K线，同时避免频繁请求历史K线造成频率受到限制。

### 请求频率

| 计划   | 单独请求                                           | 同时请求多个http接口                                                                                  |
| :--- | :--------------------------------------------- | :-------------------------------------------------------------------------------------------- |
| 免费   | 1、每10秒，可1次请求 2、每次可批量查询10组数据，每1组数据=1只产品+1种K线类型  | 1、同1秒只能请求1个口 2、所有接口相加，1分钟最大请求10次(6秒1次) ，需注意/batch-kline接口需间隔10秒 3、每天总共最大可请求1000次，超过则第二天凌晨恢复使用 |
| 基础   | 1、每3秒，只能1次请求 2、每次可批量查询100组数据，每1组数据=1只产品+1种K线类型 | 1、同1秒只能请求1个接口 2、所有接口相加，1分钟最大请求60次(1秒1次)，需注意/batch-kline接口需间隔3秒 3、每天总共最大可请求86400次，超过则第二天凌晨恢复使用 |
| 高级   | 1、每2秒，只能1次请求 2、每次可批量查询200组数据，每1组数据=1只产品+1种K线类型 | 1、所有接口相加，1分钟最大请求600次(1秒10次)，需注意/batch-kline接口需间隔2秒 2、每天总共最大可请求864000次，超过则第二天凌晨恢复使用            |
| 专业   | 1、每1秒，只能1次请求 2、每次可批量查询500组数据，每1组数据=1只产品+1种K线类型 | 1、所有接口相加，1分钟最大请求1200次(1秒20次)，需注意/batch-kline接口需间隔1秒 2、每天总共最大可请求1728000次，超过则第二天凌晨恢复使用          |
| 全部港股 | 1、每1秒，只能1次请求 2、每次可批量查询500组数据，每1组数据=1只产品+1种K线类型 | 1、所有接口相加，1分钟最大请求1200次(1秒20次)，需注意/batch-kline接口需间隔1秒 2、每天总共最大可请求1728000次，超过则第二天凌晨恢复使用          |
| 全部A股 | 1、每1秒，只能1次请求 2、每次可批量查询500组数据，每1组数据=1只产品+1种K线类型 | 1、所有接口相加，1分钟最大请求1200次(1秒20次)，需注意/batch-kline接口需间隔1秒 2、每天总共最大可请求1728000次，超过则第二天凌晨恢复使用          |
| 全部美股 | 1、每1秒，只能1次请求 2、每次可批量查询500组数据，每1组数据=1只产品+1种K线类型 | 1、所有接口相加，1分钟最大请求1200次(1秒20次)，需注意/batch-kline接口需间隔1秒 2、每天总共最大可请求1728000次，超过则第二天凌晨恢复使用          |

### 接口限制

- 1、请务必阅读：[HTTP接口限制说明](https://github.com/alltick/alltick-realtime-forex-crypto-stock-tick-finance-websocket-api/blob/main/http_interface/interface_limitation_cn.md)
- 2、请务必阅读：[错误码说明](https://github.com/alltick/alltick-realtime-forex-crypto-stock-tick-finance-websocket-api/blob/main/error_code_description_cn.md)

### 接口地址

#### 1、美股、港股、A股、大盘数据接口地址：

- 基本路径: /quote-stock-b-api/v1/batch-kline
- 完整URL: <https://quote.alltick.co/quote-stock-b-api/v1/batch-kline>

#### 2、外汇、贵金属、加密货币、原油、CFD指数、商品接口地址：

- 基本路径: /quote-b-api/v1/batch-kline
- 完整URL: <https://quote.alltick.co/quote-b-api/v1/batch-kline>

### 批量查询产品最新K线功能，由于批量查询参数比较多，放入body中。

> Body 请求参数

```json
{
  "trace": "c2a8a146-a647-4d6f-ac07-8c4805bf0b74",
  "data": {
    "symbol_list": [
      {
        "code": "700.HK",
        "kline_type": 1,
        "kline_timestamp_end": 0,
        "query_kline_num": 1,
        "adjust_type": 0
      },
      {
        "code": "GOOGL.US",
        "kline_type": 1,
        "kline_timestamp_end": 0,
        "query_kline_num": 1,
        "adjust_type": 0
      }
    ]
  }
}
```

### 请求参数

| 名称                        | 位置     | 类型        | 必选 | 说明                                                                                                                                                                                |
| ------------------------- | ------ | --------- | -- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| X-API-Key                 | header | string    | 是  | 您的token，请联系相关人员索要                                                                                                                                                                 |
| body                      | body   | object    | 是  | <br />                                                                                                                                                                            |
| » trace                   | body   | string    | 是  | 追踪码，用来查询日志使用，请保证每次请求时唯一                                                                                                                                                           |
| » data                    | body   | object    | 是  | <br />                                                                                                                                                                            |
| »» symbol_list             | body   | \[object] | 是  | <br />                                                                                                                                                                            |
| »»» code                  | body   | string    | 是  | 请查看code列表，选择你要查询的code:[点击code列表](https://docs.google.com/spreadsheets/d/1avkeR1heZSj6gXIkDeBt8X3nv4EzJetw4yFuKjSDYtA/edit?gid=495387863#gid=495387863)注意：code值大小写要与产品列表中的code保持一致 |
| »»» kline\_type           | body   | integer   | 是  | k线类型1、1是1分钟K，2是5分钟K，3是15分钟K，4是30分钟K，5是小时K，6是2小时K(股票不支持2小时)，7是4小时K(股票不支持4小时)，8是日K，9是周K，10是月K （注：股票不支持2小时K、4小时K）2、最短的k线只支持1分钟                                                       |
| »»» kline\_timestamp\_end | body   | integer   | 是  | 从指定时间往前查询K线1、传0表示从当前最新的交易日往前查k线2、指定时间请传时间戳，传时间戳表示从该时间戳往前查k线3、只有外汇贵金属加密货币支持传时间戳，股票类的code不支持                                                                                        |
| »»» query\_kline\_num     | body   | integer   | 是  | 表示查询多少根K线，该接口最大只能查询2根k线                                                                                                                                                           |
| »»» adjust\_type          | body   | integer   | 是  | 复权类型,对于股票类的code才有效，例如：0:除权,1:前复权，目前仅支持0                                                                                                                                           |

> 返回示例

> OK

```json
{
  "ret": 200,
  "msg": "ok",
  "trace": "c2a8a146-a647-4d6f-ac07-8c4805bf0b74",
  "data": {
    "kline_list": [
      {
        "code": "700.HK",
        "kline_type": 1,
        "kline_data": [
          {
            "timestamp": "1677829200",
            "open_price": "136.421",
            "close_price": "136.412",
            "high_price": "136.422",
            "low_price": "136.407",
            "volume": "0",
            "turnover": "0"
          }
        ]
      },
      {
        "code": "GOOGL.US",
        "kline_type": 1,
        "kline_data": [
          {
            "timestamp": "1677829200",
            "open_price": "136.421",
            "close_price": "136.412",
            "high_price": "136.422",
            "low_price": "136.407",
            "volume": "0",
            "turnover": "0"
          }
        ]
      }
    ]
  }
}
```

### 返回结果

| 状态码 | 状态码含义 | 说明 | 数据模型   |
| --- | ----- | -- | ------ |
| 200 | OK    | OK | Inline |

### 返回数据结构

状态码 **200**

| 名称                | 类型       | 必选   | 约束     | 中文名    | 说明                                                                                                                          |
| ----------------- | -------- | ---- | ------ | ------ | --------------------------------------------------------------------------------------------------------------------------- |
| » ret             | integer  | true | <br /> | <br /> | <br />                                                                                                                      |
| » msg             | string   | true | <br /> | <br /> | <br />                                                                                                                      |
| » trace           | string   | true | <br /> | <br /> | <br />                                                                                                                      |
| » data            | object   | true | <br /> | <br /> | <br />                                                                                                                      |
| »» kline\_list    | \[array] | true | <br /> | <br /> | <br />                                                                                                                      |
| »»» code          | string   | true | <br /> | <br /> | 产品代码                                                                                                                        |
| »»» kline\_type   | integer  | true | <br /> | <br /> | k线类型，1、1是分钟K，2是5分钟K，3是15分钟K，4是30分钟K，5是小时K，6是2小时K(股票不支持2小时)，7是4小时K(股票不支持4小时)，8是日K，9是周K，10是月K （注：股票不支持2小时K、4小时K）2、最短的k线只支持1分钟 |
| »»» kline\_data   | \[array] | true | <br /> | <br /> | <br />                                                                                                                      |
| »»»» timestamp    | string   | true | <br /> | <br /> | 该K线时间戳                                                                                                                      |
| »»»» open\_price  | string   | true | <br /> | <br /> | 该K线开盘价                                                                                                                      |
| »»»» close\_price | string   | true | <br /> | <br /> | 该K线收盘价：1、交易时段内，最新一根K线，该价格也是最新成交价 2、休市期间，最新一根K线，该价格是收盘价                                                                      |
| »»»» high\_price  | string   | true | <br /> | <br /> | 该K线最高价                                                                                                                      |
| »»»» low\_price   | string   | true | <br /> | <br /> | 该K线最低价                                                                                                                      |
| »»»» volume       | string   | true | <br /> | <br /> | 该K线成交数量                                                                                                                     |
| »»»» turnover     | string   | true | <br /> | <br /> | 该K线成交金额                                                                                                                     |
