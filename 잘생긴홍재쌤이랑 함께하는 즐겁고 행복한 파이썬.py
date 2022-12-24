#requests 모듈을 이용해서
#네이버 뉴스 메인화면에서 있는 뉴스들 제목 전체 가져오기
import requests
#headers없으면 네이버가 요청차단

# 1. 요거 뭐하는 기능이야???
# 2. 입력값이 뭐가 필요할까???

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

      
#찾는거?

#이거앞에 
#url = 'http://www.todayhumor.co.kr/board/list.php?table=bestofbest'


  
source_data = get_url_information('http://www.todayhumor.co.kr/board/list.php?table=bestofbest')

count = source_data.count('<tr class="view')

for i in range(count):
      source_data = find_front(source_data, 'top">')
      extract_data = find_back(source_data, '</a>')
      print(extract_data)

     
