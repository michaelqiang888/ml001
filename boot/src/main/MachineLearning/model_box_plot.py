# We can group the monthly data by year and get an idea of the spread of observations for each year and how this may be changing.

# We do expect to see some trend (increasing mean or median), but it may be interesting to see how the rest of the distribution may be changing.

# The example below groups the observations by year and creates one box and whisker plot for each year of observations.
# The last year (1971) only contains 9 months and may not be a useful comparison with the 12 months of observations for other years.
# Therefore, only data between 1964 and 1970 was plotted.

from pandas import Series
from pandas import DataFrame
from pandas import TimeGrouper
from matplotlib import pyplot
series = Series.from_csv('dataset.csv')
groups = series['1964':'1970'].groupby(TimeGrouper('A'))
years = DataFrame()
for name, group in groups:
	years[name.year] = group.values
years.boxplot()
pyplot.show()

# Running the example creates 7 box and whisker plots side-by-side, one for each of the 7 years of selected data.

# Some observations from reviewing the plots include:

# The median values for each year (red line) may show an increasing trend.
# The spread or middle 50% of the data (blue boxes) does appear reasonably stable.
# There are outliers each year (black crosses); these may be the tops or bottoms of the seasonal cycle.
# The last year, 1970, does look different from the trend in prior years