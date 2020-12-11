# Part 01 - Immediate Applications (2/2)

## Text Processing (continued)

As a sequence type, strings have a notion of "index", meaning each character of a string value corresponds to a positional value, from left-to-right:

```python
>>> 'make puppies great again! 🐶'[0]
'm'

>>> 'make puppies great again! 🐶'[-1]
'🐶'
```

While `0` means the first character in the sequence, `-1` here means (conceptually) the last, or the first character from the reverse-order (right-to-left). In actuality, it is a shorthand of the _(length of the string - 1)th_ (from left-to-right). Manually counting the length (number of characters) in a string can be tedious. Fortunately, there's a built-in _function_ for that:

```python
>>> len('make puppies great again! 🐶')
27

>>> 'make puppies great again! 🐶'[27 - 1]
'🐶'
```

A small detail here is that the last expression has the subtraction `27 - 1` evaluated before the index operation itself, so let us add this to our expression evaluation rule list:
* Index enclosed before unenclosed.

![puppies](https://i.imgur.com/fnkUBV2.png)

The indexing notion allows us to do a bit more than pinpoint a particular character in the sequence:

```python
>>> 'make puppies great again! 🐶'[5:12]
'puppies'
```

This is a `range` operation that "_takes the characters from index 5 to index 12 (exclusive)_", or interpreted in another way as "_takes the characters from index 5 and count up to a total of 12 - 5 = 7 characters_".

You can even specify the third variation to "jump" the sequence:

```python
>>> 'make puppies great again! 🐶'[5:12:4]
'pi'
```

Try to articulate what is happening here. You may search around the interweb for definitive answers.

## ~~Vera Verto~~ Type Casting

![transfiguration](https://i.imgur.com/YZGVtVA.gif)

Although each type comes with its distinct set of operabilities and mechanisms, there are times where they can be cast (converted) to another for various purposes.

But before that, let us meet another built-in _function_:

```python
>>> type('make puppies great again! 🐶')
<class 'str'>
```

_Functions_ are similar to _methods_ of given _types_ in the sense that both are "Callable". One of the major differences is that _methods_ are strictly applicable to the value itself of types that defined them (such as `str.upper()`), while functions may be more universally applicable:

```python
>>> type(1)
<class 'int'>

>>> type(9 / 4)
<class 'float'>
```

Follows the same expression evaluation rules we have collected so far, except that the `()` here is not for precedence-order alteration but results in a similar effect:
1. `9 / 4` gets evaluated into `2.25`.
2. `type(2.25)` gets evaluated into `<class 'float'>`.

So let us add one more expression evaluation rule to the list:
* Callable enclosed before unenclosed.

Now we are equipped with a tool to verify types, so we will not get lost from here on. Let us move on to try to cast a number into a string:

```python
>>> str(9)
'9'

>>> type(str(9))  # verify the type
<class 'str'>
```

`str` here is both a type _class_, as well as a built-in function that attempts to cast the value given to its callable enclosure to the corresponding type. In technicality, this is an example of a class _constructor_, which is a special method used to "construct" an instance of the said class.

Before diving into what has been given by the type casting, let's see what it has taken away:

```python
>>> str(9) / 4
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for /: 'str' and 'int'
```

Quite apparently, it fails. The error above means that by converting a number `9` into a string, it loses the operability to be divided, among others:

```python
>>> 4 + str(9)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'

>>> str(9) - 4
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for -: 'str' and 'int'
```

What about the multiplication operator `*`?

```python
>>> str(9) * 9
'999999999'
```

The expression resulted in a repetition of the string `'9'` by `9` times. It means that the operator `*` works between `str` and `int`, but causes an entirely different effect than what it does between two numbers.

Imagine if Bart knew this:

```python
>>> 'I WILL NOT INSTIGATE REVOLUTION' * 18
```

Instead of suffering this:

![Bart](https://i.imgur.com/8s6NSE9.png)

Similarly the addition operator `+` is allowed on strings:

```python
>>> str(9) + str(4)
'94'
```

There is not much math involved here. The expression joins (or concatenates) the two strings `'9'` and `'4'` into `'94'`.

And now let us see what the "stringified" number can do:

```python
>>> str(9).zfill(2)  # left fill '0' to the intended minimum string length (2)
'09'
```

Recall the example of modulo operation on finding the hour. Let us put that together with the newly acquired tool of `str.zfill()` method and string concatenation to present the result time in a more friendly manner:

```python
>>> str((16 + 12345) % 24).zfill(2) + ':00'
'01:00'
```

## First Reusability - Variables and Functions

Without _variables_, the example of finding and composing a friendly display of what time it is `y` hours from `x` can be very tedious since it has to be repeatedly expressed with different specific values to work:

```python
>>> str((16 + 12345) % 24).zfill(2) + ':00'  # 12345 hours from 16:00 is
'01:00'

>>> str((1 + 54321) % 24).zfill(2) + ':00'  # 12345 hours from 01:00 is
'10:00'

>>> str((10 + 1234) % 24).zfill(2) + ':00'  # 1234 hours from 10:00 is
'20:00'

...
```

This means that we have to copy/paste the same expression, and then modify the values in between, a very manual and error-prone process.

So let's substitute the two intended variables to properly abstract our intent:

```python
>>> str((x + y) % 24).zfill(2) + ':00'  # y hours from x is
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'x' is not defined
```

But this triggers an error that _variable_ name `'x'` is not defined. Notice how theoretically `y` is also not defined, but since expressions are evaluated from left-to-right, and that Python would "short-circuit" after encountering an error immediately, it gets under-reported. But it's very much there as a problem. So let's fix both:

```python
>>> x = 14  # assign 14 to variable x (to represent hour 14:00)
>>> y = 111222  # assign 111222 to variable y
>>> str((x + y) % 24).zfill(2) + ':00'  # 111222 hours from 14:00 is
'20:00'
>>> x = 12  # assign 12 to variable x
>>> str((x + y) % 24).zfill(2) + ':00'  # 111222 hours from 12:00 is
'18:00'
>>> y = 222111  # assign 222111 to variable y
>>> str((x + y) % 24).zfill(2) + ':00'  # 222111 hours from 12:00 is
'03:00'
```

Better, at least now we can copy/paste a fixed expression `str((x + y) % 24).zfill(2) + ':00'`, and only change intended variables `x` and `y` as needed. Before we move on, there is an interesting thing happening here. Notice how `x` and `y`, as variables, get _re-assigned_ a couple of times and that the value it holds is always according to the most recent assignment.

How can we truly abstract away the operation `str((x + y) % 24).zfill(2) + ':00'` or _"find out y hours from x is"_? By defining a custom function:

```python
>>> def hours_from(x, y):
...     z = str((x + y) % 24).zfill(2) + ':00'
...     return z
...
>>> hours_from(x = 12, y = 12345)
'21:00'
>>> hours_from(4, 54321)
'13:00'
```

Let us dissect out the anatomy of this function first (mentally ignore the interactive prompt symbols `>>> ` and `...`):
* `def` is a _keyword_ that leads to a function definition statement.
* The name of the function is `hours_from`.
* The parentheses after the function name signifies that as a function, it is a "Callable", and within are what this function would accept as "arguments" or values passed into the function.
* After the colon `:` and below, each statement with an indentation (conventionally 4-space), would be the "body" of the function, which is a block of code that does something but only within the _scope_ of the function. In this case, it evaluates our "hours from" _algorithm_ and assigns the value into a _local_ variable `z`.
* `return` _keyword_ is used to state the value (evaluated from the expression) to be passed out of the function, or what the function call as an expression would evaluate into. In this case, it returns (pass out of the function) the value of variable `z`.

![func](https://i.imgur.com/X7KBrAH.png)

As a subjective matter, and since now we are equipped with the some knowledge of variables, let us rewrite this function to be a bit more friendlier to read:

```python
>>> def hours_from(x, y):
...     from_x = x + y  # unbound y hours from x
...     from_x = str(from_x % 24)  # 24-hour capped hours from x, then cast to str
...     z = from_x.zfill(2) + ':00'  # left-pad and format hours from x as HH:00
...     return z  # return the value of z
```

Notice the second line inside the function body `from_x = str(from_x % 24)` being both a re-assignment, as well as having _itself_ referenced as apart of the right-hand-side expression. The right-hand side expression gets evaluated into a value and then assigned to the variable name on the left-hand side.

Also as a subjective matter, and some more understanding of how values are being passed in and out of the function:

```python
>>> def hours_from(x, y):
...     return str((x + y) % 24).zfill(2) + ':00'
```

Just like assignment statements, the return statement follows a similar rule that the right-hand-side expression gets evaluated into a value before being returned.

Now, this function can be treated as a black box and visualized through a simple flowchart:

![blackbox](https://i.imgur.com/j1SWVaR.png)

Or expressed in plain language _"y hours from x (o'clock) is z (o'clock)"_. Notice that the _implementation detail_ of how the result is derived has been _abstracted_ away. That is one of the chief purposes of authoring and utilizing custom functions.

## Exercises

### Problem 01 - `days_from()`

Take the `hours_from()` function as a reference, implement `days_from()` which should fit the description _"y days from x (o'clock) is z (o'clock)"_. You may assume that `y` is in earth days, and there are no complexities such as leap years and daylight saving times involved. In short, you can assume a day is always 24 hours.

### Problem 02 - Save Spaces with Ellipsis

The new LOCUS marketplace launch is imminent, and our design team has provided a great proposition to cut down long phrases to a fixed length and appended with an ellipsis (`...`) to indicate that there's more.

![marketplace](https://i.imgur.com/xKN73Uq.png)

Implement a function that takes an arbitrary string as an argument `s`, and another arbitrary integer as `l`, to achieve an effect so:

```python
>>> def cut(s, l):
...    # something
...    pass
...
>>> cut('who let the dogs out?', 10)
'who let th...'
```

## Helpful Resources

* [Python Built-in Types](https://docs.python.org/3.8/library/stdtypes.html)
* [Python Built-in Functions](https://docs.python.org/3.8/library/functions.html)

Please also refer to "How to Help and Get Helped" in [README](README.md) for other general pointers.
