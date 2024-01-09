#importing the necessary libraries
import selenium
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
import pandas as pd

links =[]
texts = []

driver = webdriver.Chrome()



driver.get('https://www.jumia.com.ng/mlp-official-stores/electronics/')
try:
    # extracting the links and texts
    for i in range(1,120):
        link = driver.find_element(By.XPATH,  f'//*[@id="jm"]/main/div[2]/div[3]/section/div[1]/article[{i}]/a').get_attribute('href')
        text =driver.find_element(By.XPATH,  f'//*[@id="jm"]/main/div[2]/div[3]/section/div[1]/article[{i}]/a/div[2]/h3').text
        time.sleep(2)
        links.append(link)
        texts.append(text)
except:
    pass

df = pd.DataFrame({'links':links, 'texts':texts}).to_csv('jumia.csv', index=False)