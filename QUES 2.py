y=int(input("enter"))
b=y%4
c=y%100
d=y%400
if(b==0 and c!=0):
    print("leap year")
elif(b==0 and c==0 and d==0):
    print("leap year")
else :
    print("no")
