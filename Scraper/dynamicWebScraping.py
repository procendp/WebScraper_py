###########################
# https://playwright.dev/
#  - playwright
###########################

from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
import csv

p = sync_playwright().start()

browser = p.chromium.launch(headless=False) # headless= False : open the browser / True : not open, but can do all without browser

page = browser.new_page()

page.goto("https://www.wanted.co.kr/jobsfeed")

time.sleep(4)   # making slowly for checking click well

page.click("button.Aside_searchButton__rajGo")
# page.locator("button.Aside_searchButton__rajGo").click()  # 위와 같음
# page.screenshot(path="screenshot.png")    # screenshot to browser

time.sleep(4)

page.get_by_placeholder("검색어를 입력해 주세요.").fill("flutter")  # writing to input... 이 외에도 다양한 것들로 가져올 수 있음

time.sleep(4)

page.keyboard.down("Enter")

time.sleep(4)

page.click("a#search_tab_position")

time.sleep(4)

for x in range(5):
    page.keyboard.down("End")
    time.sleep(4)

content = page.content()    # 사이트 컨텐츠 가져오기

p.stop()

soup = BeautifulSoup(content, "html.parser")

jobs = soup.find_all("div", class_="JobCard_container__REty8")  # list

jobsDB = []

for eachJob in jobs:
    link = f"https://www.wanted.co.kr/{eachJob.find('a')['href']}"
    title = eachJob.find("strong", class_="JobCard_title__HBpZf").text
    companyName = eachJob.find("span", class_="JobCard_companyName__N1YrF").text

    eachJob = {
        "title":title,
        "companyName":companyName,
        "link": link
    }
    jobsDB.append(eachJob)

file = open("Scraper/jobs.csv", "w", encoding="utf-8", newline="") # file open    # w : writing mode (default= read)
writer = csv.writer(file)   # csv 행 추가
writer.writerow(["Title", "CompanyName"]) # writerow -> List만 받음, Dictionary 불가

for job in jobsDB:
    writer.writerow(job.values())

file.close()
