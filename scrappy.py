import requests
from bs4 import BeautifulSoup
from termcolor import colored
from requests.exceptions import ConnectionError
import time
import replit
replit.clear()
print(colored("Welcome to the", "magenta"), colored("Subordinate Intelligence Encrypted", "cyan"), colored("web crawler.", "magenta"))
time.sleep(2)
print()

time.sleep(4)
print()
website = input(colored("Please enter your website (do NOT include http:// or https://) >", "yellow"))
print()
if "http://" not in website:
    website = ''.join(("http://", website))
print(colored("We're scraping %s. If this takes longer than 15 seconds, the website failed to connect." % (website), "magenta"))
time.sleep(2)
try:
    page = requests.get(website)
except ConnectionError:
    print()
    print(colored("The website you entered does not exist.", "red"))
else:
    soup = BeautifulSoup(page.content, "html.parser")
    title = soup.find('title')
    print()
    print(colored("The title of %s is %s." % (website, title.text), "cyan"))
    time.sleep(4)
    print()
    setContinue = input(colored("Would you like to scrape the rest of this page?", "yellow")).lower()
    if setContinue == "yes" or setContinue == "y" or setContinue == "yea" or setContinue == "yeah" or setContinue == "sure" or setContinue == "o yea" or setContinue == "I thought that's what I was doing bro":
        print()
        print(colored("Creating your scraped page...", "magenta"))
        time.sleep(5)
        print()
        replit.clear()
        print(colored(soup, "cyan"))
