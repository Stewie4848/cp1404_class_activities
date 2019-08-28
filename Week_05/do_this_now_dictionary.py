def main():
    name_to_age = {}
    name = input("Name: ")
    age = int(input("Age: "))
    name_to_age[name] = age
    for name, age in name_to_age.items():
        print("{}    -    {}".format(name, age))


main()
