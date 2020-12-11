# Part 01 - Immediate Applications (1/2)

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

## Exercises

### Problem 01 - Seconds from Time

Use what you have gathered so far, come up with a Python expression to answer _"what is the time after 12345 seconds from 16:00?"_.

### Problem 02 - Quotes of Strings of Quotes

One of the ways to define strings in Python is by surrounding a sequence of textual characters with quotes (`'` or `"`).

```python
>>> "a string"
'a string'

>>> 'another string'
'another string'
```

Consult the official Python documentation on the [Built-in Type `str`](https://docs.python.org/3.8/library/stdtypes.html#text-sequence-type-str) and other online resources, find out one or multiple ways to define strings such as `'tis the season for some Trick 'r Treat, says "Nobody"` which contain both types of quotes.
