from time import sleep

#Matrice =[
#["⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛"],
#["⬛" ,"👍" ,"⬛" ,"👍" ,"👍" ,"👍" ,"👍" ,"👍" ,"⬛" ,"⬛"],
#["⬛" ,"👍" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"👍" ,"👍" ,"⬛"],
#["⬛" ,"👍" ,"⬛" ,"👍" ,"👍" ,"👍" ,"⬛" ,"⬛" ,"👍" ,"⬛"],
#["⬛" ,"👍" ,"⬛" ,"👍" ,"⬛" ,"👍" ,"⬛" ,"👍", "👍" ,"⬛"],
#["⬛" ,"👍" ,"👍" ,"👍" ,"⬛" ,"👍" ,"⬛" ,"👍" ,"⬛" ,"⬛"],
#["⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"👍" ,"⬛" ,"👍" ,"👍" ,"⬛"],
#["⬛" ,"👍" ,"👍" ,"👍" ,"⬛" ,"👍" ,"⬛" ,"⬛" ,"👍" ,"⬛"],
#["⬛" ,"👍" ,"⬛" ,"👍" ,"👍" ,"👍" ,"👍" ,"👍" ,"👍" ,"⬛"],
#["⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛"],
#]





Matrice =[
["⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛", "⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛"],
["⬛" ,"👍" ,"👍" ,"👍" ,"👍" ,"👍" ,"👍" ,"👍" ,"👍", "👍" ,"👍" ,"👍" ,"👍" ,"👍" ,"👍" ,"👍" ,"👍" ,"⬛"],
["⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"👍" ,"👍", "👍" ,"⬛" ,"⬛" ,"👍" ,"👍" ,"👍" ,"👍" ,"👍" ,"⬛"],
["⬛" ,"👍" ,"👍" ,"👍" ,"👍" ,"👍" ,"👍" ,"⬛" ,"👍", "⬛" ,"👍" ,"👍" ,"⬛" ,"👍" ,"👍" ,"👍" ,"👍" ,"⬛"],
["⬛" ,"👍" ,"👍" ,"⬛" ,"👍" ,"👍" ,"👍" ,"👍" ,"⬛", "👍" ,"👍" ,"👍" ,"👍" ,"⬛" ,"👍" ,"👍" ,"👍" ,"⬛"],
["⬛" ,"👍" ,"👍" ,"⬛" ,"👍" ,"👍" ,"👍" ,"👍" ,"👍", "👍" ,"👍" ,"👍" ,"👍" ,"👍" ,"⬛" ,"👍" ,"👍" ,"⬛"],
["⬛" ,"👍" ,"⬛" ,"👍" ,"👍" ,"👍" ,"👍" ,"👍" ,"👍", "👍" ,"👍" ,"👍" ,"👍" ,"👍" ,"⬛" ,"👍" ,"👍" ,"⬛"],
["⬛" ,"👍" ,"⬛" ,"👍" ,"👍" ,"👍" ,"👍" ,"👍" ,"👍", "👍" ,"👍" ,"👍" ,"👍" ,"👍" ,"⬛" ,"👍" ,"👍" ,"⬛"],
["⬛" ,"👍" ,"👍" ,"⬛" ,"👍" ,"👍" ,"👍" ,"👍" ,"👍", "👍" ,"👍" ,"👍" ,"👍" ,"⬛" ,"👍" ,"👍" ,"👍" ,"⬛"],
["⬛" ,"👍" ,"👍" ,"⬛" ,"👍" ,"👍" ,"👍" ,"👍" ,"👍", "👍" ,"👍" ,"👍" ,"👍" ,"⬛" ,"👍" ,"👍" ,"👍" ,"⬛"],
["⬛" ,"👍" ,"👍" ,"👍" ,"⬛" ,"👍" ,"👍" ,"👍" ,"👍", "👍" ,"👍" ,"👍" ,"⬛" ,"👍" ,"👍" ,"⬛" ,"👍" ,"⬛"],
["⬛" ,"👍" ,"👍" ,"👍" ,"👍" ,"⬛" ,"⬛" ,"👍" ,"👍", "👍" ,"⬛" ,"⬛" ,"👍" ,"👍" ,"👍" ,"👍" ,"👍" ,"⬛"],
["⬛" ,"👍" ,"👍" ,"👍" ,"👍" ,"👍" ,"👍" ,"⬛" ,"⬛", "⬛" ,"👍" ,"👍" ,"👍" ,"👍" ,"⬛" ,"👍" ,"👍" ,"⬛"],
["⬛" ,"👍" ,"👍" ,"👍" ,"👍" ,"👍" ,"👍" ,"👍" ,"👍", "👍" ,"👍" ,"👍" ,"👍" ,"👍" ,"⬛" ,"👍" ,"👍" ,"⬛"],
["⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛", "⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛"],
]




Matrice =[
["⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛", "⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛"],
["⬛" ,"👍" ,"👍" ,"👍" ,"👍" ,"👍" ,"👍" ,"👍" ,"👍", "👍" ,"👍" ,"👍" ,"👍" ,"👍" ,"👍" ,"👍" ,"👍" ,"⬛"],
["⬛" ,"👍" ,"👍" ,"👍" ,"👍" ,"👍" ,"👍" ,"👍" ,"👍", "👍" ,"👍" ,"👍" ,"👍" ,"👍" ,"👍" ,"👍" ,"👍" ,"⬛"],
["⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛", "⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"👍" ,"⬛"],
["⬛" ,"👍" ,"👍" ,"👍" ,"👍" ,"⬛" ,"👍" ,"👍" ,"👍", "⬛" ,"⬛" ,"👍" ,"👍" ,"⬛" ,"👍" ,"👍" ,"👍" ,"⬛"],
["⬛" ,"👍" ,"👍" ,"⬛" ,"👍" ,"👍" ,"👍" ,"⬛" ,"👍", "⬛" ,"👍" ,"⬛" ,"👍" ,"⬛" ,"👍" ,"👍" ,"👍" ,"⬛"],
["⬛" ,"👍" ,"👍" ,"⬛" ,"👍" ,"⬛" ,"👍" ,"⬛" ,"👍", "👍" ,"👍" ,"⬛" ,"👍" ,"⬛" ,"👍" ,"⬛" ,"⬛" ,"⬛"],
["⬛" ,"👍" ,"👍" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛", "⬛" ,"👍" ,"👍" ,"👍" ,"⬛" ,"👍" ,"👍" ,"👍" ,"⬛"],
["⬛" ,"👍" ,"👍" ,"⬛" ,"👍" ,"👍" ,"👍" ,"👍" ,"👍", "👍" ,"⬛" ,"👍" ,"👍" ,"⬛" ,"👍" ,"👍" ,"👍" ,"⬛"],
["⬛" ,"👍" ,"👍" ,"⬛" ,"👍" ,"⬛" ,"👍" ,"👍" ,"👍", "👍" ,"⬛" ,"👍" ,"👍" ,"⬛" ,"⬛" ,"⬛" ,"👍" ,"⬛"],
["⬛" ,"👍" ,"👍" ,"⬛" ,"👍" ,"👍" ,"⬛" ,"👍" ,"👍", "⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"👍" ,"👍" ,"👍" ,"⬛"],
["⬛" ,"👍" ,"👍" ,"👍" ,"⬛" ,"👍" ,"👍" ,"⬛" ,"👍", "⬛" ,"👍" ,"👍" ,"👍" ,"⬛" ,"👍" ,"👍" ,"👍" ,"⬛"],
["⬛" ,"👍" ,"👍" ,"👍" ,"⬛" ,"👍" ,"👍" ,"⬛" ,"👍", "⬛" ,"👍" ,"⬛" ,"👍" ,"👍" ,"👍" ,"👍" ,"👍" ,"⬛"],
["⬛" ,"👍" ,"👍" ,"👍" ,"👍" ,"👍" ,"👍" ,"⬛" ,"👍", "👍" ,"👍" ,"⬛" ,"👍" ,"⬛" ,"👍" ,"👍" ,"👍" ,"⬛"],
["⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛", "⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛" ,"⬛"],
]




def deplacementPossible(Matrice,Depart):
    xmax = len(Matrice)
    ymax = len(Matrice[0])
    x = Depart[0]
    y = Depart[1]
    listeReturn = []
    if x >= 1:
        if Matrice[x-1][y] == "👍":
            listeReturn.append((x-1,y))
    if x <= xmax - 1:
        if Matrice[x+1][y] == "👍":
            listeReturn.append((x+1,y))
    if y >= 1:
        if Matrice[x][y-1] == "👍":
            listeReturn.append((x,y-1))
    if y <= ymax - 1:
        if Matrice[x][y+1] == "👍":
            listeReturn.append((x,y+1))

    #Matrice[x][y] = "⬛"
    #for i in range(ymax):
    #    print(Matrice[i])
    return listeReturn

def netoyage(liste):
    l = len(liste)
    flag = False
    for i in range(l):
        if not flag:
            for j in range(l):
                if not flag:
                    if liste[i] == liste[j] and i != j:
                        del liste[i]
                        netoyage(liste)
                        flag = True

    return liste










GPS = {}

depart = (1,1)


listePointAtteint = [depart]

listePointAtteintPassagePrecedant = [depart]
listePointAtteintPassage = []


for i in range(100):
    listePointAtteintPassage = []
    for i in listePointAtteintPassagePrecedant:

        listeDeplacementPossible = deplacementPossible(Matrice,i)


        for pos in listeDeplacementPossible:
            #Matrice[pos[0]][pos[1]] = "❌"
            listePointAtteintPassage.append(pos)
            listePointAtteint.append(pos)
            if not pos in GPS.keys():
                GPS[pos] = i


    listePointAtteintPassagePrecedant = netoyage(listePointAtteintPassage)



# affichage
#for i in listePointAtteint:
    #Matrice[i[0]][i[1]] = "❌"

for i in Matrice:
    print(" ".join(i))



    #sleep(0.75)
    #print("")
    #print("")
    #print("")
    #print("")
    #print("")




pos = (4,12)
Matrice[pos[0]][pos[1]] = "❌"

chemin = []
print(GPS)
while True:
    chemin.insert(0,pos)
    print(pos)
    pos = GPS[pos]
    if pos == depart:
        break


chemin.insert(0,depart)


for pos in chemin:
    Matrice[pos[0]][pos[1]] = "✅"
    for i in Matrice:
        print(" ".join(i))
    sleep(0.2)
    print("")
