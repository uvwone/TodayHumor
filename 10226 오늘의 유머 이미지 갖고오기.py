import requests
headers = \
{'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}

url = 'http://www.todayhumor.co.kr/board/view.php?table=bestofbest&no=461206&s_no=461206&page=1'
site = requests.get(url, headers=headers)
source_data = site.text

pos0 = source_data.find('<div class="viewContent">') + len('<div class="viewContent">')
source_data = source_data[pos0:]

pos00 = source_data.find('</div><!--viewContent-->')
source_data = source_data[:pos00]

count = source_data.count('<div class="')

for i in range(count):
       pos1 = source_data.find('<img src="') + len('<img src="')
       source_data = source_data[pos1:]

       pos2 = source_data.find('" width=')
       extract_data = source_data[:pos2]

       source_data = source_data[pos2+1:]
       print(i+1, extract_data.strip())
