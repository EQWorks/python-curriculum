# Part 02 - Logic Controls (2/2)

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
'0b1010101'  # leading 0 omitted, conceptually 0b0101_0101
>>> (config & 0b0100_1000) == 0b0100_1000  # query if bit 6 and 3 are both on
False
>>> bin(~0b01)  # negate
'-0b10'  # conceptually should just be 0b10
>>> bin(~0b01 & 0b11)  # force unsigned to be signed
'0b10'
```

_Notice the underscore `_` is used here as a number delimiter for readability. And just like inline comments, they are discarded by the Python runtime._

Typically bitmasking is used for system configurations and ID arrangements (such as IPv4 subnetting that most of us are unknowingly benefiting from while doomscrolling), and the advantages are:
* Compactness - a single value is stored and utilized for its underlying binary representation, where each bit is a distinct configuration.
* Efficiency - the software can perform multiple adjustments in a single operation.

Similar to how [we handle precision-sensitive arithmetic](01-immediate-applications-1.md#fixed-point-numbers), the trade-off here is that it requires implicit knowledge of what each bit represents. This issue can be mitigated by abstracting away the implicit knowledge and expose a well <a name="turn-on-day"></a>defined interface for its users:

```python
'''module: main.py'''
SUN = 0
MON = 1
TUE = 2
WED = 3
THU = 4
FRI = 5
SAT = 6

def turn_on_day(days, day_bit):
    return days | (1 << day)

# 7 days in bits, from right-to-left, SUN to SAT
days = 0b0000000
# turn on Monday
print(bin(turn_on_day(days, MON)))  # 0b1000000
```

The example above is a _module_ (notice the lack of interactive prompt `>>> `), typically represented as a file with an extension of `.py`, the third abstraction building block after previously introduced _variables_ and _functions_.

There are a few details to be noticed.

### Scopes

```python
SCOPE = 'this is outer'

def scope_test():
    print(SCOPE)  # this is outer
    SCOPE = 'this is inner'
    print(SCOPE)  # this is inner

print(SCOPE)  # this is outer
```

* The first `SCOPE` variable defined outside of and before the `scope_test()` function is at the module-scope, which we can access throughout the module.
* The first `print()` function call inside the `scope_test()` function refers to the module-scope (the function's outer scope) version of the `SCOPE` variable since we do not define any variable of the same name before this call.
* The `SCOPE` variable assignment statement after the first `print()` function call is a newly defined local variable that overrides its outer counterpart's precedence.
* The second `print()` function call at the end of the `scope_test()` function refers to the function-scope (the function's inner/local scope) version of `SCOPE` variable.
* The third `print()` function outside of and after the `scope_test()` function is only aware of the first `SCOPE` variable as it has no visibility to the inner-function-scope of the `scope_test()` function.

### Constants

By convention, variables live in the module-scope are typically capitalized and emphasized as shared _constants_ that are not usually re-assigned.

### Usage

There is no notion of `return` at the module-scope:

```python
'''module: main.py'''
def hours_from(x, y):
    z = str((x + y) % 24).zfill(2) + ':00'
    return z

hours_from(4, 54321)  # this evaluates into '13:00'
                      # but that only stays within the module-scope
```

And can be used as so:

```shell
% python main.py
```

* The `%` is similar to `>>> `, which is known as a system-level command-line prompt. It may differ from operating systems or their versions.
* Unlike the Python prompt, it is not specific to the Python runtime. The first command is to let the command-line know that we intend to invoke a Python module named `main.py` through the Python runtime.

The above command will result in no visual output because:
1. What we define in the module-scope, stays in that scope.
2. What runs within the Python runtime, stays there too.

To command the program to give us visual outputs, we need to go through a common interface that the operating system exposes, and that interface varies from operating systems. Fortunately, the Python programming language has that abstraction covered for us through the already seen `print()` function:

```python
'''module: main.py'''
def hours_from(x, y):
    z = str((x + y) % 24).zfill(2) + ':00'
    return z

print(hours_from(4, 54321))  # display outside of the Python process
```

When used:

```shell
% python main.py
13:00
```

## Error Controls and Controlled Errors

The imperative nature of logic controls we have seen are only as comprehensive as what a maker makes them be. Thus the uncaught cases become exceptions and contribute toward software flaws and errors.

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

The above would result in the error to be handled with a `pass`, practically suppressing any errors including the aforementioned `ZeroDivisionError`. It is often more beneficial to be slightly more explicit about which type of error it is to be handled:

```python
>>> a = '1'
>>> try:
...     a / 0
... except ZeroDivisionError:
...     pass
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
TypeError: unsupported operand type(s) for /: 'str' and 'int'
```

The revised example from above takes an arbitrary variable `a` and divides it by `0`. While the anticipated `ZeroDivisionError` is handled (suppressed), unhandled errors would still surface. Similar to conditional statements, one can switch through more than one exception handling:

```python
try:
    a / 0
except ZeroDivisionError:
    # handle zero division
    pass
except TypeError:
    # handle type error
    pass
except:
    # last resort to handle the rest
    pass
```

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

A module can be imported it into other modules, or the Python interactive shell, and the members of the module such as the function `hours_from` used:

```python
>>> import utility
>>> utility.hours_from(16, 12345)  # call utility module's hours_from() function
'01:00'
>>> utility.hours_from('16:00', 12345)
>>> # None, null, nil, nothing
```

A few pieces to digest from above.

Unlike the strategy of [utilizing conditions to adapt the function](02-logic-controls-1.md#hours-from), which requires explicit knowledge of the form of the arguments, the use of `try/except` essentially tells the users of the function that it is not possible. Instead of raising an exception, it does so gracefully.

While the approach does not require explicit knowledge of the form of the arguments, it still requires the understanding of when the values may violate the `int()` usage. In this case, it would raise a `ValueError` when the supplied value cannot be parsed as a base-10 integer. The `ValueError` handling is still conditional, but more vague or abstract than explicit conditions through `if` statements, yet less so than [blanket exception handling](#blanket-exception) with no type of errors specified as seen from the zero division example.

The handling of the error (block under `except`) would be a _business decision_ that its makers have to make. In the example, we instruct the function to "early exit" by `return None`. `None` is a special type in Python, with its only value also being `None`, which represents "nothing". When there is just `return` with no value for it, Python implies it as `return None`.

### Controlled Errors

To anticipate and handle errors is a significant tool. In turn, raising controlled errors allows us to better inform our users:

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
>>> from utility import hours_from  # cherry-pick needed members from a module
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

Python successfully handles the initial `ValueError` and raises the explicit `Exception` with a custom message we defined along with the original. This gives the users of this function some extra insights on both the technical details of _where_ things failed (the original `ValueError`) and _why_ it failed with the custom message conveying the intended usage patterns (the explicitly raised `Exception`). This is usually a judgment call depending on the intended users' domain expertise. One can argue that the original `ValueError` would suffice, in which case:

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

...or simply equivelantly:

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

### Assertion

So far we have only utilized either `print()` or immediate evaluation response from the interactive shell to verify correctness of our code. To verify evaluation expectations, Python provides `assert` for such a purpose:

```python
>>> from utility import hours_from
>>> assert hours_from(16, 12345) == '01:00'  # nothing
>>> assert hours_from(16, 12345) != '16:00'  # nothing
>>> assert hours_from(16, 12345) == '16:00'
Traceback (most recent call last):
  ...
AssertionError
```

As demonstrated from the above example, when the evaluation is expected (truthy), it would result in nothing, as in "no news is good news"; otherwise, it raises an `AssertionError` to signify the mismatch of evaluation expectation.

### Notes on Case Handling

The use of additional conditions to be more comprehensive always has its limit. Every line of code added to handle more cases may cause regression and break existing functionality, sometimes costing more than what it would gain.

Comparatively, uncareful error controls may hide too much useful error information that could otherwise help its makers to improve it.

While there is no definitive answer on where to draw the line on when to apply which type of case handling, makers usually need to consider many factors. To name a few:

* Whether the handling is engineeringly and societally ethical.
* Whether the handling adds more potential "corner cases" or contradicts with existing cases.
* Whether the handling is simple to reason.
* Whether the handling is simple to use.
* Whether the handling adds to the technical debt or the cost of replacement.
* ...

When the problem of choice presents itself, and there is insufficient supporting information to consider all factors, makers often resort to the "by default chocolate ice cream" scenario and make peace with simplicity. As the Unix Philosophy describes, "Do One Thing and Do it Well", embracing simplicity has become the mainstream wisdom to be applied at least in a unit abstraction level, such as functions in Python.

## Exercises

### Problem

Refer to the [`turn_on_day()`](#turn-on-day) function implementation, implement:
* `turn_off_day()`
* `toggle_day()`

### Problem

Implement a function `turn_day()` such that:

```python
SUN = 0
MON = 1
TUE = 2
WED = 3
THU = 4
FRI = 5
SAT = 6

def turn_day(days, day_bit, is_on):
    # is_on is either True or False
    # ...implementation
    pass

# tests
assert bin(turn_day(0b0000000, SAT, is_on=True)) == '0b1000000'
assert bin(turn_day(0b1111111, WED, is_on=False)) == '0b1110111'
```

### Problem

```python
def change_day(days, day_bit, mode):
    # mode can be 'on', 'off', 'toggle'
    # ...implementation
    pass
```

### Problem

```python

def is_day_on(days, day_bit):
    # ...implementation
    pass

assert is_day_on(0b1111111, WED)
assert not is_day_on(0b1110111, WED)
```
