
import random
tableau_jeu=[]
# Initialisation d'une liste de 10 éléments
for i in range (0,10):
 tableau_jeu.append (random.randint (1,10))
 
saisie=int (input ("Votre nombre entre 1 et 10 :"))


#~ Recherche séquentielle dans une liste non triée
lg_tableau_jeu = len (tableau_jeu)

# Curseur de position dans le tableau
pos = 0
# On parcourt la liste tant que la valeur n'a pas été trouvée
# ET que l'on ne dépasse pas la taille du tableau
while ((pos < lg_tableau_jeu) and (tableau_jeu [pos] != saisie)):
 pos += 1
if ( pos == lg_tableau_jeu ):
 print ("Gagné")
else:
 print ("Perdu")
print ("\nContrôle visuel")



# On affiche le tirage pour contrôle
for tirage in tableau_jeu:
  print (tirage,end=',')


print()