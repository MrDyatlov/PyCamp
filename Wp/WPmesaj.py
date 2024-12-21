from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



with open("messages.txt", "r", encoding="utf-8") as messages:
    messageList = list()
    text = messages.read()
    message = text.split("\n")


def sendMessage():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.get("https://web.whatsapp.com/")
    input("Random-Enter: ")
    messageArea = driver.find_element(By.XPATH, "//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")
    while True:
        messageArea.click()
        messageArea.send_keys(message)
        messageArea.send_keys(Keys.ENTER)




sendMessage()