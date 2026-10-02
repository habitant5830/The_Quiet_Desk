from bs4 import BeautifulSoup
import requests, openpyxl

# scraping from hackernews site
try:
    response = requests.get("https://news.ycombinator.com/")
    file = BeautifulSoup(response.text,'html.parser')
    # finding posts titles and urls from hackernews
    
    times = file.find_all('span', class_ = "age")

    for time in times:
        date = time.find("a")
        print(date["href"].split("?")[0],date["href"].split("?")[1], ":", date.text)
        break
    
    titles = file.find_all('span', class_ = "titleline")

    for title in titles:
        # finding a tags to parse links
        link = title.find("a")
        # printing link url and link text (title) separated by -
        print(link["href"], "-", link.text)
        break

except Exception as e:
    print(e)