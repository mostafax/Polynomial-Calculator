def Cacl_diff(MonoElements,MonoElements2):
 result=list()
 last_result=list()

 MonoElements_size=len(MonoElements)#get length of first list
 MonoElements2_size=len(MonoElements2)#get length of second list

 if MonoElements_size >= MonoElements2_size:#compare between size of two lists
    for x in range (0,MonoElements_size-1):
     if MonoElements[x][1] == MonoElements2[x][1] and MonoElements[x][2] == MonoElements2[x][2] and \
                   MonoElements[x][3] == MonoElements2[x][3] and MonoElements[x][4] == MonoElements2[x][4]:#check if coafficient equal coafficient symbol equal symbol and power equal power and symbol2 equal symbol2 and power2 equal power2
       #print(int(MonoElements[x][0])-int(MonoElements2[x][0]))
       result.append(((int(MonoElements[x][0])-int(MonoElements2[x][0])),MonoElements[x][1],MonoElements2[x][2],MonoElements[x][3],MonoElements2[x][4]))
    for x in range(0, 2):
     coafficient=result[x][0]
     symbol=result[x][1]
     power=result[x][2]
     symbol2=result[x][3]
     power2=result[x][4]
     last_result.append((coafficient,symbol,power,symbol2,power2))
    return last_result
 #print(last_result)
 else:
  for x in range (0,MonoElements2_size-1):
     if MonoElements[x][1] == MonoElements2[x][1] and MonoElements[x][2] == MonoElements2[x][2] and \
                    MonoElements[x][3] == MonoElements2[x][3] and MonoElements[x][4] == MonoElements2[x][4]:
       #print(int(MonoElements[0][0]) - int(MonoElements2[0][0]))
       result.append(((int(MonoElements[x][0]) - int(MonoElements2[x][0])), MonoElements[x][1], MonoElements2[x][2],
                      MonoElements[x][3], MonoElements2[x][4]))
  for x in range(0, 2):
    coafficient=result[x][0]
    symbol=result[x][1]
    power=result[x][2]
    symbol2=result[x][3]
    power2=result[x][4]
    last_result.append((coafficient,symbol,power,symbol2,power2))
 return last_result
