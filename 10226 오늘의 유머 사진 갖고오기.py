import requests
headers = \
{'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}

url = 'http://www.todayhumor.co.kr/board/list.php?table=bestofbest'
site = requests.get(url, headers=headers)
source_data = site.text

count = source_data.count('<td class="subject">')

#sitelink
for i in range(count):
      pos1 = source_data.find('<td class="subject">') + len('<td class="subject">')
      source_data = source_data[pos1:]

      pos2 = source_data.find('<a href="') + len('<a href="')
      source_data = source_data[pos2:]

      pos3 = source_data.find('" target="')
      sitelink = source_data[:pos3]

#title
      pos4 = source_data.find('top">') + len('top">')
      source_data = source_data[pos4:]

      pos5 = source_data.find('</a>')
      title = source_data[:pos5]

      pos6 = source_data.find('<span')
      source_data = source_data[pos6:]
      
      source_data = source_data[pos6+1:]

#image_range
      url2 = 'http://www.todayhumor.co.kr' + sitelink
      site = requests.get(url2, headers=headers)
      source1_data = site.text

      pos0 = source1_data.find('<div class="viewContent">') + len('<div class="viewContent">')
      source1_data = source1_data[pos0:]

      pos00 = source1_data.find('</div><!--viewContent-->')
      source1_data = source1_data[:pos00]

      count2 = source1_data.count('<img src="')
      for j in range(count2):
            pos01 = source1_data.find('<img src="') + len('<img src="')
            source1_data = source1_data[pos01:]

            pos02 = source1_data.find('"')
            image = source1_data[:pos02]

            #파일로 저장하기
            try:
                  file_name = '{0}{1}.jpg'.format(aaa, j)
                  ss = requests.get(image, headers=headers)
                  file = open(file_name, 'wb')
                  file.write(ss.content)
                  file.close()
            except Exception as e:
                  print(e)

            print(j+1, '||', title, '||', image)
