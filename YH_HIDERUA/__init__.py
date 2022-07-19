import requests
from lxml import etree

YINGHUA = 'http://www.yinghuacd.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}


def __get_yhdm_url(showid):
    """
    返回樱花动漫对应ID的动画的页面链接\n
    如输入5531，返回http://www.yinghuacd.com/show/5531.html

    :param showid: 某部番剧在樱花动漫中对应的id，即例子中的5531
    :return: 完整的链接，即例子中的链接
    """
    return f'http://www.yinghuacd.com/show/{showid}.html'


def check_yhdm_list(showid_list):
    """
    检测数据表yhdm中的番剧是否更新，返回json列表\n

    :param showid_list: showid列表
    :return: [{current_episode:'',url:'',showid:''}]
    """
    result = []
    for showid in showid_list:
        result.append(get_YH_data(showid))
    return result


def get_YH_data(showid):
    """
    根据樱花动漫show栏的id获取数据

    :param showid: show/id/
    :return: json数据
    """
    resp = requests.get(__get_yhdm_url(showid), headers=headers)
    resp.encoding = 'utf-8'
    etree_obj = etree.HTML(resp.text)
    resp.close()
    episodes = etree_obj.xpath('//div[@id="main0"]//ul/li/a/text()')
    current_episode = len(episodes)
    if 'PV' in episodes[current_episode - 1]:
        current_episode = len(episodes) - 1
    return {'current_episode': current_episode, 'url': f'{YINGHUA}/v/{showid}-{current_episode}.html', 'showid': showid}


# 测试用
if __name__ == '__main__':
    print(check_yhdm_list(['1412', '5632', '5603']))
