import random as r
a=1
for i in range(10):
    num1=r.randint(1,10)
    num2=r.randint(1,10)
    print("Question",a,":",num1,"X",num2,"= ",end="")
    ans=int(input())
    product=num1*num2
    if(ans==product and a!=10):
        print("Right!")
    elif(ans==product and a==10):
        print("Right.")
    else:
        print("Wrong.The answer is",product,".")
    a=a+1        

