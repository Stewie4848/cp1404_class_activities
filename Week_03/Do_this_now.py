def main():
    word = input("Enter word: ").lower()
    print(count_letters(word))


def count_letters(string):
    """Count the number of letters in a string"""
    count = 0
    for character in string:
        if character.isalpha():
            count += 1
    return count


def is_adult(age):
    if age >= 18:
        return True
    else:
        return False


main()
