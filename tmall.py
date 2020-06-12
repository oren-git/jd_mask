import sys
import time
from jdlogger import logger
import requests
from util import parse_json, get_session, send_wechat
from config import global_config
from datetime import datetime

if __name__ == '__main__':
    session = get_session(global_config.getRaw('config', 'taobao_cookie'))
    default_user_agent = global_config.getRaw('config', 'DEFAULT_USER_AGENT')
    url = 'https://buy.tmall.com/order/confirm_order.htm?spm=a1z0d.6639537.0.0.undefined'
    data = {
        'hex': 'n',
        'cartId': '2100691728223',
        'sellerid': '725677994',
        'cart_param': '{"items":[{"cartId":"2100691728223","itemId":"20739895092","skuId":"4227830352490","quantity":2,"createTime":1591663891000,"attr":";op:149900;cityCode:420114;itemExtra:{};"}]}',
        'unbalance': '',
        'delCartIds': '2100691728223',
        'use_cod': 'false',
        'buyer_from': 'cart',
        'page_from': 'cart',
        'source_time': str(int(time.time() * 1000)),
    }
    headers = {
        'User-Agent': default_user_agent,
        'origin': 'https://cart.taobao.com',
        'referer': 'https://cart.taobao.com/cart.htm?spm=875.7931836%2FB.a2226mz.11.661442656qyO5f&from=btop'
    }
    resp = session.post(url=url, data=data, headers=headers)
    logger.info(resp.text)
