def comprobar(a,b,c,cadena):

  if(a==0 and b==0 and c==0):
     return "Yes",cadena
  while (b!=c and   a>0 ):
    a = a-1
    b = b - 1
    c = c+2
    cadena = cadena +"C"
  if(b == c):
    while(b > 0 and c >0):
       b = b - 1
       c = c - 1
       a = a+2
       cadena = cadena +"A"
    return  "Yes",cadena
  else:
     return "No",cadena




N = int(input())
Cadena= ""
for i in range(N):
    A, B, C = list(map(int,input().split()))
    D = A+B+C
    if D<(3*(10**4)):
      resultado , Cadena = comprobar(A,B,C, Cadena)
      if(resultado == "YES"):
         print(resultado)
         print(Cadena)
      else:
         print(resultado)
       

      

  

   
    
