> [English](./rest_latest_order_book_price_query.md) | [中文](./rest_latest_order_book_price_query_cn.md)

## GET 最新盘口(Order Book)查询

## GET /v1/depth

### 接口说明

以下是每类产品最大的盘口深度：
1、不活跃的产品存在小于下面列的最大档的情况，属于正常情况
2、存在单边深度是空的情况，例如股票涨停跌停时，单边盘口可能是空的

| <br /> | 外汇、贵金属、原油、CFD指数 | 加密货币 | 港股    | 美股   | 沪深A股 |
| ------ | --------------- | ---- | ----- | ---- | ---- |
| 深度说明   | 最1档             | 最大5档 | 最大10档 | 最大1档 | 最大5档 |

### 请求频率

| 计划   | 单独请求         | 同时请求多个http接口                                                                                                     |
| :--- | :----------- | :--------------------------------------------------------------------------------------------------------------- |
| 免费   | 每10秒，只能1次请求  | 1、同1秒只能请求1个接口2、多个接口请求时，需注意/batch-kline接口需间隔10秒 3、所有接口相加，1分钟最大请求10次(6秒1次)  4、每天总共最大可请求1000次，超过则第二天凌晨恢复使用          |
| 基础   | 每1秒，只能1次请求   | 1、同1秒只能请求1个接口2、多个接口请求时，需注意/batch-kline接口需间隔3秒 3、所有接口相加，1分钟最大请求60次(1秒1次)4、每天总共最大可请求86400次，超过则第二天凌晨恢复使用            |
| 高级   | 每1秒，最大可10次请求 | 1、所以接口相加，每1秒可请求10次2、多个接口请求时，需注意/batch-kline接口需间隔2秒 3、所有接口相加，1分钟最大请求600次(1秒10次) 4、每天总共最大可请求864000次，超过则第二天凌晨恢复使用   |
| 专业   | 每1秒，最大可20次请求 | 1、所以接口相加，每1秒可请求20次2、多个接口请求时，需注意/batch-kline接口需间隔1秒 3、所有接口相加，1分钟最大请求1200次(1秒20次) 4、每天总共最大可请求1728000次，超过则第二天凌晨恢复使用 |
| 全部港股 | 每1秒，最大可20次请求 | 1、所以接口相加，每1秒可请求20次2、多个接口请求时，需注意/batch-kline接口需间隔1秒 3、所有接口相加，1分钟最大请求1200次(1秒20次) 4、每天总共最大可请求1728000次，超过则第二天凌晨恢复使用 |
| 全部A股 | 每1秒，最大可20次请求 | 1、所以接口相加，每1秒可请求20次2、多个接口请求时，需注意/batch-kline接口需间隔1秒 3、所有接口相加，1分钟最大请求1200次(1秒20次) 4、每天总共最大可请求1728000次，超过则第二天凌晨恢复使用 |
| 全部美股 | 每1秒，最大可20次请求 | 1、所以接口相加，每1秒可请求20次2、多个接口请求时，需注意/batch-kline接口需间隔1秒 3、所有接口相加，1分钟最大请求1200次(1秒20次) 4、每天总共最大可请求1728000次，超过则第二天凌晨恢复使用 |

### 接口限制

- 1、请务必阅读：[HTTP接口限制说明](https://github.com/alltick/alltick-realtime-forex-crypto-stock-tick-finance-websocket-api/blob/main/http_interface/interface_limitation_cn.md)
- 2、请务必阅读：[错误码说明](https://github.com/alltick/alltick-realtime-forex-crypto-stock-tick-finance-websocket-api/blob/main/error_code_description_cn.md)

### 接口地址

#### 1、美股、港股、A股、大盘数据接口地址：

- 基本路径: /quote-stock-b-api/v1/depth
- 完整URL: <https://quote.alltick.co/quote-stock-b-api/v1/depth/{query}>

#### 2、外汇、贵金属、加密货币、原油、CFD指数、商品接口地址：

- 基本路径: /quote-b-api/v1/depth
- 完整URL: <https://quote.alltick.co/quote-b-api/v1/depth/{query}>

### 请求参数

| 名称        | 位置     | 类型     | 必选 | 说明            |
| --------- | ------ | ------ | -- | ------------- |
| X-API-Key | header | string | 是  | 您的token       |
| query     | path  | string | 是  | 查看query请求参数说明 |

> query 请求参数

将如下json进行UrlEncode编码，赋值到url的查询字符串的query里

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

### query请求参数

| 名称             | 类型        | 必选 | 说明                                                                                                                                                                                 |
| -------------- | --------- | -- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| trace          | string    | 是  | <br />                                                                                                                                                                             |
| data           | object    | 是  | <br />                                                                                                                                                                             |
| » symbol\_list | \[object] | 是  | <br />                                                                                                                                                                             |
| »» code        | string    | 否  | 请查看code列表，选择你要查询的code：[点击code列表](https://docs.google.com/spreadsheets/d/1avkeR1heZSj6gXIkDeBt8X3nv4EzJetw4yFuKjSDYtA/edit?gid=495387863#gid=495387863) 注意：code值大小写要与产品列表中的code保持一致 |

> 返回示例

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
        "seq": "30686349",
        "tick_time": "1677830357227",
        "bids": [
          {
            "price": "136.424",
            "volume": "100000.00"
          }
        ],
        "asks": [
          {
            "price": "136.427",
            "volume": "400000.00"
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

| 名称             | 类型        | 必选    | 约束     | 中文名    | 说明                                           |
| -------------- | --------- | ----- | ------ | ------ | -------------------------------------------- |
| » ret          | integer   | true  | <br /> | <br /> | 返回code                                       |
| » msg          | string    | true  | <br /> | <br /> | 返回code对应消息                                   |
| » trace        | string    | true  | <br /> | <br /> | 请求的trace                                     |
| » data         | object    | true  | <br /> | <br /> | <br />                                       |
| »» tick\_list  | \[object] | true  | <br /> | <br /> | <br />                                       |
| »»» code       | string    | false | <br /> | <br /> | 代码                                           |
| »»» seq        | string    | false | <br /> | <br /> | 报价序号                                         |
| »»» tick\_time | string    | false | <br /> | <br /> | 报价时间戳                                        |
| »»» bids       | \[object] | false | <br /> | <br /> | bid列表                                        |
| »»»» price     | string    | false | <br /> | <br /> | 价                                            |
| »»»» volume    | string    | false | <br /> | <br /> | 量                                            |
| »»» asks       | \[object] | false | <br /> | <br /> | ask列表                                        |
| »»»» price     | string    | false | <br /> | <br /> | 价                                            |
| »»»» volume    | string    | false | <br /> | <br /> | 量1、外汇、贵金属、CFD指数不提供volume2、股票，加密货币数据均提供volume |

