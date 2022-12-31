import requests

def get_url(url):
      headers = \
      {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}
      site = requests.get(url, headers=headers)
      source_data = site.text
      return source_data

def find_f(source_data, a):
      pos = source_data.find(a) + len(a)
      source_data = source_data[pos:]
      return source_data

def find_b(source_data, a):
      pos = source_data.find(a)
      extract_data = source_data[:pos]
      return extract_data

def File(file_name):
      try:
            #file_name = '{0}{1}.jpg'.format(title, j)
            ss = requests.get(image, headers=headers)
            file = open(file_name, 'wb')
            file.write(ss.content)
            file.close()
      except Exception as e:
                  print(e)

source_data = get_url('http://www.todayhumor.co.kr/board/list.php?table=bestofbest')
count = source_data.count('<td class="subject">')

#sitelink
for i in range(count):

      source_data = find_f(source_data, '<td class="subject">')
      source_data = find_f(source_data, '<a href="')
      sitelink = find_b(source_data, '" target="')

#title

      source_data = find_f(source_data, 'top">')
      title = find_b(source_data, '</a>')

      source_data = find_f(source_data, '<span')

#image_range
      ########
      source1_data = get_url('http://www.todayhumor.co.kr'+ sitelink) 
      source1_data = find_f(source1_data, '<div class="viewContent">')
      source1_data = find_b(source1_data, '</div><!--viewContent-->')

      count2 = source1_data.count('<img src="')
      
      for j in range(count2):
            source1_data = find_f(source1_data, '<img src="')
            image = find_b(source1_data, '"')
            source1_data = find_f(source1_data, '"')
            #파일로 저장하기
            source1_data = File('{0}{1}.jpg'.format(title, j))

            print(j+1, '||', title, '||', image)
