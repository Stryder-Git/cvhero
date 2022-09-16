import pytest

import cvhero
import pandas as pd
from pandas.testing import assert_series_equal, assert_frame_equal

series_formats = [
    (
        pd.Series(range(5)),

     "pd.Series(range(0, 5, 1),index= pd.Index(range(0, 5, 1)))"
     ),

    (
        pd.Series(['2022-06-01 13:31:00+00:00', '2022-06-02 13:30:00+00:00', '2022-06-03 13:30:00+00:00'],
               index= pd.DatetimeIndex(['2022-06-01', '2022-06-02', '2022-06-03']),
               dtype= 'datetime64[ns, UTC]'),

     "pd.Series(['2022-06-01 13:30:00', '2022-06-02 13:30:00', '2022-06-03 13:30:00'],"
     "index= pd.DatetimeIndex(['2022-06-01', '2022-06-02', '2022-06-03']),"
     "dtype= 'datetime64[ns]').dt.tz_localize('UTC')"
     )
]

@pytest.mark.parametrize("series, formatted", series_formats)
def test_format_series(series, formatted):

    calced = cvhero.format(series)
    print(calced)
    assert calced == formatted
    assert_series_equal(eval(calced), series)


df_formats = [
    (
        pd.DataFrame([[0, 1, 2], [3, 4, 5]], columns= list("ABC"), index= list("ab")),
        """pd.DataFrame({
'A': pd.Series(range(0, 4, 3)), 
'B': pd.Series(range(1, 5, 3)), 
'C': pd.Series(range(2, 6, 3))
}).set_index(pd.Index(['a', 'b']))"""

     )

]

@pytest.mark.parametrize("df, formatted", df_formats)
def test_format_dataframe(df, formatted):

    calced = cvhero.format(df)
    print(calced)
    assert calced == formatted
    assert_frame_equal(eval(calced), df)






