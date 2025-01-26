# Write your code here :-)
#First question
print("Please enter a word you'd like to use")
user_word = input()
print("You chose",user_word)
print("how many times would you like this word to be repeated?")
word_rep = int(input())
#original version that isnt as clean
print(user_word * word_rep, sep=" ")
#new version that I got help from ai that spaces them properly.
#I understand why it did it this way and think it looks nicerso i wanted to include it.
#print((user_word + " ") * (word_rep - 1) + user_word)

#Second question
print("please enter your name")
name = input()
print("please enter your age")
age = int(input())
print("Hello", name + "!","You are",age,"years old.","Next year you will be", age + 1, "years old.")

#Third question
print("Please write a sentence")
sen = input()
print("Please write a word that may or may not! be in that sentence")
word = input()
print(word in sen)

#Four question

print("Please enter a word to slice")
sliced_word = input()
print("First slice of word")
index1 = int(input())
print("Followed by second slice")
index2 = int(input())
print(sliced_word[index1],sliced_word[index2])

#Five question

print("Hey you there type 3 word in")
fir = input()
sec = input()
thr = input()
print(fir,sec,thr, sep="|")
