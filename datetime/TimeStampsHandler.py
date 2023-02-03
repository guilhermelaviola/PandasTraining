# Handling datetime with Pandas
import pandas as pd
import matplotlib.pyplot as plt

# Importing the data source
# Here the dates will be automatically converted from plain text into
# timestamp objects, so we can use its functions
movie_list = pd.read_csv("../data/Movie-list.csv", parse_dates=True)

# Renaming column and displaying the first 10 movies with the new change
movie_list = movie_list.rename(columns={"Date Added": "Datetime"})
movie_list_display = movie_list.head(10)
print(movie_list_display)

# Finding and displaying the unique values from the column 'Year'
unique_year = movie_list.Year.unique()
print(unique_year)

# Handling time series data with ease
# Using pandas datetime properties
# Converting the values of the columns 'Created' into datetime objects
movie_list["Created"] = pd.to_datetime(movie_list["Created"])

# Displaying the columns 'Created', the first and last row and the oldest and most recent date
print(movie_list["Created"])
print("The first movie of the list was added in", movie_list["Created"].min(),
      "and the last movie was added in:", movie_list["Created"].max())
print("Length of our time series (in days):", movie_list["Created"].max() - movie_list["Created"].min())

# Adding a new column called 'Month Added', to represent the month the movie was added into the list
# and displaying the first 10 rows after this change
movie_list["Month Added"] = movie_list["Created"].dt.month
print(movie_list.head(10))

# What is the average 7 rating for each day of the week for each of the genres?
# Remember the split-apply-combine pattern!
avg_rating_by_week = movie_list.groupby([movie_list["Created"].dt.weekday, "Genres"])["IMDb Rating"].mean()

# Displaying the result
print(avg_rating_by_week)

#
fig, axs = plt.subplots(figsize=(10, 6))
movie_list.groupby(movie_list["Created"].dt.day)["IMDb Rating"].mean().plot(
      kind="bar", rot=0, ax=axs
)

plt.xlabel("X label")
plt.ylabel("Y label")

plt.show()

#ratings = movie_list.pivot(index="Created", columns="Your Rating", values="IMDb Rating")

#ratings_display = ratings.head()

#print(ratings_display)

