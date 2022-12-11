import requests
from bs4 import BeautifulSoup as BS
URL = 'https://cinematica.kg/'
# URL = 'http://www.manascinema.com/'

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0'
}

def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS)
    return req


def get_data(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('div', class_='movie-dummy')
    manas_flm = []
    for item in items:
        manas_flm.append(
            {
                'title': URL + item.find('div', class_='movie-title').get('title'),
                'image': URL + item.find('div', class_='movie-poster').find('img').get('src'),
                # 'description': URL + item.find('div', class_='m_data').get_text()
            }
        )
    return manas_flm


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        manas_flm1 = []
        for page in range(0,1):
            html = get_html(f'https://cinematica.kg/movies', params=page)
            manas_flm1.extend(get_data(html.text))
        return manas_flm1

    else:
        raise Exception('Error in parsing func')