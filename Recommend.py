#Import needed tools
from ast import literal_eval
from EDA import DataFrame
from DataProcessing import DataProcessor
from RecommendationEngine import RecommendationEngineer

#Create class for movies recommend
class Recommender:

    def __init__(self):

        #Create class for EDA
        self.df = DataFrame()
        self.movies_df = self.df.merge()

        #Create class for data processing
        self.dp = DataProcessor()

        #Create class for recommendation engine
        self.re = RecommendationEngineer()

    #Get top 10 recommendation to the movie
    def get_recommends(self,name):

        movies = self.movies_df

        #Point the features
        features = ['cast', 'crew', 'keywords', 'genres']

        #Leave needed features
        for feature in features:
            movies[feature] = movies[feature].apply(literal_eval)

        #Select director of movie from data
        movies['director'] = movies['crew'].apply(self.dp.get_director)

        #Select features which will been used by function get_list()
        features = ['cast', 'keywords', 'genres']

        #Use function get_list()
        for feature in features:
            movies[feature] = movies[feature].apply(self.dp.get_list)

        #Select features which will been converted
        features = ['cast', 'keywords', 'director', 'genres']

        #Use function clean_data()
        for feature in features:
            movies[feature] = movies[feature].apply(self.dp.clean_data)

        #Create vectorizer of needed metadata information
        movies['vectorizer'] = movies.apply(self.dp.create_vectorizer, axis = 1)

        #Transform vectorizer to matrix
        count_matrix = self.re.transform(movies['vectorizer'])
        cossimilarity = self.re.get_cosine_similarity(count_matrix)

        #Reset the indices of dataframe
        indices = self.df.reset_indices(movies)

        recommends = self.re.get_recommendation(name, movies, indices, cossimilarity)
        

        return recommends
