heroes = list( map(int,input().split()))
villanos = list( map(int, input().split()))


def ganar(H,V):
  values =[-1,-1,-1]
  HMY = BuscarMayor(H,-1,-1)
  VMY = BuscarMayor(V,-1,-1)
  HMD = BuscarMayor(H,HMY[0],-1)
  VMD = BuscarMayor(V,VMY[0],-1)
  HMN = BuscarMayor(H,HMY[0],HMD[0])
  VMN = BuscarMayor(V,VMY[0],VMD[0])
  if(HMY[1]<=VMY[1]):
    values[HMY[0]] = (VMD[0])+1
    values[HMD[0]] = (VMN[0])+1
    values[HMN[0]] = (VMY[0])+1
   
  elif(VMD[1]>= HMD[1]):
    values[HMY[0]] = (VMY[0])+1
    values[HMD[0]] = (VMN[0])+1
    values[HMN[0]] = (VMD[0])+1
  else:
    values[HMY[0]] = (VMY[0])+1
    values[HMN[0]] = (VMN[0])+1
    values[HMD[0]] = (VMD[0])+1
  return values

def BuscarMayor(item, index_1,index_2):
  aux = 0
  indexR = -1
  for x,i in enumerate(item):
    if(aux <i and x!=index_1 and x!=index_2):
      aux = i
      indexR = x;
  return [indexR,aux]


def casos(H,V):

  VMY = BuscarMayor(V,-1,-1)
  VMD = BuscarMayor(V,VMY[0],-1)
  VMN = BuscarMayor(V,VMY[0],VMD[0])
  HMY = BuscarMayor(H,-1,-1)
  HMD = BuscarMayor(H,HMY[0],-1)

  if((HMD[1]>VMN[1] or HMD[1]>VMD[1]) and (HMY[1]>VMY[1] or HMY[1]>VMD[1])):
    return True
  else:
    return False


    

if(casos(heroes.copy(),villanos.copy())):
  print("POSSIBLE")
  value =ganar(heroes,villanos)
  print(str(value[0])+" "+str(value[1])+" "+str(value[2]) )
else:
  print("IMPOSSIBLE")

  