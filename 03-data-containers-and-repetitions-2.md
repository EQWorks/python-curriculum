# Part 03 - Data Containers and Repetitions (2/3)

A list offers us simple access to its items through positional indexes. When the control of each item's positional correspondence is out of reach, we would need something that is more explicit to dictate what each value means.

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

Consider the above example an extension from its [original form-factor](03-data-containers-and-repetitions-1.md#lists) from the `list` introduction. We gain per-value definition though `key: value` pairs by trading off positional significance, which consequently costing more computational space to contain such data. What we gain, like with a literal dictionary, is the direct access of definitions (the value) by looking up their keys:

```python
>>> from norse_dict import row1, row2
>>> row1['poi']
'Yggdrasil'
>>> row2['cost']
1500
```

To access dictionary items, we employ a similar syntax of the positional index notion in a more literal sense.

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

From the above example, we can understand that it would be more difficult to use lists to work with data that has no guarantee of data consistency, since each index holds an implicit but also rigid definition of what each value represents.

In contrast, dictionaries would suffer some other problem precisely due to how insignificant their `key: value` pairs are ordered:

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

Since `row2` has a different order of its `key: value` pairs than `row1`, and `row3` has an extra `key` that the other two do not have, we would get a not so useful of an output if we attempt to marshall the data into a CSV, and leave its readers puzzled in perpectual pondering.

One way to solve the header association issue is to pick one data row's keys as the anchor, so we can ensure a consistent order of the values of each row:

```python
'''norse_dict.py'''
# ...
# print header row
keys = row1.keys()
print(','.join(keys))
# print each data row
for row in [row1, row2, row3]:
    values = []
    for key in keys:  # reuse ^ header keys list for order consistency
        values.append(row.get(key, ''))
    csv_row = ','.join(['"{}"'.format(v) for v in values])
    print(csv_row)
```

|poi      |revenue|cost   |visits|unique_visitors|
|---------|-------|-------|------|---------------|
|Yggdrasil|790.2  |477.85 |53    |7              |
|Valhalla |1700.65|1500   |11    |10             |
|Asgard   |3215.75|2845.79|265   |71             |

## Sets

The above solution resolves the order issue, but leaves out the keys/headers consistency problem intact.

In an ideal world, we can probably get a staple list of headers that cover all possible `key: value` pairs we may receive over the wire. In reality, keys that do not have a meaningful value are often omitted for a very good reason to save transmission bandwidth and computational space cost. In such a scenario, a more robust solution may look as such:

```python
'''norse_dict.py'''
# ...
# compute a set of comprehensive keys
keys = set()
for row in [row1, row2, row3]:
    keys = keys.union(row.keys())
# print header row
print(','.join(keys))
# print each data row
for row in [row1, row2, row3]:
    # reuse ^ header keys list for order consistency
    values = [row.get(key, '') for key in keys]
    csv_row = ','.join(['"{}"'.format(v) for v in values])
    print(csv_row)
```

|poi      |unique_visitors|revenue|cost|poi_details|visits|
|---------|---------------|-------|----|-----------|------|
|Yggdrasil|7              |790.2  |477.85|           |53    |
|Valhalla |10             |1700.65|1500|           |11    |
|Asgard   |71             |3215.75|2845.79|{'open_days': [1, 2, 3, 4, 5], 'lat': 0.0, 'lon': 0.0, 'wiki_link': 'https://en.wikipedia.org/wiki/Asgard'}|265   |

The additional operations generate a `set` of `keys` that contain the union of all possible keys from given dictionaries (the data rows) with no duplicates, thus solving the second problem from before.

## While Loop

So far we have done repetitions through the use of `for` loops. It is a very intuitive way to iterate over a finite number of values.

To work with iterative tasks that are indefinite in nature, Python offers the `while` loop for such occasions:

```python
'''while_eg.py'''
import random

n = 0
l = []
while n < random.randint(1, 100):
    l.append(n)
    n += 1

print(l)
```

Which may produce a different list each time we execute the script:

```shell
% python while_eg.py
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
% python while_eg.py
[0, 1, 2, 3]
```
