from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

# URL of the webpage to scrape
url = 'https://fueler.io/cmchelsimehta'

# Open the webpage
driver.get(url)

# Find the element with the title

try:
    elem = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/main/section/div[2]/div[2]/a')) #This is a dummy element
    )
finally:
    title_element = driver.find_elements(By.XPATH,'/html/body/main/section/div[2]/div[2]/a')
    for ele in title_element:
        print(ele.get_attribute("href"))
    driver.quit()

# Extract the text from the title element

