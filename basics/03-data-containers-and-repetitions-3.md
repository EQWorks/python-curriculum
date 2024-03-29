# Part 03 - Data Containers and Repetitions (3/3)

## Classes

Like pre-made LEGO® pieces, Python offers a rich [standard library](https://docs.python.org/3.8/library/index.html) with plenty of built-in [functions](https://docs.python.org/3.8/library/functions.html), [types](https://docs.python.org/3.8/library/stdtypes.html), and many more for building applications.

At times, there are needs to have more flexibility and customizations. Python offers its `class` interface to create custom types as our fourth reusability building block.

Let us reuse the "Norse" dataset as our input in the form of a JSON file:

```json
[
  {
    "poi": "Yggdrasil",
    "revenue": 790.2,
    "cost": 477.85,
    "visits": 53,
    "unique_visitors": 7
  },
  {
    "unique_visitors": 10,
    "revenue": 1700.65,
    "cost": 1500,
    "visits": 11,
    "poi": "Valhalla"
  },
  {
    "poi": "Asgard",
    "revenue": 3215.75,
    "cost": 2845.79,
    "visits": 265,
    "unique_visitors": 71,
    "poi_details": {
      "open_days": [
        1,
        2,
        3,
        4,
        5
      ],
      "lat": 0,
      "lon": 0,
      "wiki_link": "https://en.wikipedia.org/wiki/Asgard"
    }
  }
]
```

And with a humble start of a class implementation to handle the data:

```python
'''norse_type.py'''
import json

class Norse:

    def __init__(self, data):
        self.data = data

    def to_json(self):
        return json.dumps(self.data)

with open('./norse.json', mode='r') as f:
    data = json.load(f)

n = Norse(data)

print(type(n))
print()  # empty new line
print(n.data)
print()
print(n.to_json())
```

```shell
% python norse_type.py
<class 'norse_type.Norse'>

[{'poi': 'Yggdrasil', 'revenue': 790.2, 'cost': 477.85, 'visits': 53, 'unique_visitors': 7}, {'unique_visitors': 10, 'revenue': 1700.65, 'cost': 1500, 'visits': 11, 'poi': 'Valhalla'}, {'poi': 'Asgard', 'revenue': 3215.75, 'cost': 2845.79, 'visits': 265, 'unique_visitors': 71, 'poi_details': {'open_days': [1, 2, 3, 4, 5], 'lat': 0.0, 'lon': 0.0, 'wiki_link': 'https://en.wikipedia.org/wiki/Asgard'}}]

[{"poi": "Yggdrasil", "revenue": 790.2, "cost": 477.85, "visits": 53, "unique_visitors": 7}, {"unique_visitors": 10, "revenue": 1700.65, "cost": 1500, "visits": 11, "poi": "Valhalla"}, {"poi": "Asgard", "revenue": 3215.75, "cost": 2845.79, "visits": 265, "unique_visitors": 71, "poi_details": {"open_days": [1, 2, 3, 4, 5], "lat": 0.0, "lon": 0.0, "wiki_link": "https://en.wikipedia.org/wiki/Asgard"}}]
```

A few observations:
1. We read a JSON file, load its content into a dictionary through the built-in `json` module, then _instantiate_ (or initialize) the dictionary into a custom `Norse` type object through the "magic" `__init__()` method.
2. We verify the new instance in variable `n` as `<class 'norse_type.Norse'>`.
3. We access the instance's `data` property and verify it's indeed a list of dictionaries loaded in step 1.
4. We invoke the instance's `to_json()` method to output the JSON string derived from its `data` property.

The name "`self`" is merely a convention to indicate that it applies to the type's _instance itself_; thus, it _can_ be named as any valid variable name, as long as it is the _first_ argument of the method definition. This concept is essential to understand to make great use of classes, objects, and the programming paradigm known as _Object-oriented programming_.

### I/O - File system

Let us develop some additional capabilities to our `Norse` class, say internalize the file reading so one can instantiate a new `Norse` type object by calling `n = Norse('./data.json')`:

```python
'''norse_type.py'''
import json

def read_from(fname):
    with open(fname, mode='r') as f:
        return json.load(f)

class Norse:
    def __init__(self, data):
        if type(data) is str:
            self.data = read_from(data)
        else:
            self.data = data

    # ...

n = Norse('./norse.json')
# ...
```

The file system is one of the most critical components of a modern computer system. Though greatly differed in implementation by operating systems, programming languages like Python usually provide elegant abstractions so that the access can be convenient for the users of the language.

Let us add a file output capability to the `to_json()` method:

```python
'''norse_type.py'''
# ...

def write_to(data, fname):
    with open(fname, mode='w') as f:
        json.dump(data, f, indent=2)

class Norse:
    # ...

    def to_json(self, fname=''):
        if not fname:
            return json.dumps(self.data)

        return write_to(self.data, fname)

n = Norse('./norse.json')
n.to_json('./norse_processed.json')  # output to ./norse_processed.json
```

Of course, the content of the `norse_processed.json` file should be the same as the input `norse.json` file, as we have yet to make any changes.

### With context manager

The "`with`" statement involves an interesting Python mechanism known as runtime context management; you can read more details about it on its [official documentation](https://docs.python.org/3.8/reference/compound_stmts.html#with). In this particular case, the object returned by the built-in `open()` function implements such a context manager, eliminating the need for some chores such as closing the underlying file system I/O connectivity when it is no longer needed (or when an exception occurs).

Without the context manager, our `read_from()` function implementation may look like so:

```python
def read_from(fname):
    try:
        f = open(fname, mode='r')
        return json.load(f)
    except:
        raise
    finally:
        try:
            f.close()
        except:
            pass
```

The "`finally`" keyword is an exception control on top of the basic `try/except` we have seen already. The logic within its scope happens _regardless of_ and _after_ whether an exception occurs or not. On top of that, we issue a lazily suppressed inner `try/except` logic around the `f.close()` method invocation. Still, in reality, there may be more intricacies that need careful handling.

With a context manager, none of the above is necessary for the users to manage.

### Classes or Functions?

On many occasions, encapsulating data and expose access and operations to them through object properties and methods offer no distinct edge over simple functions. There is no settled convention of class usages among the Python or, to a certain extent, all applicable programming languages communities. As demonstrated, one viable approach is to derive out generic algorithms (such as `read_from()` and `write_to()`) in functions outside of classes while keeping only _stateful_ ones (dependent on the current property value of `data`, such as `to_json()`) inside.

Let us take the `flatten_norse()` implementation from [the previous exercise problem](03-data-containers-and-repetitions-2.md#exercises), apply it to mutate the internal state (`data`) to have each of its rows flattened. The built-in `enumerate()` function is used to generate an indexed iterator, so we have easy access to both the list's index and the corresponding individual item:

```python
'''norse_type.py'''
# ...

def flatten_norse(row):
    flat = {}

    for k, v in row.items():
        if type(v) is not dict:
            flat[k] = v
        else:
            for nk, nv in v.items():
                flat['{0}.{1}'.format(k, nk)] = nv

    return flat

def flatten_func(data):  # function equiv of flatten() method
    for i, row in enumerate(data):
        data[i] = flatten_norse(row)

class Norse:
    # ...
    def flatten(self):  # method equiv of flatten_func() function
        for i, row in enumerate(self.data):
            self.data[i] = flatten_norse(row)

n = Norse('./norse.json')

n.flatten()
# or
flatten_func(n.data)

n.to_json('./norse_processed.json')
```

Objectively, the method `n.flatten()` and the mutating function `flatten_func(n.data)` would correctly achieve the same result. Though for some, it may be more intuitive to use it through a method as it implies that the mutation operation applies to the object `n` _itself_.

```json
[
  {
    "poi": "Yggdrasil",
    "revenue": 790.2,
    "cost": 477.85,
    "visits": 53,
    "unique_visitors": 7
  },
  {
    "unique_visitors": 10,
    "revenue": 1700.65,
    "cost": 1500,
    "visits": 11,
    "poi": "Valhalla"
  },
  {
    "poi": "Asgard",
    "revenue": 3215.75,
    "cost": 2845.79,
    "visits": 265,
    "unique_visitors": 71,
    "poi_details.open_days": [
      1,
      2,
      3,
      4,
      5
    ],
    "poi_details.lat": 0,
    "poi_details.lon": 0,
    "poi_details.wiki_link": "https://en.wikipedia.org/wiki/Asgard"
  }
]
```

### Statistics

Let us proceed to add some more useful methods to the class to perform some simple statistical analysis, using the [`statistics` module](https://docs.python.org/3.8/library/statistics.html) from the built-in Python library:

```python
'''norse_type.py'''
# ...
import statistics as stats

STATS_KEYS = ['revenue', 'cost', 'visits', 'unique_visitors']

def transmute_stats(data):
    r = {}
    for key in STATS_KEYS:
        r[key] = [d[key] for d in data if d.get(key)]

    return r

class Norse:
    # ...

    def mean(self, column=''):
        ts = transmute_stats(self.data)
        if column:
            return stats.mean(ts.get(column, []))

        return {k: stats.mean(ts.get(k, [])) for k in STATS_KEYS}
```

Which can be used as:

```python
>>> from norse_type import Norse
>>> n = Norse('./norse.json')
>>> n.mean('visits')
109.66666666666667
>>> n.mean()
{'revenue': 1902.2, 'cost': 1607.88, 'visits': 109.66666666666667, 'unique_visitors': 29.333333333333332}
```

## Pandas

If we were to build a comprehensive set of abstractions to perform standard data manipulation and analysis tasks, it would take a while. Thanks to the ever-more-prosperous open-source software ecosystem, there are many well built third party libraries that offer more advanced building blocks to alleviate us from reinventing unnecessary wheels.

Among them, [Pandas](https://pandas.pydata.org/) is one of the most popular Python libraries we can use today to handle data:

```python
'''norse_pandas.py'''
import pandas as pd

df = pd.read_json('./norse.json')
print('Means:')
print(df.mean())
print('\nMedians:')
print(df.median())
print('\nStandard deviations:')
print(df.std())
```

```shell
% python norse_pandas.py
Means:
revenue            1902.200000
cost               1607.880000
visits              109.666667
unique_visitors      29.333333
dtype: float64

Medians:
revenue            1700.65
cost               1500.00
visits               53.00
unique_visitors      10.00
dtype: float64

Standard deviations:
revenue            1225.271400
cost               1187.650425
visits              136.151876
unique_visitors      36.115555
dtype: float64
```

Pandas' primary interface of abstraction is its `DataFrame` class and many utilities built around that. Let us try it with some ["real" data](data/poi_stats.json) through HTTP API as a form of input:

```python
'''poi_stats.py'''
import pandas as pd
import requests

data_url = 'https://raw.githubusercontent.com/EQWorks/python-curriculum/main/data/poi_stats.json'
with requests.get(data_url) as r:
    data = r.json()

df = pd.DataFrame.from_dict(data)
df['profit'] = df['revenue'] - df['cost']
df.to_csv('./poi_stats.csv')
```

|   | poi                          | address               | city            | province | postalcode | visitors | visits | revenue            | cost               | profit             |
|---|------------------------------|-----------------------|-----------------|----------|------------|----------|--------|--------------------|--------------------|--------------------|
| 0 | "Chang, Mccoy and Bond"      | 99480 Joanna Radial   | Robertmouth     | NS       | B3R5Y9     | 498      | 659    | 5342.720445062766  | 1295.4028830718028 | 4047.3175619909634 |
| 1 | "Rodgers, Sanders and Rojas" | 81096 Morris Trail    | Port Jacob      | SK       | S8G6S6     | 242      | 320    | 1745.2750870121083 | 1671.1420393401427 | 74.13304767196564  |
| 2 | Ayers-Clark                  | 68282 Silva Cape      | Port Jacobburgh | NB       | E8K2K1     | 1863     | 2468   | 148.48709980505885 | 75.77944071267525  | 72.7076590923836   |
| 3 | Warren Inc                   | 12053 Jonathan Common | Smithmouth      | ON       | K5C 2V4    | 1756     | 2326   | 10109.082891784037 | 3051.1382829564436 | 7057.944608827594  |
|||| 4996 more... |
||

We observe that the Pandas `DataFrame` provides a simple interface by combining the index notion and intuitive arithmetics to calculate a new `profit` column based on each row's revenue and cost. It could be performing an iterative logic for the per-row calculation and assigning the new column in some data structure behind that abstraction. All those intricacies are openly available through its [source code](https://github.com/pandas-dev/pandas/) as a form of opt-in transparency. Though for us, all we have to do is enjoy the magic of elegant abstractions.

Let us apply the same computations from [Exercise Problem 01](03-data-containers-and-repetitions-1.md#exercises):

```python
# ...
df['profit'] = df['revenue'] - df['cost']
df['profit_margin'] = df['profit'] / df['revenue']
df['avg_revenue'] = df['revenue'] / df['visitors']
df['avg_visits'] = df['visits'] / df['visitors']
df.to_csv('./poi_stats.csv')
```

|   | poi                          | address               | city            | province | postalcode | visitors | visits | revenue            | cost               | profit             | profit_margin        | avg_revenue         | avg_visits         |
|---|------------------------------|-----------------------|-----------------|----------|------------|----------|--------|--------------------|--------------------|--------------------|----------------------|---------------------|--------------------|
| 0 | "Chang, Mccoy and Bond"      | 99480 Joanna Radial   | Robertmouth     | NS       | B3R5Y9     | 498      | 659    | 5342.720445062766  | 1295.4028830718028 | 4047.3175619909634 | 0.7575387115249703   | 10.728354307354952  | 1.323293172690763  |
| 1 | "Rodgers, Sanders and Rojas" | 81096 Morris Trail    | Port Jacob      | SK       | S8G6S6     | 242      | 320    | 1745.2750870121083 | 1671.1420393401427 | 74.13304767196564  | 0.042476425764422385 | 7.211880524843423   | 1.322314049586777  |
| 2 | Ayers-Clark                  | 68282 Silva Cape      | Port Jacobburgh | NB       | E8K2K1     | 1863     | 2468   | 148.48709980505885 | 75.77944071267525  | 72.7076590923836   | 0.4896564023934589   | 0.07970322050727796 | 1.3247450348899625 |
| 3 | Warren Inc                   | 12053 Jonathan Common | Smithmouth      | ON       | K5C 2V4    | 1756     | 2326   | 10109.082891784037 | 3051.1382829564436 | 7057.944608827594  | 0.6981785276054866   | 5.756880917872459   | 1.3246013667425969 |
|||| 4996 more... |
||

The Pandas library offers many more tools for data grouping and aggregation, reshaping and pivoting, visualizations, various output formats, etc. Over time, its capability may increase and improve, as the Python programming language itself, again thanks to their respective and, to a certain extent, the larger, vibrant open-source community. Check out its [documentation](https://pandas.pydata.org/pandas-docs/stable/index.html) for a world of wonders.

## Exercises

### Problem 03 - By province

Consult the [Pandas documentation](https://pandas.pydata.org/pandas-docs/stable/index.html) and develop a way to aggregate the sum, mean, median, and standard deviation of each of the statistics (exclude margin and averages) by each province.

The result should look something like:

|    | province | visits | visits             | visits | visits             | revenue            | revenue           | revenue            | revenue            | cost               | cost               | cost               | cost               | profit             | profit             | profit             | profit             |
|----|----------|--------|--------------------|--------|--------------------|--------------------|-------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|
|    |          | sum    | mean               | median | std                | sum                | mean              | median             | std                | sum                | mean               | median             | std                | sum                | mean               | median             | std                |
| 0  | AB       | 598887 | 1631.8446866485015 | 1507.0 | 1207.924623714941  | 1957337.994993239  | 5333.346035403921 | 4240.786885035249  | 4575.746074783173  | 930678.8994299577  | 2535.9098077110566 | 1363.1918558723698 | 3028.7559039798048 | 1026659.0955632835 | 2797.4362276928705 | 1674.6194882836858 | 3048.389184867708  |
| 1  | BC       | 638877 | 1605.2185929648242 | 1349.5 | 1220.7668667803634 | 1978580.4217287588 | 4971.307592283314 | 3840.1765584358295 | 4383.045994097833  | 975978.974273682   | 2452.2084780745777 | 1317.756974819684  | 2987.269444070142  | 1002601.4474550773 | 2519.099114208737  | 1456.642594581614  | 2819.6538297965817 |
| 2  | MB       | 586669 | 1598.5531335149865 | 1388.0 | 1289.9546807749753 | 1875168.8484268421 | 5109.451903070414 | 3500.7834367026885 | 4869.189278902533  | 938731.3862600506  | 2557.851188719484  | 1242.0096502146716 | 3316.648170428593  | 936437.4621667891  | 2551.600714350924  | 1281.294747035422  | 3065.539736405138  |
| 3  | NB       | 608273 | 1635.1424731182797 | 1432.0 | 1125.3163262363764 | 2059006.5740451869 | 5534.963908723621 | 4704.69983985505   | 4666.6497498577955 | 1025300.5327992045 | 2756.1842279548505 | 1484.138490122119  | 3154.7820501850965 | 1033706.0412459819 | 2778.7796807687687 | 1363.497169224146  | 3270.187079748795  |
| 4  | NL       | 646743 | 1637.3240506329114 | 1563.0 | 1222.85177692504   | 2118422.910916356  | 5363.095977003432 | 4183.457084057332  | 4513.396565571501  | 1054429.3650957546 | 2669.441430622164  | 1771.7086514218547 | 3051.517493657928  | 1063993.5458206    | 2693.6545463812654 | 1599.5198554321696 | 3051.1808011649127 |
| 5  | NS       | 637595 | 1622.379134860051  | 1454.0 | 1251.7954641039764 | 2034452.2154869095 | 5176.72319462318  | 4084.7666699610104 | 4255.548586477431  | 1091074.877291321  | 2776.271952395219  | 1584.7014191130515 | 3082.575390074211  | 943377.3381955887  | 2400.451242227961  | 1457.9656807594583 | 2714.220441442718  |
| 6  | NT       | 577830 | 1618.5714285714287 | 1477.0 | 1183.2483182597498 | 1908704.7956147494 | 5346.512032534312 | 3952.3124125982936 | 4808.481481100075  | 948521.8355040103  | 2656.923908974819  | 1401.8898225085145 | 3272.3707981501307 | 960182.9601107397  | 2689.5881235594948 | 1433.6180285014489 | 3108.0612361655235 |
| 7  | NU       | 631057 | 1647.6684073107049 | 1454.0 | 1265.7916742234163 | 1935581.5413567151 | 5053.737705892207 | 4126.094845516309  | 4306.7692856103395 | 990783.4643165445  | 2586.901995604555  | 1516.4426268247623 | 2933.381676323078  | 944798.0770401699  | 2466.83571028765   | 1256.3603586129193 | 2859.4827653647994 |
| 8  | ON       | 661184 | 1632.553086419753  | 1498.0 | 1173.847872171513  | 2149992.8585803527 | 5308.624342173711 | 3760.22281047669   | 4878.020826307993  | 1092615.120434246  | 2697.8151121833234 | 1335.0656577729624 | 3343.486179544103  | 1057377.7381461053 | 2610.8092299903833 | 1328.6673806731064 | 3064.722852952004  |
| 9  | PE       | 660446 | 1630.7308641975308 | 1396.0 | 1325.4688929950485 | 2006591.6793894968 | 4954.547356517276 | 3683.8820853520674 | 4559.807837918415  | 1027810.106158897  | 2537.802731256536  | 1324.6894091860781 | 3002.487237274237  | 978781.5732306002  | 2416.7446252607415 | 1188.024142263028  | 3099.39169956301   |
| 10 | QC       | 537624 | 1544.896551724138  | 1366.0 | 1211.517992097268  | 1684283.1795119722 | 4839.89419399992  | 3455.2778526070815 | 4514.588635684884  | 888965.6060204294  | 2554.4988678747973 | 1448.4748889206385 | 3085.3009280447613 | 795317.573491544   | 2285.3953261251263 | 1319.9108562600452 | 2791.9855301359144 |
| 11 | SK       | 655643 | 1610.916461916462  | 1448.0 | 1174.4262524998533 | 2185932.3766825204 | 5370.841220350173 | 4231.672220589093  | 4650.6424308089445 | 1077849.2662184085 | 2648.278295376925  | 1447.2854987013666 | 3015.6933886010333 | 1108083.1104641103 | 2722.5629249732438 | 1471.9609599737491 | 3093.01972379947   |
| 12 | YT       | 645777 | 1602.424317617866  | 1389.0 | 1225.845080058123  | 2105802.451528765  | 5225.316256895198 | 4386.255527472374  | 4496.6154667642395 | 1007033.7934376163 | 2498.8431598948296 | 1423.9040285738358 | 2716.2030100055454 | 1098768.6580911453 | 2726.4730970003607 | 1705.0501130668054 | 3097.512795824044  |

_Bonus_: figure out a way to reshape the aggregation result so the double-header is flattened (such as `visits_sum`), which should look something like:

|    | province | visits_sum | visits_mean        | visits_median | visits_std         | revenue_sum        | revenue_mean      | revenue_median     | revenue_std        | cost_sum           | cost_mean          | cost_median        | cost_std           | profit_sum         | profit_mean        | profit_median      | profit_std         |
|----|----------|------------|--------------------|---------------|--------------------|--------------------|-------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|
| 0  | AB       | 598887     | 1631.8446866485015 | 1507.0        | 1207.924623714941  | 1957337.994993239  | 5333.346035403921 | 4240.786885035249  | 4575.746074783173  | 930678.8994299577  | 2535.9098077110566 | 1363.1918558723698 | 3028.7559039798048 | 1026659.0955632835 | 2797.4362276928705 | 1674.6194882836858 | 3048.389184867708  |
| 1  | BC       | 638877     | 1605.2185929648242 | 1349.5        | 1220.7668667803634 | 1978580.4217287588 | 4971.307592283314 | 3840.1765584358295 | 4383.045994097833  | 975978.974273682   | 2452.2084780745777 | 1317.756974819684  | 2987.269444070142  | 1002601.4474550773 | 2519.099114208737  | 1456.642594581614  | 2819.6538297965817 |
| 2  | MB       | 586669     | 1598.5531335149865 | 1388.0        | 1289.9546807749753 | 1875168.8484268421 | 5109.451903070414 | 3500.7834367026885 | 4869.189278902533  | 938731.3862600506  | 2557.851188719484  | 1242.0096502146716 | 3316.648170428593  | 936437.4621667891  | 2551.600714350924  | 1281.294747035422  | 3065.539736405138  |
| 3  | NB       | 608273     | 1635.1424731182797 | 1432.0        | 1125.3163262363764 | 2059006.5740451869 | 5534.963908723621 | 4704.69983985505   | 4666.6497498577955 | 1025300.5327992045 | 2756.1842279548505 | 1484.138490122119  | 3154.7820501850965 | 1033706.0412459819 | 2778.7796807687687 | 1363.497169224146  | 3270.187079748795  |
| 4  | NL       | 646743     | 1637.3240506329114 | 1563.0        | 1222.85177692504   | 2118422.910916356  | 5363.095977003432 | 4183.457084057332  | 4513.396565571501  | 1054429.3650957546 | 2669.441430622164  | 1771.7086514218547 | 3051.517493657928  | 1063993.5458206    | 2693.6545463812654 | 1599.5198554321696 | 3051.1808011649127 |
| 5  | NS       | 637595     | 1622.379134860051  | 1454.0        | 1251.7954641039764 | 2034452.2154869095 | 5176.72319462318  | 4084.7666699610104 | 4255.548586477431  | 1091074.877291321  | 2776.271952395219  | 1584.7014191130515 | 3082.575390074211  | 943377.3381955887  | 2400.451242227961  | 1457.9656807594583 | 2714.220441442718  |
| 6  | NT       | 577830     | 1618.5714285714287 | 1477.0        | 1183.2483182597498 | 1908704.7956147494 | 5346.512032534312 | 3952.3124125982936 | 4808.481481100075  | 948521.8355040103  | 2656.923908974819  | 1401.8898225085145 | 3272.3707981501307 | 960182.9601107397  | 2689.5881235594948 | 1433.6180285014489 | 3108.0612361655235 |
| 7  | NU       | 631057     | 1647.6684073107049 | 1454.0        | 1265.7916742234163 | 1935581.5413567151 | 5053.737705892207 | 4126.094845516309  | 4306.7692856103395 | 990783.4643165445  | 2586.901995604555  | 1516.4426268247623 | 2933.381676323078  | 944798.0770401699  | 2466.83571028765   | 1256.3603586129193 | 2859.4827653647994 |
| 8  | ON       | 661184     | 1632.553086419753  | 1498.0        | 1173.847872171513  | 2149992.8585803527 | 5308.624342173711 | 3760.22281047669   | 4878.020826307993  | 1092615.120434246  | 2697.8151121833234 | 1335.0656577729624 | 3343.486179544103  | 1057377.7381461053 | 2610.8092299903833 | 1328.6673806731064 | 3064.722852952004  |
| 9  | PE       | 660446     | 1630.7308641975308 | 1396.0        | 1325.4688929950485 | 2006591.6793894968 | 4954.547356517276 | 3683.8820853520674 | 4559.807837918415  | 1027810.106158897  | 2537.802731256536  | 1324.6894091860781 | 3002.487237274237  | 978781.5732306002  | 2416.7446252607415 | 1188.024142263028  | 3099.39169956301   |
| 10 | QC       | 537624     | 1544.896551724138  | 1366.0        | 1211.517992097268  | 1684283.1795119722 | 4839.89419399992  | 3455.2778526070815 | 4514.588635684884  | 888965.6060204294  | 2554.4988678747973 | 1448.4748889206385 | 3085.3009280447613 | 795317.573491544   | 2285.3953261251263 | 1319.9108562600452 | 2791.9855301359144 |
| 11 | SK       | 655643     | 1610.916461916462  | 1448.0        | 1174.4262524998533 | 2185932.3766825204 | 5370.841220350173 | 4231.672220589093  | 4650.6424308089445 | 1077849.2662184085 | 2648.278295376925  | 1447.2854987013666 | 3015.6933886010333 | 1108083.1104641103 | 2722.5629249732438 | 1471.9609599737491 | 3093.01972379947   |
| 12 | YT       | 645777     | 1602.424317617866  | 1389.0        | 1225.845080058123  | 2105802.451528765  | 5225.316256895198 | 4386.255527472374  | 4496.6154667642395 | 1007033.7934376163 | 2498.8431598948296 | 1423.9040285738358 | 2716.2030100055454 | 1098768.6580911453 | 2726.4730970003607 | 1705.0501130668054 | 3097.512795824044  |
