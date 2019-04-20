#!/usr/bin/env python

##################################################
# Flight Tracker
# Author: Rayman Jamal
# Date: April 20, 2019
##################################################

from selenium import webdriver
import pyttsx3
import sys

# Variables:
# --- Shell variable:
flight_number = sys.argv[1] # Passed through command-line

# --- Script variables:
url = "https://flightaware.com/live/flight/"
# flight_number = "wg681"
status_class = "flightPageArrivalDelayStatus"
arrival_time_class = "flightPageSummaryArrival"
on_time = "(on time)"

# Init objects:

# --- Speech engine:
engine = pyttsx3.init()

# --- Chrome:
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")

browser = webdriver.Chrome(options=chrome_options)

# Get request:
browser.get(url + flight_number)

# Parse results:
status = browser.find_element_by_class_name(status_class)
time_element = browser.find_element_by_class_name(arrival_time_class)
time = time_element.find_element_by_tag_name("em")

# Speak:

engine.say("The flight is " + status.text)
engine.say("And will arrive at")

engine.setProperty("rate", 95) # Slow down the time a bit for clarity
engine.say(time.text)

engine.runAndWait()

# Close browser:
browser.close()
