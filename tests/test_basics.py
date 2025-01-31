import pytest
import io
import sys
import polars as pl 
import pandas as pd
from contextlib import redirect_stdout
from narlogs import print_step


dataframes = [
    pl.read_csv("chickweight.csv"),
    pd.read_csv("chickweight.csv"),
]

@print_step
def identity(dataf, **kwargs):
    return dataf


@pytest.mark.parametrize("df", dataframes)
def test_identity(df):    
    f = io.StringIO()
    with redirect_stdout(f):
        identity(df)
    out = f.getvalue().strip()

    assert "time" in out
    assert "n_obs" in out
    assert "n_col" in out
    assert "step" in out
    assert "dtypes" in out


@pytest.mark.parametrize("df", dataframes)
@pytest.mark.parametrize("names", ["a", "b", ["a", "b", "c"]])
def test_identity_kwargs(df, names):    
    f = io.StringIO()
    with redirect_stdout(f):
        identity(df, **{n: 1 for n in names})
    out = f.getvalue().strip()
    for n in names:
        assert n in out
    
