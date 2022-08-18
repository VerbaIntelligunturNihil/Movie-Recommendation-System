#Import needed tools
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class RecommendationEngineer:

    #Create count vectorizer
    def __init__(self):
        self.count_vectorizer = CountVectorizer(stop_words = "english")

    #Transform vectorizer to matrix
    def transform(self,data):
        count_vectorizer = self.count_vectorizer
        count_matrix = count_vectorizer.fit_transform(data)
        return count_matrix

    #Use cosine similarity to matrix
    def get_cosine_similarity(self,count_matrix):
        cossimilarity = cosine_similarity(count_matrix, count_matrix)
        return cossimilarity
