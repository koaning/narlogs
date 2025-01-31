import marimo

__generated_with = "0.10.18"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        # narlogs

        ## Usage

        The goal of this project is to make it simple to decorate your dataframe pipeline with some logs. There is [a very nice decorator pattern for this](https://calmcode.io/course/pandas-pipe/logs) and thanks to [narwhals](https://github.com/narwhals-dev/narwhals) we can write utilities for these such that they work on a whole lot of dataframe libraries. 

        Check a quick demo below.
        """
    )
    return


@app.cell
def _():
    import time
    import polars as pl
    import pandas as pd
    from narlogs import print_step

    @print_step
    def identity(dataf, t=1):
        time.sleep(t)
        return dataf    

    # Have two dataframes from two different libraries.
    df_pd = pd.read_csv("https://raw.githubusercontent.com/koaning/narlogs/refs/heads/main/chickweight.csv")
    df_pl = pl.read_csv("https://raw.githubusercontent.com/koaning/narlogs/refs/heads/main/chickweight.csv")

    _df = df_pl.pipe(identity).pipe(identity, t=0.5)
    return df_pd, df_pl, identity, pd, pl, print_step, time


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Notice how each call to `identity` is logged here? We can use the exact same decorator on a function even if it is a pandas DataFrame.""")
    return


@app.cell
def _(df_pd, identity):
    _df = df_pd.pipe(identity).pipe(identity, t=0.5)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The logs look a bit different because the libraries deal with unnamed columns differently. 

        ## callback
        """
    )
    return


@app.cell
def _(df_pd, time):
    from narlogs import callback

    @callback
    def print_sample(dataf):
        # You can use narwhals code inside here!
        print(dataf.head(4))

    @print_sample
    def another_identity(dataf):
        time.sleep(0.5)
        return dataf

    # You will now see a sample get printed, in both cases.
    _df = df_pd.pipe(another_identity)
    return another_identity, callback, print_sample


@app.cell
def _(another_identity, df_pl):
    _df = df_pl.pipe(another_identity)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
