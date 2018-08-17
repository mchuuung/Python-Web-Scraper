import requests
from bs4 import BeautifulSoup
from csv import writer # write to csv files

response = requests.get('http://codedemos.com/sampleblog/')
soup = BeautifulSoup(response.text, 'html.parser')

posts = soup.find_all(class_ ='post-preview')

with open('posts.csv', 'w') as csv_file: # write to file "posts.csv"
    csv_writer = writer(csv_file)
    headers = ['Title', 'Link', 'Date']
    csv_writer.writerow(headers)
    for post in posts:
        title = post.find(class_='post-title').get_text()\
        .replace('\n', '')# replace '\n' with nothing
        print(title)
        link = post.find('a')['href']
        date = post.select('.post-date')[0].get_text() # obtain text at 0 index
        csv_writer.writerow([title, link, date])