import math
outrange  = input().split()
def Divisores(item):
  values =[]
  max=  math.sqrt(item)
  for i in range(2,int(round(max))):
    if(values.__contains__(i)):
      continue
    else :  
      X= item/i
      if (X - int(X)==0):
        values.append(i)
        values.append(int(X))
      X=0
  return values

def new_range(item):
  values =[-1,-1]
  X= 0
  for i in range(int(item[0]),int(item[1])+1):
    if(X==0):
      if(values[0]!= -1):
        if(sum(Divisores(int(item[1])))>int(item[1])):
          values[1]=int(item[1])
          break
        X=1

    if(sum(Divisores(i))>i):
      if(values[0] == -1):
        values[0] = i
      else:
        values[1]=i
    else:
      continue
  if(values[1] ==-1):
    values[0]=-1
  return str(values[0]) +" "+str(values[1])

print (new_range(outrange))








    
  


