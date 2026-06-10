m1=int(input("Enter marks "))
m2=int(input("Enter marks "))
m3=int(input("Enter marks "))
m4=int(input("Enter marks "))
m5=int(input("Enter marks "))

avg=(m1+m2+m3+m4+m5)/5
per=((m1+m2+m3+m4+m5)/500)*100
print("marks of subject 1",m1)
print("marks of subject 2",m2)
print("marks of subject 3",m3)
print("marks of subject 4",m4)
print("marks of subject 5",m5)

print("Avg marks is",avg)
print("Per is ",per)
if per>80:
    print("A Gradee")
elif per>=60 and per<=80:
    print("B grade")
elif per>=40 and per<=60:
    print("C grade")
else:
    print("F grade")
