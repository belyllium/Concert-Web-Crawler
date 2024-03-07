from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

path = "/Users/dongseok/codes/iPBL/competency_march/i-PBL_Competency/chromedriver"
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

url = "https://www.laphil.com/events/performances"
driver.get(url)
current_scroll_position = driver.execute_script("return window.pageYOffset;")
scroll_height = driver.execute_script("return document.body.scrollHeight;")
if current_scroll_position << scroll_height:
    driver.execute.script("window.scrollTo(0, document.body.scrollHeight);")
driver.implicitly_wait(10)

soup = BeautifulSoup(driver.page_source, "html.parser")

titles = soup.find_all(class_="info")
# print(titles)
# for title in titles:
#    print(title.text.strip())


data = []
titles = soup.find_all(class_="info")
# print(titles)
for title in titles:
    title_text = title.find(class_="name name--short").get_text(strip=True)
    # supporting-acts에 있는 텍스트를 가져옵니다.
    supporting_acts = title.find(class_="supporting-acts")
    supporting_acts_text = (
        supporting_acts.get_text(strip=True) if supporting_acts else ""
    )
    # title과 supporting_acts를 출력합니다.
    date_text = title.find(class_="date-text").get_text(strip=True)
    time_text = title.find(class_="time").get_text(strip=True).replace("\n", " ")
    time_text = " ".join(time_text.split())
    data.append({"title": title_text, "date": date_text, "time": time_text})
    # print(title_text + " " + supporting_acts_text + " " + date_text + " " + time_text)

df = pd.DataFrame(data)
print(df)
