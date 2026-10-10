# conditions
age = 45
has_kids = True


is_adult=age>=18

is_married= age>=18 and has_kids==True


# print(f"Is adult: {is_adult}")
print(f"Is married: {is_married}")


mark=65

if mark >= 80:
    print("A+")
elif mark>=70:
    print("A")
elif mark>=60:
    print("A-")
elif mark>=50:
    print("B")
else:
    print("Fail")