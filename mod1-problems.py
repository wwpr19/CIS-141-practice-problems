# 1. Create a program that prints the following output to the screen: 

#"Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked."
print("Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked.")
# My CABBAGES!!!!!!!!!!!!

# 2. Create a program that prompts for 2 numbers and then outputs the addition, subtraction, multiplication, and division of the first number by the second number.
num1 = int(input("Write first number to calculate"))
print(num1)
num2 = int(input("Write second number to calculate"))
print(num2)

print("I will now magically calculate these numbers")
print("first addition, then subtraction, then multiplication, and finaly division!")
print(num1+num2, num1-num2, num1*num2, num1/num2,)

# 3. Create a program that prompts for the side lengths of a triangle and computes the area using Heron's formula. (https://en.wikipedia.org/wiki/Heron%27s_formula)
print("We are going to calculate the area of a triangle!")


a = int(input("What is the length for side A?"))

b = int(input("What is the length for side B?"))

c = int(input("What is the length for side c?"))

print("")
print("you inputed", a, b, c)
print("")

import math

print("processing")
print("")
x = a + b + c
#print(x)
s = x / 2

print("your semiperimeter is")
print(s)
print("")
print("Now we will calculate the area of your triangle")
print("")

fa = s - a
#print(fa)
fb = s - b
#print(fb)
f_c = s - c
#print(f_c)

pre_area = s * fa * fb * f_c

print(pre_area,"this is the number prior to square rooting")
print("")

total_area = (math.sqrt(pre_area))

print("The area of your triangle is",total_area)
print("")
print("If you recived a zero, you may have entered numbers that dont equal a triangle. If so check your work and try again")

# 4. Create a program that computes different statistics given five numbers including the total, average, minimum, maximum, range, and standard deviation (https://en.wikipedia.org/wiki/Standard_deviation).# Write your code here :-)
import math
# the numbers entered
print("Enter numbers you would like to use")
print("")

num1 = int(input("First number"))
num2 = int(input("second number"))
num3 = int(input("third number"))
num4 = int(input("fourth number"))
num5 = int(input("fifth number"))
print("you entered", num1, num2, num3, num4, num5)
print("")

print("We will now get the total of these numbers")
total = num1 + num2 + num3 + num4 + num5
print(total)
print("")

print("We will now get the average(mean) of these numbers")
mean = total / 5
print(mean)
print("")

print("Now we will show the minimum")
mini = min(num1, num2, num3, num4, num5)
print(mini)
print("")

print("Now we will show the maximum")
max = max(num1, num2, num3, num4, num5)
print(max)
print("")

print("Now we will show the range")
range = max-mini
print(range)
print("")

print("Lastly we will get the standard deviation")
dnum1 = mean-num1
dnum2 = mean-num2
dnum3 = mean-num3
dnum4 = mean-num4
dnum5 = mean-num5
pdnum1 = dnum1 ** 2
pdnum2 = dnum2 ** 2
pdnum3 = dnum3 ** 2
pdnum4 = dnum4 ** 2
pdnum5 = dnum5 ** 2
#print(pdnum1)
#print(pdnum2)
#print(pdnum3)
#print(pdnum4)
#print(pdnum5)
add = pdnum1+pdnum2+pdnum3+pdnum4+pdnum5
vari = add/5
stde = math.sqrt(vari)
print("")
print("Your standard deviation is",stde)
