with open("int_text.txt") as file:
    print(sum((int(line) for line in file)))
