# def main():
#     age = input("Please enter your age: ")
#     age = age_check(age)
#     if age < 0 or age > 150:
#         age = age_check()
#
#
# def age_check(age):
#     while age is not age.isalpha():
#         print("Invalid age!")
#         age = input("Enter age:")
#         return age

is_valid_input = False
while not is_valid_input:
    try:
        age = int(input("Age:"))
        if age < 0:
            print("Age must be >=0")
        else:
            is_valid_input = True
    except ValueError:
        print("Invalid (not an integer)")
if age % 2 == 0:
    print("Your age is even")
else:
    print("Your age is odd")
print("Next year you will be", age + 1)