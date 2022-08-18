#Import needed tools
from Recommend import Recommender

#Input name of movie
name = input()

#Create class for recommend
r = Recommender()

#Get top 10 recommendation to the movie
movies = r.get_recommends(name)

#Show movies recommend to user
print("\n".join(movies))
