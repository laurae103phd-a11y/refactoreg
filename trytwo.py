#this is a check to see whether a person is eligible to apply for a role in histology where the applier must be 18 years old and have more than 3 years experience

import sys

age = int(input("What is your age in years?"))
exp = int(input("How many years experience in Histology do you have?"))
print("You are ", age, "years old")
print("You have ", exp, "years of experience in histology")
print("")

if age > 18 and exp > 3:
	print("You are eligible to apply for this role")
else:
	print("You are not eligible to apply for this role")


