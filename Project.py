import tkinter as tk
import re #reqular exprisson
from functools import partial
#####Working With File#######
# Searching in File
Check = False
def FileSearch(Fristequ, SecondEqu, Operation, Ruselt):
    global Check
    file = open("Math.txt", "r")
    Holder = str(Fristequ)+" " + str(Operation)+" " + str(SecondEqu)+" " + "=" + str(Ruselt) + "\n"
   #Serching in all File
    x = file.readlines()
    if Holder in x:
        Check = True
        print("yeah i found your word in file.")

    else:
        print("too bad there is  nothing.")
        Check=False
    #file.Close()


def fileworking(Fristequ, SecondEqu, Operation, Ruselt):
    file = open("Math.txt", "a")  # a for append
    file.write(Fristequ)
    file.write(" ")
    file.write(Operation)
    file.write(" ")
    file.write(SecondEqu)
    file.write(" ")
    file.write("=")
    file.write(str(Ruselt))
    file.write("\n")
    file.close()
    Check = False

##########End Of Working With File########

###Start Of String Procissing###

def ProsscingTheEqations(EquationToBePrccesed):
    MonoElements = list()

    for Element in re.findall('([+-]?) *([\d]*)([a-zA-Z]?)(?:\^(\d+))?',EquationToBePrccesed): #USING REQUALR EXPRISONS
        #findall(pattern, string, flags=0)
        #Return all non-overlapping matches of pattern in string, as a list of strings.
        #Explan The Exprsion (([+-]?) :Used to detect the + and - symbol )
        # \d When the UNICODE flag is not specified
        # ? Causes the resulting RE to match 0 or 1 repetitions of the preceding RE
        # [] Range of ASCII Code
        # ^ Matches the start of the string
        # * Causes the resulting RE to match 0 or more repetitions of the preceding RE, as many repetitions as are possible.
        # ?:   The first character after the '?' determines what the meaning and further syntax of the construct is.
        coeff, Symbol, Power = None, None, None #Nulllll
        #print(Element)
        #If  String Not Empty
        if Element != ('','','',''):
            #No Value of Coffinant
            if Element[1] == '':
                coeff = 1

            else:
                coeff = int(Element[1])
            if Element[0] == '-': coeff = - coeff
            if Element[3] == '':
                if Element[2] == '':
                    #If Only A Number(No Symbol)
                    Symbol = 'x'
                    Power = 0
                else:
                    Symbol = Element[2]
                    Power = 1
            else:
                Power = int(Element[3])
                Symbol = Element[2]
            #print ((coeff, Symbol, Power))
            #Adding At The End of the List
            MonoElements.append((coeff, Symbol, Power))

    return MonoElements

##End Of String Procissing##


##Start The Caculation##
def call_result_sum(label_result, n1, n2):
    global Check
    num1 = (n1.get())
    num2 = (n2.get())
    Generate = "+"
    result = ProsscingTheEqations(num1) + ProsscingTheEqations(num2)
    FileSearch(num1, num2, Generate, result)
    if Check == False:
     # prevernting The Re-Writing
     fileworking(num1, num2, Generate, result)
    print(result)

def call_result_Dif(label_result, n1, n2):
    global Check
    num1 = (n1.get())
    num2 = (n2.get())
    Generate = "-"
    result = ProsscingTheEqations(num1) + ProsscingTheEqations(num2)
    FileSearch(num1, num2, Generate, result)
    if Check == False:
     # prevernting The Re-Writing
     fileworking(num1, num2, Generate, result)
    print(result)

def call_result_Muli (Label_result,n1,n2):
    global Check
    num1 = (n1.get())
    num2 = (n2.get())
    Generate = "*"
    result = ProsscingTheEqations(num1) + ProsscingTheEqations(num2)
    FileSearch(num1, num2, Generate, result)
    if Check == False:
     # prevernting The Re-Writing
     fileworking(num1, num2, Generate, result)
    print(result)



##Ending of Caculation

######Starting The Gui Code#####
# Adjusting Layout
App = tk.Tk()
App.geometry('400x200+500+200')
App.title('Polynomial calculator')

# Varibles for Equations
FristEquation = tk.StringVar()
SecondEquation = tk.StringVar()

#labelTitle = tk.Label(App, text="Polynomial calculator").grid(row=0, column=2)
LabeelInfo = tk.Label(App, text = "Enter of Format EX: x^2+2y+5").grid(row = 0 , column =0)
labelNum1 = tk.Label(App, text="Enter The Frist Equation").grid(row=1, column=0)
labelNum2 = tk.Label(App, text="Enter The Second Equation").grid(row=2, column=0)
labelResult = tk.Label(App)
#The Answer Will Be Displayed Here!!
labelResult.grid(row=7, column=2)

entryNum1 = tk.Entry(App, textvariable=FristEquation).grid(row=1, column=2)
entryNum2 = tk.Entry(App, textvariable=SecondEquation).grid(row=2, column=2)
call_result_sum = partial(call_result_sum, labelResult, FristEquation, SecondEquation)
buttonSum = tk.Button(App,fg="blue", text="Sum", command=call_result_sum).grid(row=3, column=2)
call_result_Dif = partial(call_result_Dif, labelResult, FristEquation, SecondEquation)
buttonDif = tk.Button(App,fg="red", text="Substract", command=call_result_Dif).grid(row=4, column=2)
call_result_Muli = partial(call_result_Muli, labelResult, FristEquation, SecondEquation)
buttonMuli = tk.Button(App,fg="green", text="multiply", command=call_result_Muli).grid(row=5, column=2)
# App Runnig
App.mainloop()
############################################End of GUI PART#################