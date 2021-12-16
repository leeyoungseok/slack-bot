import requests
from bs4 import BeautifulSoup
import meal_form
import configparser
import json

def config_read():
    with open('config.json') as f:
        config = json.load(f)
    return config
    
def web_crawl(place):
    try:
        req = requests.get('http://cnuis.cnu.ac.kr/jsp/etc/toDayMenu.jsp')
    except:
        return '홈페이지를 불러올 수 없습니다'

    html = req.text
    soup = BeautifulSoup(html, 'lxml')

    selected_elements = soup.select('table.tab_color > tr > td[height="20"]')

    data=[]
    td_count=0
    for element in selected_elements:
        data.append(element.text)
        #print(td_count, element.text)
        td_count+=1

    print("td_count: ", td_count)
    
    #평일엔 td_count==29
    if td_count==29:
        return meal_form.get_form(place, data)
    else: return '오늘은 식당을 운영하지 않습니다'

#if __name__ == '__main__':
#    menu = get("취업지원회관")
#    print(menu)