# a dataset which consists information about the location of the house , price and other aspects such as square feet etc.
#
# import library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from seaborn import utils
import mpl_toolkits




data = pd.read_csv("~/datascience/house-price-prediction/kc_house_data.csv")

# use print could print out the data frame
print(data.head())
print(data.describe())


# Come up with x and y
x = np.arange(0, 5, 0.1)
y = np.sin(x)

# Just print x and y for fun
print (x)
print (y)

# Plot the x and y and you are supposed to see a sine curve
plt.plot(x, y)

# Without the line below, the figure won't show
# however, when use plt show, it will pop up a block window
plt.show()


# what is the most common house
data['bedrooms'].value_counts().plot(kind='bar')
#sns.dispine()