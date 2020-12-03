# WebWhatsapp-Automation-Selenium
# Simplest selinum automation script without the need to scan QR each time
Automate sending messages to list with Web Whatsapp


# Setup Instructions for Ubuntu (Use python3)

Download chrome driver for your chrome version from https://chromedriver.chromium.org/downloads and extract it to /usr/bin/

1. virtualenv whatsappautomation -p python3
2. cd whatsappautomation && source bin/activate
3. pip install selenium

# create contacts.csv inside whatsappautomation folder, in below format

9199999XXXXX,this is new message</br>
4442311XXXXX,not the first message</br>
3489234XXXXX,this message is different</br>

# Finally run whatsapp.py and scan QR code once, Take note on sleep time in code comments if you have slow internet

You can reach me on https://srivishnu.me


