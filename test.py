def FileSearch(Fristequ, SecondEqu, Operation, Ruselt):
    global Check
    file = open("Math.txt", "r")
    Holder = str(Fristequ)+" " + str(Operation)+" " + str(SecondEqu)+" " + "=" + str(Ruselt) + "\n"
    Splitter = str(Fristequ)+" " + str(Operation)+" " + str(SecondEqu)+" "
   #Serching in all File
    x = file.readlines()
    if Holder in x:
        Check = True
        searchingfile = open('Math.txt', 'r')
        print("yeah i found your word in file.")
        for Looking in searchingfile:
             sp = Looking.split('=')
             if Splitter ==sp[0]:
                 return sp[1]

    else:
        print("too bad there is  nothing.")
        Check=False
    #file.Close()


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
    elif Check==True:
     x= FileSearch(num1, num2, Generate, res)

    a= str(res)
     a= Removing_Symbols_From_String(a)
     Label_result.config(text="Result is " + a)
     print(res)