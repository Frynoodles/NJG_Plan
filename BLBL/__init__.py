import requests


last_info_url = 'https://api.bilibili.com/pgc/review/user?media_id='  # 可从这个获得season_id

episodes_info_url = 'https://api.bilibili.com/pgc/web/season/section?season_id='

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'referer': 'https://www.bilibili.com/'
}


def get_info(season_id):
    """
    获取更加详细的信息

    :param season_id: season id
    :return: json 数据
    """
    data = requests.get(episodes_info_url + season_id, headers=headers).json()
    if not data['message'] == 'success':
        return {}
    episodes = data['result']['main_section']['episodes']
    info = episodes[len(episodes) - 1]
    cover = info['cover']
    title = info['long_title']
    return {'cover': cover, 'title': title}


def get_BLBL_data(mid):
    """
    获取指定mid番剧的信息

    :param mid: 番剧的mid
    :return: json数据
    """
    data = requests.get(last_info_url + mid, headers=headers).json()
    media = data['result']['media']
    if not data['message'] == 'success':
        return {}
    return {'current_episode': media['new_ep']['index'], 'mid': mid, 'season_id': str(media['season_id']),
            'url': f'https://www.bilibili.com/bangumi/play/ep{media["new_ep"]["id"]}'}


if __name__ == '__main__':
    # print(requests.get(last_info_url + '28237128', headers=headers).json())
    # print(requests.get(last_info_url + '28338638', headers=headers).json())
    # print(get_BLBL_data('28338638'))
    # print(get_info('42191'))
    pass
