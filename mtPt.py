import requests
import logging

# 配置日志
logging.basicConfig(
    filename=r'C:\Users\18323\Desktop\python.log', # 设置日志文件路径
    level=logging.INFO,  # 设置日志级别
    format='%(asctime)s - %(levelname)s - %(message)s'  # 设置日志格式
)

def check_in(headers):
    url = 'https://api.juejin.cn/growth_api/v1/check_in'
    try:
        response = requests.post(url, headers=headers)
        if response.status_code == 200:
            print("签到成功:", response.json())
            logging.info("签到成功: %s", response.json())
        else:
            print("签到失败:", response.status_code, response.text)
            logging.error("签到失败: %d - %s", response.status_code, response.text)
    except Exception as e:
        logging.exception("请求异常: %s", str(e))

if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'Cookie': '__tea_cookie_tokens_2608=%257B%2522web_id%2522%253A%25227374318383540291122%2522%252C%2522user_unique_id%2522%253A%25227374318383540291122%2522%252C%2522timestamp%2522%253A1716967312034%257D; passport_csrf_token=410b16a5b047e5ec2538d32846de36b6; passport_csrf_token_default=410b16a5b047e5ec2538d32846de36b6; n_mh=muGOT84Hf5_G8_LGfQCbN03zPC1rkU77-nvMRUCsbrU; sid_guard=d62ad9eaab7148650da0c33bb02e49b6%7C1716967389%7C31535999%7CThu%2C+29-May-2025+07%3A23%3A08+GMT; uid_tt=c4f3dc0b9ab6a09aecf0e71cbaafdf86; uid_tt_ss=c4f3dc0b9ab6a09aecf0e71cbaafdf86; sid_tt=d62ad9eaab7148650da0c33bb02e49b6; sessionid=d62ad9eaab7148650da0c33bb02e49b6; sessionid_ss=d62ad9eaab7148650da0c33bb02e49b6; sid_ucp_v1=1.0.0-KGNlMWE1M2JlNGQxMjMxN2YwMjEwNDA0ZmU3YjI2ZGEwYmU5OGZlMjIKFwiokrGGgIycBRDdr9uyBhiwFDgCQPEHGgJsZiIgZDYyYWQ5ZWFhYjcxNDg2NTBkYTBjMzNiYjAyZTQ5YjY; ssid_ucp_v1=1.0.0-KGNlMWE1M2JlNGQxMjMxN2YwMjEwNDA0ZmU3YjI2ZGEwYmU5OGZlMjIKFwiokrGGgIycBRDdr9uyBhiwFDgCQPEHGgJsZiIgZDYyYWQ5ZWFhYjcxNDg2NTBkYTBjMzNiYjAyZTQ5YjY; store-region=cn-sh; store-region-src=uid; _tea_utm_cache_2608={%22utm_source%22:%22gold_browser_extension%22}; _tea_utm_cache_2018={%22utm_source%22:%22gold_browser_extension%22}; _tea_utm_cache_576092=undefined; _tea_utm_cache_6587={%22utm_source%22:%22jj_nav%22}; csrf_session_id=57f6c0c03a9517d322fb28e3cf9d3eb2'
    }
    logging.debug("Headers: %s", headers)
    check_in(headers)
    logging.debug("脚本执行完毕")
