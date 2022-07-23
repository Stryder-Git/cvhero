import pytest

import cvhero as cv
import pandas as pd
import numpy as np
from pandas.testing import assert_series_equal, assert_frame_equal
"""
dtypes
value conversions
    object
    int * 
    float
    bool
    datetime * 
        with tz
        without tz
    timedelta *
    category

* 2 with/without nan

* 2
    index/series

"""
S = pd.Series
TD = pd.Timedelta

values = [
    # int
    (S(range(5)), "range(0, 5, 1)"),
    (S([3, 4, 5, 6]), "range(3, 7, 1)"),
    (S([5, 10, 15, 20]), "range(5, 25, 5)"),
    (S([1, 3, 6, 9]), "[1, 3, 6, 9]"),

    #float
    (S([1.1, -2.3, 15.6, np.nan]), "[1.1, -2.3, 15.6, np.nan]"),
    (S([1, 2, np.nan, 3]), "[1.0, 2.0, np.nan, 3.0]"), # with nan always float

    #bool
    (S([True, np.nan, False]), "[True, np.nan, False]"),

    #datetime with tz
    (S(['2022-06-01 13:30:00+00:00', np.nan, '2022-06-03 13:30:00+00:00'],
       dtype= "datetime64[ns, UTC]"), "['2022-06-01 13:30:00', np.nan, '2022-06-03 13:30:00']"),
     #without tz
    (S(['2022-06-01 13:30:00', np.nan, '2022-06-03 13:30:00'],
       dtype= "datetime64[ns]"), "['2022-06-01 13:30:00', np.nan, '2022-06-03 13:30:00']"),

    #timedelta
     (S([TD("1D"), TD("1.5D"), np.nan, TD("2H")]), "['1 days 00:00:00', '1 days 12:00:00', np.nan, '0 days 02:00:00']")
]
@pytest.mark.parametrize("values, expected", values)
def test_convert(values, expected):

    calced, _ = cv.pandas_printer._convert(values)
    assert calced == expected


series_formats = [
    (
        pd.Series(range(5)),
        "pd.Series(range(0, 5, 1),index= pd.Index(range(0, 5, 1)))"
     ),

    (
        pd.Series(['2022-06-01 13:30:00+00:00', '2022-06-02 13:30:00+00:00', '2022-06-03 13:30:00+00:00'],
               index= pd.DatetimeIndex(['2022-06-01', '2022-06-02', '2022-06-03']),
               dtype= 'datetime64[ns, UTC]'),
        "pd.Series(['2022-06-01 13:30:00', '2022-06-02 13:30:00', '2022-06-03 13:30:00'],"
        "index= pd.DatetimeIndex(['2022-06-01', '2022-06-02', '2022-06-03']),"
        "dtype= 'datetime64[ns]').dt.tz_localize('UTC')"
     ),
    (
        pd.Series(['2022-06-01 13:30:00+00:00', np.nan, '2022-06-03 13:30:00+00:00'],
               index= pd.DatetimeIndex(['2022-06-01', '2022-06-02', '2022-06-03']),
               dtype= 'datetime64[ns, UTC]'),
        "pd.Series(['2022-06-01 13:30:00', np.nan, '2022-06-03 13:30:00'],"
        "index= pd.DatetimeIndex(['2022-06-01', '2022-06-02', '2022-06-03']),"
        "dtype= 'datetime64[ns]').dt.tz_localize('UTC')"
    ),
(
        pd.Series(['2022-06-01 13:30:00+00:00', np.nan, '2022-06-03 13:30:00+00:00'],
               index= pd.DatetimeIndex(['2022-06-01', '2022-06-02', '2022-06-03'], tz="America/New_York"),
               dtype= 'datetime64[ns, UTC]'),
        "pd.Series(['2022-06-01 13:30:00', np.nan, '2022-06-03 13:30:00'],"
        "index= pd.DatetimeIndex(['2022-06-01', '2022-06-02', '2022-06-03'],tz= 'America/New_York'),"
        "dtype= 'datetime64[ns]').dt.tz_localize('UTC')"
    )
]

@pytest.mark.parametrize("series, formatted", series_formats)
def test_format_series(series, formatted):

    calced = cv.format(series)
    print(calced)
    assert calced == formatted
    assert_series_equal(eval(calced), series)


df_formats = [
    (
        pd.DataFrame([[0, 1, 2], [3, 4, 5]], columns= list("ABC"), index= list("ab")),
        """pd.DataFrame({
'A': pd.Series(range(0, 6, 3)), 
'B': pd.Series(range(1, 7, 3)), 
'C': pd.Series(range(2, 8, 3))
}).set_index(pd.Index(['a', 'b']))"""

     ),
    (
        pd.DataFrame([[0, 1, 2], [3, np.nan, 5]], columns= list("ABC"), index= list("ab")),
        """pd.DataFrame({
'A': pd.Series(range(0, 6, 3)), 
'B': pd.Series([1.0, np.nan]), 
'C': pd.Series(range(2, 8, 3))
}).set_index(pd.Index(['a', 'b']))""")
]

@pytest.mark.parametrize("df, formatted", df_formats)
def test_format_dataframe(df, formatted):

    calced = cv.format(df)
    assert calced == formatted
    assert_frame_equal(eval(calced), df)






