#######################
# https://pypi.org/
#  - request
#  - BeautifulSoup
#######################
import requests
from bs4 import BeautifulSoup

allJobs = []

def scrapePage(url):
    print(f"Scrapping {url}...")
    response = requests.get(url)    
    # 요청 중에 503 error 발생하면 -> 웹페이지 network에서 header 따와서 붙여주자 ex) requests.get(url)
    # ex) r = requests.get("url", headers={"User-Agent":"blahblahblahblahblah..."})
    soup = BeautifulSoup(
        response.content,
        "html.parser",
    )

    # jobs = soup.find("section", id="category-2")
    jobs = soup.find("section", class_="jobs").find_all("li")[1:-1]   # call <li> all, except for the first one and last one <[1:-1]>

    for eachJob in jobs:
        # title = eachJob.find("span", class_="title").text   # only text
        # region = eachJob.find("span", class_="region").text
        # company, position, _ = eachJob.find("span", class_="company")   # _ -> 빈 변수로 생각해도 됨

        title = eachJob.find("span", class_="title").text
        company, position, region = eachJob.find_all("span", class_="company")
        url = eachJob.find("div", class_="tooltip--flag-logo").next_sibling["href"]

        jobData ={
            "title": title,
            "company": company.text,
            "position": position.text,
            "region": region.text,
            "url": f"https://weworkremotely.com{url}",  # 터미널 내에서 링크 클릭 가능
        }
        allJobs.append(jobData)

def getPages(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    return len(soup.find("div", class_="pagination").find_all("span", class_="page"))    # len : return array length

totalPages = getPages("https://weworkremotely.com/remote-full-time-jobs?page=1")

for x in range(totalPages):
    url = f"https://weworkremotely.com/remote-full-time-jobs?page{x+1}"
    scrapePage(url)
    # print("request page", x + 1)

print(len(allJobs))
# url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs"



# print(allJobs)

# print(response.content) # the source code of the URL