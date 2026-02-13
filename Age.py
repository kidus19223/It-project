def classify_person():
age=int(input("Enter your age: "))
if age>=1 and age<=12:
print("You're a Child!")
elif age>=13 and age<=17:
print("You're a Teenager!")
elif age>=18 and age<=64:
print("You're an Adult!")
elif age>=65 and age<=200:
print("You're an Senior!")

classify_person()
