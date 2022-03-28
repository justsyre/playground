''' 
••• Webscraping •••

1 - import request and get webpage thru a request
2 - import bs4

f = open('image', 'wb') --> mode should be write binary

import requests
import bs4

result = requests.get("http://www.example.com")
# type(result) should return requests.model.Response
soup = bs4.BeautifulSoup(result.text, "lxml")
print(soup)
# Grabbing element soup.select('tag|class|id')
print(soup.select('title'))
print(soup.select('title')[0].getText())
'''
## Practice one scraping toscrape.com BOOKS
## Get title of every book with 2-Star rating
import requests
import bs4

base_url = 'https://books.toscrape.com/catalogue/page-{}.html'
# res = requests.get(base_url.format(1))
# soup = bs4.BeautifulSoup(res.text, 'lxml')

# products = soup.select('.product_pod')
# example = products[0]
# # example.select('.star-rating.Two')    -> will return two stars
# # example.select('a')[1]['title']       -> will return the book title
two_star_titles = []

for n in range(1,51):

    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)

    soup = bs4.BeautifulSoup(res.text, 'lxml')
    books = soup.select(".product_pod")

    for book in books:
        if len(book.select('.star-rating.Two')) != 0:
            book_title = book.select('a')[1]['title']
            two_star_titles.append(book_title)

print(len(two_star_titles))