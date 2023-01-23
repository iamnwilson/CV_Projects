import os
import string
import requests
from bs4 import BeautifulSoup


def create_pages(number_of_pages):
    return list(range(1, number_of_pages + 1))


def create_folders(pages):
    for p in pages:
        os.mkdir(f"Page_{p}")


def get_nature_articles():
    base_url = "https://www.nature.com/nature/articles?searchType=journalSearch&sort=PubDate&year=2020&page="
    number_of_pages = int(input())
    article_type = input()
    # Create pages array
    pages = create_pages(number_of_pages)

    # Create folders
    create_folders(pages)

    # Search for articles by page
    for page in pages:
        request = requests.get(base_url + str(page))
        bs = BeautifulSoup(request.content, 'html.parser')
        articles = bs.findAll("article", class_="u-full-height")
        for child in articles:
            tag = child.find("span", class_="c-meta__type")
            if str(tag.text).lower() == article_type.lower():
                a_tag = child.find("a", class_="c-card__link")
                filename = a_tag.text.strip().replace(" ", "_").strip(string.punctuation) + ".txt"
                article_link = "https://www.nature.com" + a_tag["href"]
                article_request = requests.get(article_link, headers={'Accept-Language': 'en-US,en;q=0.5'})
                article_soup = BeautifulSoup(article_request.content, "html.parser")
                article_body = article_soup.find("div", class_="c-article-body")
                with open(os.path.join(f"Page_{str(page)}", filename), "wb") as file:
                    file.write(article_body.text.encode())


def main():
    get_nature_articles()


if __name__ == "__main__":
    main()
