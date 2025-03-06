friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

print(friends[0])
print(friends[-1])

print(friends[0::2])
print(friends[1::2])

print(friends[1:4])
print(friends[3:])

friends[3:] =["El-Zero", "El-zero"]
print(friends)

friends.insert(0, "Aya")#insert in the first index
print(friends)
friends.append("Omar")#append in the last index
print(friends)

a= friends[2:]
print(a)
a.pop(-1)
print(a)

friend = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]
all = friend + employees + school
print(all)


friends1 = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
friends1.sort()
print(friends1)

count = len(friends1)
print(count)

technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]

print(technologies[-1][0])
print(technologies[-1][-1])
