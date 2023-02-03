# Working with statistics
import pandas as pd

# Reading the .csv file
imdb_ratings = pd.read_csv("../data/imdb-10-star-ratings.csv", index_col=0, parse_dates=True)

# Calculating and displaying the user rating average
user_rating_mean = imdb_ratings["Your Rating"].mean()
print(user_rating_mean)

# Calculating and displaying the user rating and IMDb rating median
both_rating_mean = imdb_ratings[["Your Rating", "IMDb Rating"]].median()
print(both_rating_mean)

# Aggregating statistics and displaying them
aggregating_stats = imdb_ratings.describe()
print(aggregating_stats)

# Specific combinations
specific_agg = imdb_ratings.agg(
    {
        "Your Rating": ["min", "max", "mean", "median", "skew"],
        "IMDb Rating": ["min", "max", "mean", "median"]
    }
)

# Displaying the specific combinations
print(specific_agg)

# Grouping and displaying user rating mean by year of release
# mean_by_year = imdb_ratings[["Year", "Your Rating"]].groupby("Year").mean()
# or
mean_by_year = imdb_ratings.groupby("Year")["Your Rating"].mean()
print(mean_by_year)

# Grouping and displaying user rating mean by year of release and genres
mean_by_year_and_genres = imdb_ratings.groupby(["Year", "Genres"])["Your Rating"].mean()
print(mean_by_year_and_genres)

# Counting and displaying the number of observations for each year of release present in the dataframe
#year_count = imdb_ratings.groupby("Year")["Year"].count()
# or
year_count = imdb_ratings["Year"].value_counts()
print(year_count)