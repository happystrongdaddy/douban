from bs4 import BeautifulSoup
import requests

url = 'https://movie.douban.com/top250?start=0&filter='
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3861.400 QQBrowser/10.7.4313.400'
}
source = requests.get(url, headers=headers)

soup = BeautifulSoup(source.text, 'lxml')

for info in soup.find_all('div', class_="info"):

    # 提取电影名称，包括中文名称，英文名称和别名
    title_name = []
    for title in info.find_all('span', class_="title"):

        title_name.append("".join(title.text.split()))
    # 增加其他名字部分
    title_other = info.find('span', class_="other").text
    title_other = "".join(title_other.split())
    print(title_other)
    # 把list数据类型转成string类型
    title_name_str = ''.join(title_name)
    # 把电影名字整合
    title_full = title_name_str+title_other
    print(title_full)

    bd = info.p.text.strip()
    bd = "".join(bd.split())
    print(bd)
    rating_num = info.find('span', class_="rating_num").text

    star = info.find("div", class_="star").text
    rate_list = star.split()
    print(star)
    print(rate_list)

for a in range(10):
    url = 'https://movie.douban.com/top250?start='+str(a*25)+'&filter='
    # print(url)
