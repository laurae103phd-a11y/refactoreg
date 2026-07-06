#this is a check to see whether a person is eligible to apply for a role in histology where the applicant must have three years of experience working in histology and be over 18 years old

import sys#sys.argv is argument list that is passed from the command line

name = int(input(sys.argv[0]))# a user input to add their name
age = int(input(sys.argv[1]))# a user input to add in their age in years
exp = int(input(sys.argv[2]))# a user input to add the years experience in histology

print("Script name: ",sys.argv[0])
print("Age: ", sys.argv[1])
print("Years experience working in histology: ", sys.argv[1])





#print("You are ", age, "years old and have ", exp, "years of histology experience")#displays a summary of the users input of years experience and age with a string of text 
#print("")#break added for user readibility

#if age > 18 and exp > 3:#if included to define parameters of greater than 18 years of age and has more than 3 years experience
	#print("You are eligible to apply for this role")# if true, the text on this line is displayed
#else:#else code for inputs that are not above 18 years old and with more than three years experience
	#print("You are not eligible for this role")#if print displaying string text on this line if the user is less than 18 years old and/or has less than three years experience

#ANNOTATION
#this is a program to sift through applicants for a job in histology
#users are asked to input their age in years and their previous experience working in histology
#an if else function is applied to identify those that are over 18 years and have more than three years experience
#applicants that do not meet this criteria are told that they are not eligible for the role, whereas those that do are told they are eligible
