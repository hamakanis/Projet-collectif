Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>>"'forme générale s(n,m)=\sum _{{k=0}}^{{n-m}}(-1)^{k}{\binom  {n-1+k}{n-m+k}}{\binom  {2n-m}{n-m-k}}S(n-m+k,k),"'
def stirling(n,k):
      n1=n
      k1=k
     n=int(input("donner n\n"))
     k=int(input("donner k\n")) 
   
                if k<=0:
                      return 1
          


     
                      elif k<=0:
                        return 0
     
                      elif (n==0 and k==0):
                        return -1
     
                       elif n!=0 and n==k:
                         return 1
     
                       elif n<k:
                         return 0
 
                         else:
                           strl=stirling(n1-1,k1)
                           strl=k1*strl
                          return (k1*(stirling(n1-1,k1))+stirling(n1-1,k1-1))
 
print stirling(1,1)
'''nous donne à priori 1'''
 
print stirling(2,1)
'''donne -1'''
 
print stirling(3,2)
'''donne -3'''
 
print stirling(5,4)
'''donne -10'''
    
print stirling(5,5)
'''donne 1'''

 
print stirling(20,15)


