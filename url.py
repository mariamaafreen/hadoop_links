import bs4

import requests
url = "https://prwatech.in/blog/hadoop/hadoop-basic-linux-commands/"
data = requests.get(url)
soup = bs4.BeautifulSoup(data.text, 'html.parser')


for para in soup.find_all('a'):
    link = para.get("href")
    if link[0:3] =="../" and link!="#":
        print("https://prwatech.in"+link[2:len(link)])
    elif link[0]=="/" and link!="#":
        print("https://prwatech.in"+link)
    elif link!="#":
        print(link)