import json
import random
import requests
from config import global_config
from lxml import etree

def parse_json(s):
    try:
        begin = s.find('{')
        end = s.rfind('}') + 1
        return json.loads(s[begin:end])
    except Exception as e:
        return False

def get_cookies():
    """解析cookies内容并添加到cookiesJar"""
    manual_cookies = {}
    cookie_string = global_config.getRaw('config', 'cookies_String')
    if len(cookie_string) == 0:
        print('请设置cookie')
        exit(1)

    for item in cookie_string.split(';'):
        key_pare = item.strip().split('=', 1)
        if len(key_pare) != 2:
            print('cookie格式错误')
            exit(1)
        name, value = key_pare
        # 用=号分割，分割1次
        manual_cookies[name] = value
        # 为字典cookies添加内容
    cookiesJar = requests.utils.cookiejar_from_dict(manual_cookies, cookiejar=None, overwrite=True)
    return cookiesJar


def get_session():
    # 初始化session
    session = requests.session()
    session.headers = {"User-Agent": global_config.getRaw('config', 'DEFAULT_USER_AGENT'),
                       "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                       "Connection": "keep-alive"}
    checksession = requests.session()
    checksession.headers = {"User-Agent": global_config.getRaw('config', 'DEFAULT_USER_AGENT'),
                            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                            "Connection": "keep-alive"}
    # 获取cookies保存到session
    session.cookies = get_cookies()
    return session


def get_sku_title():
    """获取商品名称"""
    url = 'https://item.jd.com/{}.html'.format(global_config.getRaw('config', 'sku_id'))
    session = get_session()
    resp = session.get(url).content
    x_data = etree.HTML(resp)
    sku_title = x_data.xpath('/html/head/title/text()')
    return sku_title[0]


def send_wechat(message):
    """推送信息到微信"""
    url = 'http://sc.ftqq.com/{}.send'.format(global_config.getRaw('messenger', 'sckey'))
    payload = {
        "text": '抢购结果',
        "desp": message
    }
    headers = {
        'User-Agent': global_config.getRaw('config', 'DEFAULT_USER_AGENT')
    }
    requests.get(url, params=payload, headers=headers)
