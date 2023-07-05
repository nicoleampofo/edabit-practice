# detectWord("UcUNFYGaFYFYGtNUH") ➞ "cat"
# def detectWord(jumble):
#     lowercase_word = ""
#     for i in jumble:
#         if i.islower():
#             lowercase_word += i
#     print(lowercase_word)

# detectWord("YFemHUFBbezFBYzFBYLleGBYEFGBMENTment")

# Create afunction that returns True is a string is empty and False otherwise
# def is_empty(strin):
#     if len(strin) > 0:
#         print("False")
#     else:
#         print("True")

# is_empty("yes")

# Write a function to check if a list contains a particular number.

# def check(list_of_ints, num):
#     if num in list_of_ints:
#         print("True")
#     else:
#         print("False")

# check([1,3,5,7], 3)

# Create a recursive function that takes two parameters and repeats the string n number of times. The first parameter txt is the string to be repeated and the second parameter is the number of times the string is to be repeated.

# def repetition(a, num_of_reps):
#     print(a*num_of_reps)

# repetition("word", 3)
# def this_function_prints(word):
#     word = str(input("Enter a word here: "))
#     print(f"Here is the word:  {word}")
#     return word

# this_function_prints("salad")

# Given a string,
# return True if its length is even or False if the length is odd.
# def odd_or_even(word):
# 	len_word = len(word)
# 	if len_word%2 == 0:
# 		print("True")
# 	else:
# 		print("False")

# odd_or_even("jonathan")


# wins, draws, losses, total points
# def football_points(wins, draws, losses):
# 	win_count = 3 * wins
# 	draw_count = 1 * draws
# 	losses_count  = 0 * losses
# 	print(wins + draws + losses)

# football_points(2, 1, 4)



# A vehicle needs 10 times the amount of fuel than the distance it travels. However, it must always carry a minimum of 100 fuel before setting off.

# Create a function which calculates the amount of fuel it needs, given the distance.

# calculate_fuel(3) ➞ 100

# def calculate_fuel(distance):
#     if distance > 10:
#         fuel = distance * 10
#     else:
#         fuel = 100
#     print(fuel)

# calculate_fuel(3)

# Create a function that takes a string; we'll say that the front is the first three characters of the string. If the string length is less than three characters, the front is whatever is there. Return a new string, which is three copies of the front.

# def three_char(astring):
#     if len(astring) > 3:
#         print(astring * 3)
#     else:
#         print(astring)

# three_char("happy")

# create a function that will handle simple math expressions. The input is a string
# calculator("23+4")--> 27

# def calculator(numbers):
#     split_int = eval(numbers)
#     print(split_int)

# calculator("3*5")

# inches to feet
# def inch_to_feet(inch):
#     print(inch/12)

# inch_to_feet(324)

# given two arguments, return a list which contains the two arguments
# def return_a_list(arg1, arg2):
#     new_list = [arg1, arg2]
#     print(new_list)

# return_a_list(3,4)

# given a list of numbers, return True if the sum of the values in the list is less than 100; otherwise, False
# def list_less_than(nummies):
#     if sum(nummies) < 100:
#         print("True")
#     else:
#         print("False")

# list_less_than([99])


# create a function that takes a string and returns the concatenated first and last character
# def first_and_last(word):
#     first = word[0]
#     last = word[-1]
#     print(first + last)

# first_and_last("presidential")
