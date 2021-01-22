# Part 03 - Data Containers and Repetitions (2/3)

When using lists as data containers, it offers us simple access to its items through positional indexes. When the knowledge of each item's positional correspondence is out of reach, we would need something that is more explicit to dictate what each value means.

In Python, one of the most used data types for such a purpose is the dictionary (`dict`):

```python
'''norse_shop.py'''
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

Consider the above example an extension from its [original form-factor](03-data-containers-and-repetitions-1.md#lists) from the `list` introduction. We gain per-value definition though `key: value` pairs by trading off positional significance, which consequently costing more computational space to contain such data. Like a literal dictionary, we can access a definition (the value) by looking up its key:

```python
>>> from norse_shop import (row1, row2)
>>> row1['poi']
'Yggdrasil'
>>> row2['cost']
1500
```

To access dictionary items, we employ a similar syntax of the positional index notion in a more literal sense.
