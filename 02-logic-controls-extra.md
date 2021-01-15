# Part 02 - Logic Controls (extra)

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

Those numbers that begin with `0b` are integers expressed directly in their binary representations. The built-in function `bin` translates a regular integer (of base 10) to its binary string representation. And finally, the `int` built-in function converts the binary string representation back to an integer, with a second argument to specify its base.

Conceptually bitwise representations resemble something similar to the [string indexing](01-immediate-applications-2.md#text-processing-continued) but in a reverse order. To translate a binary representation back to its base-10 integer form:

![binary-conversion](https://i.imgur.com/wIMNUpr.png)

There are some other bitwise operations such as `<<` (left shift) and `>>` (right shift) that shifts all bits toward a desired direction:

```python
>>> bin(0b010 << 1)  # left shift and show binary string representation
'0b100'
>>> bin(0b010 >> 1)  # right shift and show binary string repr
'0b1'  # leading 0s are omitted
```

Bitwise shifts can be used to emulate integer multiplications and divisions:

```python
>>> x = 5
>>> x * 2 == x << 1
True
>>> x // 2 == x >> 1
True
```

![bitwise-shift](https://i.imgur.com/gSfrIOx.png)

### Bitmasking

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

![implicit-bits](https://i.imgur.com/r2FPguQ.png)

A (near) real-world Python example of dayparting application:

```python
>>> SUN = 0
>>> MON = 1
>>> TUE = 2
>>> WED = 3
>>> THU = 4
>>> FRI = 5
>>> SAT = 6
>>> def turn_on_day(days, day_bit):
...     return days | (1 << day_bit)
...
>>> days = 0b0000000  # 7 days in bits, from right-to-left, SUN to SAT
>>> days = turn_on_day(days, SAT)  # turn on SAT
>>> bin(days)  # examine the binary string representation of resulting days
'0b1000000'
```

## Exercises

### Problem - Days in bits

Refer to the [`turn_on_day()`](#turn-on-day) function implementation, implement the following functions.

#### `turn_off_day()`

```python
# days-bits mapping
SUN = 0
MON = 1
TUE = 2
WED = 3
THU = 4
FRI = 5
SAT = 6

def turn_off_day(days, day_bit):
    # ...implementation
    pass

# assertion tests
assert bin(turn_off_day(0b1111111, WED)) == '0b1110111'
```

#### `toggle_day()`

```python
def toggle_day(days, day_bit):
    # ...implementation
    pass

assert bin(toggle_day(0b1111111, THU)) == '0b1101111'
```

#### `turn_day()`

```python
def turn_day(days, day_bit, is_on):
    # is_on is either True or False
    # ...implementation
    pass

assert bin(turn_day(0b0000000, SAT, is_on=True)) == '0b1000000'
assert bin(turn_day(0b1111111, WED, is_on=False)) == '0b1110111'
```

#### `is_day_on()`

```python
def is_day_on(days, day_bit):
    # ...implementation
    pass

assert is_day_on(0b1111111, WED)
assert not is_day_on(0b1110111, WED)
```
