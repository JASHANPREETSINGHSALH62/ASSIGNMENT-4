marks=int(input("ENTER YOUR MARKS: "))
if(marks<25):
    print("YOUR GRADE IS F")
elif((marks>=25)and(marks<45)):
    print("YOUR GRADE IS E")
elif((marks>=45)and(marks<50)):
    print("YOUR GRADE IS D")
elif((marks>=50)and(marks<60)):
    print("YOUR GRADE IS C")
elif((marks>=60)and(marks<80)):
    print("YOUR GRADE IS B")
else:
    print("YOUR GRADE IS A")
print("THANK YOU")
