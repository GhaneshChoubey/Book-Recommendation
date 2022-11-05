# GUI -Graphical User Interface

# Liraries
#####################
#1.Tkinter
# 2.PyQt
# 3.Turtle

from tkinter import ttk
import tkinter as ttk
import numpy as np 
from unittest import result

app=ttk.Tk()
app.title("Ghanesh Book recomendation system")
app.geometry('600x400')


ttk.Label(app,text = 'Ghanesh Book recomendation system').place(x=50,y=50)
def recommend(book_name):
    # index fetch
    index = np.where(pt.index==book_name)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])),key=lambda x:x[1],reverse=True)[1:5]
    
    for i in similar_items:
        print(pt.index[i[0]])

ttk.Button(app,text='find Recomendations',font=('Arial',22),command=recommend).place(x=50,y=200)
ttk.Label(app,textvariable=result,font=('Arial',22)).place(x=10,y=300)

app.mainloop