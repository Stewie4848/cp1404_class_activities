def main():
    names = ["Tom", "Jack", "Jayde"]
    ages = [18, 19, 18]
    print(find_oldest_name(names, ages))


def find_oldest_name(names, ages):
    if not ages:
        return None
    index_of_oldest = 0
    age_of_oldest = -1
    for i, age in enumerate(ages):
        if age > age_of_oldest:
            index_of_oldest = i
            age_of_oldest = age
    return names[index_of_oldest]


main()
