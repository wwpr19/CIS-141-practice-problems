# Write your code here :-)

#1. Construct a truth table for the expression: (A AND B) OR (NOT B) where A and B 
#each can be True or False. 
#Your truth table should be commented out (as it's not valid Python code!)

#--A-- --B-- --A AND B-- --or not B--

#True   True   True       True
#False  True   False      false
#True   False  False      True
#False  False  False      True

#2. The headlights of a car should only automatically turn on when the 
#daylight outside is below a certain threshold. If a sensor threshold is 
#below the number 8, print "Headlights On"; otherwise, print "Headlights Off".

print("How bright is it outside?")
daylight = int(input())
if daylight < 8:
    print("Headlights On!")
else:
    print("Headlights Off!")

#3. Prompt the user for their bank balance. Evaluate whether the 
#balance is less than $100. Print True if the user’s balance is below $100; 
#print False, otherwise.

money = int(input("How much money do you have in your account?"))
#heres the original way I did it
if money < 100:
    print("true")
else:
    print("false")
#heres the way I think you want it to be done for the question
print(money <=100)

#4. A theater wants to enforce age restrictions for movie tickets. 
#Ask the user for their age, and tell them whether they can see G 
#(appropriate for under 13), PG-13 (appropriate for 13 to 17), or
#R (appropriate for over 18) rated movies.

age = int(input("How old are you ?"))

if age < 13:
    print("You can see a movie rated G")

elif age <=17:
    print("You can see a movie rated PG-13")
    
else:
    print("You can see a movie rated R")

#5. A store charges $5 for shipping on any order under $50. If the order 
#amount is $50 or more, shipping is free. Ask the user for the order total 
#and print the total cost, including shipping.


purch = int(input("How much is your order?"))

if purch < 50:
    print("Your total is",purch + 5)
else:
    print("Your total is",purch)
