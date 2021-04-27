from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import SessionNotCreatedException
from bs4 import BeautifulSoup
import pandas as pd
import re, os, json
from selenium import webdriver
import git, shutil, twilio
from selenium.webdriver.chrome.options import Options

def get_page():
    chrome_path = 'chromedriver.exe'
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_path, options=options)
    driver.get('https://www.indiegogo.com/projects/niche-zero-the-best-conical-burr-coffee-grinder#/')
    return driver

def send_text(b):
    from twilio.rest import Client
  
    # Your Account Sid and Auth Token from twilio.com / console
    account_sid = ''
    auth_token = ''
    with open('creds.json') as f:
        d1 = json.load(f)
        account_sid = d1['account_sid']
        auth_token = d1['auth_token']
    client = Client(account_sid, auth_token)
    message = client.messages.create(
                                  from_='+12056513878',
                                  body = b,
                                  to ='+12407146393'
                              )
    
def find_availability():
    drv =  get_page()
    soup = drv.page_source.encode('utf-8')
    soup_parsed = BeautifulSoup(soup)
    # Extracting Column
    column_product = drv.find_elements_by_xpath("""//*[@id="vCampaignPerkSelection"]/div/div/div[7]/div/div/div[2]/div[2]/div[4]/div/div/span/span""")
    txt = ''
    for c in column_product:
        txt += c.text+" "
    if (txt.split()[0] == txt.split()[-1]):
        send_text("Niche is Not Available")
    else:
        send_text("Niche is Available! Go get it boy!")
find_availability()
    
