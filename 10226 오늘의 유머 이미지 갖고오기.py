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


source_data = get_url('http://www.todayhumor.co.kr/board/view.php?table=bestofbest&no=461206&s_no=461206&page=1')
source_data = find_f(source_data, '<div class="viewContent">')
source_data = find_b(source_data, '</div><!--viewContent-->')

#pos0 = source_data.find('<div class="viewContent">') + len('<div class="viewContent">')
#source_data = source_data[pos0:]

#pos00 = source_data.find('</div><!--viewContent-->')
#source_data = source_data[:pos00]
    
count = source_data.count('<div class="')

for i in range(count):

        source_data = find_f(source_data, '<img src="')
        extract_data = find_b(source_data, '" width=')
       #pos1 = source_data.find('<img src="') + len('<img src="')
       #source_data = source_data[pos1:]

       #pos2 = source_data.find('" width=')
       #extract_data = source_data[:pos2]

       #source_data = source_data[pos2+1:]
        print(i+1, extract_data.strip())
