import os
import sys
from datetime import datetime

import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# Get the path of the executable
application_path = os.path.dirname(sys.executable)


website = "https://www.thesun.co.uk/sport/football/"
path = "/Users/milobedini/Documents/chromedriver"

# https://www.thesun.co.uk/sport/football/
# Driver allows us to interact via Selenium.

# HEADLESS MODE, Selenium does not open the browser.
options = Options()
options.headless = True

# Datetime to create a new filename for each day.
now = datetime.now()
# string from time. https://strftime.org/
# DDMMYY
today = now.strftime("%d-%m-%y")

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)
driver.get(website)

containers = driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]')

subtitles = []
links = []

for container in containers:

    subtitle = container.find_element(by="xpath", value="./a/p").text
    link = container.find_element(by="xpath", value="./a").get_attribute("href")

    subtitles.append(subtitle)
    links.append(link)

sun_dict = {
    "subtitles": subtitles,
    "links": links,
}


df_sun = pd.DataFrame(sun_dict)
# The below is due to subtitle containing some empty rows with empty strings.
df_sun["subtitles"].replace("", np.nan, inplace=True)
df_sun.dropna(subset=["subtitles"], inplace=True)

# Below to most resilient to OS changes etc.
file_name = f"sun-headlines-{today}.csv"
final_path = os.path.join(application_path, file_name)

df_sun.to_csv(final_path)

driver.quit()
