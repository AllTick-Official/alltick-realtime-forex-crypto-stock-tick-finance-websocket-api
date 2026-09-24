package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"net/url"
)

func http_example() {

	/*
		特别注意：
		github: https://github.com/alltick/realtime-forex-crypto-stock-tick-finance-websocket-api
		token申请：https://alltick.co
		把下面url中的testtoken替换为您自己的token
		外汇，加密货币（数字币），贵金属的api址：
		https://quote.alltick.co/quote-b-api
		股票api地址:
		https://quote.alltick.co/quote-stock-b-api
	*/

	// 构建查询字符串
	queryStr := `{"trace":"1111111111111111111111111","data":{"code":"AAPL.US","kline_type":1,"kline_timestamp_end":0,"query_kline_num":10,"adjust_type":0}}`
	
	// 对query进行URL编码
	encodedQuery := url.QueryEscape(queryStr)
	
	// 构建完整的URL
	baseURL := "https://quote.alltick.co/quote-stock-b-api/v1/kline"
	url := fmt.Sprintf("%s/%s", baseURL, encodedQuery)
	
	log.Println("请求内容：", url)

	req, err := http.NewRequest("GET", url, nil)
	if err != nil {
		fmt.Println("Error creating request:", err)
		return
	}

	// 将token放在Header中
	token := "testtoken"
	req.Header.Set("X-API-Key", token)

	// 发送请求
	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		fmt.Println("Error sending request:", err)
		return
	}
	defer resp.Body.Close()

	body2, err := ioutil.ReadAll(resp.Body)

	if err != nil {
		log.Println("读取响应失败：", err)
		return
	}

	log.Println("响应内容：", string(body2))

}

func main() {
	http_example()
}
