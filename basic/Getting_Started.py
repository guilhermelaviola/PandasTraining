# Getting started with Pandas
import pandas as pd

# Reading the .csv file
imdb_ratings = pd.read_csv("../data/imdb-10-star-ratings.csv")

# Displaying the dataframe (the first and last 10)
print(imdb_ratings.head(10))
print(imdb_ratings.tail(10))

# Exporting dataframe to Excel
#Imdb_Ratings.to_excel("ImdbRatings.xlsx", sheet_name="movies", index=false)

# Displaying datatypes from the dataframe (or dataset)
print(imdb_ratings.dtypes)

# Technical summary
print(imdb_ratings.info())

# Creating a variable to store the 'Release Date' column only
Release_Date = imdb_ratings["Release Date"]

# Displaying the first 5 rows of the 'Release Date' column
print(imdb_ratings.head(5))

# Checking the type of the data stored in column selected above
print(type(imdb_ratings["Release Date"]))

# Checking and displaying the shape of the dataframe (number of rows x columns)
print(imdb_ratings["Release Date"].shape)

# Selecting and displaying two different columns from the table
both_ratings = imdb_ratings[["Your Rating", "IMDb Rating"]]
print(both_ratings)

# Checking and displaying the shape of the two selected columns above
print("Shape: ", both_ratings.shape)

# Filtering and displaying ratings above 7
ratings_above_7 = imdb_ratings["Your Rating"] > 7
print(ratings_above_7)

# Displaying the shape of the filtered selection above
print("Shape: ", ratings_above_7.shape)

# Filtering movies released in 1990 and 1991 and printing the first 20 rows
released_in_1990_1991 = imdb_ratings["Year"].isin([1990, 1991])
# Would be the same thing as...
# released_in_1990_1991 = (imdb_ratings["Year"] == 1990) | (imdb_ratings["Year"] == 1991)
print(released_in_1990_1991.head(20))

# Selecting and displaying release years which are not numbers and its shape
year_nan = imdb_ratings["Year"].notna()
print(year_nan.head())
print(year_nan.shape)

# Selecting and displaying the most popular movies from the dataframe (the ones with over 100k ratings)
most_popular_movies = imdb_ratings["Num Votes"] > 100000, "Title"
print(most_popular_movies)

# Displaying a table with rows from 100 to 114 and columns from 1 to 4 with data from the dataframe using iloc
print(imdb_ratings.iloc[100:115, 1:4])