# Part 03 - Data Containers and Repetitions (3/3)

## Classes

Similar to pre-made LEGO® pieces, Python offers plenty of built-in [functions](https://docs.python.org/3.8/library/functions.html) and [types](https://docs.python.org/3.8/library/stdtypes.html) for many possible applications.

At times, there are needs to have more flexibility and customizations. Python offers its `class` interface for us to create our own _type_, as our fourth abstraction building block:

```python
'''norse_type.py'''
import json

class Norse:

    def __init__(self, data):
        self.data = data

    def to_json(self):
        return json.dumps(self.data)
```

And with a JSON file as the source for our data:

```json
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

```python
'''norse_connector.py'''
import json

from norse_type import Norse

with open('./norse.json', mode='r') as f:
    data = json.load(f)

n = Norse(data)

print(type(n))
print()
print(n.data)
print()
print(n.to_json())
```

```shell
% python norse_connector.py
<class 'norse_type.Norse'>

[{'poi': 'Yggdrasil', 'revenue': 790.2, 'cost': 477.85, 'visits': 53, 'unique_visitors': 7}, {'unique_visitors': 10, 'revenue': 1700.65, 'cost': 1500, 'visits': 11, 'poi': 'Valhalla'}, {'poi': 'Asgard', 'revenue': 3215.75, 'cost': 2845.79, 'visits': 265, 'unique_visitors': 71, 'poi_details': {'open_days': [1, 2, 3, 4, 5], 'lat': 0.0, 'lon': 0.0, 'wiki_link': 'https://en.wikipedia.org/wiki/Asgard'}}]

[{"poi": "Yggdrasil", "revenue": 790.2, "cost": 477.85, "visits": 53, "unique_visitors": 7}, {"unique_visitors": 10, "revenue": 1700.65, "cost": 1500, "visits": 11, "poi": "Valhalla"}, {"poi": "Asgard", "revenue": 3215.75, "cost": 2845.79, "visits": 265, "unique_visitors": 71, "poi_details": {"open_days": [1, 2, 3, 4, 5], "lat": 0.0, "lon": 0.0, "wiki_link": "https://en.wikipedia.org/wiki/Asgard"}}]
```

A few observations:
1. We read a JSON file, load its content into a dictionary through the built-in `json` module, then _instantiate_ the dictionary into a custom `Norse` type object.
2. We verify the type of the new instance in variable `n` as `<class 'norse_type.Norse'>`.
3. We access the instance's `data` property and verify it's indeed the dictionary loaded through in step 1.
4. We invoke the instance's `to_json()` method to output the JSON string derived from its `data` property.

The `self` name is merely a convention to indicate that it is applicable to the type's _instance itself_, thus it _can_ be named as any valid variable name, as long as it is the _first_ argument of the method definition. Many other programming languages enforce it to be called "`this`". This concept is important to understand in order to make great use of classes, objects and the programming paradigm known as _Object-oriented programming_.

### I/O - File system (input)

Let us develop some further capabilities to our `Norse` class, say internalize the file reading so one can instantiate a new `Norse` type object by calling `n = Norse('./data.json')`:

```python
'''norse_type.py'''
import json


def read_from(fname):
    with open(fname, mode='r') as f:
        return json.load(f)


class Norse:
    def __init__(self, data):
        if type(data) is str:
            self.data = read_from(data)
        else:
            self.data = data

    def to_json(self):
        return json.dumps(self.data)
```

And simplify `norse_connector` as so:

```python
'''norse_connector.py'''
from norse_type import Norse

n = Norse('./norse.json')

print(type(n))
print()
print(n.data)
print()
print(n.to_json())
```

File system is one of the most important forms of I/O (input/output) of a modern computer system. Though greatly differed in implementation by operating systems, programming languages like Python provides elegant abstraction on top of them so the way to access files regardless of where it is running on.

### With context manager

The `with` statement involves an interesting Python mechanism known as runtime context management, you can read more details about it through its [official documentation](https://docs.python.org/3.8/reference/compound_stmts.html#with). In this particular case, the built-in `open()` function implements such a context manager which eliminates the need of some common chores such as opening a file and closing it when it is no longer needed (or when an exception is raised).

### I/O - File system (output)

Let us add a file output capability to the `to_json()` method:

```python
'''norse_type.py'''
# ...

def write_to(data, fname):
    with open(fname, mode='w') as f:
        json.dump(data, f, indent=2)


class Norse:
    # ...

    def to_json(self, fname=''):
        if not fname:
            return json.dumps(self.data)

        return write_to(self.data, fname)
```

And used so:

```python
'''norse_connector.py'''
from norse_type import Norse

n = Norse('./norse.json')
# output to ./norse_processed.json
n.to_json('./norse_processed.json)
```

Of course, the content of the `norse_processed.json` file should be identical as the input `norse.json` file, as we have yet to make any changes.

### State management

In many occasions, encapsulating data and expose access and operations to them through object properties and methods offer no distinct edge over simple functions. In some programming languages, where object-oriented programming is rigidly enforced, there may be no choice but to organize all logics into various classes.

In Python, the choice is flexible, therefore utility functions that are agnostic to the internal state (the `data` property) such as `read_from()` and `write_to()` are scoped outside of the class definition. And we apply functions in the form of methods such as `to_json()` that depend on the object's internal state.

It becomes more valuable as we provide abstractions that perform further state manipulations as a gateway for a more convenient and declarative interface for its users:

```python
'''norse_type.py'''
# ...

def flatten_norse(row):
    flat = {}

    for k, v in row.items():
        if type(v) is not dict:
            flat[k] = v
        else:
            for nk, nv in v.items():
                flat['{0}.{1}'.format(k, nk)] = nv

    return flat


class Norse:
    # ...
    def flatten(self):
        for i, row in enumerate(self.data):
            self.data[i] = flatten_norse(row)
```

```python
'''norse_connector.py'''
from norse_type import Norse

n = Norse('./norse.json')

n.flatten()
n.to_json('./norse_processed.json')
```

We take the `flatten_norse()` implementation from [the exercise of last section](03-data-containers-and-repetitions-2.md#exercises), apply it to mutate the internal state `data` to have each of its rows flattened. The built-in `enumerate()` function is used to generate an indexed iterator so we have easy access to both the list's index and the corresponding individual item:

```json
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
    "poi_details.open_days": [
      1,
      2,
      3,
      4,
      5
    ],
    "poi_details.lat": 0.0,
    "poi_details.lon": 0.0,
    "poi_details.wiki_link": "https://en.wikipedia.org/wiki/Asgard"
  }
]
```

There is no settled convention among Python developers on whether to keep as much inside or outside of classes. One viable approach as demonstrated here is to derive out _stateless_ logic in the form of functions outside of classes, while keeping only _stateful_ (dependent on current property value of `data`) ones inside the class.

## Pandas

If we were to build a set of comprehensive abstractions to perform common data manipulation and analaysis tasks, it would take a while. Thanks to the ever-more-prosperous open source software ecosystem, there are many well built third party libraries that offer more advanced building blocks to alliviate us from reinventing unnecessary wheels.

Among them, [Pandas](https://pandas.pydata.org/) is one of the most popular Python libraries we can use today to handle data:

```python
'''norse_pandas.py'''
import pandas as pd

df = pd.read_json('./norse.json')
print(df)
```

```shell
% python norse_pandas.py
         poi  revenue  ...  unique_visitors                                        poi_details
0  Yggdrasil   790.20  ...                7                                                NaN
1   Valhalla  1700.65  ...               10                                                NaN
2     Asgard  3215.75  ...               71  {'open_days': [1, 2, 3, 4, 5], 'lat': 0.0, 'lo...

[3 rows x 6 columns]
```

Pandas' primary interface of abstraction is their `DataFrame`, and many utility abstractions are built around that. It does not just stop at file I/O. Let us try some simple statistics with some ["real" data](data/poi_stats.json), through HTTP API as a form of input:

```python
'''poi_stats.py'''
import pandas as pd
import requests

data_url = 'https://raw.githubusercontent.com/EQWorks/python-curriculum/03/main/data/poi_stats.json'
with requests.get(data_url) as r:
    data = r.json()

df = pd.DataFrame.from_dict(data)
print('Means:')
print(df.mean())
print('\nMedians:')
print(df.median())
print('\nStandard deviations:')
print(df.std())
```

```shell
% python poi_stats.py
Means:
visitors     952.081400
visits      1617.321000
revenue     5199.971570
cost        2609.954645
dtype: float64

Medians:
visitors     954.000000
visits      1448.000000
revenue     3986.244819
cost        1418.963295
dtype: float64

Standard deviations:
visitors     549.615419
visits      1221.698989
revenue     4575.798056
cost        3075.278290
dtype: float64
```
