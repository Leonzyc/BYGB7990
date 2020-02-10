# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 08:18:13 2019

@author: 11319
"""

import pandas as pd
import numpy as py
import matplotlib.pyplot as plt
import re
data=pd.read_csv("Students.txt",sep="\t")

instruction=("""Welcome to student system. Enter \"1,2,3,4,5,6\" to excute:
1. Display all student records
2. Display students whose last name begins with a certain string (case insensitive)
3. Display all records for students whose graduating year is a certain year
4. Display a summary report of number and percent of students in each program, for students graduating on/after a certain year
5. Quit
6. Show instruction
      """)
print(instruction)

while True:
    order=str(input("Please enter the order: ")).lower()
    year=set()
    for i in data.GradYear:
        year.add(i)
    if order=="1":
    # Find all data    
        print(data)
    elif order=="2":
    #  Find name
        Name=str(input("please input last name with a certain string: "))
        if len(Name)>1:
            Name=(Name[0].upper()+Name[1:].lower()).replace(" ","")
        else:
            Name=Name.upper()
        if True in list(data.Last.str.contains(Name)):
            print(data[data.Last.str.contains(Name)])
        else:
            print("No record")
    elif order=="3":
    # Find year
        Grad_year=int(input("Please enter the year you want to check: "))
        if Grad_year in year:
                print(data[data.GradYear==Grad_year])
        else:
                print("No record found")
    elif order=="4":
    #Summary report2
        Year=int(input("Please enter the year you want to check: "))
        if Year in year:
            frame1=pd.DataFrame(data[data.GradYear==Year].DegreeProgram.value_counts(normalize=True))
            frame1.columns=["Frequency"]
            frame1["Frequency"] = frame1["Frequency"].apply(lambda x: format(x, '.2%'))#Turn to percentage
            frame2=pd.DataFrame(data[data.GradYear==Year].DegreeProgram.value_counts())
            frame2.columns=["Number"]
            frame = frame1.join(frame2)
            print(frame)
        #Additional Function Chart
            chart=str(input("Do you want to see pie chart?(Y/N)")).upper()
            if chart=="Y":
                labels = list(frame.index)
                sizes = list(frame["Number"])
                plt.pie(sizes, labels=labels, autopct='%1.1f%%')
                plt.title('Pie Chart')
                plt.axis('equal')
                plt.show()
        else:
            print("Wrong year")
    elif order=="5":
        break
    elif order=="6":
        print(instruction)
    else:
        print("Worng order. Enter 6 to see all instruction.")