#   0,1,1,2,3,5,8,13,

def fb(n):
   if (n<0):
       print("die Zahl muss grösser als gleich 0 ")
   elif (n==0):
       return 0
   elif (n==1):
       return 1
   else :
       return( fb(n-1)+fb(n-2))
         

 
for x in range(20):
    print(fb(x))