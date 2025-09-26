# opdracht 1 HelloWorld.py
print("Hello world!")

# opdracht 2 Hobbies.py
print("Noem 3 hobbies")

Hobbie1 = input("Wat is je eerste hobbie? ")
Hobbie2 = input("Wat is je tweede hobbie? ")
Hobbie3 = input("Wat is je derder hobbie? ")

hobbieLijst = [{Hobbie1}, {Hobbie2}, {Hobbie3}]

print("dit zijn jou hobbies: ")
print(hobbieLijst)

# opdracht 3  Getallenreeks.py
x = range(0, 100, 10)
for n in x:
    print(n)