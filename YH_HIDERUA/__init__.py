import requests


def __get_yhdm_url(showid):
    """
    返回樱花动漫对应ID的动画的页面链接\n
    如输入5531，返回http://www.yinghuacd.com/show/5531.html

    :param showid: 某部番剧在樱花动漫中对应的id，即例子中的5531
    :return: 完整的链接，即例子中的链接
    """
    return f'http://www.yinghuacd.com/show/{showid}.html'

def check_yhdm_list()->dict:
    """
    检测数据表yhdm中的番剧是否更新，返回json数据\n
    {"result":"True","data":[...]}\n
    result对应该函数的执行结果，后面的data对应更新的数据

    :return: 函数执行结果和获得的数据
    """
