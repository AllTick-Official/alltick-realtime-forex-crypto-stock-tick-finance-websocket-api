> [English](./rest_static_query.md) | [中文](./rest_static_query_cn.md)

## POST 股票产品基础信息批量查询

## POST /v1/stock-info

### 接口说明

该接口仅支持批量请求美股、港股、A股产品的部分基础信息。

### 请求频率

| 计划   | 单独请求         | 同时请求多个http接口                                                                                                     |
| :--- | :----------- | :--------------------------------------------------------------------------------------------------------------- |
| 免费   | 每10秒，只能1次请求  | 1、同1秒只能请求1个接口2、多个接口请求时，需注意/batch-kline接口需间隔10秒 3、所有接口相加，1分钟最大请求10次(6秒1次) 4、每天总共最大可请求1000次，超过则第二天凌晨恢复使用           |
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

- 基本路径: /quote-stock-b-api/v1/stock-info
- 完整URL: <https://quote.alltick.co/quote-stock-b-api/v1/stock-info>

<br />

### 请求参数

| 名称        | 位置     | 类型     | 必选 | 说明            |
| --------- | ------ | ------ | -- | ------------- |
| X-API-Key | header | string | 是  | 您的token       |
| query     | body   | string | 是  | 查看query请求参数说明 |

> query 请求参数

将如下json放入请求body中

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

| 名称             | 类型        | 必选 | 说明                                                                                                                                                                                |
| -------------- | --------- | -- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| trace          | string    | 是  | <br />                                                                                                                                                                            |
| data           | object    | 是  | <br />                                                                                                                                                                            |
| » symbol\_list | \[object] | 是  | <br />                                                                                                                                                                            |
| »» code        | string    | 否  | 请查看code列表，选择你要查询的code：[点击code列表](https://docs.google.com/spreadsheets/d/1avkeR1heZSj6gXIkDeBt8X3nv4EzJetw4yFuKjSDYtA/edit?gid=495387863#gid=495387863)注意：code值大小写要与产品列表中的code保持一致 |

> 返回示例

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

### 返回结果

| 状态码 | 状态码含义 | 说明 | 数据模型   |
| --- | ----- | -- | ------ |
| 200 | OK    | OK | Inline |

### 返回数据结构

状态码 **200**

| 名称                      | 类型        | 必选    | 约束     | 中文名    | 说明         |
| ----------------------- | --------- | ----- | ------ | ------ | ---------- |
| » ret                   | integer   | true  | <br /> | <br /> | 返回code     |
| » msg                   | string    | true  | <br /> | <br /> | 返回code对应消息 |
| » trace                 | string    | true  | <br /> | <br /> | 请求的trace   |
| » data                  | object    | true  | <br /> | <br /> | <br />     |
| »» static\_info\_list   | \[object] | true  | <br /> | <br /> | <br />     |
| »»» board               | string    | false | <br /> | <br /> | 股票所属板块     |
| »»» bps                 | string    | false | <br /> | <br /> | 每股净资产      |
| »»» circulating\_shares | string    | false | <br /> | <br /> | 流通股本       |
| »»» currency            | string    | false | <br /> | <br /> | 交易币种       |
| »»» dividend\_yield     | string    | false | <br /> | <br /> | 股息         |
| »»» eps                 | string    | false | <br /> | <br /> | 每股盈利       |
| »»» eps\_ttm            | string    | false | <br /> | <br /> | 每股盈利 (TTM) |
| »»» exchange            | string    | false | <br /> | <br /> | 产品所属交易所    |
| »»» hk\_shares          | string    | false | <br /> | <br /> | 港股股本 (仅港股) |
| »»» lot\_size           | string    | false | <br /> | <br /> | 每手股数       |
| »»» name\_cn            | string    | false | <br /> | <br /> | 中文简体产品的名称  |
| »»» name\_en            | string    | false | <br /> | <br /> | 英文产品的名称    |
| »»» name\_hk            | string    | false | <br /> | <br /> | 中文繁体产品的名称  |
| »»» symbol              | string    | false | <br /> | <br /> | 产品code     |
| »»» total\_shares       | string    | false | <br /> | <br /> | 总股本        |

