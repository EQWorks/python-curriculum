from urllib.parse import urlparse

from flask import Flask, jsonify, request

from extract_tasks import (
    filter_rules,
    fetch_website_task,
    extract_titles,
    post_slack,
    classify,
    format_slack,
)


app = Flask(__name__)


def pipe(domain):
    chain = fetch_website_task.s(domain) | extract_titles.s()
    return chain()


def pipe_v2(domain, response_url):
    chain = fetch_website_task.s(domain) | extract_titles.s() | post_slack.s(response_url)
    return chain()


def pipe_v3(domain, response_url):
    chain = fetch_website_task.s(domain) | extract_titles.s() | classify.s() | format_slack.s() | post_slack.s(response_url)
    return chain()


@app.route('/', methods=['GET', 'POST'])
def get_news():
    # request.form
    # command - the slash command
    # text - after command
    # response_url - the POST back URL for follow up messages
    domain = urlparse(request.form.get('text') or request.args.get('domain'))
    domain = domain.netloc or domain.path or 'bbc.com'

    if domain not in filter_rules:
        return jsonify({
            'error': f'{domain} not supported. it needs to be one of {", ".join(filter_rules.keys())}',
        })

    # queue up the task
    response_url = request.form.get('response_url')
    if not response_url:
        pipe(domain)
    else:
        pipe_v3(domain, response_url)

    return jsonify({
        'text': f'parsing {domain} headlines',
    })
