from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


def url_decoder_requester(my_url):
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    return page_soup


def soup_parser_decoder(page_soup, tag, name):
    return page_soup.findAll(tag, {"class": name})
