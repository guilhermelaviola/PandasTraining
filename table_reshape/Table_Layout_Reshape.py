# Reshaping dataframes
import pandas as pd

# importing the data source
from matplotlib.pyplot import margins
from numpy.distutils.system_info import agg2_info

# Reading data from two different sources (.csv files)
imdb_ratings = pd.read_csv("../data/imdb-10-star-ratings.csv", index_col=0, parse_dates=True)

# Sorting the first 10 values by release date and displaying them
sorted_values = imdb_ratings.sort_values(by="Release Date").head(10)
print(sorted_values)

# Sorting the first 10 values by release date and director in descending order and displaying them
sorted_values_asc = imdb_ratings.sort_values(by=["Release Date", "Directors"], ascending=False).head(10)
print(sorted_values_asc)

# Long to wide table format
# Filtering Martin Scorsese movies from the data set
scorsese_movies = imdb_ratings[imdb_ratings["Directors"] == "Martin Scorsese"]

# Filtering Martin Scorsese movies from the data set. sorting the list by year of release
# and displaying the first 2 rows
scorsese_movies_subset = scorsese_movies.sort_index().groupby(["Year"]).head()

# Displaying both results of thw code presented above
print(scorsese_movies.head(5), scorsese_movies_subset)

# Sorting the values for the different user ratings as separate columns next to each other
# and displaying the results
pivot_subset = scorsese_movies_subset.pivot(columns="Your Rating", values="IMDb Rating")
print(pivot_subset)
scorsese_movies.head()

# Associating and plotting the different time series at the same time
#scorsese_movies.pivot(columns="Your Rating", values="IMDb Rating").plot()

#plt.show()

# I want the mean user ratings for each genres in table form.
reshape = imdb_ratings.pivot_table(
    values="IMDb Rating",
    index="Genres",
    columns="Your Rating",
    aggfunc="mean",
    margins=True,
)

print(reshape)