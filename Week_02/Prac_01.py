"""Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%
"""


# ctrl+alt+l

def main():
    sales = float(input("Enter sales: $"))
    while sales >= 0:
        if sales < 1000:
            sales_bonus = sales * 0.10
        else:
            sales_bonus = sales * 0.15
        sales = float(input("Enter sales: $"))
        print("$", sales_bonus)

main()

"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

score = float(input("Enter score: "))

if score < 0 or score > 100:
    print("Invalid score")
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")
