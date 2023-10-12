# fruits = {"apple", "banana", "cherry"}
# more_fruits = ["orange", "mango", "grapes"]
# fruits.update(more_fruits)

# car = {"brand": "Ford", "model": "Mustang", "year": 1964}
# print(car.get("model"))
# (car["year"]) = 2020
# print(car)
# car["color"]="red"
# print(car)
# print(type(car))

# gardenerbox = {"fruits": ["apple", "banana", "orange", "pear"],
#                "vegetables": ["cucumber", "potato", "tomato", "carrot"],
#                "berries": ["watermelon", "strawberry", "blackberry", "raspberry"]}
# print(gardenerbox)

# fruit = ["apple", "banana", "orange", "pear"]
# input1 = input("Enter any fruit: ")
# fruit.insert(0, input1)
# print(fruit)
# input2 = input("Enter any fruit: ")
# fruit.append(input2)
# print(fruit)
#
#
#
# vegetables = ("cucumber", "potato", "tomato", "carrot")
# print(vegetables.count("cucumber"))
#
#
# berries = {"watermelon", "strawberry", "blackberry", "raspberry"}
# berries = {"watermelon".upper(), "strawberry", "blackberry", "raspberry"}
# print(berries)
#
# fruits = {"apple": "red", "banana": "yellow", "orange": "orange", "pear": "green"}
# morefruits = {"mango": "yellow", "limon": "yellow"}
# fruits.update(morefruits)
# print(fruits)
#
#
# # avelacnel 2 elemt, user! ta input skzbiz u verjic
# # touple mej exac bar@ hashvel qani hata
# # setic vernel arajin bar@ darcne meca
# # update anel dict!

# text = input("Please enter your text in lowercase to check if it is palindrome or not: ")
# if text == text[::-1]:
#     print("Your text is palindrome.")
# else:
#     print("Your text is not palindrome.")

# text = input("Enter the text to check if it is a palindrome: ")
# text = text.casefold()
# rev_text = reversed(text)
# if list(text) == list(rev_text):
#     print("Your text is palindrome.")
# else:
#     print("Your text is not palindrome.")
#
# text = input("Enter 6 letter word to check if it is a palindrome: ")
# text = text.casefold()
# rev_text = reversed(text)
# if list(text) == list(rev_text):
#     print("Your text is palindrome.")
# else:
#     print("Your text is not palindrome.")
#
# text = input("Enter 6 letter word to check if it is a palindrome: ")
# text = text.casefold()
# if text[0] == text[-1] and text[1] == text[-2] and text[3] == text[-3]:
#     print("Your text is palindrome.")
# else:
#     print("Your text is not palindrome.")

# num1 = int(input("Enter the fisrt number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))
# if num1 > num2 and num2 < num3:
#     print(f"The middle number of the three numbers is: {num2}")
# if num2 > num1 and num1 < num3:
#     print(f"The middle number of the three numbers is: {num1}")
# if num2 > num3 and num3 < num1:
#     print(f"The middle number of the three numbers is: {num2}")

# num1=int(input("Input first number: "))
# num2=int(input("Input second number: "))
# num3=int(input("Input tird number: "))
# if num1>num2:
#     if num1<num3:
#         median= num1
#     elif num2>num3:
#         median= num2
#     else:
#         median= num3
# else:
#     if num1 > num3:
#         median = num1
#     elif num2 < num3:
#         median = num2
#     else:
#         median = num3
# print("The middle number is", median)

num1 = int(input("Enter the fisrt number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
if num1 > num2 and num2 < num3 or num2 > num1 and num1 < num3 or num2 > num3 and num3 < num1:
    print(f"The middle number of the three numbers is: {num2}")
    print(f"The middle number of the three numbers is: {num1}")
    print(f"The middle number of the three numbers is: {num2}")