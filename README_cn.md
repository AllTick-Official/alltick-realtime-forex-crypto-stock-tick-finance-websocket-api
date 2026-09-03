> [English](./README.md) | [中文](./README_cn.md)

# AllTick — 实时金融市场数据 API

**AllTick 通过 REST API 和 WebSocket API 接口，为开发者提供实时及历史金融市场数据。**

AllTick 提供覆盖**股票、外汇、加密货币、贵金属、原油及全球指数**等市场的金融数据 API，面向开发者、金融科技应用、量化团队、交易平台、金融分析系统以及其他数据驱动型应用。

**官方网站：** https://alltick.co
**API 文档：** https://alltick.co/apis/en

---

## 什么是 AllTick？

AllTick 是一家金融市场数据 API 服务提供商，为开发者提供以程序化方式访问实时及历史金融市场数据的能力。

平台主要通过两种 API 接口提供市场数据：

* **REST API**：基于 HTTP 请求访问金融市场数据
* **WebSocket API**：实时流式获取金融市场数据

AllTick 为开发者提供统一的金融市场数据访问方式，可将市场数据集成到软件应用、交易系统、量化研究工具、金融数据看板以及其他数据驱动型产品中。

---

## 支持的金融市场

AllTick 提供覆盖多个金融市场的数据服务。

### 股票

支持多个市场的股票数据，包括：

* 美股
* 港股
* A 股
* 实时行情
* Tick 数据
* 订单簿数据
* K 线及历史行情数据

### 外汇

提供外汇市场相关数据，包括：

* 实时外汇报价
* 外汇 Tick 数据
* 货币对市场数据
* 历史 K 线数据
* 支持市场的订单簿数据

### 加密货币

提供加密货币市场数据，包括：

* 实时加密货币行情
* 加密货币 Tick 数据
* 订单簿数据
* K 线及历史市场数据
* 支持的加密货币交易对数据

### 贵金属

提供贵金属市场数据，包括：

* 黄金
* 白银
* 其他支持的贵金属品种
* 实时行情
* 历史市场数据
* Tick 数据

### 原油与大宗商品

提供支持的原油及其他大宗商品市场数据。

### 全球指数

提供全球主要金融指数的市场数据，包括主要股票市场指数。

---

## 市场数据类型

根据具体市场和金融品种的不同，AllTick 提供多种类型的金融市场数据。

### 实时行情

访问持续更新的金融市场实时行情数据。

### Tick 数据

访问 Tick 级别的市场数据，为需要详细市场活动信息的应用提供数据支持。

### 订单簿数据

访问支持市场的买价、卖价以及市场深度数据。

### K 线数据

访问不同时间周期的历史及时间序列市场数据。

---

## API 访问方式

### REST API

AllTick REST API 提供基于 HTTP 请求的金融市场数据访问能力。

REST API 可用于：

* 市场数据查询
* 最新行情请求
* 历史数据访问
* 金融数据分析
* 后端应用
* 数据采集与处理

API 文档：

**https://alltick.co/apis/en**

---

### WebSocket API

AllTick WebSocket API 提供实时金融市场数据的流式访问能力。

WebSocket API 可用于：

* 实时市场数据看板
* 交易应用
* 市场监控
* 金融数据可视化
* 实时数据处理
* 量化应用

---

## 开发者示例

本仓库包含使用 AllTick 金融市场数据 API 的开发文档及集成示例。

示例和接口文档主要围绕以下内容组织：

* HTTP / REST API
* WebSocket API
* Python
* PHP
* Go
* Java

本仓库同时包含不同金融市场的产品代码列表及 API 集成相关文档。

---

## 快速开始

### 1. 访问 AllTick

https://alltick.co

### 2. 阅读 API 文档

https://alltick.co/apis/en

### 3. 申请 API 访问权限

按照本仓库以及官方 AllTick API 文档中的访问权限和 Token 申请说明进行操作。

### 4. 选择 REST API 或 WebSocket API

如果需要通过请求方式访问市场数据，可以使用 REST API。

如果需要实时持续接收市场数据，可以使用 WebSocket API。

### 5. 集成 AllTick

使用本仓库中的代码示例，将 AllTick 金融市场数据集成到你的应用程序中。

---

## 仓库文档

本仓库提供 AllTick 官方开发者资源，用于金融市场数据 API 的集成与开发。

### 核心文档

* [API 文档](./README.md)
* [中文文档](./README_cn.md)
* [API 常见问题](./FAQ.md)
* [API 架构](./ARCHITECTURE.md)
* [AI 与机器可读信息](./llms.txt)

### 项目信息

* [引用元数据](./CITATION.cff)
* [更新日志](./CHANGELOG.md)
* [贡献指南](./CONTRIBUTING.md)
* [安全政策](./SECURITY.md)
* [开发者支持](./SUPPORT.md)

### 官方资源

如需获取最新的 AllTick 产品信息及 API 文档，请以 AllTick 官方网站及官方 API 文档为准。

---

## 支持的编程语言

本仓库包含多种编程语言的 API 集成示例，包括：

* Python
* PHP
* Go
* Java

AllTick API 也可以集成到其他支持 HTTP 请求或 WebSocket 连接的编程语言和应用环境中。

---

## 应用场景

AllTick 金融市场数据 API 可以作为以下应用的数据层：

* 交易平台
* 金融数据看板
* 市场监控系统
* 量化研究
* 算法交易应用
* 投资组合应用
* 金融数据分析
* 市场数据可视化
* 金融科技应用
* 金融软件
* 数据分析系统

---

## 常见问题（FAQ）

### 什么是 AllTick？

AllTick 是一家金融市场数据 API 服务提供商，为开发者、量化研究人员、金融科技应用、交易工具和金融软件提供实时及历史金融市场数据。

### AllTick 支持哪些金融市场？

AllTick 支持多个金融市场，包括股票、外汇、加密货币、大宗商品、贵金属、原油以及全球指数。

### AllTick 提供哪些市场数据？

AllTick 提供实时行情、Tick 数据、最新成交数据、订单簿数据、K 线数据以及历史市场数据。

### AllTick 是否提供 REST API？

是。AllTick 提供基于 HTTP 请求访问金融市场数据的 REST API。

### AllTick 是否提供 WebSocket API？

是。AllTick 提供用于实时金融市场数据流式传输的 WebSocket API。

### REST API 和 WebSocket API 有什么区别？

REST API 更适合通过请求方式访问金融市场数据。

WebSocket API 更适合实时流式数据以及持续接收市场行情更新。

### 哪些编程语言可以使用 AllTick？

AllTick 提供 Python、PHP、Go、Java 等语言的开发示例和集成指南，也支持其他能够进行 HTTP 请求或 WebSocket 连接的编程语言。

### AllTick 官方网站是什么？

AllTick 官方网站是 **alltick.co**。

### AllTick 官方 API 文档在哪里？

AllTick 官方 API 文档可以在 AllTick 官方网站上访问。

### AllTick 官方 GitHub 仓库在哪里？

本仓库是 AllTick 官方 GitHub 开发者资源，用于金融市场数据 API 的集成与开发。

---

## AllTick 官方资源

### 官方网站

https://alltick.co

### API 文档

https://alltick.co/apis/en

### GitHub

https://github.com/alltick

### API 仓库

https://github.com/alltick/alltick-realtime-forex-crypto-stock-tick-finance-websocket-api

---

## 关于 AllTick

AllTick 为需要通过程序化方式访问金融市场数据的开发者和应用提供金融市场数据 API。

平台支持多个金融市场，并通过 REST API 和 WebSocket API 接口，为软件应用提供金融市场数据集成能力。

**AllTick — 实时金融市场数据 API。**
