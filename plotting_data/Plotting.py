# A few examples of how to plot data with Pandas and Matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Reading the .csv file and displaying the first 10 rows
imdb_ratings = pd.read_csv("../data/imdb-10-star-ratings.csv", index_col=0, parse_dates=True)
print(imdb_ratings.head(10))

# Plotting all columns with bar and box graphs
#imdb_ratings.plot()
#imdb_ratings.plot.box()
#plt.show()

# Plotting 'Your Rating' column with bars
#imdb_ratings["Your Rating"].plot()
#plt.show()

# Plotting 'Your Rating' x 'IMDb Rating' with scatter graph
#imdb_ratings.plot.scatter(x="Your Rating", y="IMDb Rating", alpha=0.5)
#plt.show()

# Separated plots for each column
imdb_ratings.plot.area(figsize=(10,4), subplots=True)
plt.show()