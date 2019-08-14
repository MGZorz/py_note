import requests
from lxml import etree
from fake_useragent import UserAgent
import re


def get_price_data():
    url = 'http://www.yihuodata.com/%E5%85%A8%E5%9B%BD%E6%88%90%E4%BA%A4%E5%9C%9F%E5%9C%B0%E6%88%90%E4%BA%A4%E5%9C%9F%E5%9C%B0%E5%9D%87%E4%BB%B7-%E6%9C%88%E5%BA%A6%E6%95%B0%E6%8D%AE.html'
    headers = {'User-Agent': UserAgent().chrome}

    resp = requests.get(url, headers=headers)
    e = etree.HTML(resp.text)

    dates = e.xpath('//tr/td[1]/text()')[2:]
    nums = [float(i) for i in e.xpath('//tr/td[2]/text()')[2:]]

    return dates, nums


def get_company_data():
    url = 'http://www.yihuodata.com/2008%E5%B9%B4%E7%A7%81%E8%90%A5%E4%BC%81%E4%B8%9A%E8%B0%83%E6%9F%A5%E6%95%B0%E6%8D%AE-%E5%85%A8%E5%9B%BD%E7%A7%81%E8%90%A5%E4%BC%81%E4%B8%9A%E6%8A%BD%E6%A0%B7%E8%B0%83%E6%9F%A52008%E5%B9%B4%E5%BE%AE.html'
    headers = {'User-Agent': UserAgent().chrome}

    resp = requests.get(url, headers=headers)
    e = etree.HTML(resp.text)

    addrs = [a.replace('\xa0 ', '') for a in e.xpath('//tr/td[1]/text()')[2:]]
    nums = [float(i) for i in e.xpath('//tr/td[2]/text()')[2:]]

    return addrs, nums


def get_movie_data(num):
    url = 'http://www.cbooo.cn/BoxOffice/GetDayBoxOffice?num={}'.format(num)
    headers = {'User-Agent': UserAgent().chrome}
    resp = requests.get(url, headers=headers)
    names = re.findall(r'"MovieName":"(.+?)"', resp.text)
    boxOffice = re.findall(r'"BoxOffice":"(\d+)"', resp.text)

    return names, boxOffice


def get_movie_price_data():
    url = 'http://www.cbooo.cn/year?year=2019'
    headers = {'User-Agent': UserAgent().chrome}
    resp = requests.get(url, headers=headers)
    e = etree.HTML(resp.text)
    prices = [int(n) for n in e.xpath('//tr/td[4]/text()')]
    return prices


if __name__ == '__main__':
    print(get_movie_price_data())
