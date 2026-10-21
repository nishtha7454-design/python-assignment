with open("data.txt", "w") as f:
    f.write("Hassan\nMansiya\n")

name = input("Enter a new name: ")

with open("data.txt", "a") as f:
    f.write(name + "\n")

with open("data.txt", "r") as f:
    print(f.read())
