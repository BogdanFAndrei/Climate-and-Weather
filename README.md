# Climate-and-Weather
Climate and Weather Report
This project helped me to see how it is to work in a team… which can be stressful sometimes the only constraints were working as a team as not everyone is used to work at the same rhythm with someone else, so we had small discussions about this in the beginning until the end when everyone started to work together on the program as the deadline was approaching fast. even though we chose the hardest topic with thousands of lines of data, however, I think managed to create an operational software program that meets the requirements of the project.

Project information:
We had to create a sophisticated program software that will allow the client to check the average of weather in Liverpool between certain periods of time. We already had all the information from the link below, after installing the excel file we had to create an algorithm that searches and extracts the exact information the user chose in the menu. 

Importing the data from the website into a CSV file
As a team, we gained information from this website https://en.tutiempo.net/climate about the climate in Liverpool over the years. Each of us had to extract 2 years of data (approximately 500 lines for each year). At the end of this task we ended up with roughly 6,000 lines of data. 
CSV File 
 
 
I’ve opened the CSV file in Microsoft VS Code and given the name to a variable so I can use it where I need it throughout the whole program without copying and pasting the address of the file repeatedly, this helps me to keep the program easy to understand decreasing the human error when another developer will want to make future changes on my code.

Tkinter library
 
I’ve implemented Tkinter as I thought at the beginning that’s the best idea to show our program to the audience. Instead of using text-oriented programming, we used object-oriented where the Tkinter library took place and helped us to achieve this. With Tkinter, I implemented the first menu our program had with two buttons, two dropdown menus that allowed the user to choose the year (between 2009 to 2020), and the value (Min-Max Average) letting the program know what this helping him to display the wanted graph.
 
The program had a rough start, the buttons weren’t working, the program couldn’t store the user’s input into a string variable allowing me to put it in a function and let the function find the data user’s wanted to display from the CSV file so I started researching on Google and nothing seemed to work properly so I had a meeting with the tutor and it was really helpful as he pointed me in the right direction and told me to look on a tutorial that he presented in the class. After researching the tutorial, I saw exactly what I needed for the program and implemented it, and everything turned out to work great.

Searching Algorithm + Function for user’s input
 
I’ve created a function that will use searching algorithms to look for the keyword ‘Average’ in the CSV file this lets the program store all the data that I want into one variable ‘yearData’ which is returned later. Alongside the algorithm, I implemented a feature to read the number after ‘Average’ from the CSV file this let me separate each year and used an if statement that allowed me to store only the wanted data such as if ‘data_type’ is ‘wind’ abbreviation from Wind Speed and ‘value_type’ is ‘Maximum’ the program will automatically find the 11th column in the CSV file and will take all the numbers and store them into array ‘yearData’ this helping me to make the graph later into the program. 
Function for plotting the graph
The program at the beginning didn’t have a long loop that will go through all the data that was depending on the user’s input in dropdown menus it had a lot of different functions that did the same but was not reading the searching algorithm wasn’t looking for the keyword ‘Average’ and the year depending on user’s input it was looking for the whole sentence for example ‘Average2020’ or ‘Average2019’ which didn’t let me loop it so I had to write repeatedly for each combination the user had in the drop-down menus getting to have 4000 lines of code just for this function I started researching more about how to loop it and I found the solution I used variables that will change every time the user will put a different input. Below I’ve attached two pictures before the update and after the update.
Before the update, the code’s only constraint was that couldn’t be used in the program for the feature that my colleagues were making (comparing two or three years) also, the code instead of having 1200 code lines of code will have 6000 which will make it hard to understand even for an experienced developer.
 
After the update, I have deleted the ‘with’ statement and placed all the plotting of the graph into a function allowing me to access it globally and be able to change it depending on the user’s input into the dropdown menus.
Another update that I had to make for this function is deleting the searching algorithm from it and putting it in another function that loops it until finds the right data that the user requires. 
 
Individual data visualizations 
Another update that I’ve implemented is the graph style I’ve created. I choose this style because it is easy to understand by the user and easy to maintain in case the user’s requirements will change in the future.  
Dropdown menus 
 
I’ve created a label for each dropdown menu letting the user know what to expect when he presses on the list. The ‘yearchoosen. current’ is set as a variable and stores the data that the user chooses from the dropdown menu allowing me to make the graph in another function.


This is what the user will see on the program
 
Functions for buttons
I’ve created this function to allow me to set the variable year_a, value_type that is found in the global function at the top of the program that finds the data that the user wants. Also, another variable that is declared below is “data_type” that I set to string ‘WindSpeed’ this lets the program know to go exactly to the Wind Speed line of code and to extract the data.
Afterward, I’ve called the function makePlot which is declared above the code with the three variables from this function.
 
 
Improvements
Future improvements that I can think of for this project will be a login page linked to a MySQL database allowing only the authorized personnel to use it from a business, also will help with keeping records of who is using this program and how.
Another feature that I would like to add is a feedback menu that will let the users send me emails or direct messages using the website developed for the program to tell me how their experience is with the program and how they are finding it and what future updates I can make to make it more user friendly.





This entire document reflects the work that I put into this project. 
© Bogdan-Florin Andrei
