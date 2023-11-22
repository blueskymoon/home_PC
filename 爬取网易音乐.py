import requests
from lxml import etree

headers = {
    'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

#1.请求歌手歌单页面
singer_url = input('请输入你想下载的歌手链接')
url = singer_url.replace('/#','')
response = requests.get(url=url,headers=headers)

#2.筛选所有的音乐标签数据
html = etree.html(requests.text)
music_label_list = html.xpath('//a[contains(@herf,"/song?")]')  #  //表示相对路径，[contains]是表示模糊查询，(@href,"/song?")@表示属性为/song？

#3、循环遍历每首歌的标签
for music_label in music_label_list:
    href =music_label.xpth('./@href')[0]
    music_id = href.split('=')[1]
    music_name = music_label.xpth('./text()')[0]