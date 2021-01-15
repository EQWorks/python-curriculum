# Part 02 - Logic Controls (2/2)

## Error Controls and Controlled Errors

The nature of logic controls we have seen are only as comprehensive as what a maker makes them be. Thus the uncaught cases become exceptions and contribute toward software flaws and errors.

### try/except

```python
>>> 1 / 0
Traceback (most recent call last):
  ...
ZeroDivisionError: division by zero
```

Division by zero has various consequences depending on the computation environment. In Python, such an attempt would _raise_ a `ZeroDivisionError`.

Python provides `try/except` to capture errors like this:

<a name="blanket-exception"></a>

```python
>>> try:
...     1 / 0
... except:
...     pass
```

The above handling practically suppresses any errors. It is often more beneficial to be more explicit about which type(s) of errors to handle:

```python
>>> a = 0
>>> b = '5'
>>> try:
...     b / a
... except ZeroDivisionError:
...     pass
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
TypeError: unsupported operand type(s) for /: 'str' and 'int'
```

The revised example from above takes a variable `b` and divides it by `a`. While it handles (suppresses) the anticipated `ZeroDivisionError`, the unhandled errors would still surface. Similar to conditional statements, one can switch through more than one exception handling, and nested too, to selectively cover more grounds:

```python
>>> b = 'bob'
>>> a = '5'
>>> try:
...     c = b / a
... except ZeroDivisionError:
...     # handle zero division error when a == 0
...     c = a / b
... except TypeError:
...     # handle type error
...     try:
...         c = int(b) / int(a)
...     except ValueError:
...         print('we cannot perform {0} ({1}) / {2} ({3}'.format(
...             b, type(b), a, type(a)))
... except:
...     # theoretical last resort to catch any other errors
...     pass
...
we cannot perform bob (<class 'str'>) / 5 (<class 'str'>
```

_Note_: you can find more details about the `str.format()` method in its [official documentation](https://docs.python.org/3.8/library/stdtypes.html#str.format).

We can apply error control in our tried-and-true function `hours_from()` fit in a module named `utility.py`:

```python
'''module: utility.py'''
def hours_from(x, y):
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        return None

    from_x = x + y  # unbound y hours from x
    from_x = str(from_x % 24)  # 24-hour capped hours from x, then cast to str
    z = from_x.zfill(2) + ':00'  # left-pad and format hours from x as HH:00
    return z  # return the value of z
```

We can use modules by importing them inside of other modules or in the Python interactive shell. They are the third reusability building block after the acquainted variables and functions.

The members of the `utility` module such as the function `hours_from` can be accessed as such:

```python
>>> import utility
>>> utility.hours_from(16, 12345)  # utility module's hours_from() function
'01:00'
>>> utility.hours_from('16:00', 12345)
>>> # None, null, nil, nothing
```

A few pieces to digest from above.

Unlike the strategy of [utilizing conditions to adapt the function](02-logic-controls-1.md#hours-from), which requires explicit knowledge of the form of the arguments, `try/except` essentially tells the users of the function that it is not possible. Instead of raising an exception, it does so gracefully.

This approach acknowledges what may violate the usage of the `int()` function, the part of the logic that we leverage but have no control over its inner mechanism. In this case, it would raise a `ValueError` when it cannot parse the supplied value as a base-10 integer. The `ValueError` handling is still imperative as the conditional approach, but vaguer than explicit conditions through `if` statements, yet less explicit than blanket exception handling similar to the zero division example.

We may practice the same control over the usage of the `str()` function. But it is not necessary since it is much more lenient than the `int()` function.

As a maker, it would be your executive decision to make on how to handle the error. In the example, we instruct the function to an early exit by `return None`. `None` is a data type in Python, with its only value being `None`. When there is only a `return` with nothing for it, Python implies it as `return None`. `None` is also conditionally [falsy](02-logic-controls-1.md#truthy-falsy-ternary).

### Controlled Errors

The flip side of error handling and anticipation is raising controlled errors to better inform our users:

```python
'''module: utility.py'''
def hours_from(x, y):
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        raise Exception('x and y need to be real numbers or base-10 number strings')

    from_x = x + y  # unbound y hours from x
    from_x = str(from_x % 24)  # 24-hour capped hours from x, then cast to str
    z = from_x.zfill(2) + ':00'  # left-pad and format hours from x as HH:00
    return z  # return the value of z
```

```python
>>> from utility import hours_from  # cherry-pick hours_from() function from utility module
>>> hours_from('16:00', 123)
Traceback (most recent call last):
  ...
    x = int(x)
ValueError: invalid literal for int() with base 10: '16:00'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  ...
    raise Exception('x and y need to be real numbers or base-10 number strings')
Exception: x and y need to be real numbers or base-10 number strings
```

Python successfully handles the initial `ValueError` and raises the explicit `Exception` with a custom message, providing more insights on "where" and "why" things went wrong.

Whether to raise an explicit exception is usually a judgment call depending on the intended audience and their domain expertise of the subject. One can argue that the original `ValueError` would suffice, in which case:

```python
'''module: utility.py'''
def hours_from(x, y):
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        raise

    from_x = x + y  # unbound y hours from x
    from_x = str(from_x % 24)  # 24-hour capped hours from x, then cast to str
    z = from_x.zfill(2) + ':00'  # left-pad and format hours from x as HH:00
    return z  # return the value of z
```

...or equivelantly:

```python
'''module: utility.py'''
def hours_from(x, y):
    x = int(x)
    y = int(y)

    from_x = x + y  # unbound y hours from x
    from_x = str(from_x % 24)  # 24-hour capped hours from x, then cast to str
    z = from_x.zfill(2) + ':00'  # left-pad and format hours from x as HH:00
    return z  # return the value of z
```

```python
>>> from utility import hours_from
>>> hours_from('16:00', 12345)
Traceback (most recent call last):
  ...
    x = int(x)
ValueError: invalid literal for int() with base 10: '16:00'
```

Python provides a range of [built-in exceptions](https://docs.python.org/3.8/library/exceptions.html) that can help raise controlled errors as demonstrated above.

### Assertion

So far we have only utilized either `print()` or immediate evaluation response from the interactive shell to verify correctness of our code. To do so automatically, Python provides `assert` for such a purpose:

```python
>>> from utility import hours_from
>>> assert hours_from(16, 12345) == '01:00'  # nothing, good
>>> assert hours_from(16, 12345) != '16:00'  # nothing, good
>>> assert hours_from(16, 12345) == '16:00'
Traceback (most recent call last):
  ...
AssertionError
```

As demonstrated from the above example, when the evaluation is expected (truthy), it would result in nothing, as in _no news is good news_. Otherwise, it raises an `AssertionError` to signify the mismatch of evaluation expectations.

## Notes on Logic Controls

The use of additional conditions to be more comprehensive always has its limit inherited from humans. Every line of code added to handle more cases may cause regression and break existing functionality, sometimes costing more than what it would gain.

Comparatively, uncareful or abusive error controls may hide too much useful error information that could otherwise help makers to improve software quality.

![conditions-vs-error-controls](https://i.imgur.com/Bq3k73X.png)

To decide when to apply which type of logic controls, makers usually need to consider many factors that are not always available or foreseeable. So they break the scope down to smaller unit abstractions (such as Python function) and compose more complex systems from there.

Often an elegant solution can cover most or all intended cases while being simple to implement, reason with, and use. It is also not rare that sometimes nothing is the most elegant solution.

Let us refer to "The Zen of Python, by Tim Peters":

```python
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
>>>
```

We will see more capable tools that Python has to offer in this series, and at times they would seem viable as alternatives. Use the above as a general guideline when in doubt which one is to pick for the objective at hand.

## Exercises

### Problem 03 - Sanitize hours

Recall the `hours_from()` function where we have identified that the usage of the `int()` function on the input arguments is likely the root of most issues we have seen.

Implement a `sanitize_hour()` function and use it within `hours_from()` function as such:

```python
def sanitize_hour(hour):
    # ...implementation
    # re-assign hour with the desired type and value
    return hour

def hours_from(x, y):
    try:
        x = sanitize_hour(x)
        y = sanitize_hour(y)
    except:
        return None

    from_x = x + y  # unbound y hours from x
    from_x = str(from_x % 24)  # 24-hour capped hours from x, then cast to str
    z = from_x.zfill(2) + ':00'  # left-pad and format hours from x as HH:00
    return z  # return the value of z

# assertion tests
assert hours_from(-8, 12345) == '01:00'
assert hours_from('-08:00:00', 12345) == '01:00'
assert hours_from('-08:00', 12345) == '01:00'
assert hours_from('-8:00', 12345) == '01:00'
assert hours_from('-8', 12345) == '01:00'

assert hours_from(8, 12345) == '17:00'
assert hours_from('08:00:00', 12345) == '17:00'
assert hours_from('08:00', 12345) == '17:00'
assert hours_from('08', 12345) == '17:00'
assert hours_from('8', 12345) == '17:00'

assert hours_from('abc', 12345) is None
```

Try to apply a few ways with conditions and error controls to accomplish the solution. See for yourself what your preference is.
