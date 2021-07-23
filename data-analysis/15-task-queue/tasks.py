import sqlite3

from celery import Celery
import requests
from bs4 import BeautifulSoup
import fasttext
from gensim.utils import simple_preprocess


queue = Celery(
    'news',
    broker='redis://localhost:6379/0',
    result_backend='redis://localhost:6379/1',
)

model = fasttext.load_model('./opinion.bin')


@queue.task
def add(a, b):
    return a + b


@queue.task
def fetch_website_task(url):
    r = requests.get(url)
    return url, r.text


@queue.task
def extract_titles(url, raw):
    soup = BeautifulSoup(raw, 'html.parser')
    return url, set([
        a.text.strip()
        for a in soup.find_all('a')
        if a.get('href', '').startswith('/') and 'media__link' in a['class']
    ])


@queue.task
def classify(url, titles):
    res = []
    for title in titles:
        label, score = model.predict(' '.join(simple_preprocess(title)))
        res.append({
            'url': url,
            'title': title,
            'label': label[0].replace('__label__', ''),
            'score': score[0],
        })

    return res


@queue.task
def write_db(rows):
    with sqlite3.connect('db') as db:
        db.execute('''
            CREATE TABLE IF NOT EXISTS news(
                url TEXT,
                title TEXT,
                label TEXT,
                score REAL
            );
        ''')
        db.executemany('''
            INSERT INTO news (url, title, label, score)
            VALUES (?, ?, ?, ?);
        ''', rows)
