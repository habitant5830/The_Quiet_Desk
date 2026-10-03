from bs4 import BeautifulSoup
import requests, openpyxl

# scraping from hackernews site
try:
    response = requests.get("https://news.ycombinator.com/")
    file = BeautifulSoup(response.text,'html.parser')
    # finding posts titles and urls from hackernews
    
    times = file.find_all('span', class_ = "age")
    titles = file.find_all('span', class_ = "titleline")

    for time, title in zip(times, titles):
        # get title attribute directly
        date = time["title"]
        link = title.find("a")
        print(date.split("T")[0], " - ", date.split("T")[1])
        print(link["href"], "-", link.text)   

except Exception as e:
    print(e)