# Working with derived data, for example: new columns based on data from other columns,
# changing columns names, text style, etc...
import pandas as pd

# Reading the .csv file
imdb_ratings = pd.read_csv("../data/imdb-10-star-ratings.csv", index_col=0, parse_dates=True)

# Generating a new column based on data from existing columns
imdb_ratings["Rating Comparison"] = (
        imdb_ratings["Your Rating"] - imdb_ratings["IMDb Rating"]
)

# Renaming columns
imdb_ratings_renamed = imdb_ratings.rename(
    columns={
        "Your Rating": "My Ratings",
        "Directors": "Director(s)",
        "Num Votes": "N° of Votes",
    }
)

# Changing the column names from lower to uppercase
imdb_ratings_uppercase = imdb_ratings.rename(columns=str.upper)

# Displaying the results (the tables with renamed columns and uppercase columns)
print(imdb_ratings_renamed)
print(imdb_ratings_uppercase)