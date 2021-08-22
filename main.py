from tkinter import *
import tkinter as tk
import pandas as pd
import CSV

main=Tk()
main.title("Marksheet")
main.geometry("500x300")
main.config(highlightbackground="black",highlightthickness=2)      

font = ('Trebuchet MS', 11)
            
def submit():
    search_RollNo=RollNo.get()     
    Name.configure(state=tk.NORMAL)
    Maths.configure(state=tk.NORMAL)
    Physics.configure(state=tk.NORMAL)
    Chemistry.configure(state=tk.NORMAL)
    Average.configure(state=tk.NORMAL)
            
    Name.delete(0, 'end')     
    Maths.delete(0, 'end')
    Physics.delete(0, 'end')
    Chemistry.delete(0, 'end')
    Average.delete(0, 'end')
            
    data = []     
    with open('marksheet.csv') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                data.append(row)
    col = [x[0] for x in data]      
            
    if search_RollNo in col:
        for x in range(0,len(data)):  
            if search_RollNo == data[x][0]:
                Name.insert(0, data[x][1])
                Maths.insert(0, data[x][2])
                Physics.insert(0, data[x][3])
                Chemistry.insert(0, data[x][4])
                Average.insert(0, int(data[x][2])+int(data[x][3])+int(data[x][4])/3)
            
                Name.configure(state=tk.DISABLED)    
                Maths.configure(state=tk.DISABLED)   
                Physics.configure(state=tk.DISABLED)   
                Chemistry.configure(state=tk.DISABLED)  
                Average.configure(state=tk.DISABLED)
            
frame1 = LabelFrame(main, text = 'Result').pack(expand = 'yes', fill = 'both')frame1 = LabelFrame(main, text = 'Result').pack(expand = 'yes', fill = 'both')
Label(frame1, text = 'Marksheet',font = ('Book Antiqua', 16)).place(x =190, y = 20)
Label(frame1,text="RollNo:", font = font ).place(x=50,y=80)
Label(frame1,text="Name", font = font ).place(x=50,y=120)
Label(frame1,text="Maths", font = font ).place(x=50,y=150)
Label(frame1,text="Physics", font = font ).place(x=50,y=180)
Label(frame1,text="Chemistry", font = font ).place(x=50,y=210)
Label(frame1,text="Average", font = font ).place(x=50,y=250)
            
RollNo =Entry(frame1)     
RollNo.place(x=210,y=80)

Name =Entry(frame1)     
Name.place(x=210,y=120)
            
Maths =Entry(frame1)     
Maths.place(x=210,y=150)
     
Physics =Entry(frame1)     
Physics.place(x=210,y=180)
            
Chemistry =Entry(frame1)     
Chemistry.place(x=210,y=210)
            
Average =Entry(frame1)     
Average.place(x=210,y=250)
