mylist1=["Java","C++","Python","DJango","C++"]
mylist2=[3,2,5,6,7]
mylist1.sort()
print(mylist1)
mylist2.sort()
print(mylist2)



mylist1.reverse()
print(mylist1)


mylist1.sort()
mylist1.reverse()
print(mylist1)

mylist2.sort()
mylist2.reverse()
print(mylist2)


print(sorted(mylist2))
print(sorted(mylist2,reverse=True))


print(max(mylist1))
print(min(mylist1))

print(sum(mylist2))

mycount=mylist1.count("C++")
print(mycount)


mylist1.append("C")
print(mylist1)

mylist1.insert(3,"Javascript")
print(mylist1)


positon=mylist1.index("C")
print(positon)