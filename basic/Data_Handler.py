# Getting started with Pandas. It's a very simple data handler example
import pandas as pd

# Creating a dataframe with rows, columns and assigning some values to it
actors = pd.DataFrame(
    {
        "Name": [
            "Sylvester Stallone",
            "Denzel Washington",
            "Harrison Ford",
        ],
        "YearOfBirth": [1946, 1954, 1945],
        "Sex": ["Male", "Male", "Male"],
    }
)

# Displaying the actors age columns only
ages = pd.Series([22, 34, 15])

# Displaying the dataframe 'actors' and the series 'ages'
print(actors)
print(ages)

# Displaying the youngest actor, based on the year he was born
print(actors["YearOfBirth"].max())
print(ages.max())

# The describe() method provides a quick overview of the numerical data in a DataFrame.
print(actors.describe())