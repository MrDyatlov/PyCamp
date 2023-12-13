import requests
from bs4 import BeautifulSoup
from tkinter import *

url = "https://news.ycombinator.com/"
def requester(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features="html.parser")
    #news = soup.find_all('a', {"rel":"noreferrer"})
    return soup

news = []
def parser(url):
    links = requester(url)
    link_num = 1
    for link in links.find_all('a', {"rel": "noreferrer"}):
        link = link.get('href')
        if len(news) > 0:
            news.append(link)
        elif len(news) == 1:
            continue
        elif len(news) == 2:
            del news[0]
        else:
            news.append(link)

    #print(*news, sep="\n")
        with open("linkofNews.txt", "a") as new:
            new.write(f"New{link_num}: {link}\n")
        link_num += 1


def gui():
    # coming soon
    pass