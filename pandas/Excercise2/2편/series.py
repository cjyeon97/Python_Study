import pandas as pd
import numpy as np

rng = pd.date_range('1/1/2012', periods=100, freq='S')
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
sumed = ts.resample('5Min').sum()

print(rng)
print(ts)
print(sumed)

print('=========')

rng = pd.date_range('4/12/2020 00:00', periods=5, freq='D')
ts = pd.Series(np.random.randn(len(rng)), rng)
print(ts)

ts_utc = ts.tz_localize('UTC')
print(ts_utc)

print('=========')

other_ts_utc = ts_utc.tz_convert('US/Eastern')
print(other_ts_utc)

print('=========')
rng = pd.date_range('4/12/2020', periods=5, freq='M')
ts = pd.Series(np.random.randn(len(rng)), index=rng)
print(ts)

ps = ts.to_period()
print(ps)

timestamp = ps.to_timestamp()
print(timestamp)

print('=========')
print()
print()

prng = pd.period_range('1990Q1', '2000Q4', freq='Q-NOV')
print(prng)

ts = pd.Series(np.random.randn(len(prng)), prng)
print(ts)

ts.index = (prng.asfreq('M', 'e') + 1).asfreq('H', 's') + 9 # Month +1 증가, Hour +1 증가
print(ts.head())