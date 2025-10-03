# opdracht 1 HelloWorld.py
#print("Hello world!")

# opdracht 2 Hobbies.py
#print("Noem 3 hobbies")
#
#Hobbie1 = input("Wat is je eerste hobbie? ")
#Hobbie2 = input("Wat is je tweede hobbie? ")
#Hobbie3 = input("Wat is je derde hobbie?  ")
#
#hobbieLijst = [{Hobbie1}, {Hobbie2}, {Hobbie3}]
#
#print("dit zijn jou hobbies: ")
#print(hobbieLijst)

# opdracht 3  Getallenreeks.py
#x = range(0, 100, 10)
#for n in x:
#    print(n)

# opdracht 4 spel_uitslag.py
#Player1 = int(input("Wat is de score van speler 1? "))
#Player2 = int(input("Wat is de score van speler 2? "))
#
#if (Player1 > Player2):
#    print("Speler 1 is de winnaar!!!")
#elif (Player2 > Player1):
#    print("Speler 2 is de winnaar!!!")
#elif (Player1 == Player2):
#    print("Het is gelijkspel!!")
#else:
#    print("Voer de scores opnieuw in!")

# opdracht 5 vermenigvuldigen.py
#getal1 = int(input("Wat is je eerste getal? "))
#getal2 = int(input("Wat is je tweede getal? "))
#
#def vermenigvuldiging():
#    sum = getal1 * getal2
#    print(getal1, " x ", getal2, " = ", sum)
#
#vermenigvuldiging()

# opdracht 6 rijbewijs.py
leeftijd = float(input("Wat is je leeftijd? "))

if(leeftijd > 16.5):
    print("Je mag beginnen met lessen!!")
elif(leeftijd == 16.5):
    print("\U0001F389 Gefeliciteerd, je mag nu lessen! \U0001F389")
else:
    print("Je bent te jong!")

# opdracht 7 faculty.py
faculteit = int(input("Wat is het magische getal? "))

def faculty():
    basis = 1
    for i in range(2, faculteit + 1):
        basis *= i
    return basis

print(faculty())

# opdracht 8 stemhokje.py
Dominique = 1
Zacharia = 1

MijnPresident = input("Ik kies voor: ")


while MijnPresident != "UITSLAG":
    if MijnPresident == "Dominique":
        Dominique += 1
        MijnPresident = input("Ik kies voor: ")
    elif MijnPresident == "Zacharia":
        Zacharia += 1
        MijnPresident = input("Ik kies voor: ")

def Uitslag():
    if (Dominique > Zacharia):
        print("Dominique is tot president verkozen met", Dominique, "stemmen!")
    elif (Zacharia > Dominique):
        print("Zacharia is tot president verkozen met", Zacharia, "stemmen!")
    else:
        print("Er komt een herverkiezing!")

Uitslag()

# opdracht 9 