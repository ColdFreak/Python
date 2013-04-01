#!/usr/bin/python3

# A comment
print ("Hello World!\n") 
print ("Hello #Again") # add new line automatically
print ("Hens", 25+30/6)
print ("Is it greater?",   5> -2)

cars = 100;
print ("There are", cars, "cars available.")

my_name = 'Wang Zhijun'
print ("My name is",": %s" % my_name)


hilarious = False
# Use the %r for debugging, since it displays the "raw" data of the variable
joke_evaluation = "Isn't that joke so funny?! %r"
print (joke_evaluation % hilarious)

print ("." * 10)

print ("""There's something going on here.
With the three double-quotes.
We'll be abble to type as much as we like """)


from sys import argv
script, first, second, third = argv
print ("The script is called:",script)
print ("Your first variable is:",first)
print ("Your second variable is:",second)
print ("Your third variable is:",third)
