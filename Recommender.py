#Import needed tools
from ast import literal_eval
from EDA import DataFrame
from DataProcessing import DataProcessor

#Import data from EDA
df = DataFrame()
movies_df = df.Merge()

#Create class for data processing
dp = DataProcessor()

#Point the features
features = ['cast', 'crew', 'keywords', 'genres']

#Leave needed features
for feature in features:
    movies_df[feature] = movies_df[feature].apply(literal_eval)

#Select director of movie from data
movies_df['director'] = movies_df['crew'].apply(dp.get_director)

#Select features which will been used by function get_list()
features = ['cast', 'keywords', 'genres']

#Use function get_list()
for feature in features:
    movies_df[feature] = movies_df[feature].apply(dp.get_list)

#Select features which will been converted
features = ['cast', 'keywords', 'director', 'genres']

#Use function clean_data()
for feature in features:
    movies_df[feature] = movies_df[feature].apply(dp.clean_data)

#Create vectorizer of needed metadata information
movies_df['vectorizer'] = movies_df.apply(dp.create_vectorizer, axis = 1)

print(movies_df['vectorizer'].head())
