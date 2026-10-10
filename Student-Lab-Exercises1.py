name = input("Enter your name: ")
age = int(input("Enter your age: "))
is_developer= input("Are you a developer? (yes/no): ").strip().lower() == "yes"

if age<18:
    print("Tier 3: Guest")
elif age>=18 and is_developer:
    print("Tier 1: Admin Infrastructure Access")
else:
    print("Tier 2: Standard Executive Access")