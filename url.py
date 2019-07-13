import bs4

import requests
url = "https://www.tutorialspoint.com/articles/apache-hadoop-and-its-components"
data = requests.get(url)
soup = bs4.BeautifulSoup(data.text, 'html.parser')


for para in soup.find_all('a'):
    link = para.get("href")
    if link[0:3] =="../" and link!="#":
        print("https://www.tutorialspoint.com"+link[2:len(link)])
    elif link[0]=="/" and link!="#":
        print("https://www.tutorialspoint.com"+link)
    elif link!="#":
        print(link)