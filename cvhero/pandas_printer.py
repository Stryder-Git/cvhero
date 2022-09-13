
import numpy as np
import pandas as pd
pdtypes = pd.api.types

pandas_prefix = "pd"
prettier = "\n"

def _pref():
    if pandas_prefix:
        return pandas_prefix + "."
    else:
        return ""


def _dt(s):
    try: return s.dt
    except AttributeError: return s


def _values(s):
    try: return s.values
    except AttributeError: return s


def _strtostr(s):
    return "'" + s + "'"


def _convert(values):
    dtype = str(values.dtype)
    tz = None
    if dtype.startswith("datetime64"):
        if dtype != "datetime64[ns]":
            tz = str(_dt(values).tz)
            tz = _strtostr(tz)
            values = _dt(values).tz_localize(None)
        values = values.astype("string")

    elif dtype == "timedelta64[ns]":
        values = values.astype("string")
        return _pref() + "TimedeltaIndex(" + str(list(values)) + ")", tz

    elif dtype.startswith("int"):
        values = _values(values)
        diffs = np.diff(values)
        if (diffs >= 0).all():
            diffs = np.unique(diffs)
            if diffs.shape[0] == 1:
                start = values[0]
                stop = values[-1] + 1
                step = diffs[0]
                return f"range({start}, {stop}, {step})", tz

    values = str(list(values))
    return values, tz


def format_index(index):
    dtype = str(index.dtype)

    if dtype.startswith("datetime64"):
        f = _pref() + "DatetimeIndex("
        values, tz = _convert(index)
        f += values
        if not tz is None: f += ",tz= " + tz
        return f + ")"

    if dtype == "timedelta64[ns]":
        return _convert(index)[0]

    f = _pref() + "Index("
    values, _ = _convert(index)
    return f + values + ")"


def format_series(series, ignore_index= False):
    f = _pref() + "Series("
    vals, tz = _convert(series)
    f += vals
    if not ignore_index:
        f += ",index= " + format_index(series.index)

    dtype = series.dtype
    if str(dtype).startswith("datetime64"):
        f += ",dtype= 'datetime64[ns]'"

    elif pdtypes.is_string_dtype(dtype) and not pdtypes.is_object_dtype(dtype):
        f += ",dtype= 'string'"

    f += ")"
    if tz is None: return f
    return f + ".dt.tz_localize(" + tz + ")"


def format_dataframe(df, ignore_index= False):
    f = _pref() + "DataFrame("

    f += "{" + prettier
    for col in df:
        if isinstance(col, str): f += _strtostr(col)
        else: f += str(col)
        f += ": "
        f += format_series(df[col], ignore_index= True)
        f += ", " + prettier

    f = f[:- (len(prettier) + 2)] + prettier + "})"
    if ignore_index: return f

    f += ".set_index(" + format_index(df.index) + ")"
    return f


def format_pandas(obj):
    if isinstance(obj, pd.DataFrame):
        return format_dataframe(obj)

    elif isinstance(obj, pd.Series):
        return format_series(obj)

    elif isinstance(obj, pd.Index):
        return format_index(obj)

    else:
        raise ValueError("Only pd.DataFrame, -Series, and -Index are currently supported")

def pandas_to_str(obj):
    return str(obj)
        
        
#
# pd.DataFrame({
# 	'bl': pd.Series([True, False, True]),
# 	'dr': pd.Series(['2000-01-01', '2000-01-02', '2000-01-03'],dtype= 'datetime64[ns]'),
# 	'drtz': pd.Series(['2000-01-01', '2000-01-02', '2000-01-03'],dtype= 'datetime64[ns]').dt.tz_localize('Asia/Ulaanbaatar'),
# 	'floats': pd.Series([1.0, 2.0, 3.0]),
# 	'ints': pd.Series(range(1, 4, 1)),
# 	'rints': pd.Series([2, 1, 4]),
# 	'obj': pd.Series([1, 2, 'e']),
# 	's': pd.Series(['a', 'n', 'c'],dtype= 'string'),
# 	'tds': pd.Series(pd.TimedeltaIndex(['0 days 00:01:00', '1 days 00:00:00', '7 days 00:00:00']))
# 	}).set_index(pd.Index(['a', 'b', 'c']))
#
#
# # from console
#
# import pandas as pd
# obj = pd.Series([1, 2, "e"])
# ints = pd.Series([1, 2, 3])
# floats = ints.astype("float")
# dr = pd.Series(pd.date_range("2000-01-01", "2000-01-03"))
# drtz = dr.dt.tz_localize("Asia/Ulaanbaatar")
# bl = pd.Series([True, False, True])
# s = pd.Series(list("anc"))
# s = s.astype("string")
# tds = pd.Series([pd.Timedelta("1T"), pd.Timedelta("1D"), pd.Timedelta("7D")])
# rints = pd.Series([2, 1, 4])
# all_ = dict(bl= bl, dr = dr, drtz = drtz, floats= floats, ints= ints, rints= rints, obj = obj, s = s, tds=tds)
# df = pd.DataFrame(all_).set_index(iter("abc"))
