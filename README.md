<img src="imgs/logs.png" alt="dicekit logo" width="125" align="right"/>

### narlogs

> Decorators for logging purposes for all your dataframes.

## Install

```bash
uv pip install narlogs
```

## Usage

The goal of this project is to make it simple to decorate your dataframe pipeline with some logs. There is [a very nice decorator pattern for this](https://calmcode.io/course/pandas-pipe/logs) and thanks to [narwhals](https://github.com/narwhals-dev/narwhals) we can write utilities for these such that they work on a whole lot of dataframe libraries. The main use case for this is to log useful stats about the dataframe at each step of the pipeline.

```python
import time
import polars as pl
import pandas as pd
from narlogs import print_step

# This is just some function for demo purposes, you can replace it with any function
@print_step
def identity(dataf, t=1):
    time.sleep(t)
    return dataf
    
# When we `.pipe` the function to the polars dataframe it starts printing
pl.read_csv("chickweight.csv").pipe(identity).pipe(identity, t=0.5)

# We get the exact same thing when we pipe it with a pandas dataframe, thanks to narwhals!
pd.read_csv("chickweight.csv").pipe(identity).pipe(identity, t=0.5)
```

This library also offers a general "callback" function if you want to be more flexible. Maybe you want to create an artifact of some sort or maybe you want to print a sample of the dataframe. Anything a Python function can do, it can do with this callback.

```python
import time
import pandas as pd
import polars as pl
from narlogs import callback

@callback
def print_sample(dataf):
    # You can use narwhals code inside here!
    print(dataf.head(4))

@print_sample
def identity(dataf):
    time.sleep(0.5)
    return dataf
    
# You will now see a sample get printed, in both cases.
pl.read_csv("chickweight.csv").pipe(identity)
pd.read_csv("chickweight.csv").pipe(identity)
```

## Try it live

To learn more, we recommend checking out [this Marimo notebook](https://koaning.github.io/narlogs/). You can play with narlogs straight from the browser without having to download anything!
