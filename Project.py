import tkinter as tk
from functools import partial

#read file
def fileworking(Fristequ,SecondEqu,Operation,Ruselt):
 file= open("Math.txt","w")
 file.write(Fristequ)
 file.write("\t")
 file.write(Operation)
 file.write("\t")
 file.write(SecondEqu)
 file.write("\t")
 file.write("=")
 file.write(str(Ruselt))
 file.write("\n")
 file.close()

def call_result_sum(label_result, n1, n2):
    num1 = (n1.get())
    num2 = (n2.get())
    Generate="+"
    result = int(num1) + int(num2)
    fileworking(num1,num2,Generate,result)
    label_result.config(text="Result is %d" % result)
    return
def call_result_Dif(label_result, n1, n2):
    num1 = (n1.get())
    num2 =(n2.get())
    Generate="-"
    result = int(num1) - int(num2)
    fileworking(num1,num2,Generate,result)

    label_result.config(text="Result is %d" % result)


#Adjusting Layout
App = tk.Tk()
App.geometry('400x200+500+200')
App.title('Polynomial calculator')

#Varibles for Equations
number1 = tk.StringVar()
number2 = tk.StringVar()

labelTitle = tk.Label(App, text="Polynomial calculator").grid(row=0, column=2)
labelNum1 = tk.Label(App, text="Enter The Frist Equation").grid(row=1, column=0)
labelNum2 = tk.Label(App, text="Enter The Second Equation").grid(row=2, column=0)
labelResult = tk.Label(App)
labelResult.grid(row=7, column=2)

entryNum1 = tk.Entry(App, textvariable=number1).grid(row=1, column=2)
entryNum2 = tk.Entry(App, textvariable=number2).grid(row=2, column=2)
call_result_sum = partial(call_result_sum, labelResult, number1, number2)
buttonSum = tk.Button(App, text="Sum", command=call_result_sum).grid(row=3, column=2)
call_result_Dif = partial(call_result_Dif,labelResult, number1, number2)
buttonDif = tk.Button(App,text="Substract", command=call_result_Dif).grid(row = 4,column = 2)


#App Runnig
App.mainloop()
##################################################End of GUI PART#################
