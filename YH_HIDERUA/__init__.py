import requests
from lxml import etree

YINGHUA = 'http://www.yinghuacd.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'Referer': 'http://www.yinghuacd.com/'
}


def __get_yhdm_url(showid):
    """
    返回樱花动漫对应ID的动画的页面链接\n
    如输入5531，返回http://www.yinghuacd.com/show/5531.html

    :param showid: 某部番剧在樱花动漫中对应的id，即例子中的5531
    :return: 完整的链接，即例子中的链接
    """
    return f'http://www.yinghuacd.com/show/{showid}.html'


def check_yhdm_list(showid_list: list[str]) -> dict:
    """
    检测数据表yhdm中的番剧是否更新，返回json数据\n
    {"result":"True","data":[...]}\n
    result对应该函数的执行结果，后面的data对应更新的数据

    :param showid_list: showid列表
    :type showid_list: list[str]
    :return: 函数执行结果和获得的数据
    """
    for showid in showid_list:
        pass


def get_one_am_data(showid: str) -> dict:
    resp = requests.get(YINGHUA + showid, headers=headers)
    print(resp.text)
    resp.close()
    pass


# 测试用
if __name__ == '__main__':
    pass
