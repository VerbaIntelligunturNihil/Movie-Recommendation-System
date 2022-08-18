#Import libraries
import pandas as pd

#Point the way to data
credits_df = pd.read_csv("tmdb_credits.csv")
movies_df = pd.read_csv("tmdb_movies.csv")

#Merge dataframes into one
credits_df.columns = ['id','title','cast','crew']
movies_df = movies_df.merge(credits_df, on = "id")
