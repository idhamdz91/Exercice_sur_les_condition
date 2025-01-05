#Ecrire 01 : un programme Python qui lit les notes de deux contrôles d’une matière donnée, puis calcule et affiche la moyenne obtenue. Dans le cas où la moyenne est supérieure ou égale à 10, il affichera davantage le message de félicitation suivant : Félicitations ! Vous avez validé cette matière.

'''note1 = float(input("veuillez introdure la note 01: "))

note2 = float(input("veillez introduire la note 02: "))

note=[note1, note2,]

moyenne = sum(note)/len(note)

if moyenne >= 10:

    print ("la moyenne est de : ", moyenne, "Félicitation !")

else :

        print (moyenne)

 
# Ecrire un programme Python, qui lit un nombre réels x, puis affiche son inverse 1/x. Dans le cas où x est nul, on affichera plutôt le message : L’inverse n’existe pas pour 0.
 
x = float(input("Veuiller introduire un nombre: "))

resulat = 1/x

if x != 0:

    print(resulat)

else:

    print ("l'inversse n'existe pas pour 0 ")'''


#Exercice 03 : Ecrire un programme Python qui lit deux entier a et b puis affiche selon le cas :

"""a = b ;
a < b ;
a > b."""

'''a = float(input("Veuillez introduire la valeur de a: "))
b = float(input("Veuillez introduire la valeur de b: "))

if a == b:
     print ("a=b")
elif a < b:
     print ("a<b")
else:
     print ("a>b")'''


'''Exercice 04 :Ecrire un programme Python qui lit une note entre 0 et 20 puis affiche :

Non validé, si: note < 10 ;
Passable, si : 10 ≤ note < 12 ;
Assez bien, si : 12 ≤ note < 14 ;
Bien, si : 14 ≤ note < 16 ;
Très bien, si : 16 ≤ note < 18 ;
Excellent, si : 18 ≤ note ≤ 20 ;'''

'''note = int(input("Veuillez entré une notre entre 0 et 20: "))
if note < 10:
    print ("non validé")
elif 10 <= note < 12:
    print ("Passable")
elif 12 <= note < 14:
    print ("Assez bien")
elif 14 <= note < 16:
    print ("Bien")
elif 16 <= note < 18:
    print ("Trés bien")
elif 18 <= note <= 20:
    print("Excellent ! ")
else:
    print ("Note non valide, Vuillez entré une note entre 0 et 20 !")'''

'''Ecrire 05: un programme Python qui choisi aléatoirement un nombre secret entre 1 et 10, puis demande à l’utilisateur de le prédire et donne l’un des verdicts suivants :

Bravo !: si le nombre a été bien prédis ;
Donner une deuxième et dernière chance à l’utilisateur si le nombre entré est juste en dessus ou en dessous du nombre secret et d’afficher :
Bon travail !: si cette deuxième tentative est correcte ;
Pas correct !: si elle est fausse.
Pas correct !: si la première tentative est loin du nombre secret.'''

import random
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle (liste)
mahdii = int(input("veulliez insert un nombre entre 1 et 10 : "))
aleatoirE = liste [0]
if aleatoirE == mahdii:
    print("Bon travail !")
else:
    print ("Pas correct !")
