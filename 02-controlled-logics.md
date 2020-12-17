# Part 02 - Logic Controls

Part 01 introduces some fundamental elements of the Python programming language that we can use to compose immediate but linear applications.

To wield programming as a tool for more sophisticated automation, we would need more controls.

## Control Flow

Let us revisit the `hours_from()` function from Part 01:

```python
>>> def hours_from(x, y):
...     from_x = x + y  # unbound y hours from x
...     from_x = str(from_x % 24)  # 24-hour capped hours from x, then cast to str
...     z = from_x.zfill(2) + ':00'  # left-pad and format hours from x as HH:00
...     return z  # return the value of z
...
```

Although we conclude that this function fits the description of _"y hours from x (o'clock) is z (o'clock)"_, without the understanding of the function implementation itself, one may encounter a usage error as such:

```python
>>> hours_from('16:00', 12345)
Traceback (most recent call last):
  ...
TypeError: can only concatenate str (not "int") to str
```

The flaw here is that the user of this function, which can be the one who implemented the function but have forgotten the implementation details, does not know `x` needs to be in a real number type (`int` or `float`). It becomes apparent if we dissect the statement and substitute it with violating values:

```python
>>> from_x = '16:00' + 12345
Traceback (most recent call last):
  ...
TypeError: can only concatenate str (not "int") to str
```

This can obviously be fixed by leveraging some [text processing](01-immediate-applications-2.md#text-processing-continued) and [type casting](01-immediate-applications-2.md#vera-verto-type-casting):

```python
>>> from_x = int('16:00'[0:2]) + 12345
>>> from_x
12361
```

And substitute back into our function implementation:

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

Enter the `if` statement to turn this fiasco into a net gain of functionality with backward compatibility. First, let us comb through the logic by describing the handling of `x`:

> if the type of variable `x` is a string (assuming it is always in the form of `HH:mm`), then convert the hour portion to an integer.

And apply it with what we know from Part 01:

```python
>>> x = '16:00'
>>> if type(x) is str:  # if `x` is a string
...     x = int(x[0:2])  # carve out the hour portion and convert to integer
...
>>> x
16
>>> type(x)
<class 'int'>
```

Put them together with the function:

```python
>>> def hours_from(x, y):
...     if type(x) is str:  # if `x` is a string
...         x = int(x[0:2])  # carve out the hour portion and convert to integer
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

_Note: Pay attention to the (further) indentation under the `if` keyword. Unlike _most_ other programming languages, Python regards indentations as a part of its enforced syntax rules to signify code blocks and scopes, instead of mere conventions or code styles seen in other programming languages._

We effectively change the _flow_ of how to treat `x` -- if its value is a string, it goes through some additional steps to be _parsed_ (extracted and converted) into our desired form before proceeding onto the rest steps. We can visualize through an expanded flow chart from Part 01:

![flow](https://i.imgur.com/mn3tYII.png)
