# Part 03 - Data Containers and Repetitions (2/3)

A list offers us simple access to its items through positional indexes. When the control of each item's positional correspondence is out of reach, we need something more explicit to dictate what each value means.

## Dictionaries

In Python, one of the most used data types for such a purpose is the dictionary (`dict`):

```python
'''norse_dict.py'''
row1 = {
    'poi': 'Yggdrasil',
    'revenue': 790.2,
    'cost': 477.85,
    'visits': 53,
    'unique_visitors': 7,
}
row2 = {
    'unique_visitors': 10,
    'revenue': 1700.65,
    'cost': 1500,
    'visits': 11,
    'poi': 'Valhalla',
}
```

Consider the above example an extension from its [original form-factor](03-data-containers-and-repetitions-1.md#lists) from the `list` introduction. We gain per-value definition though `key: value` pairs by trading off positional significance, consequently costing more computational space to contain such data. What we gain, like with a literal dictionary, is the direct access of definitions (the value) by looking up their keys:

```python
>>> from norse_dict import row1, row2
>>> row1['poi']
'Yggdrasil'
>>> row2['cost']
1500
```

We employ a similar syntax of the positional index notion in a more literal sense to access dictionary items.

Dictionaries are mutable like lists:

```python
>>> a = {'k1': 'v1', 'k2': 45}
>>> a['k1'] = 54
>>> a['k2'] = 'v2'
{'k1': 54, 'k2': 'v2'}
```

Dictionary values can also be of other types, including lists and dictionaries, which allows us to compose data of more complex shapes with easy access:

```python
'''norse_dict.py'''
# ...
row3 = {
    'poi': 'Asgard',
    'revenue': 3215.75,
    'cost': 2845.79,
    'visits': 265,
    'unique_visitors': 71,
    'poi_details': {
        'open_days': [1, 2, 3, 4, 5],
        'lat': 0.0,
        'lon': 0.0,
        'wiki_link': 'https://en.wikipedia.org/wiki/Asgard',
    },
}
```

```python
>>> from norse_dict import row3
>>> row3['poi_details']
{'open_days': [1, 2, 3, 4, 5], 'lat': 0.0, 'lon': 0.0, 'wiki_link': 'https://en.wikipedia.org/wiki/Asgard'}
```

Unlike lists where the data shape and specific values are bound by implicit contracts defined by positional significance of each value, dictionaries can and will often have missing _keys_:

```python
>>> from norse_dict import row1
>>> row1['poi_details']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'poi_details'
```

Evidently you cannot access a key through the index notion when it does not exist in the dictionary. Fortunately there is a method for the `dict` type for such occasions:

```python
>>> from norse_dict import row1
>>> row1.get('poi_details')  # None
>>> row1.get('poi_details', {})  # if None, default {}
{}
```

The `dict.get()` method allows us a graceful way of accessing keys that may or may not exist in a given dictionary. Lists, on the other hand, would not be as flexible to work with such scenario given the siginificance of their positional indexes:

```python
>>> from norse_dict import row3
>>> row1 = ['Yggdrasil', 790.2, 477.85, 53, 7]
>>> row2 = ['Valhalla', 1700.65, 1500, 11, 10]
>>> row3_list = list(row3.values())
>>> row3_list
['Asgard', 3215.75, 2845.79, 265, 71, {'open_days': [1, 2, 3, 4, 5], 'lat': 0.0, 'lon': 0.0, 'wiki_link': 'https://en.wikipedia.org/wiki/Asgard'}]
>>> row3[5]  # positional index of poi_details
{'open_days': [1, 2, 3, 4, 5], 'lat': 0.0, 'lon': 0.0, 'wiki_link': 'https://en.wikipedia.org/wiki/Asgard'}
>>> row1[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

From the above example, we can understand that it would be more challenging to use lists to work with data with no guarantee of data consistency since each index holds an implicit and rigid definition of what each value represents.

In contrast, dictionaries would suffer some other problem precisely due to how insignificant their `key: value` orders are:

```python
'''norse_dict.py'''
# ...
# print header row
print(','.join(row1.keys()))
# print each data row
for row in [row1, row2, row3]:
    csv_row = ','.join(['"{}"'.format(v) for v in row.values()])
    print(csv_row)
```

|poi      |revenue|cost   |visits|unique_visitors|                |
|---------|-------|-------|------|---------------|----------------|
|Yggdrasil|790.2  |477.85 |53    |7              |                |
|10       |1700.65|1500   |11    |Valhalla       |                |
|Asgard   |3215.75|2845.79|265   |71             |{'open_days': [1, 2, 3, 4, 5], 'lat': 0.0, 'lon': 0.0, 'wiki_link': 'https://en.wikipedia.org/wiki/Asgard'}|

Since `row2` has a different order of its `key: value` pairs than `row1`, and `row3` has an extra `key` that the other two do not have, we would get a not so use of output if we attempt to marshall the data into a CSV, and leave its readers puzzled in perpetual pondering.

One way to solve the header association issue is to pick one data row's keys as the anchor so that we can ensure a consistent order of the values of each row:

```python
'''norse_dict.py'''
# ...
def print_csv(rows):
    # print header row
    keys = rows[0].keys()
    print(','.join(keys))
    # print each data row
    for row in rows:
        values = []
        for key in keys:  # reuse ^ header keys list for order consistency
            values.append(row.get(key, ''))
        csv_row = ','.join(['"{}"'.format(v) for v in values])
        print(csv_row)


print_csv([row1, row2, row3])
```

|poi      |revenue|cost   |visits|unique_visitors|
|---------|-------|-------|------|---------------|
|Yggdrasil|790.2  |477.85 |53    |7              |
|Valhalla |1700.65|1500   |11    |10             |
|Asgard   |3215.75|2845.79|265   |71             |

## Sets

The above solution resolves the order issue but leaves out the keys/headers consistency problem intact.

We can probably get a staple list of headers covering all possible `key: value` pairs we may receive over the wire in an ideal world. In reality, we often omit keys that do not have a meaningful value for an excellent reason to save transmission bandwidth and computational space cost. In such a scenario, a more robust solution may look as such:

```python
'''norse_dict.py'''
# ...
# compute a set of comprehensive keys
def print_csv(rows):
    # compute a set of comprehensive keys
    keys = set()
    for row in rows:
        keys = keys.union(row.keys())
    # print header row
    print(','.join(keys))
    # print each data row
    for row in rows:
        # reuse ^ header keys list for order consistency
        values = [row.get(key, '') for key in keys]
        csv_row = ','.join(['"{}"'.format(v) for v in values])
        print(csv_row)

print_csv([row1, row2, row3])
```

|poi      |unique_visitors|revenue|cost|poi_details|visits|
|---------|---------------|-------|----|-----------|------|
|Yggdrasil|7              |790.2  |477.85|           |53    |
|Valhalla |10             |1700.65|1500|           |11    |
|Asgard   |71             |3215.75|2845.79|{'open_days': [1, 2, 3, 4, 5], 'lat': 0.0, 'lon': 0.0, 'wiki_link': 'https://en.wikipedia.org/wiki/Asgard'}|265   |

The additional operations generate a `set` of `keys` that contain the union of all possible keys from given dictionaries (the data rows) with no duplicates, thus solving the second problem from before.

## JSON Format

We use both `dict` and `list` data types to output CSVs as a form of a more universally accepted file format for data transmissions outside of the Python environment.

Another popular choice of such format would be JSON (JavaScript Object Notation), in which its `object` data type loosely correspond to Python `dict`, and its `array` data type loosely correspond to Python `list`:

```python
'''norse_dict.py'''
import json
# ...
# print all rows as one JSON string
def print_json(rows):
    json_str = json.dumps(rows, indent=2)
    print(json_str)

print_json([row1, row2, row3])
```

```shell
% python norse_dict.py
[
  {
    "poi": "Yggdrasil",
    "revenue": 790.2,
    "cost": 477.85,
    "visits": 53,
    "unique_visitors": 7
  },
  {
    "unique_visitors": 10,
    "revenue": 1700.65,
    "cost": 1500,
    "visits": 11,
    "poi": "Valhalla"
  },
  {
    "poi": "Asgard",
    "revenue": 3215.75,
    "cost": 2845.79,
    "visits": 265,
    "unique_visitors": 71,
    "poi_details": {
      "open_days": [
        1,
        2,
        3,
        4,
        5
      ],
      "lat": 0.0,
      "lon": 0.0,
      "wiki_link": "https://en.wikipedia.org/wiki/Asgard"
    }
  }
]
```

The [`json` module](https://docs.python.org/3.8/library/json.html) is from the built-in Python standard library.

## While Loop

So far, we have done repetitions through the use of `for` loops. It is a very intuitive way to iterate over a finite number of values.

To work with iterative tasks that are indefinite, Python offers the `while` loop for such occasions:

```python
'''while_stream.py'''
import requests

r = requests.get('https://httpbin.org/stream/3', stream=True)
lines = r.iter_lines()
line = next(lines, None)
while line is not None:
    print(line.decode() + '\n')
    line = next(lines, None)
```

```shell
% python while_stream.py
{"url": "https://httpbin.org/stream/3", "args": {}, "headers": {"Host": "httpbin.org", "X-Amzn-Trace-Id": "Root=1-6011b5a0-1180880b48461b4112bd8108", "User-Agent": "python-requests/2.25.1", "Accept-Encoding": "gzip, deflate", "Accept": "*/*"}, "origin": "34.x.x.x", "id": 0}

{"url": "https://httpbin.org/stream/3", "args": {}, "headers": {"Host": "httpbin.org", "X-Amzn-Trace-Id": "Root=1-6011b5a0-1180880b48461b4112bd8108", "User-Agent": "python-requests/2.25.1", "Accept-Encoding": "gzip, deflate", "Accept": "*/*"}, "origin": "34.x.x.x", "id": 1}

{"url": "https://httpbin.org/stream/3", "args": {}, "headers": {"Host": "httpbin.org", "X-Amzn-Trace-Id": "Root=1-6011b5a0-1180880b48461b4112bd8108", "User-Agent": "python-requests/2.25.1", "Accept-Encoding": "gzip, deflate", "Accept": "*/*"}, "origin": "34.x.x.x", "id": 2}
```

Let us pick apart the above example:
1. We import [`requests`](https://2.python-requests.org/en/master/), a Python module _not_ from its built-in standard library. It is a widely adopted Python module touting _HTTP for Humans ™_.
2. We perform streaming `HTTP GET` request from the target URL `https://httpbin.org/stream/3`, which specifies the number of responses we would like is `3`.
3. We initiate an iterator for the number of responses from the request and then use the built-in `next()` function to obtain each line.
4. A `while` loop keeps going unless the temporal variable `line` is `None`. Within the context of the `while` loop, after printing each available `line`, it gets re-assigned with the next one and defaults to `None` if no more.

Let us assume that the actual portion of the information we are interested in is the value corresponding to the `origin` key. What we can do is to :

```python
>>> line = '{"url": "https://httpbin.org/stream/3", "args": {}, "headers": {"Host": "httpbin.org", "X-Amzn-Trace-Id": "Root=1-6011b5a0-1180880b48461b4112bd8108", "User-Agent": "python-requests/2.25.1", "Accept-Encoding": "gzip, deflate", "Accept": "*/*"}, "origin": "34.x.x.x", "id": 2}'
>>> line[line.index('"origin": "') + len('"origin": "'):line.index('", "id"')]
'34.x.x.x'
```

The JSON `object` type, by [definition](https://www.json.org), does not guarantee `key: value` orders. This element of inconsistency means that the better approach to extract the information we need would involve the use of the `json` module to load the given JSON string into a dictionary to achieve the task:

```python
'''while_stream.py'''
import json
import requests

r = requests.get('https://httpbin.org/stream/3', stream=True)
lines = r.iter_lines()
line = next(lines, None)
while line is not None:
    data = json.loads(line)
    print(data.get('origin', 'No Trace'))
    line = next(lines, None)
```

```shell
% python while_stream.py
34.x.x.x
34.x.x.x
34.x.x.x
```

The above `while` loop can fit in a `for` loop, given that the iterator implementation is finite:

```python
'''while_stream.py'''
import json
import requests

r = requests.get('https://httpbin.org/stream/3', stream=True)
for line in r.iter_lines():
    data = json.loads(line)
    print(data.get('origin', 'No Trace'))
```

Though for indefinite use-cases, `while` loop may be more reasonable:

```python
'''guess_game.py'''
import random

correct = random.randint(0, 100)

while (guess := int(input('Guess between 0-100: '))) != correct:
    if guess > correct:
        print('{} is too large'.format(guess))
    else:
        print('{} is too small'.format(guess))
else:
    print('{} is correct'.format(guess))
```

```python
python guess_game.py
Guess between 0-100: 50
50 is too large
Guess between 0-100: 25
25 is too large
Guess between 0-100: 12
12 is too small
Guess between 0-100: 19
19 is too small
Guess between 0-100: 22
22 is correct
```

We use the `:=` operator as a way to reduce repetitive temporal variable assignments. In the absence of it, the same game may look like below:

```python
'''guess_game.py'''
import random

correct = random.randint(0, 100)
guess = int(input('Guess between 0-100: '))

while guess != correct:
    if guess > correct:
        print('{} is too large'.format(guess))
    else:
        print('{} is too small'.format(guess))

    guess = int(input('Guess between 0-100: '))
else:
    print('{} is correct'.format(guess))
```

Nowadays, games are hardly interesting unless they can play themselves out:

```python
'''guess_game_auto.py'''
import random

lower = 0
upper = 100
correct = random.randint(lower, upper)
trials = 0

while (guess := (lower + upper) // 2) != correct:
    trials += 1

    if guess > correct:
        print('{} is too large'.format(guess))
        upper = guess - 1
    else:
        print('{} is too small'.format(guess))
        lower = guess + 1

print('{0} is correct after {1} trials'.format(guess, trials))
```

```shell
% python guess_game_auto.py
50 is too large
24 is too small
37 is too large
30 is too small
33 is too small
35 is too large
34 is correct after 6 trials
```

## Loop Controls

Sometimes, we can use direct controls for more flexibility, instead of relying on the decisive factors from a `for` loop or conditions from a `while` loop:

```python
'''while_stream.py'''
import json
import requests

r = requests.get('https://httpbin.org/stream/10', stream=True)
for line in r.iter_lines():
    data = json.loads(line)

    if (_id := data.get('id')) % 2 == 0:
        continue

    origin = data.get('origin', 'No Trace')
    print('ID: {0}, origin: {1}'.format(_id, origin))
```

```shell
% python while_stream.py
ID: 1, origin: 35.x.x.x
ID: 3, origin: 35.x.x.x
ID: 5, origin: 35.x.x.x
ID: 7, origin: 35.x.x.x
ID: 9, origin: 35.x.x.x
```

The above example skips response lines with even `id` values by utilizing the `continue` statement. Similar to the use of `return` in the context of a function, it performs a conceptual _early exit_ that instructs Python to immediately carry on to the next available iteration without executing the logic's remainder.

Sometimes we would need to break out of the loop without further iterations:

```python
'''while_stream.py'''
import json
import requests

r = requests.get('https://httpbin.org/stream/3', stream=True)
for line in r.iter_lines():
    data = json.loads(line)
    origin = data.get('origin', 'No Trace')

    if origin == '192.big.brothers.eyes':
        break

    print('origin: {}'.format(origin))
```

We immediately stop the loop when we see some suspicious origin.
