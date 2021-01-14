# Part 03 - Data Containers and Repetitions

Part 02 gives us a taste of preliminary intelligence that allows the software to react based on conditions or exceptions. Some "brains", if you will.

Data containers allow us to retain more than one value per variable and perform operations on them. To make the software more convenient for the pursuit of automation, we would need some "muscles" too, which would be ways to perform repetitions.

## Lists

Similar to strings, but more capable. Lists (Python type `list`) can be used to contain a sequence of more than one type of data within.

```python
'''play_list.py'''
header = ['Country', 'Region', 'City', 'Spend', 'Cost', 'Bids', 'Impressions', 'Clicks']
row1 = ['CA', 'ON', 'Carleton Place', 56.574, 28.7143, 33432, 9431, 13]
row2 = ['CA', 'QC', 'Alma', 10.176, 4.7367, 2947, 1697, 1]
```

The above example can be conceptualized as a data table or spreadsheet. The `header` variable holds a `list` of `string` values while `row1` and `row2` each holds a `list` of mixed `string`, `float`, and `int` values.

```python
'''play_list.py'''
# ...
csv_header = ','.join(header)
print(csv_header)
```

In fact we can loosely translate a `list` into a CSV (comma-separate-values) formatted string by leveraging a `str.join()` method.

```shell
% python play_list.py > play_list.csv
% open play_list.csv
```

![csv](https://i.imgur.com/uL6psVb.png)

_Note_: the `str.join()` method can be roughly seen as a way to concatenate a sequence of strings with a common separator (or delimiter) string value. This roughly represents a school of programming paradigm known as _declaritive_ programming, where the users of the language describe the "what" is to be achieved. This distincts from another school of paradigm known as _imperative_ programming, where the users would need to describe the "how", such as string concatenation by using `+` operators.

Let us attempt the same with the actual data rows:

```python
'''play_list.py'''
# ...
csv_row1 = ','.join(row1)
print(csv_row1)
```

```shell
% python play_list.py > play_list.csv
Traceback (most recent call last):
  File "play_list.py", line 9, in <module>
    csv_row1 = ','.join(row1)
TypeError: sequence item 3: expected str instance, float found
```

An error is raised, indicating a violation of the expected type for the `str.join()` method to work only with `str` in the sequence, which in this case is the `list` `row1`.

Lists are indeed one of the sequence types, so are strings, which are sequences of individual string characters:

```python
>>> '.'.join('Canada')
'C.a.n.a.d.a'
```

Circle back to the error from above, as we identified that starting from item 3 (or the 4th item), which would be `56.574` that is of type `float`, we can apply type casting to fix that and all other non-string values:

```python
'''play_list.py'''
# ...
row1[3] = str(row1[3])
row1[4] = str(row1[4])
row1[5] = str(row1[5])
row1[6] = str(row1[6])
row1[7] = str(row1[7])
csv_row1 = ','.join(row1)
print(csv_row1)
```

![csv2](https://i.imgur.com/QHJzOl1.png)

As `list` is a sequence type as `str`, so does it have the notion of index operations just like strings. However, one key difference involves the concept of mutation:

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
'''play_list.py'''
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
4. When the condition from point 3 is satisfied, we cast the member at that given index `i` into `str` type.

_Note_: the `if` condition within the `for` loop does not serve a practical purpose and removing it entirely works because `str('already string') == 'already string'`, and the computational cost is negligible in this particular case.

Let us wrap this operation into a function and apply it to both row lists through another `for` loop:

```python
'''play_list.py'''
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
% python play_list.py > play_list.csv
% open play_list.csv
```

![csv3](https://i.imgur.com/k68KrVc.png)

## Beware of Mutations

Things are coming up nicely. Along the same module `play_list.py`, if we now want to perform arithmetics such as finding the _profit_ by subtracting _spend_ and _cost_, we will surely encounter another, albeit familiar, type error:

```python
'''play_list.py'''
# ...
# add profit header
header.append('Profit')

csv_header = ','.join(header)
print(csv_header)

for row in [row1, row2]:
    mutate_row(row)
    csv_row = ','.join(row)
    # compute profit for each row and concatenate to the csv_row
    profit = row[3] - row[4]
    # another way to concatenate strings
    csv_row = ','.join([csv_row, str(profit)])
    print(csv_row)
```

```shell
% python play_list.py > play_list.csv
Traceback (most recent call last):
  File "play_list.py", line 19, in <module>
    profit = row[3] - row[4]
TypeError: unsupported operand type(s) for -: 'str' and 'str'
```

The reason is apparent and we have seen and fixed similar issues before.

But before we attempt to do so, let us revisit the function `mutate_row()` and discuss the very concept _mutation_ it is based on.

Mutations exist for some good reasons. The most prominent is that it allows makers to make in-place operations to a data container without provisioning extra memory (space) overhead to achieve a similar objective.

But in this case, if we do tradeoff some extra cost on space, we would retain the integrity of the original rows which would allow us to carry on the intended computations for _profit_.

```python
'''play_list.py'''
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
    profit = row[3] - row[4]
    # another way to concatenate strings
    csv_row = ','.join([csv_row, str(profit)])
    print(csv_row)
```

```shell
% python play_list.py > play_list.csv
% open play_list.csv
```

![csv4](https://i.imgur.com/BgTkb95.png)

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

The greater ability that a mutable sequence type, like `list`, comes with inherently greater responsibility for its users. As a common convention and etiquette, abstractions involving mutable data containers usually carry out immutable operations (like `convert_row()`, instead of `mutate_row()`) to offer flexibility and undesired _side effects_.
