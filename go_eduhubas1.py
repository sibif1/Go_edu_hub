#1. Check the colors

# Colors = ["Yellow","Green","White","Black"]

# Fruits=["Apple","Papaya","Mango","Orange"]

# Animals=["Tiger","Lion","Deer","Zebra"]


 # i. Write a program that asks user to enter a Color/Fruit/Animal name and it should tell which category belongs to , 
 # like its is a fruit or color or Animal


# user_input = input("Enter a color and i'll tell which category.! ")
# if user_input in Colors:
# 	print("You gave a color")
# elif user_input in Fruits:
# 	print("You gave a fruit")
# elif user_input in Animals:
# 	print("You gave an animal ")
# else:
# 	print("Category not found")

# -------------------------------------------------------------------------------

# ii. Write a program that asks user to enter two cities and it tells you if they both are in same country or not.
# For example if I enter yellow and Black, it will print "Both are colors" but if I enter yellow and Tiger 
# it should print "They don't belong to same category"



# print("Enter two things to check if they are in the same category: ")

# user_input1 = input("Enter 1st thing")

# user_input2 = input("Enter 2nd thing")

# if user_input1 in Colors and user_input2 in Colors: #Be sure to check in colors for every input and not the whole statement
# 	print("in same category")
# 	print("going here 1")
# elif user_input1 in Fruits and  user_input2 in Fruits:
# 	print("in same category")
# 	print("going here 2")
# elif user_input1 in Animals and user_input2 in Animals:
# 	print("in same category")
# 	print(user_input1, user_input2)
# 	print("going here 3")
# else:
# 	print("Not in the same Category")


# -------------------------------------------------------------------------------


# 2.  Write a python program that can tell you if your grade score good or not . Normal Score range is 40 to 60.

#   i. Ask user to enter his score.

#   ii. If it is below 40 to 60 range then print that score is low

#   iii. If it is above 60 then print that it is good otherwise print that it is normal

# user_score = int(input("Enter your score : " ))
# if user_score < 40 :
# 	print("Score is low ")
# elif user_score >= 40 and user_score <=60:
# 	print("Score is Normal ")

# elif user_score >60:
# 	print("Good score!!")

# else:
# 	print("Enter a valid input")



# -------------------------------------------------------------------------------

# 3.  After appearing in exam 10 times you got this result,

# result = ["Pass","Fail","Fail","Pass","Fail","Pass","Pass","Fail","Fail","Fail"]

# Using for loop figure out how many times you got Pass



# result = ["Pass","Fail","Fail","Pass","Fail","Pass","Pass","Fail","Fail","Fail"]

# # print(len(result))
# counter = 0
# for i in range(len(result)):
# 	if result[i] =="Pass":
# 		counter += 1
# 		print("pass")

# print("You have passed {} times".format(counter))

# -------------------------------------------------------------------------------

# 4.  Write a program that prints following shape

# *

# * *

# * * *

# * * * *

# * * * * *

# * * * *

# * * *

# * *

# *



# for i in range(6):
# 	for j in range(i):
# 		print("*", end = "")
# 	print()
# for i in range(5, 0 , -1):
# 	for j in range(i):
# 		print("*", end = "")
# 	print()

#------------------------------------------------------

# 5.   Lets say you are running a 50 km race. Write a program that,

# Upon completing each 10 km asks you "are you tired?"
# If you reply "yes" then it should break and print "you didn't finish the race"
#  If you reply "no" then it should continue and ask "are you tired" on every km
# If you finish all 50 km then it should print congratulations message

# input_ans = "no "
# total_kms = 0
# for total in range(50):
# 	print(total_kms, total)
# 	if total > 0 and (total % 10 == 0):
# 		km10_input= input("are you tired? ")
# 		if km10_input == "yes":
# 			input_ans = "yes"
# 			total_kms += 1
# 			break
# 		elif km10_input == "no":
# 			input_ans = "no"
# 			total_kms += 1
# 			continue
# 		else:
# 			print("No right ans")
# 			total_kms += 1
	

# if input_ans =="yes":
# 	print("you didn't finish the race")
# elif input_ans == "no":
# 	balance_kms = 50 - total_kms
# 	for total in range(balance_kms):

# 		km1_input= input("are you tired? ")
# 		if km1_input == "yes":
# 			input_ans = "yes"
# 			break
# 		elif km1_input == "no":
# 			input_ans = "no"
# 			break
# 		else:
# 			print("No right ans")


# if total_kms == 50:
# 	print("congratulations you finished it!")


#-----------------------------------------------------------------------------------------------------------

# 6.  Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).

# for i in range(1500, 2701):
# 	if i % 7 == 0 and i % 5 ==0:
# 		print(i)

#-----------------------------------------------------------------------------------------------------------

# 7.   Print square of all numbers between 10 to 20 except even numbers

# for i in range(10,20+1):
# 	if i % 2 ==0:
# 		continue
# 	else:
# 		print(i**2)

#-----------------------------------------------------------------------------------------------------------

# 8.  Your Marks for five Test(test1 to test5) looks like this,

# marks_list = [65, 75, 2100, 95, 83]

# Write a program that asks you to enter marks and program should tell you in which test that marks occurred.
# If marks is not found then it should print that as well.

# marks_list = [65, 75, 2100, 95, 83]

# mark = int(input("Enter the mark: "))
# print(mark)
# if mark == marks_list[0]:
# 	print("Test 1", marks_list[0])
# elif mark == marks_list[1]:
# 	print("Test 2", marks_list[1])
# elif mark == marks_list[2]:
# 	print("Test 3", marks_list[2])
# elif mark == marks_list[3]:
# 	print("Test 4", marks_list[3])
# elif mark == marks_list[4]:
# 	print("Test 5", marks_list[4])
# else:
# 	print("Mark not found")

# if mark == marks_list[1]:
# 	pass
