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

Similar to how [we handle precision-sensitive arithmetic](01-immediate-applications-1.md#fixed-point-numbers), the trade-off here is the implicit knowledge of what each bit represents is a requirement. This issue can be mitigated by abstracting away the implicit knowledge and expose a well <a name="turn-on-day"></a>defined interface for its users:

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

And typically used as so:

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

# when used
print(bin(turn_day(0b0000000, SAT, is_on=True)))  # prints out 0b1000000
print(bin(turn_day(0b1111111, WED, is_on=False)))  # prints out 0b1110111
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

print(is_day_on(0b1111111, WED))  # prints True
print(is_day_on(0b1110111, WED))  # prints False
```
