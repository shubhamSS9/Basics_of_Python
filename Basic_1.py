# letter = input("Enter the letter: ")
# if (letter =='a'or 'e'or 'i'or 'o'or 'u'or 'A'or 'E'or 'I'or 'O'or 'U'):
#     print("Letter is Vowel")
# else:
#     print("letter is consonant")
# from pip._vendor.rich.prompt import result
#from numpy.core.defchararray import isnumeric
# from numpy.lib.function_base import append
# from pip._vendor.rich.prompt import result
# import string
# from dataclasses import replace
# from pip._vendor.rich.prompt import fruit
# from numpy.lib.function_base import average
# from genericpath import getsize



# def is_vowel(char):
#     all_vowel = 'aeiouAEIOU'
    
#     return char in all_vowel

    
# print(is_vowel('S'))
# print(is_vowel('i'))


# def is_group_member(num,n):
#     for i in num:
#         if(n == i ):
#             return True
            
#     return False

    
# print(is_group_member([3,5,8,7],3))
# print(is_group_member([3, 5, 8, 7], -1))


# def is_group_member(num,n):
#     for i in num:
#         if(n == i ):
#             return True
            
#     return False

    
# # print(is_group_member([3,5,8,7],3))
# # print(is_group_member([3,5,8,7],-1))
# num = input("Enter the numbers: ")
# n = input("enter no: ")
# is_group_member(num,n)


# def histogram(item):
#     for n in item:
#         output = ''
#         time = n

#         while time > 0:
#             output += '*'
#             time = time - 1

#         print(output)

# histogram([2,5,8,78])    
# def is_yedzave(name):




#     all_yz = ["shubham", "pratik", "sumya", "sonya", "kalya", "susha"]

#     # Check if the entire entered name is in the list of yz members
#     if name in all_yz:
#         if name == "shubham":
#             return "scholar"
#         elif name == "pratik":
#             return "bevda and smoker"
#         elif name == "sumya":
#             return "occasionally drink but not smoke"
#         elif name == "sonya":
#             return "only drink but hate smoke"
#         elif name == "kalya":
#             return "paisa barbad bc"
#         elif name == "susha":
#             return "lover boy"
    
#     else:
#             return "Enter the correct yz name"

# # Take user input for the yz name
# input_name = input("Enter the name of yz: ")

# # Call the function with the input and print the result
# result = is_yedzave(input_name)
# print(result)


# def is_vowel(char):
#     vowel = 'aeiouAEIOU'
#     if char in vowel:
#         return input_char, " is vowel"
#     else:
#         return input_char, " is consonant"


# input_char=input("Enter the letter: ")
# result = is_vowel(input_char)
# print(result)




# def isvowel(char):
#     return char in 'aeiou'

# print(isvowel('d'))


# def sum_of_int(A, B, C ):
    
    
#     if(A == B or B == C or C == A):
#         return 0
#     else: 
#         sum = A + B + C
#         return sum

# A = int(input("Enter the first value: "))
# B = int(input("Enter the second value: "))
# C = int(input("Enter the third value: "))

# result = sum_of_int(A,B,C)

# print(result)


# def sum_of(a, b):
#     sum= a+b
#     if (sum >= 15 and sum <= 20):
#         return 20
#     else:
#         return sum 


# a = int(input("Enter th first number: "))
# b = int(input("Enter the second number: "))
# res=sum_of(a,b)
# print(res)


# def sum_of(a, b):
#     sum = a + b
#     if sum in range(15, 20):
#         return 20
#     else:
#         return sum
        

# a = int(input("Enter the first value: "))
# b = int(input("Enter the second value: "))

# result = sum_of(a, b)
# print(result)


# def is_correct(a, b):
#     sum = a + b
#     difference= a-b
#     if a == b or sum == 5 or difference == 5:
#         return True
#     else:
#         return sum, difference
    
# a = int(input("Enter the first value: "))
# b = int(input("Enter the second value: "))
# result = is_correct(a, b)
# print(result)


# def add_object(a, b):
#     sum = a + b
#     if not (isinstance(a, int) and isinstance(b, int)):
#         return False
#     else:
#         return sum

        
# a = input("Enter the first number: ")
# b = input("Enter the second number: ")

# result = add_object(a, b)
# print(result)












# def personal_info():
#    name = "shubham"
#    age = 26
#    address="Ganesh nagar yerwada pune - 411006"
#    print("NAME: {}\nAge: {}\nADDRESS : {} ".format(name, age, address))
# personal_info()

# x = 4
# y = 3
# result = (x + y) * (x + y)
# print(("({} + {}) ^ 2 = {}").format(x,y,result))


# def form():
#     x = 4
#     y = 3
#     value = (x + y) * (x + y)
#     return(("({} + {}) ^ 2 = {}".format(y, x, value)))
# print(form())


# def future_value():
#     amt = 10000
#     nt = 3.4
#     year = 7
#     fv = amt*((1 + (0.01 * nt)) ** year)
#     return fv
    
# print(future_value())


# def fv(amt,nt,year):
#     fv = amt * ((1 + (0.01 * nt)) ** year)
#     return  fv
    
# print(fv(10000, 3.4, 7))


# def future_value():
#     amt = 10000
#     nt = 3.4
#     year =7
#     fv = amt*((1 + (0.01 * nt)) ** year)
#     return fv
    
# print(future_value())

# import os.path

# print(os.path.isfile("Basic_1.py"))

# print(os.path.isfile("basic.py"))


# def positive_no(n):
#     sum=0
#     for i in range(1, n):
#             sum = i + n
#     return sum

            
# n = int(input("Enter a number: "))
# result = positive_no(n)
# print(result)


# def convert(feet):
#     centimeters = feet * 30.48
#     return centimeters

# feet = float(input("Enter a height in feet: "))
# result = convert(feet)
# print(result)


# def hypo(a_s, o_s):
#     hypotenious = (((a_s) ** 2) + ((o_s) ** 2))
#     return hypotenious ** (1/2)


# side1 = int(input("Enter the adjasent side of angle: "))
# side2 = int(input("Enter the opposite side of angle: "))
# result = hypo(side1, side2)
# print(result)


# def height(feet):
#     inches = feet * 12
#     yards = feet * 0.33
#     miles = feet * 0.000189394
#     return inches, yards, miles

    
# convert = float(input("Enter the height in feet: "))
# result = height(convert)
# print(result)




# def height():
#     inches = 10 * 12
#     yards = 10 * 0.33
#     miles = 10 * 0.000189394
#     print("Inches: {}\nYards: {}\nMiles: {}".format(inches,yards,miles))

# height()



# def height(feet):
#     inches = feet * 12
#     yards = feet * 0.33
#     miles = feet * 0.000189394
#     return inches,  yards,  miles

# print(height(500))






# inches = 10 * 12
# yards = 10 * 0.33
# miles = 10 * 0.000189394
# print("Inches: {}\nYards: {}\nMiles: {}".format(inches,yards,miles))


# def solve(x, y):
#     sum = (x + y) * (x + y)
#     print(" {} + {} ^ 2 = {}".format(x, y, sum))
    
# solve(4, 3)


# def solve():
#     amt = 10000
#     nt = 3.5
#     year = 7
    
#     fv = amt*((1 +(0.01*3.5))**year)
#     print(fv)
#     print(nt)
    
# solve()


# def dist():
#     x1 = 2
#     x2 = 7
#     y1 = -6
#     y2 = 3
#     distance = (x2 - x1) ** 2+ (y2 - y1) ** 2
#     return distance**(1/2)
# print("Distance between two points: ", dist())


# def positive(n):
#     sum=0
#     for i in range(1, n):
#         sum = sum+i
#     print(sum)
    
# positive(10)









# def hei(feet):
#     conv = feet * 30.47
#     inch = feet * 12
#     cm = inch * 2.54
    
#     return conv, inch, cm
    
    
# print(hei(6))


# def hypo(a,b):
#     hypotenious = ((a**2)+ (b**2))
#     return hypotenious**(1/2)
    

# print(hypo(19, 9))





# def hei(feet):
#     inches= feet * 12
#     yard = feet * 3
#     miles= feet * 5280
    
#     return inches, yard, miles
    
# print(hei(6))





# def hei(feet):
#     inches= feet * 12
#     yard = feet * 3
#     miles= feet * 5280
    
#     return inches, yard, miles
    
    
# print(hei(6))


# def barbad(birth_yr, current_yr):
#     #age= 0
#     day = 0
#     age= current_yr-birth_yr 
#     # current_year=2024
#     Dys = age * 365
     
#     for i in range(birth_yr, current_yr + 1):
#         if((i % 4 == 0 or i % 100 != 0) or i % 400 == 0):
#             #print(day)
#             Dys=Dys+1
#                 # age= current_yr-birth_yr 
#         return Dys
    
# print(barbad(1997,2024))





# def is_leap_year(year):
#     # Leap year is divisible by 4, but not divisible by 100 unless it is divisible by 400
#     return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# def total_days_in_years(years):
#     total_days = 0

#     for year in range(years):
#         total_days += 366 if is_leap_year(year) else 365

#     return total_days

# years = 27
# total_days_spent = total_days_in_years(years)

# print(f"Total days spent in {years} years: {total_days_spent} days")










































# list_1=[]
# for i in range(1500, 2700):
#     if i % 7 == 0 and i % 5 == 0:
#          list_1.extend(str(i))
         
# print(list_1)
# 







# list_1=[]
# for i in range(1500, 2700):
#         if i % 7 == 0 and i % 5 == 0:
#                 list_1.append(str(i))
# print(list_1)

# c = 28
# f = ((9 / 5) * c + 32)
# print(c,"degree celsius is ", f," in fahrenheit" )




# guass=int(input("Enter the no.: "))
# for i in range(1, 9):
#         if (i == guass):
#                 print("correct")
#                 break
#         else:
#                 print("invalid")
#                 pass

# import random

# target_num, guass_num = random.randint(1, 10), 0


# while target_num != guass_num:
#         guass_num = int(input("Enter number: "))
        
# print("Well Done")



# import random

# # Generate a random number between 1 and 10 (inclusive) as the target number
# target_num, guess_num = random.randint(1, 3), 0

# # Start a loop that continues until the guessed number matches the target number
# while target_num != guess_num:
#     # Prompt the user to input a number between 1 and 10 and convert it to an integer
#     guess_num = int(input('Guess a number between 1 and 10 until you get it right : '))

# # Print a message indicating successful guessing once the correct number is guessed
# print('Well guessed!') 





# for i in range(5,0, -1):
#         for j in range(i):
#                 print("*", end=" ")
#         print("\n")































# patter problems

# for i in range(1, 5):
#     for j in range(i):
#         print("*", end="")
#     print()

# for i in range(1, 5):
#     for j in range(1, 5):
#         if j>=5-i:
#             print("*", end='')
#         else:
#             print("", end='')

#     print()

# n = int(input("enter the no.: "))
# for i in range(n):
#     # for j in range(0, n):
#         print("*", end=" ")

# n = int(input("Enter the no : "))

# for i in range(n):
#         print((str(i+1)+' ') * n)


# def family_mem(position):
#         if position == 1:
#                 return "Papa"
#         elif position == 2:
#                 return "Aai"
#         elif position == 3:
#                 return "Tai"
#         elif position == 4:
#                 return "Bhaksha"
#         elif position == 5:
#                 return "shubham"
#         else:
#                 return "Enter valid member"
                
# print(family_mem(7))


# def life(ur_age):
#         papa_age = 2024 - 1964
#         print("age of papa is: ", papa_age)
#         ur_age = papa_age-ur_age
#         if ur_age >= 25 or 27:
#                 return "Shubham"
#         elif ur_age in range(30):
#                 return "Bhaksha"
#         elif ur_age in range(26):
#                 return "Tai"
#         elif ur_age in range(9):
#                 return "Aai"        
#         else:
#              return "Enter valid age" 

               
# inter_age =int (input("Enter the age: "))
# result=life(inter_age)
# print(result)




# def auther(name):
#     if name=="khalid husani":
#         return ("The Kite Runner, Thousand splended sun")
#     elif name=="Yoyal Nova Harary":
#         return ("Homo Sepians, 21 lessons from 21st century, Homodues")
#     else:
#         return ("Enter greate auther name")
# name=input("Enter the name: ")
# result=auther(name)
# print(result)



# i=1
# while i <= 5:
#     table=5*i
#     print(table)
#     i=i+1




# for i in range(1, 6):
#     sum = 5 * i
#     print(sum)


# def area(w, l):
#     area = w * l
#     return area
    
# print(area(40, 20))


# def grt_msg(name, age):
#     return ("My name is {}, I'm {}, nice to meet you".format(name, age))

# print(grt_msg("shubham", 27))


# def check(num):
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")
        
# check(156)

# list1 = [2, 4, 3, 5, 30]
# maxi=max(list1)
# mini = min(list1)

# print(maxi, mini)


# def is_palindrome(str1):
#     str1 = str1.replace(" ", "").lower()
    
#     return str1 == str1[::-1]

# inp_str = "A man a plan a canal Panama"
# result = is_palindrome(inp_str)
    
# if result:
#     print("Palindrome")
# else:
#     print("Not")
   
# str1 = "A man a plan a canal Panam"
# str1 = str1.replace(" ", "").lower()
# resu = str1 == str1[::-1]
# if resu:
#     print("Palindrome")
# else:
#     print("Not")


# def calc(p, i, t):
#     compound_intrest = p * (1 + i) ** t
#     return compound_intrest
    
# print(calc(32.00, .6, .2))


# def convert(days):
#     years = days / 365
#     weeks = days / 7
#     day = days
#     print( years, weeks, day)

# convert(10000)

# list1 = [2, 45, 3, 6, -76]
# total=0
# for i in list1:
#     if i > 0:
#        total += i
        
# print(total)

# str1 = "Given a list of integers, find the sum of all positive"
# str1 = str1.replace(" ", "")
# print(str1)
# print(len(str1))

# a = 10
# b = 5

# a,b=b,a

# print(a)
# print(b)



# a = 50
# b = 15

# c = a
# a = b
# b = c

# print(a)
# print(b)


# def Info(name, age, avg_marks):
#     print("Student name: {}\nStudent age: {}\nStudent avg marks: {}".format(name, age, avg_marks))
    
# Info("shubham", 27, 513)


# def Info(name, age, avg_score):
#      print("name: {}\nage: {}\navg_score: {}".format(name, age, avg_score))
# Info("shubham", 27, 513)    

# concatinate two strings


# def Concat(str1, str2):
#     newString = str1 + str2
#     print(newString)
# Concat("shubham", " shinde")

# fruit = ["banana", "apple", "mango"]
# print(fruit[0])
# print(fruit[2])


# def find():
#     num = [2, 4, 5, 3, 6, 9]
#     sum=0
#     for i in num:
        
#         sum+=i
#     print(sum)
# find()       


# def cal_sum_avg(num):
#     total_sum = 0
#     for i in num:
#         total_sum = total_sum + i
#     avg = total_sum / len(num)
#     return total_sum, avg
    
    
    
# num = [4, 2, 6, 5, 8, 9]
# total_sum, avg = cal_sum_avg(num)

# print(total_sum)
# print(avg)


# def avg_marks():
#     stud1 = [65, 89, 45, 37, 79]
#     stud2 = [89, 76, 54, 80, 72]
#     stud3 = [98, 87, 86, 99, 100]
    
#     total_sum1 = 0
#     total_sum2 = 0
#     total_sum3 = 0
    
#     for i in stud1:
#         total_sum1 = total_sum1 + i

#     for i in stud2:
#         total_sum2 = total_sum2 + i
        
#     for i in stud3:
#         total_sum3 = total_sum3 + i

#     average_stud1 = total_sum1 / len(stud1)
#     average_stud2 = total_sum2 / len(stud2)
#     average_stud3 = total_sum3 / len(stud3)

#     return average_stud1, average_stud2, average_stud3
    
# print(avg_marks())


# def check(num):
#     if num >= 0:
#         print("Number is positive")
#     else:
#         print("Negative")

# check(0)


# def check(num):
#     if num > 0:
#         print("positive")
#     elif num < 0:
#         print("Negative")
#     else:
#         print("Zero")

# check(int(0.4))            

# num =0
# print("positive" if num>0 else "Negative")


# def evenOdd(num):
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")
        
# evenOdd(30)


# def sumOf(num):
#     total=0
#     for i in range(num+1):
#         total = total + i
#     print(total)
    
# sumOf(8)


# def sumOf(num):
#     if num == 1:
#         return 1
#     return num + sumOf(num - 1)
    
# print(sumOf(8))


# def sumof(num1, num2):
#     sum=0
#     for i in range(num1, num2):
#         sum = sum + i
#     print(sum)
    
# sumof(3,6)


# def grt(num1, num2):
#     if num1 > num2:
#         print("num1 is greater than num2")
#     else:
#         print("num2 is greater than num1")
        
# grt(35,76.9)

# x, y, z = input("Enter three numbers: ").split()
# print(x,y,z)





# String

# msg = "Hello"
# a = msg[0]
# print(a)
# print(msg[2])
# print(msg[-4])

# msg = "rafting"
# print(msg[1])

# string properties

# s = "Hello"
# # s[0] = "M"
# s = "Bye"
# print(s)

# replicate
# s= "shubham"
# print(50*s)

# print('z' in msg)

# built in function

# a = "shubhz"
# print(len(a))
# print(max(a))
# print(min(a))

# string method

# a = "shubham"
# b=98
# print(type(a))
# print(id(a))
# print(id(b))

# import random
# num=random.randint(1,25)
# a = "shubham"
# a.upper()
# print(num)

# name = "Shubham krishna shinde"
# print(name.isalpha())
# print(name.isdigit())
# print(name.isalnum())
# print(name.islower())
# print(name.isupper())
# print(name.startswith("S"))
# print(name.endswith("e"))

# name = "shubham"
# print(name.replace("s", "x"))

# name = "shubham"
# print(name[2:4])
# print(name[2:7])
# print(name[0])

# concatination

# name = "shinde"
# name1 = " shubham"

# fullName = name + name1
# print(fullName)

# student1 = "shubham"
# id1 = 58
# div1 = "A"
# age1 = 26

# student2 = "akshay"
# id2 = 67
# div2 = "B"
# age2 = 27

# print(div1)
# print(age2)


# def Student(name, age, rollNum):
#     return name, age, rollNum


# # print(Student("shubham", 26, 58))
# print(Student("Akshay", 27,65))
        
# a = 23
# b = 54
# A=76
# print(a)

# a = b = "shubham"
# print(a,b)

# for i in range(1, 11):
#     print(i)



# a=7
# surface_area=6*(a**2)
# volume=a**3

# print(surface_area, volume)


# def positiveNum():
# num = [40, -30, 20, 30, -29, -90]
# count = 0
# for i in num:
#     if i <= 0:
#         count = count + 1
#         print(count)
# print(count, "Total count")
        
# positiveNum()

# num = [40, 43, 70, 59, 20, -80, 8, -9]
# count=0
# for i in num:
#     if i > 0:
#         if i % 2 == 0:
#             count = count + i
            
# print(count)

# i = 1
# num=3
# while i <11:
#     table = num * i
#     print(table)
#     i=i+1

# str1 = "Shubham Shinde"
# # for ch in str1:
# #     print(str1[::-ch])
# reversed_string=""
# for i in str1:
#     reversed_string = i + reversed_string
    
# print(reversed_string)

# age = int(input("Enter the Age: "))

# if age < 13:
#     print("Child")
    
# elif age in range(13, 19):
#     print("Teenage")
    
# elif age in range(20, 59):
#     print("Adult")
    
# else:
#     print("Senior")

# age = int(input("Enter the Age: "))
# day = input("Enter the Day: ")

    
# if age > 18:
#     price = 12
#     print(price)
    
# elif day == "Wednesday":
#     print("Your Ticket Price is ", price=price-2)
    
# else:
#     price = 8
#     print(price)

# mark = int(input("Enter the Marks: "))
# if mark >= 101:
#     print("Please Enter Valid Marks")
#     exit()
# if mark >= 90:
#     print("A")
    
# elif mark >= 80:
#     print("B")
    
# elif mark >= 70:
#     print("C")
    
# elif mark >= 60:
#     print("D")
    
# else:
#     print("F")

# a = int(input("Enter 1"))
# b = int(input("Enter 2"))

# sum = a + b

# if sum % 2 == 0:
#     print(sum, "Even")

# else:
#     print(sum, "Odd")

# Reverse string

# str1 = "Shubham"

# print(str1[::-1])

# str1 = "13425"
# reversedString=""

# for i in str1:
#     reversedString = i + reversedString
# print(reversedString)
    
    
# def revers(str1):
#     reverseString = " "
#     for i in str1:
#         reverseString = i + reverseString
#     return reverseString


# a = revers("Shubham")
# print(a)



# print((3*(3+1))//2)


# def finding_missing_num(nums):
#     n = len(nums)
#     expectedNum = (n * (n + 1) // 2)
#     actualNum = sum(nums)
#     missing_num =actualNum-expectedNum
#     return missing_num


# nums = [5,8,1]
# missing_num = finding_missing_num(nums)
# print(missing_num)


# def palidrome(s):
#     s = "".join(i.lower() for i in s if i.isalnum())
#     return s == s[::-1]


# s = "ShahS"
# check = palidrome(s)
# print(check)





# BASIC Practice Probles

# print("Hello World") 

# num1 = int(input("Enter num 1: "))
# num2 = int(input("Enter num 2: "))

# addNum = num1 + num2

# print(addNum)

# num1=int(input("Enetr num 1: "))
# print(num1)

# divisor = int(input("Enter divisor: "))
# divident = int(input("Enter divident: "))

# division = divisor / divident

# print(division)


# def quotientRemainder(divident, divior):
#     quotient = divident // divior
#     remainder = divident % divior
#     return quotient, remainder

# divident = int(input("Enter divident: "))
# divisor = int(input("Enter divisor: "))

# quotient= quotientRemainder(divident, divisor)
# remainder = quotientRemainder(divident, divisor) 

# if remainder == 0:
#     print("Fool")
# else:
#     print(quotient, remainder)


# def division_with_remainder(dividend, divisor):
#     remainder = dividend % divisor
#     return remainder

# dividend = int(input("Enter the dividend: "))
# divisor = int(input("Enter the divisor: "))

# remainder = division_with_remainder(dividend, divisor)

# if remainder == 0:
#     print("fool")
# else:
#     print("The remainder is:", remainder)



# import sys
# # a = sys.getsizeof(154267987676)
# # print(a)

# # print(sys.getsizeof(6.0))
# # print(sys.getsizeof(True))

# print(sys.getsizeof("a"))




# SWAP TWO NUMBERS


# def swapNum(a, b):
#     a = a + b
#     b = a - b
#     a = a-b
#     return a, b



# a,b=swapNum(5987, 234512342)
# print(a,b)


# def swapNum(a, b):
#     temp = a
#     a = b
#     b = temp
#     return a, b,


# a, b = swapNum(5, 4)
# print(a,b)

# ascii = ord("A")
# print(ascii)


# asciii = float("A")
# print(asciii)


# def multiTwo(a, b):
#     Multiply_of_two_dec = a * b
#     return Multiply_of_two_dec


# Multiplication = multiTwo(3.98, 7.97)
# print(Multiplication)


# def EvenOdd(num):
#     if num % 2 == 0:
#         return num, " is EVEN"
#     else:
#         return num, " is ODD"

# print(EvenOdd(1997))


# def VowelOr(char):
#     lst = ["a","e","i","o","u"]
#     if char in lst:
#         print("Vowel")
#     else:
#         print("consolant")

# VowelOr("g")


# def largestNum(a, b, c):
#     if a > b or a > c:
#         print(a, "a is greater")
#     elif b > a or b > c:
#         print(b, "b is greater")
#     elif c > a or c > b:
#         print(c, "c is greater")
#     else:
#         print("All numbers are aqual")

# largestNum(29, 76, 34)

# import math
# def quad(a, b, c):
#     dis = b ** 2 - 4 * a * c
    
#     if dis < 0:
#         return None, None

#     root1 = -b + math.sqrt(dis) / 2 * a
#     root2 = -b - math.sqrt(dis) / 2 * a
#     return root1, root2

    
# root1, root2 = quad(1,-3,2)
# if root1 and root2 is not None:
#     print(root1)
#     print(root2)
# else:
#     print("not real root")


# def LeapYear(year):
#     if year % 4 == 0 or year % 100 != 0 and year % 400 == 0:
#         print(year, "Leap Year")
#     else:
#         print(year, "Not leap year")

# LeapYear(2005)


# def sumOfNatural(num):
#     sum=0
#     for i in range(1, num+1):
#         sum = i + sum
#         print(sum)

# sumOfNatural(10)

# sum = 0
# i = 1
# while i <= 10:
#     sum = sum + i
#     i = i + 1
# print(sum)


# def fact(n):
#     if n == 0:
#         return 1
#     else:
#         result = 1
#         while n > 0:
#             result = result * n
#             n = n - 1
#         return result

# print(fact(5))


# def table(n):
#     for i in range(1, 11):
#         MultiplicationTable = n * i
#         print(n, "*", i, "=", MultiplicationTable)

# table(5)


# def table(n):
#     multpletable = 1
#     i = 1
#     while i <= 10:
#         multpletable = n * i
#         print(n, "*", i, "=", multpletable)
#         i = i + 1


# table(5)


# def fibo(n):
#     if n >= 2:
#         return fibo(n - 1) + fibo(n - 2)
        
#     else:
#         return n

# print(fibo(15))


# def fibo(num):
#     n1, n2 = 0, 1
#     for i in range(2, num):
#         n3 = n1 + n2
#         n1 = n2
#         n2 = n3
#         print(n3)

# fibo(15)

# def fibo():
#     n1, n2 = 0, 1
#     for i in range(100):
#         if n1 > 100:
#             break
#         n3 = n1 + n2
#         n1 = n2
#         n2 = n3
#         print(n3)

# fibo()


# def fib(n):
#     fibnacii=[0,1]
#     for i in range(n):
#         nxt_fibnacii = fibnacii[-1] + fibnacii[-2]
#         if nxt_fibnacii <= n:
#             fibnacii.append(nxt_fibnacii)
#         else:
#             break
#     print(fibnacii)

# fib(100)   


# def fibonacii_series_upto_n(n):
#     fibonacoo_series = [0, 1]
#     for i in range(n):
#         nxt_fabonacii = fibonacoo_series[-1] + fibonacoo_series[-2]
#         if nxt_fabonacii <= n:
#             fibonacoo_series.append(nxt_fabonacii)
#         else:
#             break
#     print(fibonacoo_series)

# fibonacii_series_upto_n(100)


# def find_fib_series_upto_n(n):
#     fibonacii_series = [0, 1]
#     for i in range(n):
#         nxt_fibonacii = fibonacii_series[-1] + fibonacii_series[-2]
#         if nxt_fibonacii <= n:
#             fibonacii_series.append(nxt_fibonacii)
#         else:
#             break
#     print(fibonacii_series)

# find_fib_series_upto_n(100)


# def fib_series_upto_n(n):
#     fibonacii_series = [0, 1]
#     for i in range(n):
#         nxt_fibonacci = fibonacii_series[-1] + fibonacii_series[-2]
#         if nxt_fibonacci <= n:
#             fibonacii_series.append(nxt_fibonacci)
#         else:
#             break
#     print(fibonacii_series)

# fib_series_upto_n(100)

# Even num in list


# def EvenOdd(lst_1):
#     new_Even_lst=[]
#     new_Odd_lst=[]

#     for i in lst_1:
#         if i % 2 == 0:
#             new_Even_lst.append(i)
#         else:
#             new_Odd_lst.append(i)
#     return new_Even_lst, new_Odd_lst


# lst_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new_Even_lst, new_Odd_lst = EvenOdd(lst_1)
# print(new_Even_lst, "EVEN NUM")
# print(new_Odd_lst, "ODD NUM")


# def EvenOdd(Userlist):
#     EvenList = []
#     OddList = []
#     for i in Userlist:
#         if i % 2 == 0:
#             EvenList.append(i)
#         else:
#             OddList.append(i)

#     return EvenList, OddList


# UserList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# EvenList, OddList = EvenOdd(UserList)
# print("Even Number list: " ,EvenList)
# print("Odd Number list: " ,OddList)


# def SumOfEvenOdd(UserList):
#     EvenList = []
#     OddList = []
#     EvenNumSum = 0
#     OddNumSum=0
#     for i in UserList:
#         if i % 2 == 0:
#             EvenList.append(i)
#             EvenNumSum = EvenNumSum + i
#         else:
#             OddList.append(i)
#             OddNumSum = OddNumSum + i
#     return EvenList, OddList, EvenNumSum, OddNumSum


# UserList=[1,2,3,4,5,6,7,8,9,10]
# EvenList, OddList, EvenNumSum, OddNumSum = SumOfEvenOdd(UserList)
# print("Even Number list: ", EvenList)
# print("Odd NUmbar list: ", OddList)
# print("Sum of All Even Numbers From User List", EvenNumSum)
# print("Sum of All Odd Numbers From User List", OddNumSum)

