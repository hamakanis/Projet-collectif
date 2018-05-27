"'Réaliser par Hamak Anis ,Benaouali Adel, Baraka Ahmed ,Bendiaba Khaled RO SECT A GROUPE 1'"
from math import *


def maliste(anis):
    p = []
    i, imax = 1, 2**len(anis)-1
    while i <= imax:
        a = []
        j, jmax = 0, len(anis)-1
        while j <= jmax:
            if (i>>j)&1 == 1:
                a.append(anis[j])
            j += 1
        p.append(a)
        i += 1 
    return p       
       

def execute():
    n=int(input("Donner n: "))
    m=int(input("Donner m: "))
    anis=[]
    while n <= m:
        anis.append(n)
        n=n+1

    p=maliste(anis)
    c=0
    for i in range (len(p)):
        m=1
        for j in range (len(p[i])):
            m=m*p[i][j]
        if sqrt(m)== int(sqrt(m)):
            c=c+1
    print("C(n,m)=",c)
execute()    
while True:
  
  
  retry=input("Réessayer oui ou non ? ")
 
  if retry=="oui":
       execute()
       
       
  elif retry=="non":
      print("byyyye\n")
      break
  else:
      print("Reponse différente de oui ou non répondez oui ou non :)")
   

     
