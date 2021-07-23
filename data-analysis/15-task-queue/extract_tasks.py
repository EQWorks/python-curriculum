from celery import Celery
import requests
from bs4 import BeautifulSoup


queue = Celery(
    'news',
    broker='redis://localhost:6379/0',
    result_backend='redis://localhost:6379/1',
)


@queue.task
def add(a, b):
    return a + b


@queue.task
def fetch_website_task(url):
    r = requests.get(url)
    return url, r.text


def bbc(tag):
    return tag.name == 'a' and 'media__link' in tag.get('class', []) and tag.get('href', '').startswith('/') and tag.text.strip()

def guardian(tag):
    return tag.name == 'a' and tag.get('data-link-name') == 'article' and tag.text.strip()

def wp(tag):
    return tag.name == 'span' and tag.parent.name == 'a' and tag.text.strip()

def fox(tag):
    return tag.name == 'a' and tag.parent.name == 'h2' and 'title' in tag.parent.get('class') and tag.text.strip()

def wsj(tag):
    return any(['headline' in cls for cls in tag.get('class', [])]) and tag.text.strip()


filter_rules = {
    'bbc.com': bbc,
    'theguardian.com': guardian,
    'washingtonpost.com': wp,
    'foxnews.com': fox,
    'wsj.com': wsj,
}


@queue.task
def extract_titles(url, raw):
    soup = BeautifulSoup(raw, 'html.parser')
    return url, set([
        tag.text.strip()
        for tag in soup.find_all(filter_rules[url])
    ])
