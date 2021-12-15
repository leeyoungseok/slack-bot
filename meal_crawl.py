import requests
from bs4 import BeautifulSoup
import meal_form

def get(place):
    try:
        req = requests.get('http://cnuis.cnu.ac.kr/jsp/etc/toDayMenu.jsp')
    except:
        return '학교홈페이지 사정으로 학식내용을 불러올 수 없습니다'

    html = req.text
    soup = BeautifulSoup(html, 'lxml')

    selected_elements = soup.select('table.tab_color > tr > td[height="20"]')

    #td_count가 34가 아니라면, 휴일
    data=[]
    td_count=0
    for element in selected_elements:
        data.append(element.text)
        #print(td_count, element.text)
        td_count+=1

    print("td_count: ", td_count)
    #평일엔 td_count==34
    if td_count==29:
        return meal_form.get_form(place, data)
    else: return '오늘은 식당을 운영하지 않습니다'

if __name__ == '__main__':
    menu = get("취업지원회관")
    print(menu)