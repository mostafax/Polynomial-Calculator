eq1= '5x+10x+3y+30'
eq2='-7x+7y+10-20'
sy ='+'
tot =eq1+' '+sy+' '+eq2+' '
print(tot)

searchingfile= open('Math.txt', 'r')
for line in searchingfile:
  x= line.split('=')
  if tot== x[0]:
     print (x[1])

     #WOrKINGGG


