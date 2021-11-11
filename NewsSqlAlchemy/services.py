from coin_market_news import news_scraper
from bs4 import BeautifulSoup
from models import News, add_news_to_db, get_the_news
coinScraper = news_scraper()


def PutResults(cryptoname):
    result = coinScraper.find_coin_news("bitcoin")
    for news in result:
        title = news.find("h2", class_ = "tw-text-xl").text.strip()
        overview = news.find("div", class_ = "post-body").text.strip()
        link = news.find('a', href=True)["href"]
        paragraphs = coinScraper.ScrapTheLink(link)
        print(title)
        print(overview)
        print(link)
        print(paragraphs)
        add_news_to_db(title, overview, link, paragraphs)

def GetResults():
    newsets =  get_the_news()
    return newsets

# result = coinScraper.find_coin_news("bitcoin")
# for news in result:
#     title = news.find("h2", class_ = "tw-text-xl").text.strip()
#     overview = news.find("div", class_ = "post-body").text.strip()
#     link = news.find('a', href=True)["href"]
#     paragraphs = coinScraper.ScrapTheLink(link)
#     print(title)
#     print(overview)
#     print(link)
#     print(paragraphs)
#     add_news_to_db(title, overview, link, paragraphs)
# PutResults("ada")

