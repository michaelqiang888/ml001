# Reviewing plots of the density of observations can provide further insight into the structure of the data.

# The example below creates a histogram and density plot of the observations without any temporal structure.

from pandas import Series
from matplotlib import pyplot
series = Series.from_csv('dataset.csv')
pyplot.figure(1)
pyplot.subplot(211)
series.hist()
pyplot.subplot(212)
series.plot(kind='kde')
pyplot.show()