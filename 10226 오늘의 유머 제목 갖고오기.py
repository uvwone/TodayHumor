#requests 모듈을 이용해서
#네이버 뉴스 메인화면에서 있는 뉴스들 제목 전체 가져오기
import requests

#headers없으면 네이버가 요청차단

def get_url(url):
    headers = \
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}
    site = requests.get(url, headers=headers)       #내용 가져오기
    source_data = site.text
    return source_data


def find_f(source_data, word):
    pos = source_data.find(word) + len(word)
    source_data = source_data[pos:]
    return source_data

def find_b(source_data, word):
    pos = source_data.find(word)
    extract_data = source_data[:pos]
    return extract_data

source_data = get_url('https://news.naver.com')
count = source_data.count('"cjs_t">')


for i in range(count):
    source_data = find_f(source_data, '"cjs_t">')
    extract_data = find_b(source_data, '</div>')
            #pos1 = source_data.find('"cjs_t">') + len('"cjs_t">')       #뉴스 앞 부분위치 지정
           # source_data = source_data[pos1:]                            #해당 위치로 이동

            #pos2 = source_data.find('</div>')         #뉴스 뒷부분 위치 저장
            #extract_data = source_data[: pos2]        #앞부분부터 뒷부분까지 내용 추출해서 저장

            #source_data = source_data[pos2+1:]         #다음뉴스를 찾기위해 뒷부분을 이동시키기
    print(i+1, extract_data)                  #화면에 출력
