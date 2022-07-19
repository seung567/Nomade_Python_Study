import requests
from bs4 import BeautifulSoup


LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

def extract_indeed_pages() :

    # 페이지 정보 가져오기
    result = requests.get(URL)

    # 추출 형식 정하기
    soup = BeautifulSoup(result.text, "html.parser")

    pagination = soup.find("div", {"class":"pagination"})

    links = pagination.find_all("a")

    pages= []

    for link in links[:-1] :
        pages.append(int(link.string))


    max_page = pages[-1]

    return max_page


def extract_indeed_jobs(last_page):

    jobs = []

    # for page in range(last_page) :

    result = requests.get(f"{URL}&start={0*LIMIT}")

    soup = BeautifulSoup(result.text, "html.parser")

    results = soup.find_all("div" , {"class" : "jobsearch-SerpJobCard"})

    for result in results :

        print(result.find("div" , {"class" : "title"}))
    
    return jobs


last_indeed_page = extract_indeed_pages()

extract_indeed_jobs(last_indeed_page)