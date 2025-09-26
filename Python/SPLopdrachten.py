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

# opdracht 4 spel_uitslag.py
Player1 = input("Wat is de score van speler 1? ")
Player2 = input("Wat is de score van speler 2? ")

if (Player1 > Player2):
    print("Speler 1 is de winnaar!!!")
elif (Player2 > Player1):
    print("Speler 2 is de winnaar!!!")
elif (Player1 == Player2):
    print("Het is gelijkspel!")
else:
    print("Voer de scores opnieuw in!")