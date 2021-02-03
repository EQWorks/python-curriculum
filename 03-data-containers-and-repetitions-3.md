# Part 03 - Data Containers and Repetitions (3/3)

## Classes

Similar to pre-made LEGO® pieces, Python offers plenty of built-in [functions](https://docs.python.org/3.8/library/functions.html) and [types](https://docs.python.org/3.8/library/stdtypes.html) for many possible applications.

At times, there are needs to have more flexibility and customizations. Python offers its `class` interface for us to create custom _types_ as our fourth reusability building block:

```python
'''norse_type.py'''
import json

class Norse:

    def __init__(self, data):
        self.data = data

    def to_json(self):
        return json.dumps(self.data)
```

And with a JSON file as the source for our data:

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
      "lat": 0.0,
      "lon": 0.0,
      "wiki_link": "https://en.wikipedia.org/wiki/Asgard"
    }
  }
]
```

```python
'''norse_connector.py'''
import json

from norse_type import Norse

with open('./norse.json', mode='r') as f:
    data = json.load(f)

n = Norse(data)

print(type(n))
print()
print(n.data)
print()
print(n.to_json())
```

```shell
% python norse_connector.py
<class 'norse_type.Norse'>

[{'poi': 'Yggdrasil', 'revenue': 790.2, 'cost': 477.85, 'visits': 53, 'unique_visitors': 7}, {'unique_visitors': 10, 'revenue': 1700.65, 'cost': 1500, 'visits': 11, 'poi': 'Valhalla'}, {'poi': 'Asgard', 'revenue': 3215.75, 'cost': 2845.79, 'visits': 265, 'unique_visitors': 71, 'poi_details': {'open_days': [1, 2, 3, 4, 5], 'lat': 0.0, 'lon': 0.0, 'wiki_link': 'https://en.wikipedia.org/wiki/Asgard'}}]

[{"poi": "Yggdrasil", "revenue": 790.2, "cost": 477.85, "visits": 53, "unique_visitors": 7}, {"unique_visitors": 10, "revenue": 1700.65, "cost": 1500, "visits": 11, "poi": "Valhalla"}, {"poi": "Asgard", "revenue": 3215.75, "cost": 2845.79, "visits": 265, "unique_visitors": 71, "poi_details": {"open_days": [1, 2, 3, 4, 5], "lat": 0.0, "lon": 0.0, "wiki_link": "https://en.wikipedia.org/wiki/Asgard"}}]
```

A few observations:
1. We read a JSON file, load its content into a dictionary through the built-in `json` module, then _instantiate_ the dictionary into a custom `Norse` type object.
2. We verify the new instance in variable `n` as `<class 'norse_type.Norse'>`.
3. We access the instance's `data` property and verify it's indeed the dictionary loaded through in step 1.
4. We invoke the instance's `to_json()` method to output the JSON string derived from its `data` property.

The name "`self`" is merely a convention to indicate that it applies to the type's _instance itself_; thus, it _can_ be named as any valid variable name, as long as it is the _first_ argument of the method definition. This concept is essential to understand to make great use of classes, objects, and the programming paradigm known as _Object-oriented programming_.

## I/O - File system (input)

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

    def to_json(self):
        return json.dumps(self.data)
```

And simplify `norse_connector` as so:

```python
'''norse_connector.py'''
from norse_type import Norse

n = Norse('./norse.json')

print(type(n))
print()
print(n.data)
print()
print(n.to_json())
```

The file system is one of the most critical components of a modern computer system. Though greatly differed in implementation by operating systems, programming languages like Python provides an elegant abstraction on top of them, so the way to access files regardless of where it is running on.

## With context manager

The "`with`" statement involves an interesting Python mechanism known as runtime context management; you can read more details about it on its [official documentation](https://docs.python.org/3.8/reference/compound_stmts.html#with). In this particular case, the built-in `open()` function implements such a context manager, eliminating the need for some chores such as closing it when it is no longer needed (or when an exception occurs).

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

The "`finally`" keyword is exception handling flow control on top of the basic `try/except` we have seen already. The logic within its scope happens _regardless_ and _after_ of whether an exception occurs or not. On top of that, we issue a lazily suppressed inner `try/except` logic around the `f.close()` method invocation. Still, in reality, there may be more intricacies that need careful handling.

With a context manager, none of the above is necessary.

## I/O - File system (output)

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
```

And used so:

```python
'''norse_connector.py'''
from norse_type import Norse

n = Norse('./norse.json')
# output to ./norse_processed.json
n.to_json('./norse_processed.json)
```

Of course, the content of the `norse_processed.json` file should be the same as the input `norse.json` file, as we have yet to make any changes.

## State management

On many occasions, encapsulating data and expose access and operations to them through object properties and methods offer no distinct edge over simple functions. In some programming languages, where the object-oriented paradigm is more rigid, there may be no choice but to organize all logics into various classes.

In Python, the choice is flexible; therefore, utility functions that are agnostic to the internal state (the `data` property), such as `read_from()` and `write_to()`, are outside of the class definition. And we apply functions in the form of methods such as `to_json()` that depend on the object's internal state.

It becomes more valuable as we provide abstractions that perform further state manipulations as a gateway for a more convenient and declarative interface for its users:

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


class Norse:
    # ...
    def flatten(self):
        for i, row in enumerate(self.data):
            self.data[i] = flatten_norse(row)
```

```python
'''norse_connector.py'''
from norse_type import Norse

n = Norse('./norse.json')

n.flatten()
n.to_json('./norse_processed.json')
```

We take the `flatten_norse()` implementation from [the exercise of the last section](03-data-containers-and-repetitions-2.md#exercises), apply it to mutate the internal state (`data`) to have each of its rows flattened. The built-in `enumerate()` function is used to generate an indexed iterator, so we have easy access to both the list's index and the corresponding individual item:

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
    "poi_details.lat": 0.0,
    "poi_details.lon": 0.0,
    "poi_details.wiki_link": "https://en.wikipedia.org/wiki/Asgard"
  }
]
```

There is no settled convention among Python developers on whether to keep as much inside or outside classes. As demonstrated here, one viable approach is to derive out _stateless_ logic in functions outside of classes while keeping only _stateful_ (dependent on the current property value of `data`) ones inside the class.

## Pandas

If we were to build a set of abstractions to perform standard data manipulation and analysis tasks, it would take a while. Thanks to the ever-more-prosperous open-source software ecosystem, there are many well built third party libraries that offer more advanced building blocks to alleviate us from reinventing unnecessary wheels.

Among them, [Pandas](https://pandas.pydata.org/) is one of the most popular Python libraries we can use today to handle data:

```python
'''norse_pandas.py'''
import pandas as pd

df = pd.read_json('./norse.json')
print(df)
```

```shell
% python norse_pandas.py
         poi  revenue  ...  unique_visitors                                        poi_details
0  Yggdrasil   790.20  ...                7                                                NaN
1   Valhalla  1700.65  ...               10                                                NaN
2     Asgard  3215.75  ...               71  {'open_days': [1, 2, 3, 4, 5], 'lat': 0.0, 'lo...

[3 rows x 6 columns]
```

Pandas' primary interface of abstraction is its `DataFrame` class and many utility abstractions built around that. It does not just stop at file I/O. Let us try some simple statistics with some ["real" data](data/poi_stats.json) through HTTP API as a form of input:

```python
'''poi_stats.py'''
import pandas as pd
import requests

data_url = 'https://raw.githubusercontent.com/EQWorks/python-curriculum/03/main/data/poi_stats.json'
with requests.get(data_url) as r:
    data = r.json()

df = pd.DataFrame.from_dict(data)
print('Means:')
print(df.mean())
print('\nMedians:')
print(df.median())
print('\nStandard deviations:')
print(df.std())
```

```shell
% python poi_stats.py
Means:
visitors     952.081400
visits      1617.321000
revenue     5199.971570
cost        2609.954645
dtype: float64

Medians:
visitors     954.000000
visits      1448.000000
revenue     3986.244819
cost        1418.963295
dtype: float64

Standard deviations:
visitors     549.615419
visits      1221.698989
revenue     4575.798056
cost        3075.278290
dtype: float64
```

Now let us adapt what we have done with the "Norse" series of examples, such as calculating profits:

```python
'''poi_stats.py'''
# ...
df['profit'] = df['revenue'] - df['cost']
df.to_csv('./poi_stats.csv')
```

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

The Pandas library offers many more tools for tasks such as data grouping and aggregation, reshaping and pivoting, visualizations and various output formats, etc. Over time, it is safe to say that its capability will only increase and improve, as the Python programming language itself, again thanks to their respective and, to a certain extent, the larger, vibrant open-source community. Check out its [documentation](https://pandas.pydata.org/pandas-docs/stable/index.html) for a world of wonders.

## Exercises

### Problem 03 - By province

Consult the [Pandas documentation](https://pandas.pydata.org/pandas-docs/stable/index.html) and come up with a way to aggregate the sum, mean, median, and standard deviation of each of the statistics (including the additionally computed ones such as profit and average visits) by each province.

The result should look something like:
|    | province | visits | visits             | visits | visits             | revenue            | revenue           | revenue            | revenue            | cost               | cost               | cost               | cost               | profit             | profit             | profit             | profit             | profit_margin      | profit_margin       | profit_margin       | profit_margin       | avg_revenue        | avg_revenue        | avg_revenue        | avg_revenue        | avg_visits        | avg_visits         | avg_visits         | avg_visits         |
|----|----------|--------|--------------------|--------|--------------------|--------------------|-------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|---------------------|---------------------|---------------------|--------------------|--------------------|--------------------|--------------------|-------------------|--------------------|--------------------|--------------------|
|    |          | sum    | mean               | median | std                | sum                | mean              | median             | std                | sum                | mean               | median             | std                | sum                | mean               | median             | std                | sum                | mean                | median              | std                 | sum                | mean               | median             | std                | sum               | mean               | median             | std                |
| 0  | AB       | 598887 | 1631.8446866485015 | 1507.0 | 1207.924623714941  | 1957337.994993239  | 5333.346035403921 | 4240.786885035249  | 4575.746074783173  | 930678.8994299577  | 2535.9098077110566 | 1363.1918558723698 | 3028.7559039798048 | 1026659.0955632835 | 2797.4362276928705 | 1674.6194882836858 | 3048.389184867708  | 189.03174281622393 | 0.515072868709057   | 0.5358386843071626  | 0.2937413215410847  | 2052.3651239743313 | 5.592275542164391  | 5.881491599290104  | 3.05017305844765   | 629.4025670213682 | 1.714993370630431  | 1.3247045582442318 | 0.734931621156547  |
| 1  | BC       | 638877 | 1605.2185929648242 | 1349.5 | 1220.7668667803634 | 1978580.4217287588 | 4971.307592283314 | 3840.1765584358295 | 4383.045994097833  | 975978.974273682   | 2452.2084780745777 | 1317.756974819684  | 2987.269444070142  | 1002601.4474550773 | 2519.099114208737  | 1456.642594581614  | 2819.6538297965817 | 201.54756159093552 | 0.5064009085199385  | 0.5108019532576503  | 0.2883294308996133  | 2173.13940025551   | 5.46014924687314   | 5.505089972925412  | 3.1941247683840577 | 678.8830965177937 | 1.705736423411542  | 1.3246467184573083 | 0.7304688345898803 |
| 2  | MB       | 586669 | 1598.5531335149865 | 1388.0 | 1289.9546807749753 | 1875168.8484268421 | 5109.451903070414 | 3500.7834367026885 | 4869.189278902533  | 938731.3862600506  | 2557.851188719484  | 1242.0096502146716 | 3316.648170428593  | 936437.4621667891  | 2551.600714350924  | 1281.294747035422  | 3065.539736405138  | 186.06466235565173 | 0.5069881808055906  | 0.5214781517115458  | 0.29098496608363267 | 1947.756997963502  | 5.307239776467308  | 5.467918075426598  | 3.109666926278816  | 621.9424691049891 | 1.6946661283514688 | 1.3246575342465754 | 0.7324269133738563 |
| 3  | NB       | 608273 | 1635.1424731182797 | 1432.0 | 1125.3163262363764 | 2059006.5740451869 | 5534.963908723621 | 4704.69983985505   | 4666.6497498577955 | 1025300.5327992045 | 2756.1842279548505 | 1484.138490122119  | 3154.7820501850965 | 1033706.0412459819 | 2778.7796807687687 | 1363.497169224146  | 3270.187079748795  | 182.48782114137796 | 0.4905586589821988  | 0.4918752949616552  | 0.3017846032004308  | 2064.8130979106463 | 5.550572843845823  | 5.446731561940034  | 3.2084376527186245 | 637.1759601129978 | 1.7128386024542952 | 1.3247232472324724 | 0.7216921428832263 |
| 4  | NL       | 646743 | 1637.3240506329114 | 1563.0 | 1222.85177692504   | 2118422.910916356  | 5363.095977003432 | 4183.457084057332  | 4513.396565571501  | 1054429.3650957546 | 2669.441430622164  | 1771.7086514218547 | 3051.517493657928  | 1063993.5458206    | 2693.6545463812654 | 1599.5198554321696 | 3051.1808011649127 | 197.1415353177354  | 0.4990924944752795  | 0.5279308029047325  | 0.2867521359931386  | 2233.004971205556  | 5.653177142292547  | 5.4318005436470544 | 3.1462684779204286 | 661.9709157696991 | 1.6758757361258205 | 1.3246999368288062 | 0.6727963366408819 |
| 5  | NS       | 637595 | 1622.379134860051  | 1454.0 | 1251.7954641039764 | 2034452.2154869095 | 5176.72319462318  | 4084.7666699610104 | 4255.548586477431  | 1091074.877291321  | 2776.271952395219  | 1584.7014191130515 | 3082.575390074211  | 943377.3381955887  | 2400.451242227961  | 1457.9656807594583 | 2714.220441442718  | 191.35350061883864 | 0.4881466852521394  | 0.47790293608849477 | 0.28804095120315304 | 2212.4039939724034 | 5.643887739725519  | 5.855592923713941  | 3.0452292434785395 | 661.3610634649785 | 1.6871455700637208 | 1.32471347376714   | 0.689425812497983  |
| 6  | NT       | 577830 | 1618.5714285714287 | 1477.0 | 1183.2483182597498 | 1908704.7956147494 | 5346.512032534312 | 3952.3124125982936 | 4808.481481100075  | 948521.8355040103  | 2656.923908974819  | 1401.8898225085145 | 3272.3707981501307 | 960182.9601107397  | 2689.5881235594948 | 1433.6180285014489 | 3108.0612361655235 | 179.66441125407468 | 0.5032616561738786  | 0.5240304728551597  | 0.2914134184055701  | 1944.332579838116  | 5.446309747445703  | 5.192272239305644  | 3.2625370426076308 | 604.4345917555702 | 1.6930940945534179 | 1.3246636771300448 | 0.7047846150974095 |
| 7  | NU       | 631057 | 1647.6684073107049 | 1454.0 | 1265.7916742234163 | 1935581.5413567151 | 5053.737705892207 | 4126.094845516309  | 4306.7692856103395 | 990783.4643165445  | 2586.901995604555  | 1516.4426268247623 | 2933.381676323078  | 944798.0770401699  | 2466.83571028765   | 1256.3603586129193 | 2859.4827653647994 | 190.77732981222508 | 0.498113132668995   | 0.5073903903605268  | 0.29903270386330577 | 2052.1961399522506 | 5.358214464627286  | 5.38977765516271   | 3.131775199095578  | 653.2394384427178 | 1.705586001155921  | 1.3246753246753247 | 0.7411919526901833 |
| 8  | ON       | 661184 | 1632.553086419753  | 1498.0 | 1173.847872171513  | 2149992.8585803527 | 5308.624342173711 | 3760.22281047669   | 4878.020826307993  | 1092615.120434246  | 2697.8151121833234 | 1335.0656577729624 | 3343.486179544103  | 1057377.7381461053 | 2610.8092299903833 | 1328.6673806731064 | 3064.722852952004  | 200.6899278205538  | 0.4979898953363618  | 0.47286384540271614 | 0.2913548786937918  | 2204.055853784603  | 5.4691212252719685 | 5.600182798616679  | 3.240375734355566  | 679.6297616608067 | 1.6864262075950538 | 1.3247106875425458 | 0.6643991317329212 |
| 9  | PE       | 660446 | 1630.7308641975308 | 1396.0 | 1325.4688929950485 | 2006591.6793894968 | 4954.547356517276 | 3683.8820853520674 | 4559.807837918415  | 1027810.106158897  | 2537.802731256536  | 1324.6894091860781 | 3002.487237274237  | 978781.5732306002  | 2416.7446252607415 | 1188.024142263028  | 3099.39169956301   | 194.37943389147418 | 0.4799492194851214  | 0.450621859289436   | 0.29148324748908927 | 2168.9023980349098 | 5.35531456304916   | 5.2274313193149435 | 3.217676410631112  | 689.4349109188995 | 1.7023084220219742 | 1.3246861924686193 | 0.7302998973713671 |
| 10 | QC       | 537624 | 1544.896551724138  | 1366.0 | 1211.517992097268  | 1684283.1795119722 | 4839.89419399992  | 3455.2778526070815 | 4514.588635684884  | 888965.6060204294  | 2554.4988678747973 | 1448.4748889206385 | 3085.3009280447613 | 795317.573491544   | 2285.3953261251263 | 1319.9108562600452 | 2791.9855301359144 | 167.73549240216067 | 0.4833875861733737  | 0.47937853360409466 | 0.28306882031407615 | 1898.9011398911969 | 5.472337578937167  | 5.621113762620495  | 3.239636742800708  | 595.6582224940682 | 1.7165943011356433 | 1.3246835443037974 | 0.6911504335633325 |
| 11 | SK       | 655643 | 1610.916461916462  | 1448.0 | 1174.4262524998533 | 2185932.3766825204 | 5370.841220350173 | 4231.672220589093  | 4650.6424308089445 | 1077849.2662184085 | 2648.278295376925  | 1447.2854987013666 | 3015.6933886010333 | 1108083.1104641103 | 2722.5629249732438 | 1471.9609599737491 | 3093.01972379947   | 202.288525719234   | 0.49702340471556267 | 0.4900270811676682  | 0.29720002742275614 | 2213.9601732004858 | 5.439705585259179  | 5.289861474291585  | 3.172249584160175  | 683.6020523260257 | 1.6796119221769674 | 1.3247252747252747 | 0.6852932999288859 |
| 12 | YT       | 645777 | 1602.424317617866  | 1389.0 | 1225.845080058123  | 2105802.451528765  | 5225.316256895198 | 4386.255527472374  | 4496.6154667642395 | 1007033.7934376163 | 2498.8431598948296 | 1423.9040285738358 | 2716.2030100055454 | 1098768.6580911453 | 2726.4730970003607 | 1705.0501130668054 | 3097.512795824044  | 205.3882786787595  | 0.5096483341904702  | 0.5212960295107677  | 0.2853590723541542  | 2264.974376233344  | 5.62028381199341   | 5.5811116305193895 | 3.211527377010319  | 667.9002003506628 | 1.6573205964036297 | 1.3246402877697843 | 0.6489204555507264 |

_Bonus_: figure out a way to reshape the aggregation result so the double-header is flattened (such as `visits_sum`), which should look something like:

|    | province | visits_sum | visits_mean        | visits_median | visits_std         | revenue_sum        | revenue_mean      | revenue_median     | revenue_std        | cost_sum           | cost_mean          | cost_median        | cost_std           | profit_sum         | profit_mean        | profit_median      | profit_std         | profit_margin_sum  | profit_margin_mean  | profit_margin_median | profit_margin_std   | avg_revenue_sum    | avg_revenue_mean   | avg_revenue_median | avg_revenue_std    | avg_visits_sum    | avg_visits_mean    | avg_visits_median  | avg_visits_std     |
|----|----------|------------|--------------------|---------------|--------------------|--------------------|-------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|---------------------|----------------------|---------------------|--------------------|--------------------|--------------------|--------------------|-------------------|--------------------|--------------------|--------------------|
| 0  | AB       | 598887     | 1631.8446866485015 | 1507.0        | 1207.924623714941  | 1957337.994993239  | 5333.346035403921 | 4240.786885035249  | 4575.746074783173  | 930678.8994299577  | 2535.9098077110566 | 1363.1918558723698 | 3028.7559039798048 | 1026659.0955632835 | 2797.4362276928705 | 1674.6194882836858 | 3048.389184867708  | 189.03174281622393 | 0.515072868709057   | 0.5358386843071626   | 0.2937413215410847  | 2052.3651239743313 | 5.592275542164391  | 5.881491599290104  | 3.05017305844765   | 629.4025670213682 | 1.714993370630431  | 1.3247045582442318 | 0.734931621156547  |
| 1  | BC       | 638877     | 1605.2185929648242 | 1349.5        | 1220.7668667803634 | 1978580.4217287588 | 4971.307592283314 | 3840.1765584358295 | 4383.045994097833  | 975978.974273682   | 2452.2084780745777 | 1317.756974819684  | 2987.269444070142  | 1002601.4474550773 | 2519.099114208737  | 1456.642594581614  | 2819.6538297965817 | 201.54756159093552 | 0.5064009085199385  | 0.5108019532576503   | 0.2883294308996133  | 2173.13940025551   | 5.46014924687314   | 5.505089972925412  | 3.1941247683840577 | 678.8830965177937 | 1.705736423411542  | 1.3246467184573083 | 0.7304688345898803 |
| 2  | MB       | 586669     | 1598.5531335149865 | 1388.0        | 1289.9546807749753 | 1875168.8484268421 | 5109.451903070414 | 3500.7834367026885 | 4869.189278902533  | 938731.3862600506  | 2557.851188719484  | 1242.0096502146716 | 3316.648170428593  | 936437.4621667891  | 2551.600714350924  | 1281.294747035422  | 3065.539736405138  | 186.06466235565173 | 0.5069881808055906  | 0.5214781517115458   | 0.29098496608363267 | 1947.756997963502  | 5.307239776467308  | 5.467918075426598  | 3.109666926278816  | 621.9424691049891 | 1.6946661283514688 | 1.3246575342465754 | 0.7324269133738563 |
| 3  | NB       | 608273     | 1635.1424731182797 | 1432.0        | 1125.3163262363764 | 2059006.5740451869 | 5534.963908723621 | 4704.69983985505   | 4666.6497498577955 | 1025300.5327992045 | 2756.1842279548505 | 1484.138490122119  | 3154.7820501850965 | 1033706.0412459819 | 2778.7796807687687 | 1363.497169224146  | 3270.187079748795  | 182.48782114137796 | 0.4905586589821988  | 0.4918752949616552   | 0.3017846032004308  | 2064.8130979106463 | 5.550572843845823  | 5.446731561940034  | 3.2084376527186245 | 637.1759601129978 | 1.7128386024542952 | 1.3247232472324724 | 0.7216921428832263 |
| 4  | NL       | 646743     | 1637.3240506329114 | 1563.0        | 1222.85177692504   | 2118422.910916356  | 5363.095977003432 | 4183.457084057332  | 4513.396565571501  | 1054429.3650957546 | 2669.441430622164  | 1771.7086514218547 | 3051.517493657928  | 1063993.5458206    | 2693.6545463812654 | 1599.5198554321696 | 3051.1808011649127 | 197.1415353177354  | 0.4990924944752795  | 0.5279308029047325   | 0.2867521359931386  | 2233.004971205556  | 5.653177142292547  | 5.4318005436470544 | 3.1462684779204286 | 661.9709157696991 | 1.6758757361258205 | 1.3246999368288062 | 0.6727963366408819 |
| 5  | NS       | 637595     | 1622.379134860051  | 1454.0        | 1251.7954641039764 | 2034452.2154869095 | 5176.72319462318  | 4084.7666699610104 | 4255.548586477431  | 1091074.877291321  | 2776.271952395219  | 1584.7014191130515 | 3082.575390074211  | 943377.3381955887  | 2400.451242227961  | 1457.9656807594583 | 2714.220441442718  | 191.35350061883864 | 0.4881466852521394  | 0.47790293608849477  | 0.28804095120315304 | 2212.4039939724034 | 5.643887739725519  | 5.855592923713941  | 3.0452292434785395 | 661.3610634649785 | 1.6871455700637208 | 1.32471347376714   | 0.689425812497983  |
| 6  | NT       | 577830     | 1618.5714285714287 | 1477.0        | 1183.2483182597498 | 1908704.7956147494 | 5346.512032534312 | 3952.3124125982936 | 4808.481481100075  | 948521.8355040103  | 2656.923908974819  | 1401.8898225085145 | 3272.3707981501307 | 960182.9601107397  | 2689.5881235594948 | 1433.6180285014489 | 3108.0612361655235 | 179.66441125407468 | 0.5032616561738786  | 0.5240304728551597   | 0.2914134184055701  | 1944.332579838116  | 5.446309747445703  | 5.192272239305644  | 3.2625370426076308 | 604.4345917555702 | 1.6930940945534179 | 1.3246636771300448 | 0.7047846150974095 |
| 7  | NU       | 631057     | 1647.6684073107049 | 1454.0        | 1265.7916742234163 | 1935581.5413567151 | 5053.737705892207 | 4126.094845516309  | 4306.7692856103395 | 990783.4643165445  | 2586.901995604555  | 1516.4426268247623 | 2933.381676323078  | 944798.0770401699  | 2466.83571028765   | 1256.3603586129193 | 2859.4827653647994 | 190.77732981222508 | 0.498113132668995   | 0.5073903903605268   | 0.29903270386330577 | 2052.1961399522506 | 5.358214464627286  | 5.38977765516271   | 3.131775199095578  | 653.2394384427178 | 1.705586001155921  | 1.3246753246753247 | 0.7411919526901833 |
| 8  | ON       | 661184     | 1632.553086419753  | 1498.0        | 1173.847872171513  | 2149992.8585803527 | 5308.624342173711 | 3760.22281047669   | 4878.020826307993  | 1092615.120434246  | 2697.8151121833234 | 1335.0656577729624 | 3343.486179544103  | 1057377.7381461053 | 2610.8092299903833 | 1328.6673806731064 | 3064.722852952004  | 200.6899278205538  | 0.4979898953363618  | 0.47286384540271614  | 0.2913548786937918  | 2204.055853784603  | 5.4691212252719685 | 5.600182798616679  | 3.240375734355566  | 679.6297616608067 | 1.6864262075950538 | 1.3247106875425458 | 0.6643991317329212 |
| 9  | PE       | 660446     | 1630.7308641975308 | 1396.0        | 1325.4688929950485 | 2006591.6793894968 | 4954.547356517276 | 3683.8820853520674 | 4559.807837918415  | 1027810.106158897  | 2537.802731256536  | 1324.6894091860781 | 3002.487237274237  | 978781.5732306002  | 2416.7446252607415 | 1188.024142263028  | 3099.39169956301   | 194.37943389147418 | 0.4799492194851214  | 0.450621859289436    | 0.29148324748908927 | 2168.9023980349098 | 5.35531456304916   | 5.2274313193149435 | 3.217676410631112  | 689.4349109188995 | 1.7023084220219742 | 1.3246861924686193 | 0.7302998973713671 |
| 10 | QC       | 537624     | 1544.896551724138  | 1366.0        | 1211.517992097268  | 1684283.1795119722 | 4839.89419399992  | 3455.2778526070815 | 4514.588635684884  | 888965.6060204294  | 2554.4988678747973 | 1448.4748889206385 | 3085.3009280447613 | 795317.573491544   | 2285.3953261251263 | 1319.9108562600452 | 2791.9855301359144 | 167.73549240216067 | 0.4833875861733737  | 0.47937853360409466  | 0.28306882031407615 | 1898.9011398911969 | 5.472337578937167  | 5.621113762620495  | 3.239636742800708  | 595.6582224940682 | 1.7165943011356433 | 1.3246835443037974 | 0.6911504335633325 |
| 11 | SK       | 655643     | 1610.916461916462  | 1448.0        | 1174.4262524998533 | 2185932.3766825204 | 5370.841220350173 | 4231.672220589093  | 4650.6424308089445 | 1077849.2662184085 | 2648.278295376925  | 1447.2854987013666 | 3015.6933886010333 | 1108083.1104641103 | 2722.5629249732438 | 1471.9609599737491 | 3093.01972379947   | 202.288525719234   | 0.49702340471556267 | 0.4900270811676682   | 0.29720002742275614 | 2213.9601732004858 | 5.439705585259179  | 5.289861474291585  | 3.172249584160175  | 683.6020523260257 | 1.6796119221769674 | 1.3247252747252747 | 0.6852932999288859 |
| 12 | YT       | 645777     | 1602.424317617866  | 1389.0        | 1225.845080058123  | 2105802.451528765  | 5225.316256895198 | 4386.255527472374  | 4496.6154667642395 | 1007033.7934376163 | 2498.8431598948296 | 1423.9040285738358 | 2716.2030100055454 | 1098768.6580911453 | 2726.4730970003607 | 1705.0501130668054 | 3097.512795824044  | 205.3882786787595  | 0.5096483341904702  | 0.5212960295107677   | 0.2853590723541542  | 2264.974376233344  | 5.62028381199341   | 5.5811116305193895 | 3.211527377010319  | 667.9002003506628 | 1.6573205964036297 | 1.3246402877697843 | 0.6489204555507264 |
