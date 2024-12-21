from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import time


with open("messages.txt", "r", encoding="utf-8") as messages:
    messageList = list()
    text = messages.read()
    messages = text.split("\n")


def sendMessage():
    flag = False
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.get("https://web.whatsapp.com/")
    input("Random-Enter: ")
    messageArea = driver.find_element(By.XPATH, "//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")
    while True:
        messageArea.click()
        wpSource = driver.page_source
        soup = bs(wpSource, "lxml")
        onoff = soup.find_all("div", {"class": ["zzgSd", "_3e6xi"]})
        try:
            online = onoff[0].span.text
            print(online)
            if (online in ["çevrimiçi", "online"]) and flag == False:
                print("online")
                msgSend = messages
                messageArea.send_keys(msgSend)
                messageArea.send_keys(Keys.ENTER)
                flag = True
            elif online not in ["çevrimiçi", "online"]:
                print("Şu an çevrimdışı.")
                flag = False
        except:
            print("Şu an çevrimdışı.")
            flag = False

        time.sleep(5)


sendMessage()
