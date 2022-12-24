import requests
def get_url_information(url):
      headers = \
      {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}
      site = requests.get(url, headers=headers)
      source_data = site.text
      return source_data

def find_front(source_data, word):
      pos = source_data.find(word) + len(word)
      source_data = source_data[pos:]
      return source_data

def find_back(s, w):
      pos = s.find(w)
      extract = s[:pos]
      return extract

def file_down(file_name):
      try:
            #file_name = '{0}{1}.jpg'.format(a1, j)
            ss = requests.get(image, headers=headers)
            file = open(file_name, 'wb')
            file.write(ss.content)
            file.close()

      except Exception as e:
            print(e)
      

source_data = get_url_information('http://www.todayhumor.co.kr/board/list.php?table=bestofbest')


count = source_data.count('<td class="subject">')

#sitelink
for i in range(count):
      source_data = find_front(source_data, '<td class="subject">')
      
      #pos1 = source_data.find('<td class="subject">') + len('<td class="subject">')
      #source_data = source_data[pos1:]

      source_data = find_front(source_data, '<a href="')
      
      #pos2 = source_data.find('<a href="') + len('<a href="')
      #source_data = source_data[pos2:]

      sitelink = find_back(source_data, '" target="')
      #pos3 = source_data.find('" target="')
      #sitelink = source_data[:pos3]

#title

      source_data = find_front(source_data, 'top">')
      #pos4 = source_data.find('top">') + len('top">')
      #source_data = source_data[pos4:]

      title = find_back(source_data, '</a>')
      #pos5 = source_data.find('</a>')
      #title = source_data[:pos5]

      source_data = find_front(source_data, '<span')
      #pos6 = source_data.find('<span')
      #source_data = source_data[pos6:]

      #source_data = source_data[pos6+1:]

#image_range
      source1_data = get_url_information('http://www.todayhumor.co.kr' + sitelink)
      #url = 'http://www.todayhumor.co.kr' + sitelink
      #site = requests.get(url, headers=headers)
      #source1_data = site.text

      source1_data = find_front(source1_data, '<div class="viewContent">')
      #pos0 = source1_data.find('<div class="viewContent">') + len('<div class="viewContent">')
      #source1_data = source1_data[pos0:]

      source1_data = find_back(source1_data, '</div><!--viewContent-->') 
      #pos00 = source1_data.find('</div><!--viewContent-->')
      #source1_data = source1_data[:pos00]

      count2 = source1_data.count('<img src="')
      for j in range(count2):

            source1_data = find_front(source1_data, '<img src="')
            #pos01 = source1_data.find('<img src="') + len('<img src="')
            #source1_data = source1_data[pos01:]

            image = find_back(source1_data, '"')
            #pos02 = source1_data.find('"')
            #image = source1_data[:pos02]

            #파일로 저장하기  #파일만 해결하면 될 거 같은데..
            source1_data = file_down('{0}{1}.jpg'.format(title, j))

            print(j+1, '||', title, '||', image)
