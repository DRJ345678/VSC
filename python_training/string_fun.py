name = input("What is your first and last name? ")
print("Uppercase:", name.upper())
print("Reversed:", name[::-1])
print("First name:", name.split()[0])

char_count = len(name.replace(" ",""))
print("Character count (no spaces):", char_count)