import requests
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
}
page = 0
url = 'https://api.vc.bilibili.com/link_draw/v2/Photo/list?category=cos&type=hot&page_num=' + str(page) + '&page_size=20'
imgurl = 'https://api.vc.bilibili.com/link_draw/v1/doc/detail?doc_id='
for page in range(1, 25):
    a = requests.get(url)
    data = a.json()    # 每个页面返回的json
    for i in data['data']['items']:
        try:
            doc_id = i['item']['doc_id']
            newimgurl = imgurl + str(doc_id)
            actinfo = requests.get(url=newimgurl, headers=headers)
            actinfo = actinfo.json()
            title = actinfo['data']['item']['title']
            print(title)
            os.makedirs(title)
            item = 0
            for ii in actinfo['data']['item']['pictures']:
                try:

                    item += 1
                    pic = requests.get(ii['img_src'])
                    pwd = filepwd + '/' + str(item) + '.jpg'
                    f = open(pwd, 'wb')
                    f.write(pic.content)
                    f.close()
                except:
                    continue
        except:
            continue