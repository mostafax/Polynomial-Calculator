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


class term:
    coff = 0

    sub_term = ""

    power = list()

    symbol = ""

    def __init__(self):

        self.coff = 0

        self.sub_term = " "

        self.symbol = ""

        self.power = []

    def get_coff(self):

        if self.sub_term[0] != '-':
            if ord(self.sub_term[0]) >= 65 and ord(self.sub_term[0]) <= 90 or ord(self.sub_term[0]) >= 97 and ord(
                    self.sub_term[0]) <= 122:
                self.coff = 1
                return self.coff

        if self.sub_term[0] == '-':

            for i in range(1, len(self.sub_term)):
                if ord(self.sub_term[1]) >= 65 and ord(self.sub_term[1]) <= 90 or ord(
                        self.sub_term[1]) >= 97 and ord(self.sub_term[1]) <= 122:
                    self.coff = -1
                    return self.coff
                if ord(self.sub_term[i]) >= 65 and ord(self.sub_term[i]) <= 90 or ord(
                        self.sub_term[i]) >= 97 and ord(self.sub_term[i]) <= 122:
                    break
                else:

                    self.coff *= 10

                    self.coff += ord(self.sub_term[i]) - 48

            self.coff *= -1
            return self.coff


        else:

            for i in range(len(self.sub_term)):

                if ord(self.sub_term[i]) >= 65 and ord(self.sub_term[i]) <= 90 or ord(
                        self.sub_term[i]) >= 97 and ord(self.sub_term[i]) <= 122:

                    break

                else:

                    self.coff *= 10

                    self.coff += ord(self.sub_term[i]) - 48
            return self.coff

    def get_symbol(self):

        for i in range(len(self.sub_term)):

            if ord(self.sub_term[i]) >= 65 and ord(self.sub_term[i]) <= 90 or ord(self.sub_term[i]) >= 97 and ord(
                    self.sub_term[i]) <= 122:
                self.symbol += self.sub_term[i]

        self.symbol += "1"
        self.symbol += "1"

        return self.symbol

    def get_power(self):

        pow_of_var1 = 0

        pow_of_var2 = 0

        flag1 = False

        flag2 = False

        test = False

        count = 0

        for i in range(len(self.sub_term)):

            if ord(self.sub_term[i]) >= 65 and ord(self.sub_term[i]) <= 90 or ord(self.sub_term[i]) >= 97 and ord(
                    self.sub_term[i]) <= 122:
                count += 1

            if self.sub_term[i] == '^':

                if count == 2:
                    test = True

                flag = False

                flag1 = True

                for j in range(i + 1, len(self.sub_term)):

                    if self.sub_term[j] == '^':

                        flag2 = True

                        for k in range(j + 1, len(self.sub_term)):
                            pow_of_var2 *= 10

                            pow_of_var2 += ord(self.sub_term[k]) - 48

                        flag = True

                        break

                    else:

                        if not ord(self.sub_term[j]) >= 65 and ord(self.sub_term[j]) <= 90 or not ord(
                                self.sub_term[j]) >= 97 and ord(self.sub_term[j]) <= 122:
                            pow_of_var1 *= 10

                            pow_of_var1 += ord(self.sub_term[j]) - 48

                if (flag is True):
                    break

        if (flag1 is False) and (flag2 is False):

            if count == 1:

                pow_of_var1 = 1

            elif count == 2:

                pow_of_var2 = 1

                pow_of_var1 = 1

            else:

                pow_of_var2 = 0

                pow_of_var1 = 0

        if (flag1 is True) and (flag2 is False):

            if count == 2:

                pow_of_var2 = 1

            else:

                pow_of_var2 = 0

        if (test is True):
            self.power.append(pow_of_var2)

            self.power.append(pow_of_var1)

            return self.power

        self.power.append(pow_of_var1)

        self.power.append(pow_of_var2)

        return self.power


def caller(z):
    a = term()

    a.sub_term = z

    a.coff = a.get_coff()

    a.symbol = a.get_symbol()

    a.power = a.get_power()

    result = ""

    result = ((a.coff, a.symbol[0], a.power[0], a.symbol[1], a.power[1]))

    return result


def find_term(x):
    y = list()
    y = x
    for i in range(len(x)):

        if x[i] == "-" and x[0][0] != "-":
            y = x.replace('-', '+-')

    return y


def split_term(x):
    x2 = list()

    x2 = [0]

    x2 = x.split("+")

    return x2


def arragment_term(x):
    y = list()

    coff = 0

    pow1 = 0

    pow2 = 0

    var = ''

    var2 = ''

    for i in range(0, len(x)):

        coff = x[i][0]

        pow1 = x[i][2]

        pow2 = x[i][4]

        var = x[i][1]

        var2 = x[i][3]

        if ord(var) > ord(var2):

            temp1 = var

            var = var2

            var2 = temp1

            temp2 = pow1

            pow1 = pow2

            pow2 = temp2

            y.append((coff, var, pow1, var2, pow2))

        else:

            y.append(x[i])

    return y


def make_term(y):
    terms_of_equ = list()

    for i in range(len(y)):
        terms_of_equ.append((caller(y[i])))

    return terms_of_equ

def ProsscingTheEqations(EquationToBePrccesed):

  equ = EquationToBePrccesed

  equ1 = find_term(equ)

  equ_after_split = split_term(equ1)

  terms_equ = make_term(equ_after_split)

  equ_after_arragment = arragment_term(terms_equ)

  return equ_after_arragment


##End Of String Procissing##
def contact(eq):

    final_result = list()

    result = eq

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


#final display
def display(eq):
    final = eq
    string_final = " "
    for i in range(0, len(final)):

        if (final[i][0] != 0):

            if (final[i][0] > 0 and i != 0):
                string_final += "+"
            string_final += str(final[i][0])
            if (final[i][1] != '1'):
                string_final += str(final[i][1])
            if (final[i][2] != 0):
                if (final[i][2] == 1):
                    string_final += str(final[i][2])
                else:
                    string_final += "^"
                    string_final += str(final[i][2])
            if (final[i][3] != '1'):
                string_final += str(final[i][3])
            if (final[i][4] != 0):
                if (final[i][4] != 1):
                    string_final += "^"
                    string_final += str(final[i][4])
        else:
            string_final="0"
    return string_final

##Start The Caculation##

def add(eq1, eq2):
    removed=list()
    removed2=list()
    result=list()
    eq1=contact(eq1)
    eq2=contact(eq2)
    for i in range(len(eq1)):
        for j in range(len(eq2)):
            if eq1[i][1] == eq2[j][1] and eq1[i][2] == eq2[j][2] and eq1[i][3] == eq2[j][3 ] and eq1[i][4] == eq2[j][4]:

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
    FileSearch(num1, num2, Generate, result)
    if Check == False:
     # prevernting The Re-Writing
     fileworking(num1, num2, Generate, result)
    a = res
    a = display(a)
    label_result.config(text="Result is " + a)


def calc_diff(MonoElements,MonoElements2):
 result=list()
 last_result=list()
 seet=set()
 if MonoElements==[]:
     MonoElements.append((0,0,0,0,0))
 if MonoElements2 == []:
     MonoElements2.append((0, 0, 0, 0, 0))

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
    if c==MonoElements_size:
       result.append((-MonoElements2[x][0], MonoElements2[x][1], MonoElements2[x][2],
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
    if c==MonoElements2_size:
       #result.append((MonoElements2[x][0], MonoElements2[x][1], MonoElements2[x][2],
        #           MonoElements2[x][3], MonoElements2[x][4]))
       result.append((MonoElements[z][0], MonoElements[z][1], MonoElements[z][2],
                   MonoElements[z][3], MonoElements[z][4]))
 length = len(result)
 for x in range(0,length):  # from x because we(-)to x and to length-x because the length will decrease by the the elements we (-) it
           coafficient = result[x][0]
           symbol = result[x][1]
           power = result[x][2]
           symbol2 = result[x][3]
           power2 = result[x][4]
           if coafficient == 0:
             #  coafficient = 0
               symbol = ""
               power = ""
               symbol2 = ""
               power2 = ""
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
    result = contact(result)
    result2 = contact(result2)
    res = calc_diff(result,result2)
    FileSearch(num1, num2, Generate, res)
    if Check == False:
     # prevernting The Re-Writing
     fileworking(num1, num2, Generate, res)
    a = res
    a = display(a)
    label_result.config(text="Result is " + a)


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
    a= res
    a= display(a)
    Label_result.config(text="Result is " + a)


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
