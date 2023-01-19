from typing import final
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd
from datetime import datetime
import os
import sys

application_path = os.path.dirname(sys.executable)

now = datetime.now()
month_day_year=now.strftime("%m%d%Y") #MMDDYYYY
 
website = "https://www.thesun.co.uk/sport/football/"
path = "/home/kcesar/Downloads/chromedriver"

#Headless Mode
options=Options()
options.headless = True


service=Service(executable_path=path)
driver=webdriver.Chrome(service=service, options=options)
driver.get(website)

containers = driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]')

#crating lists
titles = []
subtitles = []
links = []

# //div[@class="teaser__copy-container"]/a/h3
for container in containers:
    title = container.find_element(by="xpath", value='./a/h3').text
    subtitle = container.find_element(by="xpath", value= './a/p').text
    link = container.find_element(by="xpath", value='./a').get_attribute("href")
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)
   

#crear diccionario {'Key': listname}
mydict = {'titulo': titles, 'subtitulo' : subtitles, 'enlace':  links}


df_headlines = pd.DataFrame(mydict)
file_name = f'headline-{month_day_year}.csv'
final_path= os.path.join(application_path,file_name)
df_headlines.to_csv(final_path)
## we run pyinstaller --onefile wc2.py to make an executable
driver.quit()
