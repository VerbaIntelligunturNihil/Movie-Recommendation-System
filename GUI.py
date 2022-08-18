#Import needed tools
from tkinter import *
from tkinter import ttk, messagebox
from Recommend import Recommender
import pandas as pd

#Create class for GUI
class WindowsManager:

    def __init__(self, window):

        #ComboBox setting
        movies_df = pd.read_csv("tmdb_movies.csv")
        self.movies_combobox = ttk.Combobox(window)
        self.movies_values = []
        for element in range(0,len(movies_df)):
            self.movies_values.append(movies_df['original_title'][element])
        self.movies_combobox['values'] = sorted(self.movies_values)
        self.movies_combobox.place(x = 10, y = 11, width = 400, height = 25)

        #Combobox bind setting
        self.movies_combobox.bind('<KeyRelease>', self.CheckInput)

        #Button setting
        self.search_movies_button = Button(window, text = "Search")
        self.search_movies_button.place(x = 420, y = 10, width = 50, height = 25)

        #Button bind setting
        self.search_movies_button.bind('<Button-1>', self.SearchMovie)

        #Treeview setting
        columns = ('#1')
        self.movies_recommendation_treeview = ttk.Treeview(window, columns = columns, show = 'headings')
        self.movies_recommendation_treeview.heading('#1', text = "Movies Recommendation")
        self.movies_recommendation_treeview.place(x = 10, y = 45, width = 460, height = 226)

    #Show movie by inputted data
    def CheckInput(self, event):

        #Take information from Combobox
        value = event.widget.get()

        #Search movies in combobox by inputted value
        if value == '':
            self.movies_combobox['values'] = self.movies_values
        else:
            data = []
            for element in self.movies_values:
                if value.lower() in element.lower():
                    data.append(element)

            self.movies_combobox['values'] = data



    #Search movie by name
    def SearchMovie(self, event):

        #Create class for recommend
        r = Recommender()

        #Get top 10 recommendation to the movie
        movies = r.get_recommends(self.movies_combobox.get())

        #Clear treeview
        self.movies_recommendation_treeview.delete(*self.movies_recommendation_treeview.get_children())

        #Check available of the recommendations
        if movies[0] != "":

            #Input data into treeview
            data = []
            for element in movies:
                data.append((element))

            for element in range (0, 10):
                self.movies_recommendation_treeview.insert("","end", iid = element, values = (data[element],))

        else:

            #Show message about error to user
            messagebox.showerror('Error', 'Inputted movie is not in this system')
