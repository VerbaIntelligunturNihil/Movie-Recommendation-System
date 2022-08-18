#Import needed tools
import pandas as pd

#Create class for EDA
class DataFrame:

    #Point the way to data
    def __init__(self):
        self.credits_df = pd.read_csv("tmdb_credits.csv")
        self.movies_df = pd.read_csv("tmdb_movies.csv")

    #Merge dataframes into one
    def Merge(self):
        movies_df = self.movies_df
        credits_df = self.credits_df
        credits_df.columns = ['id','title','cast','crew']
        df = movies_df.merge(credits_df, on = "id")
        return df
