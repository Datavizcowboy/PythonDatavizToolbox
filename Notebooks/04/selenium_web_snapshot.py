from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# This is not needed if chromedriver is already on your path:
chromedriver_path = "/Users/simon/bin/chromedriver"

options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1250,2080")
#options.add_argument("--verbose")

#driver = webdriver.Chrome(options=options, chromedriver_path=executable_path)
driver = webdriver.Chrome(options=options)
driver.get("https://mitigasolutions.com")
#driver.get("http://localhost:8080/Catbond_Map")
driver.set_window_size(1400,2000)

#time.sleep(5)
driver.save_screenshot('/Users/datavizcowboy/Desktop/map.png')
driver.quit()

