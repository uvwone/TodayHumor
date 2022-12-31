import requests

def get_url(url):
    headers = \
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}

    for a in range(1, 6):
        #url = 'http://www.todayhumor.co.kr/board/list.php?table=bestofbest&page={0}'.format(a)
        site = requests.get(url, headers=headers)
        source_data = site.text

        #count = source_data.count('<td class="subject">')
    return source_data

def find_f(source_data, a):
    pos = source_data.find(a) + len(a)
    source_data = source_data[pos:]
    return source_data

def find_b(source_data, a):
    pos = source_data.find(a)
    extract_data = source_data[:pos]
    return extract_data

       
#sitelink
source_data = get_url('http://www.todayhumor.co.kr/board/list.php?table=bestofbest')
count = source_data.count('<td class="subject">')

for i in range(count):

      source_data = find_f(source_data, '<td class="subject">')
      source_data = find_f(source_data, '<a href="')
      sitelink = find_b(source_data, '" target="')
            #pos1 = source_data.find('<td class="subject">') + len('<td class="subject">')
            #source_data = source_data[pos1:]

            #pos2 = source_data.find('<a href="') + len('<a href="')
            #source_data = source_data[pos2:]

            #pos3 = source_data.find('" target="')
            #sitelink = source_data[:pos3]

      #titleaa

      source_data = find_f(source_data, 'top">')
      title = find_b(source_data, '</a>')
      source_data = find_f(source_data, '<span')
            
            #pos4 = source_data.find('top">') + len('top">')
            #source_data = source_data[pos4:]

            #pos5 = source_data.find('</a>')
            #title = source_data[:pos5]

            #pos6 = source_data.find('<span')
            #source_data = source_data[pos6:]
            
            #source_data = source_data[pos6+1:]

      #image_range
      source_data = get_url('http://www.todayhumor.co.kr'+sitelink)
      count2 = source_data.count('<img src="')
            #url2 = 'http://www.todayhumor.co.kr' + sitelink
            #site = requests.get(url2, headers=headers)
            #source1_data = site.text

      source_data = find_f(source_data, '<div class="viewContent">')
      source_data = find_f(source_data, '</div><!--viewContent-->')
            #pos0 = source1_data.find('<div class="viewContent">') + len('<div class="viewContent">')
            #source1_data = source1_data[pos0:]

            #pos00 = source1_data.find('</div><!--viewContent-->')
            #source1_data = source1_data[:pos00]


      for j in range(count2):

            source_data = find_f(source_data, '<img src="')
            image = find_b(source_data, '"')
            #pos01 = source1_data.find('<img src="') + len('<img src="')
            #source1_data = source1_data[pos01:]

            #pos02 = source1_data.find('"')
            #image = source1_data[:pos02]

                  #파일로 저장하기

                  ##aaa = title.replace('?', 'a')
                  
                  ##file_name = '{0}{1}.jpg'.format(aaa, j)
                  ##ss = requests.get(image, headers=headers)
                  ##file = open(file_name, 'wb')
                  #file.write(ss.content)

                  ##file.close()

            print(j+1, '|', title, '||', image)
            
