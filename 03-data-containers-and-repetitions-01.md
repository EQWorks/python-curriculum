# Part 03 - Data Containers and Repetitions (1/3)

Part 02 gives us a taste of rudimentary intelligence that allows the software to react based on conditions or exceptions. Some brains, if you will.

Data containers allow us to retain more than one value per variable and perform operations on them. To make the software more convenient for the pursuit of automation, we would need some muscles too, which would be ways to perform repetitions.

## Lists

Similar to strings, but more capable, Python Lists (`list`) can contain a sequence of more than one type of data within.

```python
'''norse_shop.py'''
header = ['poi', 'revenue', 'cost', 'visits', 'unique_visitors']
row1 = ['Yggdrasil', 790.2, 477.85, 53, 7]
row2 = ['Valhalla', 1700.65, 1500, 11, 10]
```

One can conceptualize the above example as a data table or spreadsheet. The `header` variable holds a `list` of `string` values while `row1` and `row2` each contain a `list` of mixed `string`, `float`, and `int` values.

```python
'''norse_shop.py'''
# ...
csv_header = ','.join(header)
print(csv_header)
```

In fact we can loosely translate a `list` into a CSV (comma-separate-values) formatted string by leveraging a `str.join()` method.

```shell
% python norse_shop.py
```

|poi      |revenue|cost  |visits|unique_visitors|
|---------|-------|------|------|---------------|
|         |       |      |      |               |

Let us attempt the same with the actual data rows:

```python
'''norse_shop.py'''
# ...
csv_row1 = ','.join(row1)
print(csv_row1)

csv_row2 = ','.join(row2)
print(csv_row2)
```

```shell
% python norse_shop.py
Traceback (most recent call last):
  File "norse_shop.py", line 9, in <module>
    csv_row1 = ','.join(row1)
TypeError: sequence item 1: expected str instance, float found
```

The above error indicates a violation of the expected type for the `str.join()` method to work only with a sequence of `str` values. As we identify that starting from item 1 in `row1` (or the second item), which would be `790.2` that is of type `float`, we can apply type casting to fix that and all other non-string values:

```python
'''norse_shop.py'''
# ...
row1[1] = str(row1[1])  # index 1 (second item)
row1[2] = str(row1[2])  # index 2 (third item)
row1[3] = str(row1[3])  # index 3 (fourth item)
row1[4] = str(row1[4])  # index 3 (fourth item)
csv_row1 = ','.join(row1)
print(csv_row1)
```

|poi      |revenue|cost  |visits|unique_visitors|
|---------|-------|------|------|---------------|
|Yggdrasil|790.2  |477.85|53    |7              |

As `list` is a sequence type like `str`, so does it have the notion of index operations. However, one key difference involves the concept of mutation:

```python
>>> s = 'Canada'
>>> s[0] = 'B'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> l = ['C', 'a', 'n', 'a', 'd', 'a']
>>> l[0] = 'B'
>>> l[-2] = 'n'
>>> l
['B', 'a', 'n', 'a', 'n', 'a']
>>> ''.join(l)
'Banana'
```

Individual items of a string cannot be mutated by assignment, while in a list they can.

## For Loop

Performing operations on individual items of a list one by one feel like a chore. Through a `for` loop we can automate that chore away:

```python
'''norse_shop.py'''
# ...
for i in range(len(row1)):
    if type(row1[i]) is not str:
        row1[i] = str(row1[i])

csv_row1 = ','.join(row1)
print(csv_row1)
```

To digest the code snippet above:
1. A `range()` of item indexes of the targeting `list` (`row1`) with the help of the `len()` function.
2. A `for` loop iterates `in` that range of indexes, where each temporal variable `i` represents the positional index from left-to-right (or from 0 to length - 1) corresponds to each list item.
3. An `if` condition specifies our intent to cast non-string values into the `str` type.
4. When the condition from point 3 is satisfied, we _mutate_ the item at that given index `i` by casting it into the `str` type.

_Note_: the `if` condition within the `for` loop does not serve a practical purpose. Removing it works because `str('already string') == 'already string'`, and the computational cost is negligible in this particular case.

Let us wrap this operation into a function and apply it to both rows through another `for` loop:

```python
'''norse_shop.py'''
# ...
def mutate_row(row):
    for i in range(len(row)):
        row[i] = str(row[i])

for row in [row1, row2]:
    mutate_row(row)
    csv_row = ','.join(row)
    print(csv_row)
```

```shell
% python norse_shop.py
```

|poi      |revenue|cost  |visits|unique_visitors|
|---------|-------|------|------|---------------|
|Yggdrasil|790.2  |477.85|53    |7              |
|Valhalla |1700.65|1500  |11    |10             |


Notice the difference in the `for` loop usages. Unlike in the `mutate_row()` function, the outer loop iterates through a list of lists by _value_ (instead of by index). Both cases are an iteration of sequences with different objectives and access patterns.

## Beware of Mutations

Things are coming up nicely. But if we want to find the _profit_ (`revenue - cost`), we will surely encounter another, albeit familiar, type error:

```python
'''norse_shop.py'''
# ...
# add profit header
header.append('profit')

csv_header = ','.join(header)
print(csv_header)

for row in [row1, row2]:
    mutate_row(row)
    csv_row = ','.join(row)
    # compute profit for each row and concatenate to the csv_row
    profit = row[1] - row[2]
    # another way to concatenate strings
    csv_row = ','.join([csv_row, str(profit)])
    print(csv_row)
```

```shell
% python norse_shop.py
Traceback (most recent call last):
  File "norse_shop.py", line 17, in <module>
    profit = row[1] - row[2]
TypeError: unsupported operand type(s) for -: 'str' and 'str'
```

The issue is trivial to fix. Before we attempt to do so, let us revisit the function `mutate_row()` and discuss the very concept of _mutation_.

Mutations exist for some good reasons. The most prominent is that it allows us to make in-place operations to a data container without provisioning extra memory (space) overhead to achieve the same objective.

But in this case, if we do tradeoff some extra cost on space, we would retain the integrity of the original rows to carry on the intended computations for _profit_ in a straightforward manner.

```python
'''norse_shop.py'''
# ...
def convert_row(row):
    new_row = []

    for i in range(len(row)):
        new_row.append(str(row[i]))

    return new_row

for row in [row1, row2]:
    new_row = convert_row(row)
    csv_row = ','.join(new_row)
    # compute profit for each row and concatenate to the csv_row
    profit = row[1] - row[2]
    # another way to concatenate strings
    csv_row = ','.join([csv_row, str(profit)])
    print(csv_row)
```

```shell
% python norse_shop.py
```

|poi      |revenue|cost  |visits|unique_visitors|profit           |
|---------|-------|------|------|---------------|-----------------|
|Yggdrasil|790.2  |477.85|53    |7              |312.35           |
|Valhalla |1700.65|1500  |11    |10             |200.6500000000001|

You may argue that we can perform all necessary computations before the mutation for CSV string formation. While that is true, the point of avoiding them is about where the responsibility of the original data integrity lies. Mutable approaches such as `mutate_row()` give no flexibility and push that responsibility to its users before the mutation, while immutable ways like `convert_row()` do so more gracefully with options for users aftermath:

```python
# users have a flexible choice with an immutable approach
new_row1 = convert_row(row1)  # assign anew
row1 = convert_row(row1)  # override the original to emulate mutation if desired

# workaround with a mutable approach
# basically re-implement `convert_row()` itself
new_row1 = []

for i in range(len(row1)):
    new_row1.append(row1[i])

mutate_row(new_row1)  # new_row1 is now mutated
```

The capability that a mutable data type (such as `list`) grants require greater responsibility from its users. As a convention and etiquette, abstractions involving mutable data types usually carry out immutable operations.

## List Mechanisms

## Shallow Copy

The intention to use a `for` loop to generate `new_row` is basically to copy the original list so that any potential mutation conducted on `new_row` does not contaminate the original. Python lists come with a built-in method for such a purpose:

```python
def convert_copy_row(row):
    new_row = row.copy()

    for i in range(len(new_row)):
        new_row[i] = str(new_row[i])

    return new_row
```

Unlike `convert_row()` function where we start with an empty `list` and iteratively populate with the string version of the `row` items, `convert_copy_row()` function starts with a shallow copy of `row`, and perform in-place mutation on the copy instead of the original. It is however only a _shallow_ copy of the immediate items, which means that if any of the items are also mutable data types, they may still suffer from undesired mutations:

```python
a = ['a', [1, 2, 3]]
b = a.copy()
# mutation tests
b[0] = 'b'
assert b[0] == 'b'
assert a[0] == 'a'  # list a still intact
b[1][0] = 10
assert b[1][0] == 10
assert a[1][0] == 1  # would raise AssertionError
```

```python
Traceback (most recent call last):
  ...
    assert a[1][0] == 1
AssertionError
```

To fix above, you can iteratively copy the nested list items:

```python
a = ['a', [1, 2, 3]]
# custom deeper copy
b = []  # outer new list
for i in range(len(a)):
    if type(a[i]) is list:
        inner = []  # inner new list
        for ii in range(len(a[i])):
            inner.append(a[i][ii])  # make "deeper" of the nested items
        b.append(inner)
    else:
        b.append(a[i])
# mutation tests
b[0] = 'b'
assert b[0] == 'b'
assert a[0] == 'a'  # list a still intact
b[1][0] = 10
assert b[1][0] == 10
assert a[1][0] == 1
```

We should prefer a flat list data structure to avoid undesired mutations on nested mutable data items. Recall "The Zen of Python" (`>>> import this`):

> Flat is better than nested.

```python
a = ['a', 1, 2, 3]
b = a.copy()
# mutation tests
b[0] = 'b'
assert b[0] == 'b'
assert a[0] == 'a'  # list a still intact
b[2] = 10
assert b[2] == 10
assert a[2] == 1
```

## Comprehensions

In computer science terms, copy a list using a `for` loop is _imperative_ (programmers describe the "how"), whereas the `list.copy()` method represents a _declarative_ way (programmers state the "what").

The imperative techniques are usually more verbose but offer more internal visibility of the mechanism. On the other hand, their declarative counterparts (where applicable) offer simplicity with less control.

The Python language offers a compromise between the two, called comprehensions, that offer greater control than the declarative equivalent while keeping the expressions less verbose than the imperative ways:

```python
a = ['a', 1, 2, 3]
# copy `a` through list comprehension
b = [v for v in a]
```

This approach leverages the fact that we only intend to utilize the individual values of the items of the original list. With this in mind, the original `norse_shop.py` can be revised as such:

```python
'''norse_shop.py'''
header = ['poi', 'revenue', 'cost', 'visits', 'unique_visitors']
row1 = ['Yggdrasil', 790.2, 477.85, 53, 7]
row2 = ['Valhalla', 1700.65, 1500, 11, 10]

header.append('profit')
csv_header = ','.join(header)
print(csv_header)

def get_profit(row):
    return row[1] - row[2]

for row in [row1, row2]:
    # list comprehension to replace `convert_row()`
    new_row = [str(v) for v in row]
    # compute profit
    profit = get_profit(row)
    new_row.append(str(profit))
    # transform to CSV string and print out
    csv_row = ','.join(new_row)
    print(csv_row)
```

## Concatenations

Like strings, lists can be concatenated too:

```python
header = ['poi', 'revenue', 'cost', 'visits', 'unique_visitors']
header = header + ['profit', 'profit_margin', 'avg_revenue', 'avg_visits']

csv_header = ','.join(header)
print(csv_header)
```

|poi      |revenue|cost  |visits|unique_visitors|profit           |profit_margin      |avg_revenue       |avg_visits       |
|---------|-------|------|------|---------------|-----------------|-------------------|------------------|-----------------|
|         |       |      |      |               |                 |                   |                  |                 |

## Exercises

### Problem 01 - Profit margin, average revenue, average visits

Take the final `norse_shop.py` as a base, implement:

* `get_profit_margin()` - to compute the profit margin based on `profit / revenue`
* `get_avg_revenue()` - to compute the average `revenue` by `unique_visitors`
* `get_avg_visits()` - to compute the average `visits` by `unique_visitors`

Then apply these newly implemented functions to enrich the output CSV as such:

|poi      |revenue|cost  |visits|unique_visitors|profit           |profit_margin      |avg_revenue       |avg_visits       |
|---------|-------|------|------|---------------|-----------------|-------------------|------------------|-----------------|
|Yggdrasil|790.2  |477.85|53    |7              |312.35           |0.3952796760313845 |112.88571428571429|7.571428571428571|
|Valhalla |1700.65|1500  |11    |10             |200.6500000000001|0.11798430012054219|170.065           |1.1              |
