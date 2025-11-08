#Indiquer les notes du barême ci-dessous entre les crochets séparé par une virgule
bareme = [30,20,20,20]
Nbr_notes = len(bareme)
print(bareme)

def eleve():
    j = 0
    notes_eleve = []
    for j in range(Nbr_notes):
        notes_eleve.append(
            float(input(f"Entrez la note n° {j+1} de l'élève: ")))
    somme_eleve = sum(notes_eleve)
    note20 = (somme_eleve*20)/sum(bareme)
    note20 = round(note20, 2)
    print("la moyenne de l'élève est: " + str(note20) + " /20")


modif_bareme = input("Voulez-vous modifier le barême? (y/n) : ")
if modif_bareme == "y":
    bareme.clear()
    Nbr_notes = int(input("Entrez le nombre de notes du barême: "))
    i = 0
    while i < Nbr_notes:
        i += 1
        bareme.append(int(input(f"Entrez la note n° {i}: ")))
    print(bareme)
    eleve()

else:
    eleve()
