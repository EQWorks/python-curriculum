# Part 03 - Data Containers and Repetitions

Part 02 gives us a taste of rudimentary intelligence that allows the software to react based on conditions or exceptions. Some "brains", if you will.

Data containers allow us to retain more than one value per variable and perform operations on them. To make the software more convenient for the pursuit of automation, we would need some "muscles" too, which would be ways to perform repetitions.

## Lists

Similar to strings, but more capable. Lists (Python type `list`) can be used to contain a sequence of more than one type of data within.

```python
'''norse_shop.py'''
header = ['poi', 'revenue', 'cost', 'visits', 'unique_visitors']
row1 = ['Yggdrasil', 790.2, 477.85, 53, 7]
row2 = ['Valhalla', 1700.65, 1500, 11, 10]
```

The above example can be conceptualized as a data table or spreadsheet. The `header` variable holds a `list` of `string` values while `row1` and `row2` each holds a `list` of mixed `string`, `float`, and `int` values.

```python
'''norse_shop.py'''
# ...
csv_header = ','.join(header)
print(csv_header)
```

In fact we can loosely translate a `list` into a CSV (comma-separate-values) formatted string by leveraging a `str.join()` method.

```shell
% python norse_shop.py > norse_shop.csv
% open norse_shop.csv
```

![csv](https://i.imgur.com/mR1qxIN.png)

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
% python norse_shop.py > norse_shop.csv
Traceback (most recent call last):
  File "norse_shop.py", line 9, in <module>
    csv_row1 = ','.join(row1)
TypeError: sequence item 1: expected str instance, float found
```

An error is raised, indicating a violation of the expected type for the `str.join()` method to work only with a sequence of `str` values. As we identify that starting from item 1 in `row1` (or the second item), which would be `790.2` that is of type `float`, we can apply type casting to fix that and all other non-string values:

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

![csv2](https://i.imgur.com/oLLfzrF.png)

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

Individual members of a string cannot be mutated by assignment, while in lists they can.

## For loop

Performing operations on individual members of a list one by one _works_ but feels like a chore. Through a `for` loop we can automate that chore away:

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
1. A `for` loop iterates `in` a `range()` based on the length of the targeting `list` (`len(row1)`).
2. Each iteration gets an `i` value that ranges from `0` to the length of the list minus 1, which corresponds to each index position of the list members.
3. An `if` condition specifies our intent to cast non-string values into the `str` type.
4. When the condition from point 3 is satisfied, we _mutate_ the member at that given index `i` by casting it into the `str` type.

_Note_: the `if` condition within the `for` loop does not serve a practical purpose and removing it entirely works because `str('already string') == 'already string'`, and the computational cost is negligible in this particular case.

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
% python norse_shop.py > norse_shop.csv
% open norse_shop.csv
```

![csv3](https://i.imgur.com/73hg556.png)

## Beware of Mutations

Things are coming up nicely. Along the same module `norse_shop.py`, if we now want to perform arithmetics such as finding the _profit_ by subtracting _revenue_ and _cost_, we will surely encounter another, albeit familiar, type error:

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
% python norse_shop.py > norse_shop.csv
Traceback (most recent call last):
  File "norse_shop.py", line 17, in <module>
    profit = row[1] - row[2]
TypeError: unsupported operand type(s) for -: 'str' and 'str'
```

The reason is obvious and it is trivial to fix. Before we attempt to do so, let us revisit the function `mutate_row()` and discuss the very concept _mutation_ it is based on.

Mutations exist for some good reasons. The most prominent is that it allows makers to make in-place operations to a data container without provisioning extra memory (space) overhead to achieve the same objective.

But in this case, if we do tradeoff some extra cost on space, we would retain the integrity of the original rows which would allow us to carry on the intended computations for _profit_.

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
% python norse_shop.py > norse_shop.csv
% open norse_shop.csv
```

![csv4](https://i.imgur.com/caQqDo9.png)

You may argue that you can carry out the computation of profit before the mutation of the original row list. Whilst true, the point of avoiding mutations, or at least unannounced mutations, is that software is usually written and used collaboratively, abstractions such as `mutate_row()` pushes the responsibility of determining whether the original data container's integrity should be kept to its users, while immutable approaches like `convert_row()` simply does not alternate the original data container it receives as its argument, and leave the flexibility to its users if they want to override the original or not:

```python
# users have a flexible choice with an immutable approach
new_row1 = convert_row(row1)  # assign anew
row1 = convert_row(row1)  # override the original to emulate mutation if desired

# workaround with a mutable approach
# basically re-implement convert_row() itself
new_row1 = []

for i in range(len(row1)):
    new_row1.append(row1[i])

mutate_row(new_row1)  # new_row1 is now mutated
```

The greater ability that a mutable sequence type grants, like `list`, comes with inherently greater responsibility for its users. As a common convention and etiquette, abstractions involving mutable data containers usually carry out immutable operations (like `convert_row()`, instead of `mutate_row()`) to offer flexibility and undesired _side effects_.


The `covert_row()` function employs an _imperative_ approach and can be quite verbose to write and tedious to maintain, especially if we want to operate based on a given mutable sequence type like our data rows. Fortunately, Python provides some alternatives that are more succinct.

### Shallow Copy

The intention of the use of a for loop to generate `new_row` is basically to copy the original list so that any potential mutation conducted on `new_row` does not carried over to the original.

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

Recall "The Zen of Python" (`>>> import this`):

> Flat is better than nested.

In scenarios where the formfactor of the source data (such as `a` from above example) can be controlled, we should always try to flatten it so that there are no nested mutable data types to handle, and a rather simple and _declarative_ `list.copy()` can get the job done elegantly.

<!--
### Comprehension

...middle ground between declarative and verbose imperative...

...final version of the full script of norse_shop.py...
-->

## Exercises

### Problem 01 - Profit margin, average revenue, average visits

Take the final `norse_shop.py` as a base, implement:

* `add_profit_margin()` - to compute the profit margin based on `profit / revenue * 100%`
* `add_avg_revenue()` - to compute the average `revenue` per `unique_visitor`
* `add_avg_visits()` - to compute the average `visits` per `unique_visitor`

<!-- TODO: show sample output etc. -->
