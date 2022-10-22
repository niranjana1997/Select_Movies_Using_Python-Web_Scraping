import random

# Third party module to send get request
import requests as req
# Used to parse HTML
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/"


def main():
    # To send a get request to IMDB
    res = req.get(url)
    # To get the HTML
    html = res.text
    # Looking for <td> element with class = 'titleColumn'
    # BeautifulSoup is used, default html parser is used
    soup = BeautifulSoup(html, 'html.parser')
    # selects td elements with class = 'titleColumn'
    movie_tag = soup.select('td.titleColumn')
    
    # function to get year
    def get_year(tag):
        split = tag.text.split()
        return split[-1]
    # list comprehension to store all movie years in list by calling get_year method
    years = [get_year(tag) for tag in movie_tag]

    # gets actors and titles
    inner_movie_tag = soup.select('td.titleColumn a')
    actors = [tag['title'] for tag in inner_movie_tag]
    titles = [tag.text for tag in inner_movie_tag]
    
    # Gets rating values from td tag named posterColumn and a span inside with name 'ir'
    rating_tag = soup.select("td.posterColumn span[name=ir]")
    ratings = [float(tag['data-value']) for tag in rating_tag]
    print(ratings)
    
    num_movies = len(titles)
    #Making a random choice
if __name__ == "__main__":
    main()
