# 1 Write Python code that prints your name, student number and email address.
name="LUBINA MUHAMMAD"
num="ST28"
mail="lubiinas@gmail.com"
print("Name of the student:",name)
print("Student number:",num)
print("Email address:",mail)
# Write Python code that prints your name, student number and email address using escape sequences.
print(name,'\n',num,'\n',mail,'\n')
# Write Python code that add, subtract, multiply and divide the two numbers. we can use the two numbers 14 and 7.
a=14
b=7
print("14+7=",a+b,"\n14-7=",a-b,"\n14*7=",a*b,"\n14/2=",a/b)
# Write Python code that displays the numbers from 1 to 5 as steps.
for i in range(1,6):
    print(i)
# Write Python code that outputs the following sentence (including the quotation marks and line break) to the screen:
print('"SDK" stands for "Software Development Kit", whereas "IDE" stands for "Integrated Development Environment".')
# Practice Escape Sequences
print("python is an \"awesome\" language.")
print("python\n\t2023")
print('I\'m from Entri.\b')
print("\65")  # ASCII code for '5'
print("\x65")  # Hexadecimal for 'e'
print("Entri", "2023", sep="\n")
print("Entri", "2023", sep="\b")
print("Entri", "2023", sep="*", end="\b\b\b\b")
num = 23
textnum = "57"
decimal = 98.3

# Print types
print(type(num))
print(type(textnum))
print(type(decimal))

# Sum and its type
total = num + int(textnum) + decimal
print("Sum:", total)
print("Type of sum:", type(total))
# Calculate Minutes in a Year
days_in_year = 365
hours_in_day = 24
minutes_in_hour = 60
total_minutes = days_in_year * hours_in_day * minutes_in_hour
print(f"Total number of minutes in a year: {total_minutes}")
# Greeting with Name
name = input("Please enter your name: ")
print(f"Hi {name}, welcome to Python programming :)")
# Pounds to Dollars Conversion
pounds = float(input("Please enter amount in pounds: £"))
exchange_rate = 1.25  # Example rate
dollars = pounds * exchange_rate
print(f"£{pounds} are ${dollars:.2f}")
