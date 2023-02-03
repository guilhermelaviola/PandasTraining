# Combining (or concatenating) data
import pandas as pd

# Reading data from two different sources (.csv files)
movie_list = pd.read_csv("../data/Movie-list.csv", parse_dates=True)
underrated_movies = pd.read_csv("../data/Underrated.csv", parse_dates=True)

# Configuring the table to display only certain columns. In the exaple below, only the three mentioned
#movie_list = movie_list[["Position", "Created", "Title"]]

# Displaying the first 10 movies from the first list and the first 5 from the second
movie_list.head(10)
underrated_movies.head(5)

# Combining the data from both tables
all_movies = pd.concat([movie_list, underrated_movies], axis=0)

# Checking table shapes for all tables: the first, the second and the aggregated table
print("``movie_list`` table shape: ", movie_list.shape)
print("``underrated_movies`` table shape: ", underrated_movies.shape)
print("``all_movies`` table shape: ", all_movies.shape)

# Sorting the values of the aggregate table by 'Date Rated' and displaying the first 15 movies
all_movies = all_movies.sort_values("Date Rated")
all_movies_display = all_movies.head(15)
print(all_movies_display)

# Combining the data from both tables, separating the data from both sources by keys and displaying
# the first 10 movies of the concatenated list
all_movies = pd.concat([movie_list, underrated_movies], keys=["Position"])
all_movies_display = all_movies.head(10)
print(all_movies_display)

# The function reset_index can be used to convert any level of an index to a column
# all_movies.reset_index(level=0)

# Multiple tables can be concatenated both column-wise and row-wise using the concat function.
# For database-like merging/joining of tables, use the merge function.