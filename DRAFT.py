
def Removing_Symbols_From_String(OneString):

    Chars_To_Remove = ['(',',', ']', '[', ' ',')']
    # a=a.translate(None,''.join(Chars_To_Remove)) Python 2.7
    OneString = OneString.replace(")","+")
    OneString = OneString.translate(str.maketrans('', '', ''.join(Chars_To_Remove)))
    OneString = OneString[0:-1]
    OneString = OneString.replace("+-", "-")
    OneString = OneString.replace("'", "")
    print(OneString)
    g = list(OneString)
    l = list()
    f = len(OneString)
    for x in range(0,f):
     #if f+2>=x:
        if OneString[x]=='0':
            if (g[x-1]>=str('A')and g[x-1]<=str('z')):
                f-= 1
                print(g[x-1])
                g[x-1] = ''
                g[x]=''

    OneString ="".join(g)


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
eq1= '''[(35, 'x', 0, 'y', 0), (10, 'x', 20, 'y', 20)]'''

print(Removing_Symbols_From_String(eq1))