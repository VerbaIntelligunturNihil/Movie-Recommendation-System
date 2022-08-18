#Import needed tools
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class RecommendationEngineer:

    #Create count vectorizer
    def __init__(self):
        self.count_vectorizer = CountVectorizer(stop_words = "english")

    #Transform vectorizer to matrix
    def transform(self, data):
        count_vectorizer = self.count_vectorizer
        count_matrix = count_vectorizer.fit_transform(data)
        return count_matrix

    #Use cosine similarity to matrix
    def get_cosine_similarity(self, count_matrix):
        cossimilarity = cosine_similarity(count_matrix, count_matrix)
        return cossimilarity

    #Get top 10 recommendation to the movie
    def get_recommendation(self, title, df, indices, cossimilarity):
        index = indices[title]
        similarity_scores = list(enumerate(cossimilarity[index]))
        similarity_scores = sorted(similarity_scores, key = lambda x: x[1], reverse = True)
        similarity_scores = similarity_scores[1:11]

        movies_indices = [element[0] for element in similarity_scores]
        movies = df["original_title"].iloc[movies_indices].values[0:9]
        return movies
