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

    for Element in re.findall('([+-]?) *([\d]*)([a-zA-Z]?)(?:\^(\d+))? *([a-zA-Z]?)(?:\^(\d+))?',EquationToBePrccesed): #USING REQUALR EXPRISONS
        #findall(pattern, string, flags=0)
        #Return all non-overlapping matches of pattern in string, as a list of strings.
        #Explan The Exprsion (([+-]?) :Used to detect the + and - symbol )
        # \d When the UNICODE flag is not specified
        # ? Causes the resulting RE to match 0 or 1 repetitions of the preceding RE
        # [] Range of ASCII Code
        # ^ Matches the start of the string
        # * Causes the resulting RE to match 0 or more repetitions of the preceding RE, as many repetitions as are possible.
        # ?:   The first character after the '?' determines what the meaning and further syntax of the construct is.
        coeff, Symbol, Power ,Symbol2, Power2 = None, None, None,None,None #Nulllll

        #print(Element)
        #If  String Not Empty
        if Element != ('','','','','',''):
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
            if Element[5] == '':
                if Element[4] == '':
                    # If Only A Number(No Symbol)
                    Symbol2 = 'y'
                    Power2 = 0
                else:
                    Symbol2 = Element[4]
                    Power2 = 1
            else:
                Power2 = int(Element[5])
                Symbol2 = Element[4]

            #Adding At The End of the List
            if Symbol>Symbol2:
                #Swaping Low
                temp2 = Power
                Power = Power2
                Power2 = temp2
                temp = Symbol
                Symbol =Symbol2
                Symbol2 = temp

            MonoElements.append((coeff, Symbol, Power,Symbol2,Power2))


    return MonoElements

##End Of String Procissing##

def Removing_Symbols_From_String(OneString):
    Chars_To_Remove = ['(',',', ']', '[', ' ',')']
    # a=a.translate(None,''.join(Chars_To_Remove)) Python 2.7
    OneString = OneString.replace(")","+")
    OneString = OneString.translate(str.maketrans('', '', ''.join(Chars_To_Remove)))
    OneString = OneString[0:-1]
    OneString = OneString.replace("+-", "-")
    OneString = OneString.replace("'", "")
    '''''
    f = len(OneString)
    for x in  range(0,f):
     if x <= f+4:
        if OneString[x]=='0':
            if OneString[x+1] >= 'A' and OneString[x+1]<='z':
                if OneString[x+2]==0:
                    if OneString[x + 3] >='A' and OneString[x + 3] < 'z':
                        if OneString[x+4]==0:
                            OneString = OneString.replace(OneString[x:x+4],"")

'''
    return OneString


##Start The Caculation##

def add(eq1, eq2):
    #list1 = eq1
    list2 = eq2
    size1 = len(eq1)
    size2 = len(eq2)
    removed=list()
    removed2=list()
    result=list()

    for i in range(0, size1):
        for j in range(0, size2):
            if eq1[i][1] == eq2[j][1] and eq1[i][2] == eq2[j][2] and eq1[i][3] == eq2[j][3 ] and eq1[i][
                4] == eq2[j][4]:
                x=(eq1[i][0] + eq2[j][0])
                result.append((x,eq1[i][1],eq1[i][2],eq1[i][3],eq1[i][4]))
                removed.append(eq2[j])
                removed2.append(eq1[i])


    for i in range(len(eq2)):
        check=True
        for j in range(len(removed)):
            if removed[j]== eq2[i]:
                check=False
        if (check==True):
             result.append(eq2[i])


    for i in range(len(eq1)):
        check=True
        for j in range(len(removed2)):
            if removed2[j]== eq1[i]:
                check=False
        if (check==True):
             result.append(eq1[i])


    for j in range(len(result)):
        if result[j][0]==0:
            result[j]=[0,0,0,0,0]


    return (result)

def call_result_sum(label_result, n1, n2):
    global Check
    num1 = (n1.get())
    num2 = (n2.get())
    Generate = "+"
    result = ProsscingTheEqations(num1)
    result2 = ProsscingTheEqations(num2)
    res =  add(result,result2)
    print(res)
    FileSearch(num1, num2, Generate, result)
    if Check == False:
     # prevernting The Re-Writing
     fileworking(num1, num2, Generate, result)
    print(result)
    a = str(res)
    a = Removing_Symbols_From_String(a)
    label_result.config(text="Result is " + a)
    print(res)


def calc_diff(MonoElements,MonoElements2):
 result=list()
 last_result=list()
 seet=set()
 MonoElements_size=len(MonoElements)#get length of first list
 MonoElements2_size=len(MonoElements2)#get length of second list

 for x in range(0, MonoElements2_size):
  c = 0
  for z in range(0, MonoElements_size):

    if MonoElements[z][1] == MonoElements2[x][1] and MonoElements[z][2] == MonoElements2[x][2] and \
                     MonoElements[z][3] == MonoElements2[x][3] and MonoElements[z][4] == MonoElements2[x][4]:
         result.append(((int(MonoElements[z][0]) - int(MonoElements2[x][0])), MonoElements[z][1], MonoElements[z][2],
                        MonoElements[z][3], MonoElements[z][4]))
         break
    else:
         c+=1
         #print(c)
         #print(result)
    if (c==MonoElements_size-1 and MonoElements_size!=1)or(c==MonoElements_size and MonoElements_size ==1):
       result.append((MonoElements2[x][0], MonoElements2[x][1], MonoElements2[x][2],
                   MonoElements2[x][3], MonoElements2[x][4]))
       #result.append((MonoElements[z][0], MonoElements[z][1], MonoElements[z][2],
         #          MonoElements[z][3], MonoElements[z][4]))

#print(result)
 for z in range(0, MonoElements_size):
  c = 0
  for x in range(0, MonoElements2_size):
    if MonoElements[z][1] == MonoElements2[x][1] and MonoElements[z][2] == MonoElements2[x][2] and \
                     MonoElements[z][3] == MonoElements2[x][3] and MonoElements[z][4] == MonoElements2[x][4]:
         result.append(((int(MonoElements[z][0]) - int(MonoElements2[x][0])), MonoElements[z][1], MonoElements[z][2],
                        MonoElements[z][3], MonoElements[z][4]))
         break
    else:
         c+=1
         #print(MonoElements[z][0])
         #print(result)
    if (c==MonoElements2_size-1 and MonoElements2_size!=1)or(c==MonoElements2_size and MonoElements2_size == 1):
       #result.append((MonoElements2[x][0], MonoElements2[x][1], MonoElements2[x][2],
        #           MonoElements2[x][3], MonoElements2[x][4]))
       result.append((MonoElements[z][0], MonoElements[z][1], MonoElements[z][2],
                   MonoElements[z][3], MonoElements[z][4]))
 length = len(result)
 for x in range(0,length):  # from x because we(-)to x and to length-x because the length will decrease by the the elements we (-) it
           coafficient = result[x][0]
           symbol=result[x][1]
           power = result[x][2]
           symbol2 = result[x][3]
           power2 = result[x][4]
           if coafficient == 0:
             #  coafficient = 0
               symbol = "0"
               power = "0"
               symbol2 = "0"
               power2 = "0"
           last_result.append((coafficient, symbol, power, symbol2, power2))
           t=tuple(last_result)
           sett=set(t)

 #print(sett)
 return sorted(sett,reverse=True)


def call_result_Dif(label_result, n1, n2):
    global Check
    num1 = (n1.get())
    num2 = (n2.get())
    Generate = "-"
    result = ProsscingTheEqations(num1)
    result2 = ProsscingTheEqations(num2)
    res = calc_diff(result,result2)
    FileSearch(num1, num2, Generate, res)
    if Check == False:
     # prevernting The Re-Writing
     fileworking(num1, num2, Generate, res)
    a = str(res)
    a = Removing_Symbols_From_String(a)
    label_result.config(text="Result is " + a)
    print(res)


def calc_multi(eq1, eq2):
    list1 = eq1
    list2 = eq2
    size1 = len(list1)
    size2 = len(list2)
    result = list()
    check = False
    for i in range(0, size1):
        for j in range(0, size2):
            if (list1[i][0] == 0 and list2[j][0] == 0):
                a = 0
                b = 0
                c = 0
                d = 0
                e = 0
            else:
                a = list1[i][0] * list2[j][0]
                if (list1[i][1] == list2[j][1]):
                    b = list1[i][1]
                elif (list1[i][1] == '1' and list2[j][1] != '1'):

                    b = list2[j][1]
                elif (list1[i][1] != '1' and list2[j][1] == '1'):
                    b = list1[i][1]

                c = list1[i][2] + list2[j][2]
                if (list1[i][3] == list2[j][3]):
                    d = list1[i][3]
                elif (list1[i][3] == '1' and list2[j][3] != '1'):
                    d = list2[j][3]
                elif (list1[i][3] != '1' and list2[j][3] == '1'):
                    d = list1[i][3]
                elif (list1[i][3] != '1' and list2[j][3] != '1' and list1[i][3] != list2[j][3]):
                    s = list1[i][1]
                    r = list2[j][3]
                    c = list1[i][4]
                    check = True
                    e = list2[j][4]
                    if (s < r):
                        b = s
                        d = r
                if (check != True):
                    e = list1[i][4] + list2[j][4]
            result.append((a, b, c, d, e))

    final_result = list()

    for i in range(0, len(result)):
        sum1 = 0
        temp = 0
        found = False
        for j in range(0, len(result)):

            if (i != j):
                if result[i][2] == result[j][2] and result[i][4] == result[j][4]:
                    sum1 += int(result[i][0]) + int(result[j][0])
                    found = True
                    result[j] = ('2', '2', '2', '2', '2')
                    temp = temp + 1
        if (found == True):
            for k in range(0, temp - 1):
                sum1 = sum1 - int(result[i][0])
            if (sum1 != '2' and result[i][1] != '2' and result[i][2] != '2' and result[i][3] != '2' and result[i][
                4] != '2'):
                if (sum1 != 0):
                    final_result.append((sum1, result[i][1], result[i][2], result[i][3], result[i][4]))
        else:
            if (result[i][0] != '2' and result[i][1] != '2' and result[i][2] != '2' and result[i][3] != '2' and
                        result[i][4] != '2'):
                if (result[i][0] != 0):
                    final_result.append((result[i][0], result[i][1], result[i][2], result[i][3], result[i][4]))

    return final_result


def call_result_Muli (Label_result,n1,n2):
    global Check
    num1 = (n1.get())
    num2 = (n2.get())
    Generate = "*"
    result = ProsscingTheEqations(num1)
    result2 = ProsscingTheEqations(num2)
    #print(result+result2)
    res = calc_multi(result,result2)
    #print(x)
    FileSearch(num1, num2, Generate, res)
    if Check == False:
     # prevernting The Re-Writing
     fileworking(num1, num2, Generate, res)
    a= str(res)
    a= Removing_Symbols_From_String(a)
    Label_result.config(text="Result is " + a)
    print(res)


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
