# 1- write a program which takes 2 inputs from the user :
#    weight(kg) and height(meter) and prints the BMI in the output.

weight = float(input('in kg:'))
height = float(input('in mtr:'))
BMI = weight/height**2
print('The BMI is:', BMI)

# 2- write a program which takes the name of the user as input and replace all the occurrence of character 'a' in the
#    name to 'b' and print it.

name = input('The name is:')
print('The name is :', name.replace('a', 'b'))

# 3- write a program which takes 2 inputs from user as principal amount (int) and rate of annual interest (float) and
#    print the expected total amount  after  2 years.
#    example : principle : 100 , interest percent 10  then amount after 2 years will be : 100*1.1*1.1 = 121

principle_amount = int(input('The principle amount is:'))
interest = float(input('The interest rate is:'))
time = float(input('The duration in yrs:'))
total_amount = principle_amount * (1 + interest/100)**time
print('The total amount is:', total_amount)

# 4- write a program which takes city name from user input. irrespective of in which case user enters the city name,
#    print the city name in camel case meaning first letter should be capital and rest in small.

city = input('The city name is:')
print(city.capitalize())

# if city contains more than 1 word

city = input('The city name is:')
print(city.title())

# 5- write a program which takes the name of the user as input and print the index of character 'a' in the string.
#    if 'a' is not there then return -1.

name = input()
print('The index is:' ,name.find('a'))

'''
difference between find and index methods
 if the particular string is not present in the input, index gives an error whereas find returns -1
'''

# 6-  Display the number of letters in the below string
#     my_word = "antidisestablishmentarianism"

my_word = "antidisestablishmentarianism"
print(f'The length of the string is {len(my_word)}')

# 7- take 3 inputs from user : first name , last name and age . Display the information in below format
# example
# first name : MOhit
# last name : sharma
# age 32
#
# Display : my name is Mohit Sharma and I am 32 years old.
# note that first letter of first name and last name both should be in capital letters and rest in small.

first_name = input('Enter first name here:')
last_name = input('Enter last name here:')
age = int(input('Enter age here:'))
print(f'My name is {first_name.capitalize()} {last_name.capitalize()} and I am {age} years old.')

# 8- take 3 inputs from user : first name , last name and company name.
# create the email alias for the user and display it.
# Email alias is first 2 letters of first name , last 3 letters of last name and @company.com
# example
# first name : MOhit
# last name : sharma
# company : infosys
#
# Display : morma@infosys.com
#
# note full email id should -be in lower case

first_name = input('Enter first name here:')
last_name = input('Enter last name here:')
company = input('Enter company name here:')
print(f"The email_id is: {first_name[:2].lower()}{last_name[-3:].lower()}@{company.lower()}.com")
