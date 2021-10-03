def pocet_suborov():
    while True:
        cislo = input("Zadajte počet súborov")
        try:
            return int(cislo)
        except ValueError:
            print("Nebolo zadané celé číslo!")

input = []
pocet = 0

with open("basnicka.txt") as subor:
    for slovo in subor:
        input += slovo.split()

for i in range(pocet_suborov()):
    pocet += 1
    if pocet == len(input):
        pocet -= len(input)
    with open(f"""slovo{pocet}""", mode="w") as subor:
        print(input[pocet - 1], file=subor)