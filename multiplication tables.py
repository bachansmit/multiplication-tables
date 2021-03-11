# Multiplication tables
# Make python do them... don't memorise it

user_input = int(input("Enter a number: "))
print("Multiplication Tables:")

for table in range(11):
    print(user_input, " × ", str(table), " = ", user_input * int(table))
