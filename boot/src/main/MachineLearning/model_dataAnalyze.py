
# Running the example provides a number of summary statistics to review.

# Some observations from these statistics include:

# The number of observations (count) matches our expectation, meaning we are handling the data correctly.
# The mean is about 4,641, which we might consider our level in this series.
# The standard deviation (average spread from the mean) is relatively large at 2,486 sales.
# The percentiles along with the standard deviation do suggest a large spread to the data.

# count       94.000000
# mean      4666.010638
# std       2484.748262
# min       1573.000000
# 25%       3049.000000
# 50%       4031.500000
# 75%       5170.250000
# max      13916.000000
# dtype: float64

from pandas import Series
series = Series.from_csv('dataset.csv')
print(series.describe())

# Plot and Analyze
# There may be an increasing trend of sales over time.
# There appears to be systematic seasonality to the sales for each year.
# The seasonal signal appears to be growing over time, suggesting a multiplicative relationship (increasing change).
# There do not appear to be any obvious outliers.
# The seasonality suggests that the series is almost certainly non-stationary.

# There may be benefit in explicitly modeling the seasonal component and removing it.
# You may also explore using differencing with one or two levels in order to make the series stationary.

# The increasing trend or growth in the seasonal component may suggest the use of a log or other power transform.

from pandas import Series
from matplotlib import pyplot
series = Series.from_csv('dataset.csv')
series.plot()
pyplot.show()

