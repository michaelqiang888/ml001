

# We can confirm the assumption that the seasonality is a yearly cycle by eyeballing line plots of the dataset by year.

# The example below takes the 7 full years of data as separate groups and creates one line plot for each.
# The line plots are aligned vertically to help spot any year-to-year pattern.

from pandas import Series
from pandas import DataFrame
from pandas import TimeGrouper
from matplotlib import pyplot
series = Series.from_csv('dataset.csv')
groups = series['1964':'1970'].groupby(TimeGrouper('A'))
years = DataFrame()
pyplot.figure()
i = 1
n_groups = len(groups)
for name, group in groups:
	pyplot.subplot((n_groups*100) + 10 + i)
	i += 1
	pyplot.plot(group)
pyplot.show()
