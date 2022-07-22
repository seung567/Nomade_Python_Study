import os
import csv
import requests
from bs4 import BeautifulSoup


# 각 홈페이지 URL 추출
def alba_url_val():
    os.system("cls")
    url = "http://www.alba.co.kr"

    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")

    brand = soup.find("div", {"id": "MainSuperBrand"})
    brand_info = brand.find_all("li", {"class": "impact"})

    return brand_info


def link_title(url):

    name = url.find("span", {"class": "company"}).string
    link = url.find("a", {"class": "goodsBox-info"})
    links = link["href"]

    return name, links


# 정보 가져오기


def alba_info(brand_url, name=""):
    print(brand_url)
    result1 = requests.get(brand_url)
    soup1 = BeautifulSoup(result1.text, "html.parser")

    job = soup1.find("div", {"class", "goodsJob"})
    tbody = job.find("tbody")
    tr = tbody.find_all("tr", {"class": ""})

    try:
        count = job.find("p", {"class": "jobCount"}).strong.string
    except:
        try:
            count = job.find("p", {"class": "listCount"}).strong.string
        except:
            pass

    return tr, count


def alba_search(info, title):

    alba_dit = {'name': title, 'jobs': []}

    #for i in info:
    loacl = info.find("td", {"class": "local"}).text.replace("\xa0","")  # 근무지
    company = info.find("span", {"class": "company"}).text.strip()  # 매장명
    # 근무시간
    time_val = time = info.find("span", {"class": "time"})
    if time_val == None:
        time = info.find("span", {"class": "consult"}).text.strip()
    else:
        time = info.find("span", {"class": "time"}).text.strip()
    pay = info.find("span", {"class": "number"}).text.strip()
    try:
      uptime = info.find("td", {"class", "regDate"}).strong.string
    except:
      uptime = info.find("td", {"class", "regDate"}).string
      
    #print(f"{loacl} / {company} / {time} / {pay} /{uptime}\n")

    alba_dit['jobs'] = {
        'loacl': loacl,
        'title': company,
        'time': time,
        'pay': pay,
        'uptime': uptime
    }
    return alba_dit

