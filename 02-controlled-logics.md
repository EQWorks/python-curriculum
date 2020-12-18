# Part 02 - Logic Controls

Part 01 introduces some fundamental elements of the Python programming language that we can use to compose immediate but linear applications.

To wield programming as a tool for more sophisticated automation, we would need more controls.

## Conditions

Recall the [`hours_from()` function from Part 01](01-immediate-applications-2.md#by-defining-a-custom-function).

Although we conclude that this function fits the description of _"y hours from x (o'clock) is z (o'clock)"_, without the understanding of the function implementation itself, one may encounter a usage error as such:

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
```

And use it happily:

```python
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

We could have communicated the change to the team before it became effective. But in this particular context, we know how to handle the two cases definitively.

Enter the `if` statement to turn this fiasco into a net gain of functionality with _backward compatibility_. First, let us comb through the logic by describing the handling of `x`:

> if the type of variable `x` is a string (assuming it is always in the form of `HH:mm`), then convert the hour portion to an integer.

And apply it with what we know from Part 01:

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

_Note: Pay attention to the (further) indentation under the `if` keyword. Unlike most other programming languages, Python regards indentations as a part of its enforced syntax rules to signify code blocks and lexical scopes, instead of mere conventions or code styles seen in other programming languages._

We effectively change the _flow_ of how to treat argument variable `x` -- if its value is a string, it goes through some additional steps to be _parsed_ (extracted and converted) into our desired form before proceeding onto the rest. We can visualize through an expanded flowchart:

![flow](https://i.imgur.com/mn3tYII.png)
