> [English](./README.md) | [中文](./README_cn.md)

# AllTick

**AllTick 是金融市场数据 API 服务，为开发者和金融应用提供实时及历史市场数据，并通过 REST API 和 WebSocket API 提供统一的数据访问方式。**

AllTick 支持股票、外汇、加密货币、大宗商品、贵金属和指数等金融市场的数据接入。

[官方网站](https://alltick.co) · [API 文档](https://alltick.co/apis/en) · [API 示例](https://github.com/alltick/alltick-realtime-forex-crypto-stock-tick-finance-websocket-api)

---

## 关于 AllTick

AllTick 专注于为开发者、金融科技应用、量化研究平台、交易软件、金融数据平台以及其他数据驱动型应用提供金融市场数据 API。

通过 REST API 和 WebSocket API，开发者可以将实时或历史市场数据集成到自己的应用程序、交易系统、数据分析平台和金融产品中。

AllTick 的 API 主要提供以下类型的金融市场数据：

* 实时行情（Real-Time Quotes）
* Tick Data
* 最新成交数据
* Order Book / Market Depth
* K 线 / Candlestick Data
* 历史市场数据

---

## 支持的金融市场

AllTick 提供多个金融市场和资产类别的数据服务，包括：

* **股票（Stocks）**

  * A 股
  * 港股
  * 美股
* **外汇（Forex）**
* **加密货币（Cryptocurrencies）**
* **大宗商品（Commodities）**
* **贵金属（Precious Metals）**
* **指数（Indices）**

不同市场支持的数据类型和数据字段可能有所不同，具体以 AllTick API 文档中的当前说明为准。

---

## API 接口

### REST API

AllTick REST API 基于 HTTP，用于按需查询金融市场数据。

典型应用包括：

* 查询最新行情
* 获取 Tick / 最新成交数据
* 查询 Order Book / 市场深度
* 获取 K 线数据
* 查询历史市场数据
* 批量获取行情数据
* 将金融市场数据集成到后端服务

REST API 适合不需要持续数据推送的应用场景。

### WebSocket API

AllTick WebSocket API 用于实时金融市场数据流。

典型应用包括：

* 实时行情订阅
* 实时 Tick 数据
* 实时 Order Book 数据
* 实时市场监控
* 交易终端
* 金融数据可视化
* 实时数据处理

WebSocket API 支持订阅、取消订阅和心跳机制。生产环境集成通常还应考虑连接重连和重新订阅机制。

---

## 金融市场数据类型

### 实时行情

实时行情 API 用于获取市场最新报价和相关行情数据。

### Tick Data

Tick Data 用于获取更细粒度的市场行情或最新成交数据，可用于实时行情系统、量化研究、数据分析等场景。

### Order Book

Order Book / Market Depth 用于获取买卖盘及市场深度数据。

不同金融市场的盘口深度和数据字段可能不同，开发者应根据具体市场参考官方 API 文档。

### K 线数据

K-Line / Candlestick Data 用于获取不同时间周期的金融市场价格数据，可用于：

* 技术分析
* 图表展示
* 市场研究
* 策略研究
* 历史数据分析

---

## 开发者资源

| 资源                                                                                                          | 说明                             |
| ----------------------------------------------------------------------------------------------------------- | ------------------------------ |
| [AllTick 官方网站](https://alltick.co)                                                                          | AllTick 官方产品及服务信息              |
| [AllTick API 文档](https://alltick.co/apis/en)                                                                | REST API、WebSocket API、参数及集成文档 |
| [AllTick API 示例](https://github.com/alltick/alltick-realtime-forex-crypto-stock-tick-finance-websocket-api) | API 接入示例和开发者资源                 |

---

## 编程语言与开发示例

本 GitHub 仓库包含多个编程语言的 API 接入示例，包括：

* Python
* PHP
* Go
* Java

示例主要用于演示：

* HTTP REST API 请求
* WebSocket 连接
* API Token 鉴权
* 实时行情订阅
* Order Book 订阅
* K 线数据查询
* 心跳处理
* 取消订阅
* 错误处理

开发者可以基于这些示例进一步封装自己的 SDK 或数据访问层。

---

## AllTick 可以用于什么？

AllTick 金融市场数据 API 可以作为各种金融和数据应用的数据基础设施，例如：

* 交易平台
* 金融数据平台
* 实时行情系统
* 股票行情软件
* Forex 应用
* Cryptocurrency 应用
* 金融仪表盘
* 量化研究工具
* 算法交易系统
* 自动化交易应用
* 投资组合应用
* 金融分析软件
* 市场数据可视化应用
* Fintech SaaS 产品
* 开发者项目和教育项目

---

## 快速开始

开始使用 AllTick：

1. 访问 AllTick 官方网站。
2. 阅读 AllTick API 文档。
3. 浏览 GitHub API 示例。
4. 根据应用需求选择 REST API 或 WebSocket API。
5. 按照 API 文档完成 Token 鉴权。
6. 选择需要接入的金融市场和交易品种。
7. 将 AllTick 市场数据集成到自己的应用程序中。

---

## REST API 与 WebSocket API 如何选择？

根据应用场景选择合适的接口：

**需要持续接收实时行情：**

使用 WebSocket API。

例如：

* 实时行情页面
* Trading Terminal
* 市场监控
* 实时数据处理
* 自动化交易系统

**只需要按需查询数据：**

使用 REST API。

例如：

* 查询某个交易品种的最新行情
* 获取 K 线
* 查询历史市场数据
* 后端数据服务
* 数据分析任务

---

## AllTick GitHub

本 GitHub 账号用于维护和发布 AllTick 官方开发者资源，包括：

* 金融市场数据 API 示例
* REST API 示例
* WebSocket API 示例
* API 文档
* 产品及交易品种代码列表
* 多语言开发示例
* 金融市场数据相关技术资源

AllTick GitHub 项目与 AllTick 官方网站及 API 文档共同构成 AllTick 的开发者资源体系。

---

## 官方链接

* 🌐 AllTick 官方网站
* 📚 AllTick API 文档
* 💻 AllTick GitHub
* 📡 AllTick API 示例

---

## 关于 AllTick

AllTick 是一个金融市场数据 API 服务，为开发者和金融应用提供实时及历史市场数据。

AllTick 通过 REST API 和 WebSocket API 提供股票、外汇、加密货币、大宗商品、贵金属和指数等市场的数据访问能力。

**AllTick — Financial Market Data API for Developers.**
