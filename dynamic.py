mylist=[]
count=int(input("How Many Records?"))
for i in range(0,count):
    myvalue=input("Enter Your Value")
    mylist.append(myvalue)
mytuple =tuple(mylist)
print(mytuple)
