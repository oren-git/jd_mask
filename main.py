import sys
from jd_mask_spider_requests import Jd_Mask_Spider

if __name__ == '__main__':
    a = """
  ________   __    _ 
 |___  /\ \ / /   | |
    / /  \ V /    | |
   / /    > < _   | |
  / /__  / . \ |__| |1.预约商品
 /_____|/_/ \_\____/ 其他.秒杀抢购商品 
    """
    start_tool = Jd_Mask_Spider()
    print(a)
    choice_function = input('选择功能:')
    if choice_function == '1':
        start_tool.login()
        start_tool.make_reserve()
    else:
        start_tool.request_seckill_url()
        start_tool.request_seckill_checkout_page()
        start_tool.submit_seckill_order()
