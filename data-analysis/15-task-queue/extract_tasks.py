import json

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
def fetch_website_task(domain, response_url):
    r = requests.get(f'https://{domain}')
    return {
        'domain': domain,
        'raw': r.text,
        'response_url': response_url,
    }


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
def extract_titles(data):
    raw = data.get('raw')
    domain = data.get('domain')
    soup = BeautifulSoup(raw, 'html.parser')

    return {
        'titles': [
            {'text': tag.text.strip(), 'link': tag['href'] or tag.parent['href']}
            for tag in soup.find_all(filter_rules[domain])
        ],
        **data,
    }


@queue.task
def post_slack(data):
    response_url = data.get('response_url')
    titles = data.get('titles')
    if not response_url or not titles:
        return

    titles = json.dumps(titles, indent=2)
    requests.post(
        response_url,
        json={'text': f'```{titles}```'},
    )
    return
