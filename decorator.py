""" def my_decorator(func):
    def wrapper():
        print("Befor function")
        func()
        print("After function")
    return wrapper

def say_hi():
    print("Hello")

say_hi_function = my_decorator(say_hi)
say_hi_function()
 """

# import re
# text = " cat bat rat atm"
# print(re.findall(".at", text))

import re

text = "Call me at 9876543210 or email test@gmail.com"

phone = re.findall("\d{10}", text)
email = re.findall("\w+@\w+\.\w+", text)
print(phone)
print(email)
