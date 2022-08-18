#Import needed tools
from tkinter import *
from GUI import WindowsManager

#Window setting
window = Tk()
w = WindowsManager(window)
window.title("Movie Recommendation System")
window.geometry("480x281")
window.resizable(False,False)
window.mainloop()
