import pytest
import io
import sys
import polars as pl 
from contextlib import redirect_stdout
from narlogs import print_step

df = pl.read_csv("chickweight.csv")


@print_step
def identity(dataf, **kwargs):
    return dataf



def test_identity():    
    f = io.StringIO()
    with redirect_stdout(f):
        identity(df)
    out = f.getvalue().strip()

    assert "time" in out
    assert "n_obs" in out
    assert "n_col" in out
    assert "step" in out
    assert "dtypes" in out


@pytest.mark.parametrize("names", ["a", "b", ["a", "b", "c"]])
def test_identity_kwargs(names):    
    f = io.StringIO()
    with redirect_stdout(f):
        identity(df, **{n: 1 for n in names})
    out = f.getvalue().strip()
    for n in names:
        assert n in out
    
