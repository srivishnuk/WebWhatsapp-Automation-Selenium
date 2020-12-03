from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv

driver = webdriver.Chrome()
baseurl = "https://web.whatsapp.com"
driver.get(baseurl)
#increase sleep time if your internet is slow or you need more time to scan,This is one time QR scan for sending 1 whole list
time.sleep(5)

with open('contacts.csv', newline='') as csvfile:
    readContacts = csv.reader(csvfile)
    for phone, msg in readContacts:
        phonnum = phone
        message = msg
        
        sameTab = (baseurl + '/send?phone=' + str(phonnum))
        driver.get(sameTab)
        #increase sleep time if your internet is slow,This is to load new chats
        time.sleep(5)
        content = driver.switch_to.active_element
        content.send_keys(message)
        content.send_keys(Keys.RETURN)
        #Increase sleep time if you have a slow internet to avoid webwhatsapp create a 'Leave Site' alert since browser tries to load new chat before message sent
        time.sleep(5)


