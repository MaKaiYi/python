import sys
import io

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
else:
    # 适用于Python <3.7
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import requests
import time
import datetime

def my_function():
    timestamp = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))) # 北京时间
    try:
        response = requests.get("https://api.juejin.cn/growth_api/v1/")
        response.raise_for_status()
        print(f"[{timestamp}] API 请求成功")
    except requests.exceptions.RequestException as e:
        print(f"[{timestamp}] API 请求失败: {e}")

def check_sign_in_status(base_url, headers):
    api = "get_today_status"
    url = base_url + api
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if data['err_no'] == 0:
            if data['data'] is True:
                print("【今日是否签到】", "已签到")
                return True
            elif data['data'] is False:
                print("【今日是否签到】", "未签到")
                return False
        else:
            print("【当前登录状态】", "未登录,请登录")
            pass
            return False
    else:
        print("【请求失败】", response.status_code)
        return False


def sign_in(base_url, params, headers):
    # data = '{}'
    data = ''
    url = f"{base_url}check_in"
    response = requests.post(url, headers=headers, data=data,params=params)
    if response.status_code == 200:
        try:
            data = response.json()
            if data['err_no'] == 0 and data['err_msg'] == "success":
                print("【当前签到状态】", "签到成功")
                return True
            elif data['err_no'] == 3013 and data['err_msg'] == "掘金酱提示：签到失败了~":
                print("【当前签到状态】", data['err_msg'])
                return False
            elif data['err_no'] == 15001:
                print("【当前签到状态】", '重复签到')
                return True
            else:
                print("【当前签到状态】", data['err_msg'])
                return False
        except requests.JSONDecodeError:
            print("【签到功能】服务器返回的数据无法解析为JSON格式。")
            return False


def get_points(base_url, headers):
    api = "get_cur_point"
    url = base_url + api
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()
            if data['err_no'] == 0 and data['err_msg'] == "success":
                print("【矿石最新余额】", data['data'])
                return data['data']
        except requests.JSONDecodeError:
            print("【获取余额功能】服务器返回的数据无法解析为JSON格式。")
            return False


def get_free(base_url,params, headers):
    url = f"{base_url}lottery_config/get"
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        try:
            data = response.json()
            if data['err_no'] == 0 and data['err_msg'] == "success":
                if data['data']['free_count'] > 0:
                    print("【免费抽奖次数】", data['data']['free_count'])
                    return True
                else:
                    print("【免费抽奖次数】", data['data']['free_count'])
                    return False
        except requests.JSONDecodeError:
            print("【获取免费抽奖次数功能】服务器返回的数据无法解析为JSON格式。")
            return False


def draw(base_url, params, headers):
    url = f"{base_url}lottery/draw"
    # data = '{}'
    data = ''
    response = requests.post(url, headers=headers, data=data,params=params)
    if response.status_code == 200:
        try:
            data = response.json()
            if data['err_no'] == 0 and data['err_msg'] == "success":
                print("【今日抽奖奖品】", data['data']['lottery_name'])
        except requests.JSONDecodeError:
            print("【抽奖功能】服务器返回的数据无法解析为JSON格式。")
            return False


def get_win(base_url, aid, uuid, spider, headers):
    api = "lottery_lucky/my_lucky"
    url = base_url + api
    data = {
        "aid": aid,
        "uuid": uuid,
        "spider": spider
    }
    response = requests.post(url, data=data, headers=headers)
    if response.status_code == 200:
        try:
            data = response.json()
            if data['err_no'] == 0 and data['err_msg'] == "success":
                total_value = data['data']['total_value']
                points = get_points(base_url, header1)
                cha = points - (6000 - total_value) * 20
                print("【当前幸运数值】：", total_value)
                if cha >= 0:
                    print("【距离中奖还差】：0 矿石！")
                elif cha <= 0:
                    print("【距离中奖还差】：", str(abs(cha)) + "矿石！")
        except requests.JSONDecodeError:
            print("【获取免费抽奖次数功能】服务器返回的数据无法解析为JSON格式。")
            return False
    else:
        print("【请求失败】", response.status_code)
        return False



if __name__ == "__main__":
    # 掘金自动签到并抽奖脚本
    my_function()
    # 在左侧的搜索框输入：get_cur_point回车 ，点击任意接口
    cookie ="_tea_utm_cache_2608={%22utm_source%22:%22gold_browser_extension%22}; _tea_utm_cache_2018={%22utm_source%22:%22gold_browser_extension%22}; __tea_cookie_tokens_2608=%257B%2522web_id%2522%253A%25227461602104806540835%2522%252C%2522user_unique_id%2522%253A%25227461602104806540835%2522%252C%2522timestamp%2522%253A1737289647422%257D; passport_csrf_token=b7c6ad6c1b33086fbbe532908c1dd44a; passport_csrf_token_default=b7c6ad6c1b33086fbbe532908c1dd44a; n_mh=muGOT84Hf5_G8_LGfQCbN03zPC1rkU77-nvMRUCsbrU; passport_auth_status=453e32db433428e446b67714e3bb6fa4%2C; passport_auth_status_ss=453e32db433428e446b67714e3bb6fa4%2C; sid_guard=b2614dbe1ea734e2c85b458f136a742e%7C1737289671%7C31536000%7CMon%2C+19-Jan-2026+12%3A27%3A51+GMT; uid_tt=49ca1ca1b34aa5ebecbb3b827be24826; uid_tt_ss=49ca1ca1b34aa5ebecbb3b827be24826; sid_tt=b2614dbe1ea734e2c85b458f136a742e; sessionid=b2614dbe1ea734e2c85b458f136a742e; sessionid_ss=b2614dbe1ea734e2c85b458f136a742e; is_staff_user=false; sid_ucp_v1=1.0.0-KDAxODQxMTAxZTdhZGZjYzg4NjE4ZTU4MjE3YmU5NzBlZDE4MzI5MWIKFwiokrGGgIycBRDH37O8BhiwFDgCQPEHGgJsZiIgYjI2MTRkYmUxZWE3MzRlMmM4NWI0NThmMTM2YTc0MmU; ssid_ucp_v1=1.0.0-KDAxODQxMTAxZTdhZGZjYzg4NjE4ZTU4MjE3YmU5NzBlZDE4MzI5MWIKFwiokrGGgIycBRDH37O8BhiwFDgCQPEHGgJsZiIgYjI2MTRkYmUxZWE3MzRlMmM4NWI0NThmMTM2YTc0MmU; store-region=cn-sh; store-region-src=uid; csrf_session_id=d309ec1893b03730e0d3b23dac72b005"
    aid = "2608"
    uuid = "7461602104806540835"
    spider = "0"
    # msToken  获取后测试 url解码和未解码 哪种可以使用
    # 解密网址1:https://www.toolhelper.cn/EncodeDecode/Url
    # 解密网址2:https://www.bejson.com/enc/urlencode/index.html#google%20vignette

    msToken = '8a_cB7Va9nYETlcsM1wvBeRcLA_8fW1ZGmko5ACgt0I_0M7YFP384eDyZjP0cdq-kVV8htMsIA_QKMZQJ2ygep7CfZqKGl6QVE3UaWA58e2UiHulod3lQGZaym0OO2QfPA=='
    a_bogus = 'Y7sQ6OhdMsm1LDfu0hDz9rsmI1W0YW5dgZEzgD7xczLD'
    base_url = "https://api.juejin.cn/growth_api/v1/"

    common_params = {"aid": aid, "uuid": uuid, "spider": spider, "msToken": msToken, "a_bogus": a_bogus}
    header1 = {
        'Cookie': cookie,
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36'
    }

    if check_sign_in_status(base_url, header1):
        if get_free(base_url,common_params, header1):
            draw(base_url,common_params, header1)
            pass
        else:
            pass
    else:
        if not sign_in(base_url, common_params, header1):
            sign_in(base_url, common_params, header1)
        if get_free(base_url,common_params, header1):
            draw(base_url, common_params, header1)
            pass
        else:
            pass
    get_win(base_url, aid, uuid, spider, header1)
