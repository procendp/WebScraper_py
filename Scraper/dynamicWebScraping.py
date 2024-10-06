###########################
# https://playwright.dev/
#  - playwright
###########################
from playwright.sync_api import sync_playwright
import time

p = sync_playwright().start()

browser = p.chromium.launch(headless=False) # headless= False : open the browser / True : not open, but can do all without browser

page = browser.new_page()

page.goto("https://www.wanted.co.kr/jobsfeed")

time.sleep(7)   # making slowly for checking click well

page.click("button.Aside_searchButton__rajGo")
# page.locator("button.Aside_searchButton__rajGo").click()  # 위와 같음

time.sleep(7)

page.get_by_placeholder("검색어를 입력해 주세요.").fill("flutter")  # 이 외에도 다양한 것들로 가져올 수 있음

p.stop()
# page.screenshot(path="screenshot.png")    # screenshot to browser