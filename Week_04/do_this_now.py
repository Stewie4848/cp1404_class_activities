name = input("Name:")
VOWELS = "aeiou"
vowel_count = 0
for characters in name:
    if characters.lower() in VOWELS:
        vowel_count += 1

print("Out of {} letters, {} has {} vowels".format(len(name), name, vowel_count))
