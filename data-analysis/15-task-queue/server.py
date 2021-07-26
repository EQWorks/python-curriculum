from urllib.parse import urlparse

from flask import Flask, jsonify, request

from extract_tasks import filter_rules, fetch_website_task, extract_titles, post_slack


app = Flask(__name__)


def pipe(domain, response_url):
    chain = fetch_website_task.s(domain, response_url) | extract_titles.s() | post_slack.s()
    return chain()


@app.route('/', methods=['GET', 'POST'])
def get_news():
    # request.form
    # command - the slash command
    # text - after command
    # response_url - the POST back URL for follow up messages
    domain = urlparse(request.form.get('text'))
    domain = domain.netloc or domain.path

    if domain not in filter_rules:
        return jsonify({
            'error': f'{domain} not supported',
        })

    response_url = request.form.get('response_url')
    # queue up the task
    pipe(domain, response_url)
    return jsonify({
        'text': f'parsing {domain} headlines for fact/opinion scores',
    })
