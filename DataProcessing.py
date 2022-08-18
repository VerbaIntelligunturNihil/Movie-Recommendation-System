#Import needed tools
import numpy as np

#Create class for data processing
class DataProcessor:

    #Get movie director
    def get_director(self, data):
        for element in data:
            if element['job'] == "Director":
                return element['name']
        return np.nan

    #Get top 5 elements or the entire list whicever is more
    def get_list(self, data):
        if isinstance(data, list):
            names = [element['name'] for element in data]

            if len(names) > 5:
                names = names[:5]

            return names

        return []

    #Convert features into lowercase and remove all spaces between them
    def clean_data(self, row):
        if isinstance(row, list):
            return [str.lower(element.replace(" ","")) for element in row]
        else:
            if isinstance(row, str):
                return str.lower(row.replace(" ",""))
            else:
                return ""

    #Extract metadata information to input into the vectorizer
    def create_vectorizer(self, features):
        return (" ".join(features['keywords']) + " " +
               " ".join(features['cast']) + " " +
               " ".join(features['director']) + " " +
               " ".join(features['genres']))
