#Selenium 可以真正“渲染”网页，加载 JavaScript 动态内容。

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


service=Service('/usr/local/bin/chromedriver')

driver=webdriver.Chrome(service=service)


driver.get("https://m.shicimingju.com/book/hongloumeng.html")

time.sleep(3)

ch_list=driver.find_elements(By.XPATH,'/html/body/div[3]/div[2]/div[3]/div/a')

data=[]

#先获取章回和url，因为在打开具体URL时，ch_list请求会失效
for ch in ch_list:
    ch_name=ch.text
    ch_url = ch.get_attribute("href")
    data.append((ch_name,ch_url))
    print(data)

#获取内容
for ch_name,ch_url in data:
    driver.get(ch_url)
    time.sleep(3)
    content = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[2]/div').text
    new_content = content.replace("\n", "")
    #写入
    with open("hongloumeng.txt", "a", encoding="utf-8") as f:
        f.write(f'{ch_name}\n{new_content}')

driver.quit()


