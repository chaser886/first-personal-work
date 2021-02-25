import re
import time
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}

sou='1613797084480'
cursor = '0'
new_list = []
new_list1=[]

for item in range(0,1046):
    url = "https://coral.qq.com/article/5963120294/comment/v2?callback=_article5963120294commentv2&orinum=10&oriorder=o&pageflag=1&cursor=" + cursor + "&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=1&_=" + str(sou)
    source = requests.get(url, headers=headers).content.decode()
    result = re.findall('"content":"(.*?)",', source, re.S)
    new_list.append(result)
    cursor = re.findall('"last":"(.*?)","', source, re.S)[0]

with open("zyq.txt", "w", encoding="utf-8", errors="ignore") as f:
    for item in new_list:
        for j in item:
            f.write(j)
            f.write("\n")
# new_list=list()
# base_url = 'https://coral.qq.com/article/5963120294/comment/v2?callback=_article5963120294commentv2&orinum=10&oriorder=o&pageflag=1&cursor=0&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=1&_=1614226392907'
# html=requests.get(base_url,headers=header).content.decode(encoding='gbk')
# cursor=re.findall('.*?"last":"(.*?)"',html,re.S)
#
# for i in ranges(0,1046):
#     sources += 1
#     url = 'https://coral.qq.com/article/5963120294/comment/v2?callback=_article5963120294commentv2&orinum=10&oriorder=o&pageflag=1&cursor=‘ + str(cursor) + ’&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=1&_='+str(sources)
#     html = requests.get(url,headers = header).content.decode()
#     cursor = re.findall('.*?"last":"(.*?)"', html, re.S)
#
#     item_dict=re.findall('"content=":"(.*?)"',html,re.S)
#     new_list.append(item_dict)
# print(new_list)
# # with open('zyq.csv','w',encoding='utf-8') as f:
# #     writer =csv.DictWriter(f,fieldnames=[''])
# #     writer .writeheader()
# #     writer .writerows(new_list)