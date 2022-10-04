from cProfile import label
import tkinter as tk
from tkinter import *
from tkinter import ttk
from unicodedata import decimal
import csv
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import statistics
from setuptools import Command


def getYearData(year, data_type, value_type):
    filename = 'FinallOneCSV.csv'
    with open(filename, 'r') as csvfile:
        datareader = csv.reader(csvfile)
        yearData = []
        for row in datareader:
            if row[0].find('Average'+str(year)) != -1:
                if(data_type == 'temperature'):
                    if(value_type == 'Maximum'):
                        yearData.append(float(row[2]))
                    elif(value_type == 'Average'):
                        yearData.append(float(row[3]))
                    elif(value_type == 'Minimum'):
                        yearData.append(float(row[4]))
                elif(data_type == 'DewPoint'):
                    if(value_type == 'Maximum'):
                        yearData.append(float(row[5]))
                    elif(value_type == 'Average'):
                        yearData.append(float(row[6]))
                    elif(value_type == 'Minimum'):
                        yearData.append(float(row[7]))
                elif(data_type == 'Humidity'):
                    if(value_type == 'Maximum'):
                        yearData.append(float(row[8]))
                    elif(value_type == 'Average'):
                        yearData.append(float(row[9]))
                    elif(value_type == 'Minimum'):
                        yearData.append(float(row[10]))
                elif(data_type == 'WindSpeed'):
                    if(value_type == 'Maximum'):
                        yearData.append(float(row[11]))
                    elif(value_type == 'Average'):
                        yearData.append(float(row[12]))
                    elif(value_type == 'Minimum'):
                        yearData.append(float(row[13]))
                elif(data_type == 'Pressure'):
                    if(value_type == 'Maximum'):
                        yearData.append(float(row[14]))
                    elif(value_type == 'Average'):
                        yearData.append(float(row[15]))
                    elif(value_type == 'Minimum'):
                        yearData.append(float(row[16]))
    return yearData
def makePlot( year_a, data_type, value_type):

    year_a_data = getYearData(year_a, data_type, value_type)
    
    month_labels =['January','February','March','April' ,'May','June','July','August','September','October','November','December']
    plt.figure(figsize=(12,5))

    plt.plot(month_labels,year_a_data, '-ok',color='green',linestyle='dashed',markerfacecolor='green')
    plt.grid(axis= 'y')
    plt.title(str(year_a))
    plt.xlabel('Month')
    plt.ylabel(data_type + " " + value_type)
    plt.show()
   
def maketwoPlots( year_a, year_b, data_type, value_type):

    year_a_data = getYearData(year_a, data_type, value_type)
    year_b_data = getYearData(year_b, data_type, value_type)

    month_labels =['January','February','March','April' ,'May','June','July','August','September','October','November','December']
    plt.figure(figsize=(12,5))

    plt.plot(month_labels,year_a_data, '-ok',color='green',linestyle='dashed',markerfacecolor='green')
    plt.plot(month_labels,year_b_data, '-ok',color='blue',linestyle='dashed',markerfacecolor='blue')
    plt.grid(axis= 'y')
    plt.title(str(year_a) + " - " + str(year_b))
    plt.xlabel('Month')
    plt.ylabel(data_type + " " + value_type)
    plt.show()

#Create Intro Menu
start = Tk()
start.title("Climate and Weather Team 20")
start.configure(background="aqua")

#App placement
app_width = 500
app_height = 350

screen_width = start.winfo_screenwidth()
screen_height = start.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

start.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

#Creates Headline for Intro
start1 = ttk.Label(start, text = "\u0332".join("Liverpool's Weather and Climate"),
          background = 'aqua', foreground ="black",
          font = ("Times New Roman", 15))
start1.place(x = 135, y = 10)

start2 = ttk.Label(start, text = "This system is designed to provide data on the weather and climate in Liverpool." 
+ "\r\n" +
"This was designed and created by:"
+ "\r\n" +
"- Ryan Hacine-Bacha"
+ "\r\n" +
"- Bogdan-Florin Andrei"
+ "\r\n" +
"- Eoin Boyle"
+ "\r\n" +
"- Elaine Wong"
+ "\r\n" +
"- Xiao Long Qi Andrei"
+ "\r\n" +
"Once you hit the start button you will be able to select one of our many features. ",
          background = 'aqua', foreground ="Black",
          font = ("Times New Roman", 10))
start2.place(x = 40, y = 50)

#Function for start button
def main ():
    mai = Tk()
    mai.title("Main Menu")
    mai.geometry('760x320')
    mai.configure(background="light green")
    start.destroy()

    #App placement
    app_width = 760
    app_height = 320

    screen_width = mai.winfo_screenwidth()
    screen_height = mai.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    mai.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
   
    #Label for Main Menu
    mainlabel = ttk.Label(mai, text = "\u0332".join("Main Menu"),
          background = 'lightgreen', foreground ="Black",
          font = ("Times New Roman", 15))      
    mainlabel.place(x=240, y=10)

    #YEAR ONE options
    ml5 = ttk.Label(mai, text = "One Year",
          background = 'light green', foreground ="black",
          font = ("Times New Roman", 15))      
    ml5.place(x=50, y=50)

    btn1 = Button(mai,text="Temperature (° F)", width=20, command=op1)
    btn1.place(x=10, y=100)
   
    btn2 = Button(mai,text="Drew Point (° F)", width=20, command=op2)
    btn2.place(x=10, y=150)

    btn3 = Button(mai,text="Humidity (%)", width=20, command=op3)
    btn3.place(x=10, y=200)
    
    btn4 = Button(mai,text="Wind Speed (mph)", width=20, command=op4)
    btn4.place(x=10, y=250)
   
   #YEAR TWO options
    ml5 = ttk.Label(mai, text = "Two Years",
          background = 'light green', foreground ="black",
          font = ("Times New Roman", 15))      
    ml5.place(x=240, y=50)

    btn6 = Button(mai,text="Temperature (° F)", width=20, command=TempComp)
    btn6.place(x=205, y=100)

    btn7 = Button(mai,text="Dew Point (° F)", width=20, command=DewComp)
    btn7.place(x=205, y=150)

    btn8 = Button(mai,text="Humidity (%)", width=20, command=HumidityComp)
    btn8.place(x=205, y=200)

    btn9 = Button(mai,text="Wind Speed (mph)", width=20, command=WindComp)
    btn9.place(x=205, y=250)

    #YEAR THREE options
    ml5 = ttk.Label(mai, text = "Three years",
          background = 'light green', foreground ="black",
          font = ("Times New Roman", 15))      
    ml5.place(x=430, y=50)

    btn10 = Button(mai,text="Temperature (° F)", width=20, command=op1p2)
    btn10.place(x=400, y=100)
    
    btn11 = Button(mai,text="Dew Point (° F)", width=20, command=op2p2)
    btn11.place(x=400, y=150)
    
    btn12 =Button(mai,text="Humidity (%)", width=20, command=op3p2)
    btn12.place(x=400, y=200)
   
    btn13 = Button(mai,text="Wind Speed (mph)", width=20, command=op4p2)
    btn13.place(x=400, y=250)
    #YEAR FOUR options
    ml5 = ttk.Label(mai, text = "Four Years",
          background = 'light green', foreground ="black",
          font = ("Times New Roman", 15))      
    ml5.place(x=625, y=50)

    btn14 = Button(mai,text="Temperature (° F)", width=20, command=rn1)
    btn14.place(x=600, y=100)

    btn15 = Button(mai,text="Dew Point (° F)", width=20, command=rn2)
    btn15.place(x=600, y=150)

    btn16 = Button(mai,text="Humidity (%)", width=20, command=rn3)
    btn16.place(x=600, y=200)

    btn17 = Button(mai,text="Wind Speed (mph)", width=20, command=rn4)
    btn17.place(x=600, y=250)

#Adding Function for start Button
bntStart1 = Button(start,text="Click to start", width=15, command=main, background = 'lightgreen', foreground ="Black")
bntStart1.place(x=180, y=300)


#Option 1 Function
def op1 ():
    op1 = Tk()
    op1.title("Temperature (° F)")
    op1.configure(background="darkorange")

    #App placement
    app_width = 400
    app_height = 240

    screen_width = op1.winfo_screenwidth()
    screen_height = op1.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    op1.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    lbl = ttk.Label(op1, text = "Temperature (° F)",
          background = 'darkorange', foreground ="black",
          font = ("Times New Roman", 15))
    lbl.place(x=80, y=18)

# label max/average/min
    lbl1 = ttk.Label(op1, text = "Select the Year :",
          background = 'darkorange', foreground ="black",
          font = ("Times New Roman", 10))  
    lbl1.place(x=10, y=80)

# Combobox creation
    n = tk.StringVar()
    yearchoosen = ttk.Combobox(op1, width = 27, textvariable = n)
    yearchoosen.place(x=110, y=80)

# Adding combobox drop down list
    yearchoosen['values'] = ('2009',
                        '2010',
                        '2011',
                        '2012',
                        '2013',
                         '2014',
                         '2015',
                          '2016',
                          '2017',
                          '2018',
                          '2019',
                          '2020')
    yearchoosen.place(x=110, y=80)
    yearchoosen.current()

# label value
    lbl2 = ttk.Label(op1, text = "Select the value :",
        background = 'darkorange', foreground ="black",
          font = ("Times New Roman", 10))
    lbl2.place(x=10, y=130)

# Combobox creation
    n = tk.StringVar()
    typevalue = ttk.Combobox(op1, width = 27, textvariable = n)
    typevalue.place(x=110, y=130)

# Adding combobox drop down list
    typevalue['values'] = ('Minimum',
                          'Average',
                          'Maximum')
    typevalue.place(x=110, y=130)
    typevalue.current()

#Submitbutton function +++++ Function for finding data
    def click():
        year_a = yearchoosen.get()
        value_type = typevalue.get()
        data_type='temperature'
       
        makePlot(year_a,data_type,value_type)

#addbutton
    btn = Button(op1,text="Submit", width=6, command=click)
    btn.place(x=120, y=180)

#add exit button
    btn1 = Button(op1,text="Quit", width=6, command=op1.destroy) 
    btn1.place(x=220, y=180)

    op1.mainloop()

    #Option 2 Function
def op2 ():
    op2 = Tk()
    op2.title("Dew Point (° F)")
    op2.configure(background="darkorange")

    #App placement
    app_width = 400
    app_height = 240

    screen_width = op2.winfo_screenwidth()
    screen_height = op2.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    op2.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    lbl = ttk.Label(op2, text = "Dew Point (° F)",
          background = 'darkorange', foreground ="black",
          font = ("Times New Roman", 15))
    lbl.place(x=80, y=18)

# label max/average/min
    lbl1 = ttk.Label(op2, text = "Select the Year :",
          background = 'darkorange', foreground ="black",
          font = ("Times New Roman", 10))  
    lbl1.place(x=10, y=80)

# Combobox creation
    n = tk.StringVar()
    yearchoosen = ttk.Combobox(op2, width = 27, textvariable = n)
    yearchoosen.place(x=110, y=80)

# Adding combobox drop down list
    yearchoosen['values'] = ('2009',
                        '2010',
                        '2011',
                        '2012',
                        '2013',
                         '2014',
                         '2015',
                          '2016',
                          '2017',
                          '2018',
                          '2019',
                          '2020')
    yearchoosen.place(x=110, y=80)
    yearchoosen.current()

# label value
    lbl2 = ttk.Label(op2, text = "Select the value :",
        background = 'darkorange', foreground ="black",
          font = ("Times New Roman", 10))
    lbl2.place(x=10, y=130)

# Combobox creation
    n = tk.StringVar()
    typevalue = ttk.Combobox(op2, width = 27, textvariable = n)
    typevalue.place(x=110, y=130)

# Adding combobox drop down list
    typevalue['values'] = ('Minimum',
                          'Average',
                          'Maximum')
    typevalue.place(x=110, y=130)
    typevalue.current()

#Submitbutton function +++++ Function for finding data
    def click():
        year_a = yearchoosen.get()
        value_type = typevalue.get()
        data_type='DewPoint'
       
        makePlot(year_a,data_type,value_type)

#addbutton
    btn = Button(op2,text="Submit", width=6, command=click)
    btn.place(x=120, y=180)

#add exit button
    btn1 = Button(op2,text="Quit", width=6, command=op2.destroy) 
    btn1.place(x=220, y=180)

    op2.mainloop()

#Option 3 Function
def op3 ():
    op3 = Tk()
    op3.title("Humidity (%)")
    op3.configure(background="darkorange")

    #App placement
    app_width = 400
    app_height = 240

    screen_width = op3.winfo_screenwidth()
    screen_height = op3.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    op3.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    lbl = ttk.Label(op3, text = "Humidity (%)",
          background = 'darkorange', foreground ="black",
          font = ("Times New Roman", 15))
    lbl.place(x=80, y=18)

# label max/average/min
    lbl1 = ttk.Label(op3, text = "Select the Year :",
          background = 'darkorange', foreground ="black",
          font = ("Times New Roman", 10))  
    lbl1.place(x=10, y=80)

# Combobox creation
    n = tk.StringVar()
    yearchoosen = ttk.Combobox(op3, width = 27, textvariable = n)
    yearchoosen.place(x=110, y=80)

# Adding combobox drop down list
    yearchoosen['values'] = ('2009',
                        '2010',
                        '2011',
                        '2012',
                        '2013',
                         '2014',
                         '2015',
                          '2016',
                          '2017',
                          '2018',
                          '2019',
                          '2020')
    yearchoosen.place(x=110, y=80)
    yearchoosen.current()

# label value
    lbl2 = ttk.Label(op3, text = "Select the value :",
        background = 'darkorange', foreground ="black",
          font = ("Times New Roman", 10))
    lbl2.place(x=10, y=130)

# Combobox creation
    n = tk.StringVar()
    typevalue = ttk.Combobox(op3, width = 27, textvariable = n)
    typevalue.place(x=110, y=130)

# Adding combobox drop down list
    typevalue['values'] = ('Minimum',
                          'Average',
                          'Maximum')
    typevalue.place(x=110, y=130)
    typevalue.current()

#Submitbutton function +++++ Function for finding data
    def click():
        year_a = yearchoosen.get()
        value_type = typevalue.get()
        data_type='Humidity'
       
        makePlot(year_a,data_type,value_type)

#addbutton
    btn = Button(op3,text="Submit", width=6, command=click)
    btn.place(x=120, y=180)

#add exit button
    btn1 = Button(op3,text="Quit", width=6, command=op3.destroy) 
    btn1.place(x=220, y=180)

    op3.mainloop()

    #Option 4 Function
#Option 3 Function
def op4 ():
    op4 = Tk()
    op4.title("Wind Speed (mph)")
    op4.configure(background="darkorange")

    #App placement
    app_width = 400
    app_height = 240

    screen_width = op4.winfo_screenwidth()
    screen_height = op4.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    op4.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    lbl = ttk.Label(op4, text = "Wind Speed (mph)",
          background = 'darkorange', foreground ="black",
          font = ("Times New Roman", 15))
    lbl.place(x=80, y=18)

# label max/average/min
    lbl1 = ttk.Label(op4, text = "Select the Year :",
          background = 'darkorange', foreground ="black",
          font = ("Times New Roman", 10))  
    lbl1.place(x=10, y=80)

# Combobox creation
    n = tk.StringVar()
    yearchoosen = ttk.Combobox(op4, width = 27, textvariable = n)
    yearchoosen.place(x=110, y=80)

# Adding combobox drop down list
    yearchoosen['values'] = ('2009',
                        '2010',
                        '2011',
                        '2012',
                        '2013',
                         '2014',
                         '2015',
                          '2016',
                          '2017',
                          '2018',
                          '2019',
                          '2020')
    yearchoosen.place(x=110, y=80)
    yearchoosen.current()

# label value
    lbl2 = ttk.Label(op4, text = "Select the value :",
        background = 'darkorange', foreground ="black",
          font = ("Times New Roman", 10))
    lbl2.place(x=10, y=130)

# Combobox creation
    n = tk.StringVar()
    typevalue = ttk.Combobox(op4, width = 27, textvariable = n)
    typevalue.place(x=110, y=130)

# Adding combobox drop down list
    typevalue['values'] = ('Minimum',
                          'Average',
                          'Maximum')
    typevalue.place(x=110, y=130)
    typevalue.current()

#Submitbutton function +++++ Function for finding data
    def click():
        year_a = yearchoosen.get()
        value_type = typevalue.get()
        data_type='WindSpeed'
       
        makePlot(year_a,data_type,value_type)

#addbutton
    btn = Button(op4,text="Submit", width=6, command=click)
    btn.place(x=120, y=180)

#add exit button
    btn1 = Button(op4,text="Quit", width=6, command=op4.destroy) 
    btn1.place(x=220, y=180)

    op4.mainloop()

# Finding max temp of a year
def findMaxValueYear(year_a, data_type):
    maxValueYear=[]
    for year in year_a:
        value_type = 'Maximum'
        year_a_data=getYearData(year, data_type, value_type)
        maxValueYear.append(max(year_a_data))

    return maxValueYear

# Finding mean temp of a year
def findMeanValueYear(year_a, data_type):
    meanValueYear=[]
    for year in year_a:
        value_type = 'Average'
        year_a_data=getYearData(year, data_type, value_type)
        meanValueYear.append(statistics.mean(year_a_data))

    return meanValueYear


# Finding min temp of a year
def findMinValueYear(year_a, data_type):
    minValueYear=[]
    for year in year_a:
        value_type = 'Minimum'
        year_a_data=getYearData(year, data_type, value_type)
        minValueYear.append(min(year_a_data))

    return minValueYear

# Function to make a single comparison graph. 
def makeComPlot(year, data_type):

    # Getting max, mean and min values to plot
    maxValuesYear = findMaxValueYear(year, data_type)
    meanValuesYear = findMeanValueYear(year, data_type)
    minValuesYear = findMinValueYear(year, data_type)
    
    # Gathering better y axis labels that includes the measurements
    if (data_type=='temperature'):
        ylabel="Temperature (° F)"
    if (data_type=='DewPoint'):
        ylabel="Dew Point (° F)"
    if (data_type=='Humidity'):
        ylabel="Humidity (%)"
    if (data_type=='WindSpeed'):
        ylabel="Wind Speed (mph)"

    # Creating a figure and adding a title, y and x labels and a grid
    plt.figure(figsize=(12,5))
    plt.title(f"Comparing the maximum, mean & minimum {data_type} values of {year[0]}, {year[1]} & {year[2]}")
    plt.ylabel(ylabel)
    plt.xlabel('Years')
    plt.grid(axis= 'y')

    # Adding vertical lines between the points 
    plt.vlines(x=year, ymin=minValuesYear, ymax=[maxValuesYear], colors='black', ls='-', lw=2)

    # Plotting 
    plt.plot(year,maxValuesYear, 'dk',markersize = 10, color='blue',linestyle='',markerfacecolor='blue', label="Maximum")
    plt.plot(year,meanValuesYear, 'sk',markersize = 10, color='magenta',linestyle='',markerfacecolor='magenta', label="Mean")
    plt.plot(year,minValuesYear, 'ok', markersize = 10, color='red',linestyle='',markerfacecolor='red', label="Minimum")

    # Adding a legend
    plt.legend(bbox_to_anchor=(1.1, 1.05))

    plt.show()

years = ['2009','2010','2011','2012','2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']

# Option 1.2 Function
def op1p2 ():

    # Creating the layout
    op1p2 = Tk()
    op1p2.title("Comparing Yearly Temperature (° F)")
    op1p2.configure(background="yellow")

    #App placement
    app_width = 500
    app_height = 320

    screen_width = op1p2.winfo_screenwidth()
    screen_height = op1p2.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    op1p2.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    lbl0 = ttk.Label(op1p2, text = "Comparing Yearly Temperature (° F)", 
          background = 'yellow', foreground ="black", 
          font = ("Times New Roman", 15))
    lbl0.place(x=100, y=20)

    # Year Selection 1 by creating labels, comboboxes & combobox drop down lists
    lbl1 = ttk.Label(op1p2, text = "Select Year 1 :",
          background = 'yellow', foreground ="black", 
          font = ("Times New Roman", 10))
    lbl1.place(x=80, y=100)
          
    n = tk.StringVar()
    yearchoosen1 = ttk.Combobox(op1p2, width = 27, textvariable = n)
    yearchoosen1['values'] = years
    yearchoosen1.current()
    yearchoosen1.place(x=180, y=100)

    # Year Selection 2 by creating labels, comboboxes & combobox drop down lists
    lbl2 = ttk.Label(op1p2, text = "Select Year 2 :",
        background = 'yellow', foreground ="black", 
          font = ("Times New Roman", 10))
    lbl2.place(x=80, y=155)

    n = tk.StringVar()
    yearchoosen2 = ttk.Combobox(op1p2, width = 27, textvariable = n)
    yearchoosen2['values'] = years
    yearchoosen2.current()
    yearchoosen2.place(x=180, y=155)

    # Year Selection 3 by creating labels, comboboxes & combobox drop down lists
    lbl3 = ttk.Label(op1p2, text = "Select Year 3 :",
          background = 'yellow', foreground ="black",
          font = ("Times New Roman", 10))       
    lbl3.place(x=80, y=210)

    n = tk.StringVar()
    yearchoosen3 = ttk.Combobox(op1p2, width = 27, textvariable = n)
    yearchoosen3['values'] = years
    yearchoosen3.current()
    yearchoosen3.place(x=180, y=210)

    # Submit button function to make ComPlot
    def clickop1p2():
        year1= yearchoosen1.get()
        year2= yearchoosen2.get()
        year3= yearchoosen3.get()
        yearSelections = [year1, year2, year3]

        makeComPlot(yearSelections,'temperature')

    #Adding submit & exit buttons
    btn = Button(op1p2,text="Submit", width=6, command=clickop1p2)
    btn.place(x=185, y=260)

    btn1 = Button(op1p2,text="Quit", width=6, command=op1p2.destroy)
    btn1.place(x=285, y=260)

    op1p2.mainloop()

# Option 2.2 function
def op2p2 ():

    # Creating the layout
    op2p2 = Tk()
    op2p2.title("Comparing Yearly Dew Point (° F)")
    op2p2.configure(background="yellow")

    #App placement
    app_width = 500
    app_height = 320

    screen_width = op2p2.winfo_screenwidth()
    screen_height = op2p2.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    op2p2.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    lbl0 = ttk.Label(op2p2, text = "Comparing Yearly Dew Point (° F)", 
          background = 'yellow', foreground ="black", 
          font = ("Times New Roman", 15))
    lbl0.place(x=100, y=20)

    # Year Selection 1 by creating labels, comboboxes & combobox drop down lists
    lbl1 = ttk.Label(op2p2, text = "Select Year 1 :",
          background = 'yellow', foreground ="black", 
          font = ("Times New Roman", 10))
    lbl1.place(x=80, y=100)
          
    n = tk.StringVar()
    yearchoosen1 = ttk.Combobox(op2p2, width = 27, textvariable = n)
    yearchoosen1['values'] = years
    yearchoosen1.current()
    yearchoosen1.place(x=180, y=100)

    # Year Selection 2 by creating labels, comboboxes & combobox drop down lists
    lbl2 = ttk.Label(op2p2, text = "Select Year 2 :",
        background = 'yellow', foreground ="black", 
          font = ("Times New Roman", 10))
    lbl2.place(x=80, y=155)

    n = tk.StringVar()
    yearchoosen2 = ttk.Combobox(op2p2, width = 27, textvariable = n)
    yearchoosen2['values'] = years
    yearchoosen2.current()
    yearchoosen2.place(x=180, y=155)

    # Year Selection 3 by creating labels, comboboxes & combobox drop down lists
    lbl3 = ttk.Label(op2p2, text = "Select Year 3 :",
          background = 'yellow', foreground ="black",
          font = ("Times New Roman", 10))       
    lbl3.place(x=80, y=210)

    n = tk.StringVar()
    yearchoosen3 = ttk.Combobox(op2p2, width = 27, textvariable = n)
    yearchoosen3['values'] = years
    yearchoosen3.current()
    yearchoosen3.place(x=180, y=210)

    # Submit button function to make ComPlot
    def clickop2p2():
        year1= yearchoosen1.get()
        year2= yearchoosen2.get()
        year3= yearchoosen3.get()
        yearSelections = [year1, year2, year3]

        makeComPlot(yearSelections,'DewPoint')

    #Adding submit & exit buttons
    btn = Button(op2p2,text="Submit", width=6, command=clickop2p2)
    btn.place(x=185, y=260)

    btn1 = Button(op2p2,text="Quit", width=6, command=op2p2.destroy)
    btn1.place(x=285, y=260)

    op2p2.mainloop()

# Option 3.2 Function
def op3p2 ():

    # Creating the layout
    op3p2 = Tk()
    op3p2.title("Comparing Yearly Humidity (%)")
    op3p2.configure(background="yellow")

    #App placement
    app_width = 500
    app_height = 320

    screen_width = op3p2.winfo_screenwidth()
    screen_height = op3p2.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    op3p2.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    lbl0 = ttk.Label(op3p2, text = "Comparing Yearly Humidity (%)", 
          background = 'yellow', foreground ="black", 
          font = ("Times New Roman", 15))
    lbl0.place(x=100, y=20)

    # Year Selection 1 by creating labels, comboboxes & combobox drop down lists
    lbl1 = ttk.Label(op3p2, text = "Select Year 1 :",
          background = 'yellow', foreground ="black", 
          font = ("Times New Roman", 10))
    lbl1.place(x=80, y=100)
          
    n = tk.StringVar()
    yearchoosen1 = ttk.Combobox(op3p2, width = 27, textvariable = n)
    yearchoosen1['values'] = years
    yearchoosen1.current()
    yearchoosen1.place(x=180, y=100)

    # Year Selection 2 by creating labels, comboboxes & combobox drop down lists
    lbl2 = ttk.Label(op3p2, text = "Select Year 2 :",
        background = 'yellow', foreground ="black", 
          font = ("Times New Roman", 10))
    lbl2.place(x=80, y=155)

    n = tk.StringVar()
    yearchoosen2 = ttk.Combobox(op3p2, width = 27, textvariable = n)
    yearchoosen2['values'] = years
    yearchoosen2.current()
    yearchoosen2.place(x=180, y=155)

    # Year Selection 3 by creating labels, comboboxes & combobox drop down lists
    lbl3 = ttk.Label(op3p2, text = "Select Year 3 :",
          background = 'yellow', foreground ="black",
          font = ("Times New Roman", 10))       
    lbl3.place(x=80, y=210)

    n = tk.StringVar()
    yearchoosen3 = ttk.Combobox(op3p2, width = 27, textvariable = n)
    yearchoosen3['values'] = years
    yearchoosen3.current()
    yearchoosen3.place(x=180, y=210)

    # Submit button function to make ComPlot
    def clickop3p2():
        year1= yearchoosen1.get()
        year2= yearchoosen2.get()
        year3= yearchoosen3.get()
        yearSelections = [year1, year2, year3]

        makeComPlot(yearSelections,'Humidity')

    #Adding submit & exit buttons
    btn = Button(op3p2,text="Submit", width=6, command=clickop3p2)
    btn.place(x=185, y=260)

    btn1 = Button(op3p2,text="Quit", width=6, command=op3p2.destroy)
    btn1.place(x=285, y=260)

    op3p2.mainloop()

# Option 4.2 Function
def op4p2 ():

    # Creating the layout
    op4p2 = Tk()
    op4p2.title("Comparing Yearly Wind Speed (mph)")
    op4p2.configure(background="yellow")

    #App placement
    app_width = 500
    app_height = 320

    screen_width = op4p2.winfo_screenwidth()
    screen_height = op4p2.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    op4p2.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    lbl0 = ttk.Label(op4p2, text = "Comparing Yearly WindSpeed (mph)", 
          background = 'yellow', foreground ="black", 
          font = ("Times New Roman", 15))
    lbl0.place(x=100, y=20)

    # Year Selection 1 by creating labels, comboboxes & combobox drop down lists
    lbl1 = ttk.Label(op4p2, text = "Select Year 1 :",
          background = 'yellow', foreground ="black", 
          font = ("Times New Roman", 10))
    lbl1.place(x=80, y=100)
          
    n = tk.StringVar()
    yearchoosen1 = ttk.Combobox(op4p2, width = 27, textvariable = n)
    yearchoosen1['values'] = years
    yearchoosen1.current()
    yearchoosen1.place(x=180, y=100)

    # Year Selection 2 by creating labels, comboboxes & combobox drop down lists
    lbl2 = ttk.Label(op4p2, text = "Select Year 2 :",
        background = 'yellow', foreground ="black", 
          font = ("Times New Roman", 10))
    lbl2.place(x=80, y=155)

    n = tk.StringVar()
    yearchoosen2 = ttk.Combobox(op4p2, width = 27, textvariable = n)
    yearchoosen2['values'] = years
    yearchoosen2.current()
    yearchoosen2.place(x=180, y=155)

    # Year Selection 3 by creating labels, comboboxes & combobox drop down lists
    lbl3 = ttk.Label(op4p2, text = "Select Year 3 :",
          background = 'yellow', foreground ="black",
          font = ("Times New Roman", 10))       
    lbl3.place(x=80, y=210)

    n = tk.StringVar()
    yearchoosen3 = ttk.Combobox(op4p2, width = 27, textvariable = n)
    yearchoosen3['values'] = years
    yearchoosen3.current()
    yearchoosen3.place(x=180, y=210)

    # Submit button function to make ComPlot
    def clickop4p2():
        year1= yearchoosen1.get()
        year2= yearchoosen2.get()
        year3= yearchoosen3.get()
        yearSelections = [year1, year2, year3]

        makeComPlot(yearSelections,'WindSpeed')

    #Adding submit & exit buttons
    btn = Button(op4p2,text="Submit", width=6, command=clickop4p2)
    btn.place(x=185, y=260)

    btn1 = Button(op4p2,text="Quit", width=6, command=op4p2.destroy)
    btn1.place(x=285, y=260)

    op4p2.mainloop()

#---------------------------------------------------------------------------------------------------------------
#Option 6
def TempComp ():
    TempComp = Tk()
    TempComp.title("Temperature")
    TempComp.configure(background="light yellow")

    #App placement
    app_width = 500
    app_height = 320

    screen_width = TempComp.winfo_screenwidth()
    screen_height = TempComp.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    TempComp.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    lbl = ttk.Label(TempComp, text = "Temperature", 
          background = 'light yellow', foreground ="black", 
          font = ("Times New Roman", 15))
    lbl.place(x=200, y=20)
    
# label max/average/min 
    lbl1 = ttk.Label(TempComp, text = "Select first Year :",
        background = 'light yellow', foreground ="black",
        font = ("Times New Roman", 10))
    lbl1.place(x=80, y=80)  

    lbl2 = ttk.Label(TempComp, text = "Select second Year :",
        background = 'light yellow', foreground ="black",
        font = ("Times New Roman", 10))
    lbl2.place(x=80, y=138)        

# Combobox creation
    n = tk.StringVar()
    m = tk.StringVar()

    yearchoosen = ttk.Combobox(TempComp, width = 27, textvariable = n)
    
    yearchoosen2 = ttk.Combobox(TempComp, width = 27, textvariable = m)

# Adding combobox drop down list
    yearchoosen['values'] = ('2009',
                        '2010',
                        '2011',
                        '2012',
                        '2013',
                         '2014',
                         '2015',
                          '2016',
                          '2017',
                          '2018',
                          '2019',
                          '2020')
    yearchoosen.place(x=200, y=80)
    yearchoosen.current()
    
    yearchoosen2['values'] = ('2009',
                        '2010',
                        '2011',
                        '2012',
                        '2013',
                         '2014',
                         '2015',
                          '2016',
                          '2017',
                          '2018',
                          '2019',
                          '2020')
    yearchoosen2.place(x=200, y=138)
    yearchoosen2.current()

# label year
    lbl5 = ttk.Label(TempComp, text = "Select the value :",
        background = 'light yellow', foreground ="black",
        font = ("Times New Roman", 10))
    lbl5.place(x=80, y=200)

# Combobox creation
    n = tk.StringVar()
    typevalue = ttk.Combobox(TempComp, width = 27, textvariable = n)

# Adding combobox drop down list
    typevalue['values'] = ('Minimum', 
                          'Average',
                          'Maximum')
    typevalue.place(x=200, y=200)
    typevalue.current()

#Submitbutton function
    def click6():
        year_a = yearchoosen.get()
        year_b = yearchoosen2.get()
        value_type = typevalue.get()
        data_type='temperature'
        
        maketwoPlots(year_a, year_b, data_type, value_type)

#addbutton 
    lbl6 = Button(TempComp,text="Submit", width=6, command=click6)
    lbl6.place(x=220, y=245)

#add exit button
    lbl7 = Button(TempComp,text="Quit", width=6, command=TempComp.destroy)
    lbl7.place(x=315, y=245)

    TempComp.mainloop()

#Option7
def DewComp ():
    DewComp = Tk()
    DewComp.title("Dew Point")
    DewComp.configure(background="light yellow")

    #App placement
    app_width = 500
    app_height = 320

    screen_width = DewComp.winfo_screenwidth()
    screen_height = DewComp.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    DewComp.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    lbl = ttk.Label(DewComp, text = "Dew Point", 
          background = 'light yellow', foreground ="black", 
          font = ("Times New Roman", 15))
    lbl.place(x=200, y=20)
    
# label max/average/min 
    lbl1 = ttk.Label(DewComp, text = "Select first Year :",
        background = 'light yellow', foreground ="black",
        font = ("Times New Roman", 10))
    lbl1.place(x=80, y=80)  

    lbl2 = ttk.Label(DewComp, text = "Select second Year :",
        background = 'light yellow', foreground ="black",
        font = ("Times New Roman", 10))
    lbl2.place(x=80, y=138)        

# Combobox creation
    n = tk.StringVar()
    m = tk.StringVar()

    yearchoosen = ttk.Combobox(DewComp, width = 27, textvariable = n)
    
    yearchoosen2 = ttk.Combobox(DewComp, width = 27, textvariable = m)

# Adding combobox drop down list
    yearchoosen['values'] = ('2009',
                        '2010',
                        '2011',
                        '2012',
                        '2013',
                         '2014',
                         '2015',
                          '2016',
                          '2017',
                          '2018',
                          '2019',
                          '2020')
    yearchoosen.place(x=200, y=80)
    yearchoosen.current()
    
    yearchoosen2['values'] = ('2009',
                        '2010',
                        '2011',
                        '2012',
                        '2013',
                         '2014',
                         '2015',
                          '2016',
                          '2017',
                          '2018',
                          '2019',
                          '2020')
    yearchoosen2.place(x=200, y=138)
    yearchoosen2.current()

# label year
    lbl5 = ttk.Label(DewComp, text = "Select the value :",
        background = 'light yellow', foreground ="black",
        font = ("Times New Roman", 10))
    lbl5.place(x=80, y=200)

# Combobox creation
    n = tk.StringVar()
    typevalue = ttk.Combobox(DewComp, width = 27, textvariable = n)

# Adding combobox drop down list
    typevalue['values'] = ('Minimum', 
                          'Average',
                          'Maximum')
    typevalue.place(x=200, y=200)
    typevalue.current()

#Submitbutton function
    def click6():
        year_a = yearchoosen.get()
        year_b = yearchoosen2.get()
        value_type = typevalue.get()
        data_type='DewPoint'
        
        maketwoPlots(year_a, year_b, data_type, value_type)

#addbutton 
    lbl6 = Button(DewComp,text="Submit", width=6, command=click6)
    lbl6.place(x=220, y=245)

#add exit button
    lbl7 = Button(DewComp,text="Quit", width=6, command=DewComp.destroy)
    lbl7.place(x=315, y=245)

    DewComp.mainloop()

#Option8
def HumidityComp ():
    HumidityComp = Tk()
    HumidityComp.title("Humidity")
    HumidityComp.configure(background="light yellow")

    #App placement
    app_width = 500
    app_height = 320

    screen_width = HumidityComp.winfo_screenwidth()
    screen_height = HumidityComp.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    HumidityComp.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    lbl = ttk.Label(HumidityComp, text = "Humidity", 
          background = 'light yellow', foreground ="black", 
          font = ("Times New Roman", 15))
    lbl.place(x=200, y=20)
    
# label max/average/min 
    lbl1 = ttk.Label(HumidityComp, text = "Select first Year :",
        background = 'light yellow', foreground ="black",
        font = ("Times New Roman", 10))
    lbl1.place(x=80, y=80)  

    lbl2 = ttk.Label(HumidityComp, text = "Select second Year :",
        background = 'light yellow', foreground ="black",
        font = ("Times New Roman", 10))
    lbl2.place(x=80, y=138)        

# Combobox creation
    n = tk.StringVar()
    m = tk.StringVar()

    yearchoosen = ttk.Combobox(HumidityComp, width = 27, textvariable = n)
    
    yearchoosen2 = ttk.Combobox(HumidityComp, width = 27, textvariable = m)

# Adding combobox drop down list
    yearchoosen['values'] = ('2009',
                        '2010',
                        '2011',
                        '2012',
                        '2013',
                         '2014',
                         '2015',
                          '2016',
                          '2017',
                          '2018',
                          '2019',
                          '2020')
    yearchoosen.place(x=200, y=80)
    yearchoosen.current()
    
    yearchoosen2['values'] = ('2009',
                        '2010',
                        '2011',
                        '2012',
                        '2013',
                         '2014',
                         '2015',
                          '2016',
                          '2017',
                          '2018',
                          '2019',
                          '2020')
    yearchoosen2.place(x=200, y=138)
    yearchoosen2.current()

# label year
    lbl5 = ttk.Label(HumidityComp, text = "Select the value :",
        background = 'light yellow', foreground ="black",
        font = ("Times New Roman", 10))
    lbl5.place(x=80, y=200)

# Combobox creation
    n = tk.StringVar()
    typevalue = ttk.Combobox(HumidityComp, width = 27, textvariable = n)

# Adding combobox drop down list
    typevalue['values'] = ('Minimum', 
                          'Average',
                          'Maximum')
    typevalue.place(x=200, y=200)
    typevalue.current()

#Submitbutton function
    def click6():
        year_a = yearchoosen.get()
        year_b = yearchoosen2.get()
        value_type = typevalue.get()
        data_type='Humidity'
        
        maketwoPlots(year_a, year_b, data_type, value_type)

#addbutton 
    lbl6 = Button(HumidityComp,text="Submit", width=6, command=click6)
    lbl6.place(x=220, y=245)

#add exit button
    lbl7 = Button(HumidityComp,text="Quit", width=6, command=HumidityComp.destroy)
    lbl7.place(x=315, y=245)

    HumidityComp.mainloop()
 
 #Option9
def WindComp ():
    WindComp = Tk()
    WindComp.title("Wind Speed")
    WindComp.configure(background="light yellow")

    #App placement
    app_width = 500
    app_height = 320

    screen_width = WindComp.winfo_screenwidth()
    screen_height = WindComp.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    WindComp.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    lbl = ttk.Label(WindComp, text = "Wind Speed", 
          background = 'light yellow', foreground ="black", 
          font = ("Times New Roman", 15))
    lbl.place(x=200, y=20)
    
# label max/average/min 
    lbl1 = ttk.Label(WindComp, text = "Select first Year :",
        background = 'light yellow', foreground ="black",
        font = ("Times New Roman", 10))
    lbl1.place(x=80, y=80)  

    lbl2 = ttk.Label(WindComp, text = "Select second Year :",
        background = 'light yellow', foreground ="black",
        font = ("Times New Roman", 10))
    lbl2.place(x=80, y=138)        

# Combobox creation
    n = tk.StringVar()
    m = tk.StringVar()

    yearchoosen = ttk.Combobox(WindComp, width = 27, textvariable = n)
    
    yearchoosen2 = ttk.Combobox(WindComp, width = 27, textvariable = m)

# Adding combobox drop down list
    yearchoosen['values'] = ('2009',
                        '2010',
                        '2011',
                        '2012',
                        '2013',
                         '2014',
                         '2015',
                          '2016',
                          '2017',
                          '2018',
                          '2019',
                          '2020')
    yearchoosen.place(x=200, y=80)
    yearchoosen.current()
    
    yearchoosen2['values'] = ('2009',
                        '2010',
                        '2011',
                        '2012',
                        '2013',
                         '2014',
                         '2015',
                          '2016',
                          '2017',
                          '2018',
                          '2019',
                          '2020')
    yearchoosen2.place(x=200, y=138)
    yearchoosen2.current()

# label year
    lbl5 = ttk.Label(WindComp, text = "Select the value :",
        background = 'light yellow', foreground ="black",
        font = ("Times New Roman", 10))
    lbl5.place(x=80, y=200)

# Combobox creation
    n = tk.StringVar()
    typevalue = ttk.Combobox(WindComp, width = 27, textvariable = n)

# Adding combobox drop down list
    typevalue['values'] = ('Minimum', 
                          'Average',
                          'Maximum')
    typevalue.place(x=200, y=200)
    typevalue.current()

#Submitbutton function
    def click6():
        year_a = yearchoosen.get()
        year_b = yearchoosen2.get()
        value_type = typevalue.get()
        data_type='WindComp'
        
        maketwoPlots(year_a, year_b, data_type, value_type)

#addbutton 
    lbl6 = Button(WindComp,text="Submit", width=6, command=click6)
    lbl6.place(x=220, y=245)

#add exit button
    lbl7 = Button(WindComp,text="Quit", width=6, command=WindComp.destroy)
    lbl7.place(x=315, y=245)

    WindComp.mainloop()

    op1p2 = Tk()
    op1p2.title("Comparing Yearly Temperature (° F)")
    op1p2.configure(background="yellow")
#--------------------------------------------------------------------------------------RYAN
def makefourplot(year, data_type):

    # Getting max, mean and min values to plot
    maxValuesYear = findMaxValueYear(year, data_type)
    meanValuesYear = findMeanValueYear(year, data_type)
    minValuesYear = findMinValueYear(year, data_type)
    
    # Gathering better y axis labels that includes the measurements
    if (data_type=='temperature'):
        ylabel="Temperature (° F)"
    if (data_type=='DewPoint'):
        ylabel="Dew Point (° F)"
    if (data_type=='Humidity'):
        ylabel="Humidity (%)"
    if (data_type=='WindSpeed'):
        ylabel="Wind Speed (mph)"

    # Creating a figure and adding a title, y and x labels and a grid
    plt.figure(figsize=(12,5))
    plt.title(f"Comparing the maximum, mean & minimum {data_type} values of {year[0]}, {year[1]} , {year[2]}& {year[3]}")
    plt.ylabel(ylabel)
    plt.xlabel('Years')
    plt.grid(axis= 'y')


    # Plotting 
    plt.scatter(year,maxValuesYear, s = 150, label="Maximum")
    plt.scatter(year,meanValuesYear, s = 150, label="Mean")
    plt.scatter(year,minValuesYear, s =150, label="Minimum")

    # Adding a legend
    plt.legend(bbox_to_anchor=(1.1, 1.05))

    plt.show()

    years = ['2009','2010','2011','2012','2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']


def rn1():
    rn1 = Tk()
    rn1.title("Comparing Yearly Temperature (° F)")
    rn1.configure(background="purple")
#App placement
    app_width = 500
    app_height = 450

    screen_width = rn1.winfo_screenwidth()
    screen_height = rn1.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    rn1.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    lbl0 = ttk.Label(rn1, text = "Comparing Yearly Temperature (° F)", 
          background = 'purple', foreground ="black", 
          font = ("Times New Roman", 15))
    lbl0.place(x=100, y=20)

    # Year Selection 1 by creating labels, comboboxes & combobox drop down lists
    lbl1 = ttk.Label(rn1, text = "Select Year 1 :",
          background = 'purple', foreground ="black", 
          font = ("Times New Roman", 10))
    lbl1.place(x=80, y=100)
          
    n = tk.StringVar()
    yearchoosen1 = ttk.Combobox(rn1, width = 27, textvariable = n)
    yearchoosen1['values'] = years
    yearchoosen1.current()
    yearchoosen1.place(x=180, y=100)

    # Year Selection 2 by creating labels, comboboxes & combobox drop down lists
    lbl2 = ttk.Label(rn1, text = "Select Year 2 :",
        background = 'purple', foreground ="black", 
          font = ("Times New Roman", 10))
    lbl2.place(x=80, y=155)

    n = tk.StringVar()
    yearchoosen2 = ttk.Combobox(rn1, width = 27, textvariable = n)
    yearchoosen2['values'] = years
    yearchoosen2.current()
    yearchoosen2.place(x=180, y=155)

    # Year Selection 3 by creating labels, comboboxes & combobox drop down lists
    lbl3 = ttk.Label(rn1, text = "Select Year 3 :",
          background = 'purple', foreground ="black",
          font = ("Times New Roman", 10))       
    lbl3.place(x=80, y=210)

    n = tk.StringVar()
    yearchoosen3 = ttk.Combobox(rn1, width = 27, textvariable = n)
    yearchoosen3['values'] = years
    yearchoosen3.current()
    yearchoosen3.place(x=180, y=210)

    
    # Year Selection 4 by creating labels, comboboxes & combobox drop down lists
    lbl4 = ttk.Label(rn1, text = "Select Year 4 :",
          background = 'purple', foreground ="black",
          font = ("Times New Roman", 10))       
    lbl4.place(x=80, y=265)

    n = tk.StringVar()
    yearchoosen4 = ttk.Combobox(rn1, width = 27, textvariable = n)
    yearchoosen4['values'] = years
    yearchoosen4.current()
    yearchoosen4.place(x=180, y=265)

        # Submit button function to make ComPlot
    def clickrn1():
        year1= yearchoosen1.get()
        year2= yearchoosen2.get()
        year3= yearchoosen3.get()
        year4=yearchoosen4.get()
        yearSelections = [year1, year2, year3,year4]

        makefourplot(yearSelections,'temperature')

    #Adding submit & exit buttons
    btn = Button(rn1,text="Submit", width=6, command=clickrn1)
    btn.place(x=185, y=300)

    btn1 = Button(rn1,text="Quit", width=6, command=rn1.destroy)
    btn1.place(x=285, y=300)

    rn1.mainloop()

def rn2():
    rn2 = Tk()
    rn2.title("Comparing Yearly Dew Point (° F)")
    rn2.configure(background="purple")
#App placement
    app_width = 500
    app_height = 450

    screen_width = rn2.winfo_screenwidth()
    screen_height = rn2.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    rn2.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    lbl0 = ttk.Label(rn2, text = "Comparing Yearly Dew Point (° F)", 
          background = 'purple', foreground ="black", 
          font = ("Times New Roman", 15))
    lbl0.place(x=100, y=20)

    # Year Selection 1 by creating labels, comboboxes & combobox drop down lists
    lbl1 = ttk.Label(rn2, text = "Select Year 1 :",
          background = 'purple', foreground ="black", 
          font = ("Times New Roman", 10))
    lbl1.place(x=80, y=100)
          
    n = tk.StringVar()
    yearchoosen1 = ttk.Combobox(rn2, width = 27, textvariable = n)
    yearchoosen1['values'] = years
    yearchoosen1.current()
    yearchoosen1.place(x=180, y=100)

    # Year Selection 2 by creating labels, comboboxes & combobox drop down lists
    lbl2 = ttk.Label(rn2, text = "Select Year 2 :",
        background = 'purple', foreground ="black", 
          font = ("Times New Roman", 10))
    lbl2.place(x=80, y=155)

    n = tk.StringVar()
    yearchoosen2 = ttk.Combobox(rn2, width = 27, textvariable = n)
    yearchoosen2['values'] = years
    yearchoosen2.current()
    yearchoosen2.place(x=180, y=155)

    # Year Selection 3 by creating labels, comboboxes & combobox drop down lists
    lbl3 = ttk.Label(rn2, text = "Select Year 3 :",
          background = 'purple', foreground ="black",
          font = ("Times New Roman", 10))       
    lbl3.place(x=80, y=210)

    n = tk.StringVar()
    yearchoosen3 = ttk.Combobox(rn2, width = 27, textvariable = n)
    yearchoosen3['values'] = years
    yearchoosen3.current()
    yearchoosen3.place(x=180, y=210)

    
    # Year Selection 4 by creating labels, comboboxes & combobox drop down lists
    lbl4 = ttk.Label(rn2, text = "Select Year 4 :",
          background = 'purple', foreground ="black",
          font = ("Times New Roman", 10))       
    lbl4.place(x=80, y=265)

    n = tk.StringVar()
    yearchoosen4 = ttk.Combobox(rn2, width = 27, textvariable = n)
    yearchoosen4['values'] = years
    yearchoosen4.current()
    yearchoosen4.place(x=180, y=265)

        # Submit button function to make ComPlot
    def clickrn2():
        year1= yearchoosen1.get()
        year2= yearchoosen2.get()
        year3= yearchoosen3.get()
        year4=yearchoosen4.get()
        yearSelections = [year1, year2, year3,year4]

        makefourplot(yearSelections,'temperature')

    #Adding submit & exit buttons
    btn = Button(rn2,text="Submit", width=6, command=clickrn2)
    btn.place(x=185, y=300)

    btn1 = Button(rn2,text="Quit", width=6, command=rn2.destroy)
    btn1.place(x=285, y=300)

    rn2.mainloop()

def rn3():
    rn3 = Tk()
    rn3.title("Comparing Yearly Dew Point (° F)")
    rn3.configure(background="purple")
#App placement
    app_width = 500
    app_height = 450

    screen_width = rn3.winfo_screenwidth()
    screen_height = rn3.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    rn3.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    lbl0 = ttk.Label(rn3, text = "Comparing Yearly Dew Point (° F)", 
          background = 'purple', foreground ="black", 
          font = ("Times New Roman", 15))
    lbl0.place(x=100, y=20)

    # Year Selection 1 by creating labels, comboboxes & combobox drop down lists
    lbl1 = ttk.Label(rn3, text = "Select Year 1 :",
          background = 'purple', foreground ="black", 
          font = ("Times New Roman", 10))
    lbl1.place(x=80, y=100)
          
    n = tk.StringVar()
    yearchoosen1 = ttk.Combobox(rn3, width = 27, textvariable = n)
    yearchoosen1['values'] = years
    yearchoosen1.current()
    yearchoosen1.place(x=180, y=100)

    # Year Selection 2 by creating labels, comboboxes & combobox drop down lists
    lbl2 = ttk.Label(rn3, text = "Select Year 2 :",
        background = 'purple', foreground ="black", 
          font = ("Times New Roman", 10))
    lbl2.place(x=80, y=155)

    n = tk.StringVar()
    yearchoosen2 = ttk.Combobox(rn3, width = 27, textvariable = n)
    yearchoosen2['values'] = years
    yearchoosen2.current()
    yearchoosen2.place(x=180, y=155)

    # Year Selection 3 by creating labels, comboboxes & combobox drop down lists
    lbl3 = ttk.Label(rn3, text = "Select Year 3 :",
          background = 'purple', foreground ="black",
          font = ("Times New Roman", 10))       
    lbl3.place(x=80, y=210)

    n = tk.StringVar()
    yearchoosen3 = ttk.Combobox(rn3, width = 27, textvariable = n)
    yearchoosen3['values'] = years
    yearchoosen3.current()
    yearchoosen3.place(x=180, y=210)

    
    # Year Selection 4 by creating labels, comboboxes & combobox drop down lists
    lbl4 = ttk.Label(rn3, text = "Select Year 4 :",
          background = 'purple', foreground ="black",
          font = ("Times New Roman", 10))       
    lbl4.place(x=80, y=265)

    n = tk.StringVar()
    yearchoosen4 = ttk.Combobox(rn3, width = 27, textvariable = n)
    yearchoosen4['values'] = years
    yearchoosen4.current()
    yearchoosen4.place(x=180, y=265)

        # Submit button function to make ComPlot
    def clickrn3():
        year1= yearchoosen1.get()
        year2= yearchoosen2.get()
        year3= yearchoosen3.get()
        year4=yearchoosen4.get()
        yearSelections = [year1, year2, year3,year4]

        makefourplot(yearSelections,'temperature')

    #Adding submit & exit buttons
    btn = Button(rn3,text="Submit", width=6, command=clickrn3)
    btn.place(x=185, y=300)

    btn1 = Button(rn3,text="Quit", width=6, command=rn3.destroy)
    btn1.place(x=285, y=300)

    rn3.mainloop()

def rn4():
    rn4 = Tk()
    rn4.title("Comparing Yearly Dew Point (° F)")
    rn4.configure(background="purple")
#App placement
    app_width = 500
    app_height = 450

    screen_width = rn4.winfo_screenwidth()
    screen_height = rn4.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    rn4.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    lbl0 = ttk.Label(rn4, text = "Comparing Yearly Dew Point (° F)", 
          background = 'purple', foreground ="black", 
          font = ("Times New Roman", 15))
    lbl0.place(x=100, y=20)

    # Year Selection 1 by creating labels, comboboxes & combobox drop down lists
    lbl1 = ttk.Label(rn4, text = "Select Year 1 :",
          background = 'purple', foreground ="black", 
          font = ("Times New Roman", 10))
    lbl1.place(x=80, y=100)
          
    n = tk.StringVar()
    yearchoosen1 = ttk.Combobox(rn4, width = 27, textvariable = n)
    yearchoosen1['values'] = years
    yearchoosen1.current()
    yearchoosen1.place(x=180, y=100)

    # Year Selection 2 by creating labels, comboboxes & combobox drop down lists
    lbl2 = ttk.Label(rn4, text = "Select Year 2 :",
        background = 'purple', foreground ="black", 
          font = ("Times New Roman", 10))
    lbl2.place(x=80, y=155)

    n = tk.StringVar()
    yearchoosen2 = ttk.Combobox(rn4, width = 27, textvariable = n)
    yearchoosen2['values'] = years
    yearchoosen2.current()
    yearchoosen2.place(x=180, y=155)

    # Year Selection 3 by creating labels, comboboxes & combobox drop down lists
    lbl3 = ttk.Label(rn4, text = "Select Year 3 :",
          background = 'purple', foreground ="black",
          font = ("Times New Roman", 10))       
    lbl3.place(x=80, y=210)

    n = tk.StringVar()
    yearchoosen3 = ttk.Combobox(rn4, width = 27, textvariable = n)
    yearchoosen3['values'] = years
    yearchoosen3.current()
    yearchoosen3.place(x=180, y=210)

    
    # Year Selection 4 by creating labels, comboboxes & combobox drop down lists
    lbl4 = ttk.Label(rn4, text = "Select Year 4 :",
          background = 'purple', foreground ="black",
          font = ("Times New Roman", 10))       
    lbl4.place(x=80, y=265)

    n = tk.StringVar()
    yearchoosen4 = ttk.Combobox(rn4, width = 27, textvariable = n)
    yearchoosen4['values'] = years
    yearchoosen4.current()
    yearchoosen4.place(x=180, y=265)

        # Submit button function to make ComPlot
    def clickrn4():
        year1= yearchoosen1.get()
        year2= yearchoosen2.get()
        year3= yearchoosen3.get()
        year4=yearchoosen4.get()
        yearSelections = [year1, year2, year3,year4]

        makefourplot(yearSelections,'temperature')

    #Adding submit & exit buttons
    btn = Button(rn4,text="Submit", width=6, command=clickrn4)
    btn.place(x=185, y=300)

    btn1 = Button(rn4,text="Quit", width=6, command=rn4.destroy)
    btn1.place(x=285, y=300)

    rn4.mainloop()
    
    from cProfile import label
import tkinter as tk
from tkinter import *
from tkinter import ttk
from unicodedata import decimal
import csv
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import statistics
from setuptools import Command

def getYearData(year, data_type, value_type):
    filename = 'FinallOneCSV.csv'
    with open(filename, 'r') as csvfile:
        datareader = csv.reader(csvfile)
        yearData = []
        for row in datareader:
            if row[0].find('Average'+str(year)) != -1:
                if(data_type == 'temperature'):
                    if(value_type == 'Maximum'):
                        yearData.append(float(row[2]))
                    elif(value_type == 'Average'):
                        yearData.append(float(row[3]))
                    elif(value_type == 'Minimum'):
                        yearData.append(float(row[4]))
                elif(data_type == 'DewPoint'):
                    if(value_type == 'Maximum'):
                        yearData.append(float(row[5]))
                    elif(value_type == 'Average'):
                        yearData.append(float(row[6]))
                    elif(value_type == 'Minimum'):
                        yearData.append(float(row[7]))
                elif(data_type == 'Humidity'):
                    if(value_type == 'Maximum'):
                        yearData.append(float(row[8]))
                    elif(value_type == 'Average'):
                        yearData.append(float(row[9]))
                    elif(value_type == 'Minimum'):
                        yearData.append(float(row[10]))
                elif(data_type == 'WindSpeed'):
                    if(value_type == 'Maximum'):
                        yearData.append(float(row[11]))
                    elif(value_type == 'Average'):
                        yearData.append(float(row[12]))
                    elif(value_type == 'Minimum'):
                        yearData.append(float(row[13]))
                elif(data_type == 'Pressure'):
                    if(value_type == 'Maximum'):
                        yearData.append(float(row[14]))
                    elif(value_type == 'Average'):
                        yearData.append(float(row[15]))
                    elif(value_type == 'Minimum'):
                        yearData.append(float(row[16]))
    return yearData


start = Tk()
start.title("n Menu")
start.configure(background="white")

    #App placement
app_width = 400
app_height = 350

screen_width = start.winfo_screenwidth()
screen_height = start.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

start.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
   
    #Label for Main Menu
mainlabel = ttk.Label(start, text = "\u0332".join("Main Menu"),
          background = 'white', foreground ="Black",
          font = ("Times New Roman", 15))      
mainlabel.place(x=130, y=10)


    # Finding max temp of a year
def findMaxValueYear(year_a, data_type):
    maxValueYear=[]
    for year in year_a:
        value_type = 'Maximum'
        year_a_data=getYearData(year, data_type, value_type)
        maxValueYear.append(max(year_a_data))

    return maxValueYear

# Finding mean temp of a year
def findMeanValueYear(year_a, data_type):
    meanValueYear=[]
    for year in year_a:
        value_type = 'Average'
        year_a_data=getYearData(year, data_type, value_type)
        meanValueYear.append(statistics.mean(year_a_data))

    return meanValueYear

# Finding min temp of a year
def findMinValueYear(year_a, data_type):
    minValueYear=[]
    for year in year_a:
        value_type = 'Minimum'
        year_a_data=getYearData(year, data_type, value_type)
        minValueYear.append(min(year_a_data))

    return minValueYear

def makefiveplot(year, data_type):

    # Getting max, mean and min values to plot
    maxValuesYear = findMaxValueYear(year, data_type)
    meanValuesYear = findMeanValueYear(year, data_type)
    minValuesYear = findMinValueYear(year, data_type)
   
    # Gathering better y axis labels that includes the measurements
    if (data_type=='temperature'):
        ylabel="Temperature (° F)"
    if (data_type=='DewPoint'):
        ylabel="Dew Point (° F)"
    if (data_type=='Humidity'):
        ylabel="Humidity (%)"
    if (data_type=='WindSpeed'):
        ylabel="Wind Speed (mph)"

    # Creating a figure and adding a title, y and x labels and a grid
    plt.figure(figsize=(12,5))
    plt.title(f"Comparing the maximum, mean & minimum {data_type} values of {year[0]}, {year[1]} , {year[2]}, {year[3]}& {year[4]}")
    plt.ylabel(ylabel)
    plt.xlabel('Years')
    plt.grid(axis= 'y')


    # Plotting
    plt.bar(year,maxValuesYear, s = 150, label="Maximum")
    plt.bar(year,meanValuesYear, s = 150, label="Mean")
    plt.bar(year,minValuesYear, s =150, label="Minimum")

    # Adding a legend
    plt.legend(bbox_to_anchor=(1.1, 1.05))

    plt.show()

years = ['2009','2010','2011','2012','2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']


def eb1():
    eb1 = Tk()
    eb1.title("Comparing Yearly Temperature (° F)")
    eb1.configure(background="white")
#App placement
    app_width = 500
    app_height = 450

    screen_width = eb1.winfo_screenwidth()
    screen_height = eb1.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    eb1.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    lbl0 = ttk.Label(eb1, text = "Comparing Yearly Temperature (° F)",
          background = 'white', foreground ="black",
          font = ("Times New Roman", 15))
    lbl0.place(x=100, y=20)

    # Year Selection 1 by creating labels, comboboxes & combobox drop down lists
    lbl1 = ttk.Label(eb1, text = "Select Year 1 :",
          background = 'white', foreground ="black",
          font = ("Times New Roman", 10))
    lbl1.place(x=80, y=100)
         
    n = tk.StringVar()
    yearchoosen1 = ttk.Combobox(eb1, width = 27, textvariable = n)
    yearchoosen1['values'] = years
    yearchoosen1.current()
    yearchoosen1.place(x=180, y=100)

    # Year Selection 2 by creating labels, comboboxes & combobox drop down lists
    lbl2 = ttk.Label(eb1, text = "Select Year 2 :",
        background = 'white', foreground ="black",
          font = ("Times New Roman", 10))
    lbl2.place(x=80, y=155)

    n = tk.StringVar()
    yearchoosen2 = ttk.Combobox(eb1, width = 27, textvariable = n)
    yearchoosen2['values'] = years
    yearchoosen2.current()
    yearchoosen2.place(x=180, y=155)

    # Year Selection 3 by creating labels, comboboxes & combobox drop down lists
    lbl3 = ttk.Label(eb1, text = "Select Year 3 :",
          background = 'white', foreground ="black",
          font = ("Times New Roman", 10))      
    lbl3.place(x=80, y=210)

    n = tk.StringVar()
    yearchoosen3 = ttk.Combobox(eb1, width = 27, textvariable = n)
    yearchoosen3['values'] = years
    yearchoosen3.current()
    yearchoosen3.place(x=180, y=210)

   
    # Year Selection 4 by creating labels, comboboxes & combobox drop down lists
    lbl4 = ttk.Label(eb1, text = "Select Year 4 :",
          background = 'white', foreground ="black",
          font = ("Times New Roman", 10))      
    lbl4.place(x=80, y=265)

    n = tk.StringVar()
    yearchoosen4 = ttk.Combobox(eb1, width = 27, textvariable = n)
    yearchoosen4['values'] = years
    yearchoosen4.current()
    yearchoosen4.place(x=180, y=265)

  # Year Selection 5 by creating labels, comboboxes & combobox drop down lists
    lbl4 = ttk.Label(eb1, text = "Select Year 5 :",
          background = 'white', foreground ="black",
          font = ("Times New Roman", 10))      
    lbl4.place(x=80, y=320)

    n = tk.StringVar()
    yearchoosen5 = ttk.Combobox(eb1, width = 27, textvariable = n)
    yearchoosen5['values'] = years
    yearchoosen5.current()
    yearchoosen5.place(x=180, y=320)

        # Submit button function to make ComPlot
    def clickeb1():
        year1= yearchoosen1.get()
        year2= yearchoosen2.get()
        year3= yearchoosen3.get()
        year4=yearchoosen4.get()
        year5=yearchoosen5.get()
        yearSelections = [year1, year2, year3,year4,year5]

        makefiveplot(yearSelections,'temperature')

    #Adding submit & exit buttons
    btn = Button(eb1,text="Submit", width=6, command=clickeb1)
    btn.place(x=185, y=365)

    btn1 = Button(eb1,text="Quit", width=6, command=eb1.destroy)
    btn1.place(x=285, y=365)

    eb1.mainloop()

def eb2():
    eb2 = Tk()
    eb2.title("Comparing Yearly Dew Point (° F)")
    eb2.configure(background="white")
#App placement
    app_width = 500
    app_height = 450

    screen_width = eb2.winfo_screenwidth()
    screen_height = eb2.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    eb2.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    lbl0 = ttk.Label(eb2, text = "Comparing Yearly Dew Point (° F)",
          background = 'white', foreground ="black",
          font = ("Times New Roman", 15))
    lbl0.place(x=100, y=20)

    # Year Selection 1 by creating labels, comboboxes & combobox drop down lists
    lbl1 = ttk.Label(eb2, text = "Select Year 1 :",
          background = 'white', foreground ="black",
          font = ("Times New Roman", 10))
    lbl1.place(x=80, y=100)
         
    n = tk.StringVar()
    yearchoosen1 = ttk.Combobox(eb2, width = 27, textvariable = n)
    yearchoosen1['values'] = years
    yearchoosen1.current()
    yearchoosen1.place(x=180, y=100)

    # Year Selection 2 by creating labels, comboboxes & combobox drop down lists
    lbl2 = ttk.Label(eb2, text = "Select Year 2 :",
        background = 'white', foreground ="black",
          font = ("Times New Roman", 10))
    lbl2.place(x=80, y=155)

    n = tk.StringVar()
    yearchoosen2 = ttk.Combobox(eb2, width = 27, textvariable = n)
    yearchoosen2['values'] = years
    yearchoosen2.current()
    yearchoosen2.place(x=180, y=155)

    # Year Selection 3 by creating labels, comboboxes & combobox drop down lists
    lbl3 = ttk.Label(eb2, text = "Select Year 3 :",
          background = 'white', foreground ="black",
          font = ("Times New Roman", 10))      
    lbl3.place(x=80, y=210)

    n = tk.StringVar()
    yearchoosen3 = ttk.Combobox(eb2, width = 27, textvariable = n)
    yearchoosen3['values'] = years
    yearchoosen3.current()
    yearchoosen3.place(x=180, y=210)

   
    # Year Selection 4 by creating labels, comboboxes & combobox drop down lists
    lbl4 = ttk.Label(eb2, text = "Select Year 4 :",
          background = 'white', foreground ="black",
          font = ("Times New Roman", 10))      
    lbl4.place(x=80, y=265)

    n = tk.StringVar()
    yearchoosen4 = ttk.Combobox(eb2, width = 27, textvariable = n)
    yearchoosen4['values'] = years
    yearchoosen4.current()
    yearchoosen4.place(x=180, y=265)

      # Year Selection 5 by creating labels, comboboxes & combobox drop down lists
    lbl4 = ttk.Label(eb2, text = "Select Year 5 :",
          background = 'white', foreground ="black",
          font = ("Times New Roman", 10))      
    lbl4.place(x=80, y=320)

    n = tk.StringVar()
    yearchoosen5 = ttk.Combobox(eb2, width = 27, textvariable = n)
    yearchoosen5['values'] = years
    yearchoosen5.current()
    yearchoosen5.place(x=180, y=320)

        # Submit button function to make ComPlot
    def clickeb2():
        year1= yearchoosen1.get()
        year2= yearchoosen2.get()
        year3= yearchoosen3.get()
        year4=yearchoosen4.get()
        year5=yearchoosen5.get()
        yearSelections = [year1, year2, year3,year4,year5]

        makefiveplot(yearSelections,'dew point')

    #Adding submit & exit buttons
    btn = Button(eb2,text="Submit", width=6, command=clickeb2)
    btn.place(x=185, y=365)

    btn1 = Button(eb2,text="Quit", width=6, command=eb2.destroy)
    btn1.place(x=285, y=365)


    eb2.mainloop()

def eb3():
    eb3 = Tk()
    eb3.title("Comparing Yearly Humidity")
    eb3.configure(background="white")
#App placement
    app_width = 500
    app_height = 450

    screen_width = eb3.winfo_screenwidth()
    screen_height = eb3.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    eb3.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    lbl0 = ttk.Label(eb3, text = "Comparing Yearly Humidty",
          background = 'purple', foreground ="black",
          font = ("Times New Roman", 15))
    lbl0.place(x=100, y=20)

    # Year Selection 1 by creating labels, comboboxes & combobox drop down lists
    lbl1 = ttk.Label(eb3, text = "Select Year 1 :",
          background = 'purple', foreground ="black",
          font = ("Times New Roman", 10))
    lbl1.place(x=80, y=100)
         
    n = tk.StringVar()
    yearchoosen1 = ttk.Combobox(eb3, width = 27, textvariable = n)
    yearchoosen1['values'] = years
    yearchoosen1.current()
    yearchoosen1.place(x=180, y=100)

    # Year Selection 2 by creating labels, comboboxes & combobox drop down lists
    lbl2 = ttk.Label(eb3, text = "Select Year 2 :",
        background = 'purple', foreground ="black",
          font = ("Times New Roman", 10))
    lbl2.place(x=80, y=155)

    n = tk.StringVar()
    yearchoosen2 = ttk.Combobox(eb3, width = 27, textvariable = n)
    yearchoosen2['values'] = years
    yearchoosen2.current()
    yearchoosen2.place(x=180, y=155)

    # Year Selection 3 by creating labels, comboboxes & combobox drop down lists
    lbl3 = ttk.Label(eb3, text = "Select Year 3 :",
          background = 'purple', foreground ="black",
          font = ("Times New Roman", 10))      
    lbl3.place(x=80, y=210)

    n = tk.StringVar()
    yearchoosen3 = ttk.Combobox(eb3, width = 27, textvariable = n)
    yearchoosen3['values'] = years
    yearchoosen3.current()
    yearchoosen3.place(x=180, y=210)

   
    # Year Selection 4 by creating labels, comboboxes & combobox drop down lists
    lbl4 = ttk.Label(eb3, text = "Select Year 4 :",
          background = 'purple', foreground ="black",
          font = ("Times New Roman", 10))      
    lbl4.place(x=80, y=265)

    n = tk.StringVar()
    yearchoosen4 = ttk.Combobox(eb3, width = 27, textvariable = n)
    yearchoosen4['values'] = years
    yearchoosen4.current()
    yearchoosen4.place(x=180, y=265)

# Year Selection 5 by creating labels, comboboxes & combobox drop down lists
    lbl4 = ttk.Label(eb3, text = "Select Year 5 :",
          background = 'purple', foreground ="black",
          font = ("Times New Roman", 10))      
    lbl4.place(x=80, y=320)

    n = tk.StringVar()
    yearchoosen5 = ttk.Combobox(eb3, width = 27, textvariable = n)
    yearchoosen5['values'] = years
    yearchoosen5.current()
    yearchoosen5.place(x=180, y=320)

        # Submit button function to make ComPlot
    def clickeb3():
        year1= yearchoosen1.get()
        year2= yearchoosen2.get()
        year3= yearchoosen3.get()
        year4=yearchoosen4.get()
        year5=yearchoosen5.get()
        yearSelections = [year1, year2, year3,year4,year5]

        makefiveplot(yearSelections,'Humidity')

    #Adding submit & exit buttons
    btn = Button(eb3,text="Submit", width=6, command=clickeb3)
    btn.place(x=185, y=365)

    btn1 = Button(eb3,text="Quit", width=6, command=eb3.destroy)
    btn1.place(x=285, y=365)


    eb3.mainloop()

def eb4():
    eb4 = Tk()
    eb4.title("Comparing Yearly wind Point speed")
    eb4.configure(background="white")
#App placement
    app_width = 500
    app_height = 450

    screen_width = eb4.winfo_screenwidth()
    screen_height = eb4.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    eb4.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    lbl0 = ttk.Label(eb4, text = "Comparing Yearly wind speed",
          background = 'purple', foreground ="black",
          font = ("Times New Roman", 15))
    lbl0.place(x=100, y=20)

    # Year Selection 1 by creating labels, comboboxes & combobox drop down lists
    lbl1 = ttk.Label(eb4, text = "Select Year 1 :",
          background = 'purple', foreground ="black",
          font = ("Times New Roman", 10))
    lbl1.place(x=80, y=100)
         
    n = tk.StringVar()
    yearchoosen1 = ttk.Combobox(eb4, width = 27, textvariable = n)
    yearchoosen1['values'] = years
    yearchoosen1.current()
    yearchoosen1.place(x=180, y=100)

    # Year Selection 2 by creating labels, comboboxes & combobox drop down lists
    lbl2 = ttk.Label(eb4, text = "Select Year 2 :",
        background = 'purple', foreground ="black",
          font = ("Times New Roman", 10))
    lbl2.place(x=80, y=155)

    n = tk.StringVar()
    yearchoosen2 = ttk.Combobox(eb4, width = 27, textvariable = n)
    yearchoosen2['values'] = years
    yearchoosen2.current()
    yearchoosen2.place(x=180, y=155)

    # Year Selection 3 by creating labels, comboboxes & combobox drop down lists
    lbl3 = ttk.Label(eb4, text = "Select Year 3 :",
          background = 'purple', foreground ="black",
          font = ("Times New Roman", 10))      
    lbl3.place(x=80, y=210)

    n = tk.StringVar()
    yearchoosen3 = ttk.Combobox(eb4, width = 27, textvariable = n)
    yearchoosen3['values'] = years
    yearchoosen3.current()
    yearchoosen3.place(x=180, y=210)

   
    # Year Selection 4 by creating labels, comboboxes & combobox drop down lists
    lbl4 = ttk.Label(eb4, text = "Select Year 4 :",
          background = 'purple', foreground ="black",
          font = ("Times New Roman", 10))      
    lbl4.place(x=80, y=265)

    n = tk.StringVar()
    yearchoosen4 = ttk.Combobox(eb4, width = 27, textvariable = n)
    yearchoosen4['values'] = years
    yearchoosen4.current()
    yearchoosen4.place(x=180, y=265)

    # Year Selection 5 by creating labels, comboboxes & combobox drop down lists
    lbl4 = ttk.Label(eb4, text = "Select Year 5 :",
          background = 'purple', foreground ="black",
          font = ("Times New Roman", 10))      
    lbl4.place(x=80, y=320)

    n = tk.StringVar()
    yearchoosen5 = ttk.Combobox(eb4, width = 27, textvariable = n)
    yearchoosen5['values'] = years
    yearchoosen5.current()
    yearchoosen5.place(x=180, y=320)

        # Submit button function to make ComPlot
    def clickeb4():
        year1= yearchoosen1.get()
        year2= yearchoosen2.get()
        year3= yearchoosen3.get()
        year4=yearchoosen4.get()
        year5=yearchoosen5.get()
        yearSelections = [year1, year2, year3,year4,year5]

        makefiveplot(yearSelections,'wind speed')

    #Adding submit & exit buttons
    btn = Button(eb4,text="Submit", width=6, command=clickeb4)
    btn.place(x=185, y=365)

    btn1 = Button(eb4,text="Quit", width=6, command=eb4.destroy)
    btn1.place(x=285, y=365)


    eb4.mainloop()

         #YEAR FIVE options
ml5 = ttk.Label(start, text = "Five Years",
          background = 'light green', foreground ="black",
          font = ("Times New Roman", 15))      
ml5.place(x=625, y=50)

btn14 = Button(start,text="Temperature (° F)", width=20, command=eb1)
btn14.place(x=120, y=100)

btn15 = Button(start,text="Dew Point (° F)", width=20, command=eb2)
btn15.place(x=120, y=150)

btn16 = Button(start,text="Humidity (%)", width=20, command=eb3)
btn16.place(x=120, y=200)

btn17 = Button(start,text="Wind Speed (mph)", width=20, command=eb4)
btn17.place(x=120, y=250)

start.mainloop()