import operator
import urllib.request as ur
from bs4 import BeautifulSoup as bs
# 웹사이트 정보 가져오기
url = 'https://quotes.toscrape.com/tag/life/'
# 데이터 전처리
html = ur.urlopen(url)
soup = bs(html.read(), 'html.parser')

word_dict = {}
    # 명언 가져오기
for quote_data in soup.find_all('span'):
    quote = quote_data.text
    #단어 빈도 word_dict에 저장
    splited_list = quote.strip().replace("\"","").replace(",","").replace(".","").split(" ")
    for word in splited_list:
        if word in word_dict.keys():
            word_dict[word] += 1
        else:
            word_dict[word] = 1
#빈도 기준 내림차순 정렬
sorted_word_dict= sorted(word_dict.items(), key= operator.itemgetter(1), reverse= True)

#빈도 상위 5개 단어 출력 
word_list = list(sorted_word_dict)
print("등장 횟수 상위 5개 단어")
for i in range(0, 5):
    print(f"{word_list[i][0]} : {word_list[i][1]}") 