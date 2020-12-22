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
...
```

Logically, _"if x is divisible by 2 without remainders, it's even; otherwise (else) it's odd (not even)"_. Notice the values returned, `True` and `False`. They are the only two available values of another Python built-in type `bool` (Boolean):

```python
>>> type(True)
<class 'bool'>
>>> type(False)
<class 'bool'>
```

This logic can be compressed by employing what is known as "early exit", or "early return":

```python
>>> def is_even(x):
...     if x % 2 == 0:
...         return True  # if this gets executed, the rest is skipped
...     return False
...
```

We can omit the closing `else` block because `return`, among some other means, effectively _exits_ or _terminates_ the function upon execution. And the rest of the statements within this function gets skipped.

This can be yet more succinct:

```python
>>> def is_even(x):
...     return x % 2 == 0
```

The essence of what happens above lies in the expression `x % 2 == 0`. From left to right, it evaluates as:
1. `x % 2` -> `remainder`
2. `remainder == 0` -> `bool` (`True` or `False`)

The `==` operator is for equality comparison between two values. The `is` keyword/operator from earlier is _conceptually_ a stronger equality comparison between two values, as well as their types:

```python
>>> 3.0 == 3  # value equality
True
>>> 3.0 is 3  # value and type
False
>>> 3.0 is 3.0  # identity (value and type) equality
True
>>> type('a string') is str  # identity equality
True
```

On top of `==`, there are `>`, `<`, `>=`, `<=`, and `!=` operators for comparisons. Play around with them to test your expectations, which should be intuitive.

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

When the string is empty, its length is `0` of type `int`. In this context, Python interprets `0` as "Falsy", while all other non-0 integer values are considered "Truthy".

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

Conceptually this is known as a _ternary_ operation. Unlike some other languages, Python does not have dedicated ternary operators, but a shorthand emulation based on existing `if` statements.

## Boolean Operations

There is a way to express the conditional statement without using `if` from the previous case:

```python
>>> s = ''
>>> s or 'Empty string'
'Empty string'
```

In this case, we can describe the above as _"non-empty string `s` or `'Empty string'`"_. The `or` logic operator takes two operands (one on each side) and has a "truth-table" as such:

| Left   |    | Right  | Output |
|--------|----|--------|--------|
| Truthy | or | Truthy | Left   |
| Truthy | or | Falsy  | Left   |
| Falsy  | or | Truthy | Right  |
| Falsy  | or | Falsy  | Right  |

If we mix-in the concept of evaluation short-circuiting:

| Left   |    | Right  | Output |
|--------|----|--------|--------|
| Truthy | or | Any    | Left   |
| Falsy  | or | Any    | Right  |

One-liner as:

> The first truthy value encountered until exhausted to the last.

```python
>>> def first_tru(v1, v2, v3, v4):
...     return v1 or v2 or v3 or v4
...
>>> first_tru(0, 0.0, '', False)
False
>>> first_tru(1, 100, 1000, 10000)
1
```

Similarly, the `and` logical operator:

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

One-liner:

> The first falsy value encountered until exhausted to the last.

```python
>>> def first_mal(v1, v2, v3, v4):
...     return v1 and v2 and v3 and v4
...
>>> first_mal(0, 0.0, '', False)
0
>>> first_mal(1, 100, 1000, 10000)
10000
```

Play around with both functions by feeding arbitrary values of arbitrary types and see if they all behave as expected.

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

## Bitwise Operations

Boolean operations are useful for conditional logic controls and truthy value filtering. We can do similar things with the essential representation of the value system -- binary bits.

```python
>>> 0 | 1  # bitwise OR
1
>>> 0 & 1  # bitwise AND
0
>>> 0b010 | 0b001
3
>>> bin(3)
'0b11'
>>> int('0b11', 2)
3
```

Those numbers began with `0b` are integers expressed directly in their binary representations. The built-in function `bin` translates a regular integer (of base 10) to its binary string representation. And finally, the `int` built-in function converts the binary string representation back to an integer, with a second argument to specify its base.

There are some other bitwise operations such as `<<` (left shift) and `>>` (right shift) that shifts all bits toward a desired direction:

```python
>>> bin(0b010 << 1)  # left shift and show binary string representation
'0b100'
>>> bin(0b010 >> 1)  # right shift and show binary string repr
'0b1'  # leading 0s are omitted
```

Bitwise shifts can be used to emulate integer multiplications and divisions:

```python
>>> x = 3
>>> x * 2 == x << 1
True
>>> x // 2 == x >> 1
True
```

But more broadly, bitwise operations are used as bitmasking, where a single value is used for its bit-level information:

```python
>>> config = 0b1010_1010
>>> bin(config | 0b1111_0000)  # turn ON bits 7-4, leave bits 3-0 intact
'0b11111010'
>>> bin(config & 0b0000_1111)  # turn OFF bits 7-4, leave bits 3-0 intact
'0b1010'
>>> bin(config ^ 0b1111_1111)  # toggle all bits (using XOR, exclusive OR)
'0b1010101'
>>> bin(config | (1 << 4))  # turn ON the bit 4 (5th from right)
'0b10111010'
>>> (config & 0b0100_1000) == 0b0100_1000  # query if bit 6 and 3 are both on
False
```

_Notice the underscore `_` is used here as a number delimiter for readability. And just like inline comments, they are discarded by the Python runtime._

Typically the advantages are:
* Compactness - a single value is stored and utilized for its underlying binary representation, where each bit is a distinct configuration.
* Performance - the software can perform multiple adjustments in a single operation.

Bitwise operations come with a sacrifice that understanding of what each bit represents is required.

Aside from configurations, systems utilize bitmasking for ID arrangements and distributions. One of the most prominent examples is IPv4 (Internet Protocol version 4) subnetting.

![subnetting](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Subnetting_Concept.svg/1920px-Subnetting_Concept.svg.png)
