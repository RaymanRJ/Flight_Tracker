import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = "https://flightaware.com/live/flight/"
flight_number = "wg681"
status_class = "flightPageArrivalDelayStatus"

flight_page = requests.get(url + flight_number)

print(flight_page.content)

browser = webdriver.Chrome()
browser.get(url + flight_number)

elem = browser.find_element_by_class_name(status_class)  # Find the html box

print(elem.text)
print(elem)

browser.close()