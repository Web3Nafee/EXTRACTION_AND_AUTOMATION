#This script is used to extract email addresses from indeed.com
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import time

driver = webdriver.Chrome()
for t in range(10, 110, 10):
    driver.get(f'https://www.indeed.com/jobs?q=data+analyst+entry+level+remote+email&l=USA&start={t}&vjk=0350ff67477cfabf')

    a =[1,2,3,4,5,7,8,9,10,11,13,14,15,16,17]
    for x in a:
        try:
            driver.find_element(By.XPATH, f"//li[@class='css-5lfssm eu4oa1w0'][{x}]/div/div/div/div/div/table/tbody/tr/td/div/h2/a").click()
            time.sleep(1)
            b = driver.find_element(By.XPATH, '//*[@id="jobDescriptionText"]').text
            with open ('info.txt', 'a') as c:
                c.write(f'{b}\n')

        except:
            pass
            
    print(f'page{t} done')




def extract_emails(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    matche = re.findall(email_pattern, text, re.IGNORECASE)
    matches = list(set(matche))
    return matches


with open ('info.txt', 'r') as file:
    files =file.read()


# Extract email addresses
email_addresses = extract_emails(files)

# writing  extracted email addresses into a text file
with open('mail_address.txt', 'a') as c:
    for email in email_addresses:
        c.write(f'{email}\n')
