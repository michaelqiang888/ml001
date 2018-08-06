### load data stock market data
# An Introduction to Stock Market Data Analysis with Python
# obtaining the data from Yahoo! Finance using pandas,
# visualizing stock data, moving averages,
# developing a moving-average crossover strategy, backtesting, and benchmarking.



#Getting Data from Yahoo! Finance with pandas
# The following code create directly a DataFrame object containing stock information.
import pandas as pd
#import pandas.io.data as web  # Package and modules for importing data; this code may change depending on pandas version
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
from pandas_datareader import data
import datetime

# We will look at stock prices over the past year, starting at January 1, 2016
#start = datetime.datetime(2018, 1, 1)
#end = datetime.date.today()

# Let's get Apple stock data; Apple's ticker symbol is AAPL
# First argument is the series we want, second is the source ("yahoo" for Yahoo! Finance), third is the start date, fourth is the end date
#aapl = data.DataReader('AAPL', 'google', '2017-01-01')
ibm = data.DataReader('IBM',  'yahoo', datetime(2000, 1, 1), datetime(2012, 1, 1))

#type(aapl)