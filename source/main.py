#!/usr/bin/env python3

"""
Flight Tracker
Author: Rayman Jamal
Date: April 20, 2019

This script is designed to run as a cronjob on Ubuntu, with the
flight number  passed as a command-line argument.

Flights are retrieved from https://www.flightaware.com using a Chrome
browser on Selenium. This introduces some instability however, as this
system will probably not work if any changes are made to that website.

Selenium is used to avoid the need of signing up for an API key to search
for flight times. As most websites are created through JavaScript,
Python's request module would not work. Selenium allows JavaScript to run and
populate the DOM, which can then be parsed after.
"""

from selenium import webdriver
import pyttsx3
import sys

# region Variables

# region Shell Variable

flight_number = None
try:
    flight_number = sys.argv[1]  # Passed through command-line
except IndexError:
    # Hit because no argument was passed
    print("User must pass a flight number as a command-line argument")
    print("Example:")
    print("python3 main.py wg681")
    quit()
# endregion

# region Script Variables:
url = "https://flightaware.com/live/flight/"
status_class = "flightPageArrivalDelayStatus"
arrival_time_class = "flightPageSummaryArrival"
on_time = "(on time)"
# endregion
# endregion

# region Initialize Objects:

# region Speech Engine:
engine = pyttsx3.init()
# endregion

# region Chrome browser:
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")

print("Looking up flight " + flight_number)
browser = webdriver.Chrome(options=chrome_options)
# endregion
# endregion

# region Main

# Get request:
browser.get(url + flight_number)

# Parse results:
status = browser.find_element_by_class_name(status_class)
time_element = browser.find_element_by_class_name(arrival_time_class)
time = time_element.find_element_by_tag_name("em")

# Speak:

flight_status = "The flight is " + status.text

engine.say(flight_status)
engine.say("And will arrive at")
engine.setProperty("rate", 150)  # Slow down the time a bit for clarity
engine.say(time.text)
engine.runAndWait()

# Print to console:

print(flight_status)
print("And will arrive at " + time.text)

# Close browser:

browser.close()

# endregion
