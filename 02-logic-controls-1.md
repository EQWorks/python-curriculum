# Part 02 - Logic Controls (1/2)

Part 01 introduces some fundamental elements of the Python programming language that we can use to compose immediate but linear applications.

To wield programming as a tool for more sophisticated automation, we would need more controls.

## Conditions

Recall the [`hours_from()` function from Part 01](01-immediate-applications-2.md#by-defining-a-custom-function).

Without the understanding of the function implementation itself, one may encounter a usage error as such:

```python
>>> hours_from('16:00', 12345)
Traceback (most recent call last):
  ...
TypeError: can only concatenate str (not "int") to str
```

The flaw here is that the user of this function, which can be the one who implemented it but have forgotten the implementation details, does not know `x` needs to be in a real number type (`int` or `float`).

This can obviously be fixed by leveraging some [text processing](01-immediate-applications-2.md#text-processing-continued) and [type casting](01-immediate-applications-2.md#vera-verto-type-casting):

```python
>>> def hours_from(x, y):
...     from_x = int(x[0:2]) + y  # unbound y hours from x
...     from_x = str(from_x % 24)  # 24-hour capped hours from x, then cast to str
...     z = from_x.zfill(2) + ':00'  # left-pad and format hours from x as HH:00
...     return z  # return the value of z
...
>>> hours_from('16:00', 12345)
'01:00'
```

...until you get mad pings from teammates who build various applications using your function the old way:

```python
>>> hours_from(16, 12345)
Traceback (most recent call last):
  ...
TypeError: 'int' object is not subscriptable
```

This highlights an often-overlooked cost of software updates -- the cost of _backward incompatibility_. In this particular case, we can address the compatibility issue using conditional reasoning:

> _if_ the type of variable `x` is a string (assuming it is always in the form of `HH:mm`), then convert the hour portion to an integer.

And apply it using the Python `if` statement:

<a name="hours-from"></a>

```python
>>> def hours_from(x, y):
...     if type(x) is str:  # if `x` is a string
...         x = int(x[0:2])  # extract the hour portion and convert to integer
...     from_x = x + y  # unbound y hours from x
...     from_x = str(from_x % 24)  # 24-hour capped hours from x, then cast to str
...     z = from_x.zfill(2) + ':00'  # left-pad and format hours from x as HH:00
...     return z  # return the value of z
...
>>> hours_from(16, 12345)
'01:00'
>>> hours_from('16:00', 12345)
'01:00'
```

_Note: Pay attention to the (further) indentation under the `if` keyword. Unlike most other programming languages, Python regards indentations as a part of its enforced syntax rules to signify code blocks and lexical scopes, instead of just mere conventions or code styles._

We effectively change the _flow_ of how to treat the argument variable `x` and visualize through an expanded flowchart as such:

![flow](https://i.imgur.com/2oo7LWk.png)

An `if` statement can end with an `else`:

```python
>>> def is_even(x):
...     if x % 2 == 0:
...         return True
...     else:
...         return False
...
>>> is_even(3)
False
```

Logically, _"if x is divisible by 2 without remainders, it's even; otherwise (else) it's odd (not even)"_. Notice the values returned, `True` and `False`. They are the only two available values of another Python built-in type `bool` (Boolean):

```python
>>> type(True)
<class 'bool'>
>>> type(False)
<class 'bool'>
```

Within the scope of a function, the logic can be concise by employing what is known as "early exit":

```python
>>> def is_even(x):
...     if x % 2 == 0:
...         return True  # if this gets executed, skip the rest
...     return False
```

We can omit the closing `else` block because `return` (among a few other means) effectively _exits_ the function upon execution. And the rest of the statements within this function are skipped.

This can be yet more <a name="is-even-succinct"></a>succinct:

```python
>>> def is_even(x):
...     return x % 2 == 0
```

The essence of what happens above lies in the expression `x % 2 == 0`. From left to right:
1. `x % 2` evaluates into a _remainder_ (of type `int` or `float`)
2. `remainder == 0` evaluates into a `bool` value (`True` or `False`)

### Comparisons

The `==` operator is for equality comparison between two values since `=` is already reserved for assignment statements. The `is` from earlier is _conceptually_ a stronger equality comparison between two identities (value and type):

```python
>>> 3.0 == 3  # value equality
True
>>> 3.0 is 3  # identity equality
False
>>> 3.0 is 3.0  # identity equality
True
>>> type('a string') is str  # identity equality
True
```

On top of `==`, there are `>`, `<`, `>=`, `<=`, and `!=` operators for value comparisons. Play around with them to test your expectations, which should be intuitive.

### Truthy, Falsy, Ternary

The value beside the conditional keyword (such as `if`) does not need to be in the `bool` type:

```python
>>> s = ''
>>> if len(s):
...     s
... else:
...     'Empty string'
...
'Empty string'
```

When the string is empty, its length is `0` of type `int`. In this context, Python interprets `0` as "Falsy" and all non-0 integers as "Truthy".

In fact, an empty string is already "Falsy", otherwise "Truthy":

```python
>>> s = ''
>>> if s:
...     s
... else:
...     'Empty string'
...
'Empty string'
```

There is a style to express this whole `if` statement more succinctly:

```python
>>> s = ''
>>> s if s else 'Empty string'
'Empty string'
```

Conceptually this is known as a <a name="ternary"></a>_ternary_ operation. Unlike some other languages, Python does not have dedicated operators for ternary, but a shorthand emulation based on existing `if` statements.

### Switch Cases

We cannot always state all logical cases with an `if/else` pair or together with an "early exit" using only an `if` and an implied `else` statement.

There are times where we would need to handle intermediate cases using `elif` (else-if). Imagine if we want to implement a function to safeguard the displayed content to a safe range of ages:

```python
>>> def age_safe(age, lower, upper):
...     if age < lower:
...         return False
...     elif age > upper:
...         return False
...     return True  # implied final else
```

### Nested Conditions

We can nest conditional statements, and conceptually nesting the `age_safe()` conditions by invoking the function within:

```python
>>> def age_skip(age, lower, upper, skip):
...     if age_safe(age, lower, upper):  # outer-if
...         if age == skip:  # inner-if
...             return True
...         return False  # implied inner-else
...     return True  # implied final outer-else
```

In this particular case, we can apply a small twist on the inner `if/else` pair:

```python
>>> def age_skip(age, lower, upper, skip):
...     if age_safe(age, lower, upper):  # outer-if
...         if age != skip:  # inner-if
...             return False
...         return True  # implied inner-else
...     return True  # implied final outer-else
```

We can then further simplify based on the fact that both (implied) inner and out-else cases result in the same outcome:

```python
>>> def age_skip(age, lower, upper, skip):
...     if age_safe(age, lower, upper):  # outer-if
...         if age != skip:  # inner-if
...             return False
...     return True  # implied final else
```

## Boolean Operations

There is a way to express the conditional statement without using `if` from the [ternary example](#ternary):

```python
>>> s = ''
>>> s or 'Empty string'
'Empty string'
```

The `or` logic operator takes two operands (one on each side) and has a _truth-table_ as such:

| Left   |    | Right  | Output |
|--------|----|--------|--------|
| Truthy | or | Truthy | Left   |
| Truthy | or | Falsy  | Left   |
| Falsy  | or | Truthy | Right  |
| Falsy  | or | Falsy  | Right  |

If we mix-in the concept of evaluation short-circuiting (similar to "early exit"):

| Left   |    | Right  | Output |
|--------|----|--------|--------|
| Truthy | or | Any    | Left   |
| Falsy  | or | Any    | Right  |

We can rewrite the [switch cases example](#switch-cases) based on the realization of either the `if` _or_ the `elif` case results in the same outcome:

```python
>>> def age_safe(age, lower, upper):
...     if (age < lower) or (age > upper):
...         return False
...     return True  # implied final else
```

Similarly, the `and` logical operator has such a _truth-table_:

| Left   |     | Right  | Output |
|--------|-----|--------|--------|
| Falsy  | and | Truthy | Left   |
| Falsy  | and | Falsy  | Left   |
| Truthy | and | Truthy | Right  |
| Truthy | and | Falsy  | Right  |

With short-circuiting:

| Left   |     | Right  | Output |
|--------|-----|--------|--------|
| Falsy  | and | Any    | Left   |
| Truthy | and | Any    | Right  |

We often utilize the `and` logical operator to simplify [nested conditions](#nested-conditions):

<a name="age-skip-last"></a>

```python
>>> def age_skip(age, lower, upper, skip):
...     if age_safe(age, lower, upper) and age != skip:
...         return False
...     return True  # implied final else
```

The last logical operator is `not`, which negates the value:

```python
>>> not True
False
>>> not False
True
>>> not 0
True
>>> s = ''
>>> 'Empty string' if not s else s
'Empty string'
```

Following the [`is_even()` example](#is-even-succinct), combining the fact that comparison expressions such as `age < lower` and `age > upper` evaluate into `bool` values, we can further simplify our `age_safe()` function as such:

```python
>>> def age_safe(age, lower, upper):
...     return not ((age < lower) or (age > upper))
```

### De Morgan's laws

As a relatively subjective matter, the one-liner `age_safe()` function implementation _can_ be logically confusing.

Fortunately, a technique derived from the studies of Boolean Algebra, particularly [_De Morgan's laws_](https://en.wikipedia.org/wiki/De_Morgan%27s_laws), allows us to re-interpret the logical expressions to suit more:

> not (A or B) = not A and not B; and

> not (A and B) = not A or not B

Apply that into `age_safe()`:

```python
>>> def age_safe(age, lower, upper):
...     return not (age < lower) and not (age > upper)
```

With some further realization on `not <` can be `>=` and `not >` can be `<=`:

<a name="age-safe-last"></a>

```python
>>> def age_safe(age, lower, upper):
...     return (age >= lower) and (age <= upper)
```

All examples from above are correct, and no one way is objectively better or worse than the other ways that achieve the same objective. Try to attend to your readers of the code (that could be your future self), use the most natural way to express your logic controls while keeping your objectives straight.

## Exercises

### Problem 01 - Skip simply

Re-interpret the [`age_skip()` function implementation](#age-skip-last) so it is in a similarly simplified manner as the [last `age_safe()` implementation](#age-safe-last).

### Problem 02 - Beefier `hours_from()`

Further improve the [`hours_from()` implementation](#hours-from) to:

* Correctly handle negative `x` values
* Correctly handle both single and double-digit string `x` hour values
* Correctly handle string `x` values with or without hour-minute delimiter `:`

```python
>>> hours_from(-8, 12345)
'01:00'
>>> hours_from('-08:00', 12345)
'01:00'
>>> hours_from('-8:00', 12345)
'01:00'
>>> hours_from('-8', 12345)
'01:00'
>>> hours_from(8, 12345)
'17:00'
>>> hours_from('08:00', 12345)
'17:00'
>>> hours_from('08', 12345)
'17:00'
>>> hours_from('8', 12345)
'17:00'
```
