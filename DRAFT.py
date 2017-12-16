pt3= input( 'please enter the closed price at day t3.')
pt1= input( 'please enter the closed price at day t1.')
returns = ( (pt3 - pt1)/pt1 )
if returns >= 0.1 :
    print ("buy")
elif returns < 0.1 and returns > -0.1 :
    print ("stay stable")
elif returns <= -0.1 :
    print ("sell")
else :
    print (" error")