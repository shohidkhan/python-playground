num1=[1,100,34,7, 2, 3, 4, 5]

# insert an element at the end of the list
num1.append(6)
print(num1)

# insert an element at a specific index
num1.insert(2, "hi")
print(num1)


# remove an element from the list
num1.remove("hi")
print(num1)


# remove an element at a specific index
# del num1[2]
num1.pop(2)
print(num1)

# remove the last element
num1.pop()
print(num1)



# sort the list in ascending order
num1.sort()
print(num1)


# length of the list
print(len(num1))