# Flight Tracker

This script is designed to run as a cronjob on Ubuntu, with the
flight number  passed as a command-line argument.

Flights are retrieved from scraping through https://www.flightaware.com 
using a Chrome browser on Selenium. This introduces some instability 
however, as this system will probably not work if certain div names are 
changed on that website.

Selenium is used to avoid the need of signing up for an API key to search
for flight times. As most websites are created through JavaScript,
Python's request module would not work. Selenium allows JavaScript to run and
populate the DOM, which can then be parsed after.
