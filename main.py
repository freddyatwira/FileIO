names =[]
name = input("Enter a name: ").capitalize()

names.append(name)


with open("names.txt", "a") as file:
    file.write(f"{name}\n")

print("Done!")

with open("names.txt", "r") as file:
    for line in file:
        print(line.strip())