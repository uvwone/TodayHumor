import requests
headers = \
{'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}
url = 'http://www.todayhumor.co.kr/board/list.php?table=bestofbest'
site = requests.get(url, headers=headers)
source_data = site.text

count = source_data.count('<td class="subject">')

for i in range(count):
       pos1 = source_data.find('<td class="subject">') + len('<td class="subject">')
       source_data = source_data[pos1:]

       pos2 = source_data.find('<a href="') + len('<a href="')
       source_data = source_data[pos2:]

       pos3 = source_data.find('" target="')
       extract_data = source_data[:pos3]

       source_data = source_data[pos3+1:]
       print(i+1, extract_data.strip())
