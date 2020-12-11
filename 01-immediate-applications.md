# Part 01 - Immediate Applications

Upon [installation](https://www.python.org/downloads/), you can already program some immediate applications.

## Arithmetics

```python
>>> 9 - 1  # subtraction
8

>>> 4 + 2  # addition
6

>>> 1 / 4  # division
0.25

>>> 2 * 5  # multiplication
10

>>> 2 ** 9  # exponentiation
512

>>> 2 ** 9 - 1 / 4 + 2 * 5  # evaluation precedences
521.75

>>> 2 ** ((9 - 1) / (4 + 2) * 5)  # evaluation precedences alterated
101.59366732596473
```

All of the above are examples of Python _expressions_ (as shown beside interactive prompt `>>> `) which evaluate to eventual _values_ (as presented below the interactive prompt `>>> `).

Each _expression_ may have elements such as _operands_ (such as the numbers), as well as _operators_ (such as `+`).

Expression evaluation follows a set of rules, from what we have seen so far:
* [A table of built-in expression evaluation precedence](https://docs.python.org/3.8/reference/expressions.html#operator-precedence) which mostly inherits from relevant domains.
* Parentheses enclosed before unenclosed.
* In case of nested parentheses enclosures, inner before outer.

The text after `#` is a type of inline _comments_, which are only for humans to read and discarded by the machine. They are not a part of expressions.

## First Intimidation - Floating-Point Numbers

```python
>>> 10 / 3
3.3333333333333335
```

Notice the oddity in the output value `3.3333333333333335`?

It is known as a _floating-point arithmetic error_ or _round-off error_ since real numbers are only emulations of the underlying binaries, a product and trade-off of digitization.

![real numbers](https://i.imgur.com/fThGhlh.png)

So by design, this type of error cannot be eliminated in digitally based systems but can only be managed by taking trade-offs between ranges and precisions. When it is not managed well, [it resulted in matters of life and death](https://en.wikipedia.org/wiki/Round-off_error#Real_world_example:_Patriot_missile_failure_due_to_magnification_of_roundoff_error).

For this reason, precision-sensitive data usually gets stored and calculated in fixed-point numbers -- or integers with an implicit definition of the fraction scale it represents. For instance, if we want to perform the same division, instead of `10.00 / 3`, we will scale everything to cents (1/100 of a dollar):

```python
>>> 1000 / 3  # 1000 cents
333.3333333333333
```

Now it is a bit better without the odd `5` at the end of the fraction. And if we choose a desired fractional precision and can afford to forego the remainder, let us say down to 1/10 of a cent (1/1000 of a dollar):

```python
>>> 10000 // 3  # 10000 mills, integer division
3333
```

Unlike divisions, `//` performs specifically an integer division (or floor division) and forgoes the remainder.

The above is a real-life example of a creative workaround of an innate limit by applying controlled trade-offs.

And if we want to know how much remainder we have foregone, we can use the _modulo_ operator `%` to do so:

```python
>>> 10000 % 3  # modulo, for integer division remainders
1
```

The modulo `%` operator can be practical in a couple of other ways:

```python
>>> 864192 % 7  # is 864192 divisible by 7 (without remainders)?
0

>>> (16 + 12345) % 24  # what's the time after 12345 hours from 16:00?
1
```

## Text Processing

If using Python as a glorified calculator is not good enough for you, let us do some text processing.

```python
>>> 'make puppies great again! 🐶'.upper()
'MAKE PUPPIES GREAT AGAIN! 🐶'
```

What's up? Letter cases, of course.

Follow the same expression evaluation rules we have collected from before, let us pick apart the above expression.

`'make puppies great again! 🐶'` portion defines a _string_ value or a sequence of textual characters. In Python, these string values are of the built-in `str` _type_

Each type corresponds to a _class_ that has a set of internal mechanisms referred to as _methods_ that make use of the value it holds. In this particular case, we are applying a letter case transformation mechanism `upper()` to _return_ a copy of the original text with all letters in uppercase. The notion of `()` means it is a form of "Callable" that activates the said mechanism.

Methods that _returns_ (evaluates into) a value enables us to do:

```python
>>> 'make puppies great again! 🐶'.title().swapcase()  # title, then swap lower/upper cases
'mAKE pUPPIES gREAT aGAIN! 🐶'
```

The last example _calls_ two methods in a chain, and it is evaluated as expected, from left-to-right:
1. `'make puppies great again! 🐶'.title()` gets evaluated into `'Make Puppies Great Again! 🐶'`.
2. Then `'Make Puppies Great Again! 🐶'.swapcase()` gets evaluated into what you see.

_Note: aside from `str` we have also seen two of the numeric built-in types, `int` (or integer) and `float` (or floating-point number), in the [Arithmetics](#arithmetics) section from before. We will see more built-in types and their methods along with the series, and we will get to define our types when we get to the details of defining custom classes and their methods._

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
* `def` is a keyword that leads to a function definition statement.
* The name of the function is `hours_from`.
* The parentheses after the function name signifies that as a function, it is a "Callable", and within are what this function would accept as "arguments" or values passed into the function.
* After the colon `:` and below, with a 4-space indentation, would be the "body" of the function, which is a block of code that does something but only within the _scope_ of the function. In this case, it evaluates our "hours from" _algorithm_ and assigns the value into a _local_ variable `z`.
* `return` keyword is used to state the value (evaluated from the expression) to be passed out of the function, or what the function call as an expression would evaluate into. In this case, it returns the variable `z` (and what value it would hold).

Now, this function can be treated as a black box and visualized through a simple flowchart:

![blackbox](https://i.imgur.com/j1SWVaR.png)

Or expressed in plain language _"y hours from x (o'clock) is z (o'clock)"_. Notice that the _implementation detail_ of how the result is derived has been _abstracted_ away. That is one of the chief purposes of authoring and utilizing custom functions.

## Exercises

### Problem 01 - `days_from()`

Take the `hours_from()` function as a reference, implement `days_from()` which should fit the description _"y days from x (o'clock) is z (o'clock)"_. You may assume that `y` is in earth days, and there are no complexities such as leap years and daylight saving times involved. In short, you can assume a day is always 24 hours.

### Problem 02 - Save Spaces with Ellipsis

The new LOCUS marketplace launch is imminent, and our design team has provided a great proposition to cut down long phrases to a fixed length and appended with an ellipsis (`...`) to indicate that there's more.

Implement a function that takes an arbitrary string as an argument `s`, and another arbitrary integer as `l`, to achieve an effect so:

```python
>>> def cut(s, l):
...    # something
...    pass
...
>>> cut('who let the dogs out?', 10)
'who let th...'
```
