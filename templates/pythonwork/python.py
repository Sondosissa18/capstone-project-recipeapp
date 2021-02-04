# lists = [1, 2, 3, 4]

# for num in lists:
#     print(num * 20)

# wlists = ["Elie", "Tim", "Matt"]

# for char in wlists:
#     print(list(char[0]))

# lists = [1, 2, 3, 4, 5, 6]

# for num in lists:
#     if num % 2 == 0:
#         print(num)

# wlists = ["Elie", "Tim", "Matt"]

# for word in wlists:
#     print(word[::-1].lower())
# for i in range(0, 3):
#     for num in range(0, 3):
#         print(i, num)

# nums = [[i for i in range(0, 10)] for num in range(0, 10)]
# print(nums)


# lists = [("name", "Elie"), ("job", "Instructor")]

# diction = dict(lists)
# print(diction)
# list1 = ["CA", "NJ", "RI"]
# list2 = ["California", "New Jersey", "Rhode Island"]

# listsss = {list1[i]: list2[i] for i in range(0, len(list1))}

# print(listsss)


# dicti = {char: 0 for char in ["a", "e", "i", "o", "u"]}
# print(dicti)


# for k , v for chr(65, 91).():
#     print(k.index() , v)

# dicti = {char: 0 for char in ["a", "e", "i", "o", "u"]}


# def different(a, b):
#     return a - b


# print(different(2, 2))

# days = ["monday", "tuesday", "wed", "thursday", "fiday", "satu", "sunday"]
# num = [1, 2, 3, 4, 5, 6, 7]
# # for i in range(0, 7):
# newlist = [days[i] num[i] for i in range(0, len(num))]
# print(newlist())


# def print_day(num):
#     try:
#         return ["monday", "tuesday", "wed", "thursday", "fiday", "satu", "sunday"][
#             num - 1
#         ]
#     except IndexError as e:
#         return None


# print(print_day(7))


# def lastelement(num):
#     try:
#         return num[-1]
#     except IndexError as e:
#         return None


# print(lastelement([]))


# def number_compare(num1, num2):
#     if num1 > num2:
#         print("First is greater.")
#     elif num1 < num2:
#         print("Second is greater.")
#     else:
#         print("Numbers are equal.")


# print(number_compare(3, 3))


# def single_letter_count(string, letter):
#     return string.lower().count(letter.lower())


# print(single_letter_count("hello", "l"))


# def multiple_letter_count(string):
#     return {letter: string.count(letter) for letter in string}


# print(multiple_letter_count("hello"))


# def list_manipulation(lists, command, location, value=None):
#     if command == "remove" and location == "end":
#         return lists.pop()
#     elif command == "remove" and location == "beginning":
#         return lists.pop(0)
#     elif command == "add" and location == "beginning":
#         lists.append(0, value)
#         return lists
#     elif command == "add" and location == "end":
#         lists.append(value)
#         return lists


# print(list_manipulation([1, 2, 3], "remove", "end"))


# def is_palindrome(word):
#     if word[::] == word[::-1]:
#         return True
#     else:
#         return False


# print(is_palindrome("testing"))

# def frequency(lists, search_term):
#     return lists.count(search_term)


# print(frequency([1,2,3,4,4,4], 4))


# def flip_case(string, letter):
#     return string.reverse(lettter)


# print(flip_case("Hardy har har", "h"))
# /////////// need to redo it


# def multiply_even_numbers(nums):
#     total = 1
#     for num in nums:
#         if num % 2 == 0:
#             total = total * num
#     return total


# print(multiply_even_numbers([2, 3, 4, 5, 6]))

# from statistics import mode

# print(mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]))


# def capitalize(string):
#     return string.title()


# print(capitalize("tim"))


# def compact(stringl):
#     return [val for val in string if val]


# print(compact([0, 1, 2, "", [], False, {}, None, "All done"]))


# def partition(list, fn):
#     return [[val for val in list if fn(val)], [val for val in list if not fn(val)]]


# print(partition([1, 2, 3, 4]))
# /////////// need to redo it


# def intersection(ls1, ls2):
#     return [val for val in ls1 if val in ls2]


# print(intersection([1, 2, 3], [2, 3, 4]))
# //// retun val of list 1 if it in list 2


# def once(fn):
#     fn.is_called = False
#     def inner(*args):
#         if not(fn.is_called) = True
#         return fn(*args)
#     return inner

# one_addition(2,2)
