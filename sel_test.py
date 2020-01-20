import bs4 
import requests
from selenium import webdriver
import time

driver = webdriver.Chrome(r"C:\Users\Christopher\Desktop\PythonCode\YT_Subtitles\chromedriver.exe")

driver.get('http://www.google.com/');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()
