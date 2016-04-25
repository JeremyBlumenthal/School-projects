"""
   projet_1 = "M'enfin"
   author = "Jeremy Blumenthal"
   matricule = "000397371"
   cours = "INFO-F-101"
   groupe_tp_et_assistant = "Groupe 1, Thierry Massart"
"""
from random import randint, seed
s = int(input("Entrez la seed: "))
seed(s)
H_MAX = 1080 # Correspond à l'heure de fin de journée, 18h00.
t_tot = 0 # Temps total travaillé.
h = 540 # Heure actuelle de la journée.
def temps(x):
    """
       Fonction qui convertit le temps en un tuple heures, minutes.
    """
    h = x//60
    m = x - (h * 60)
    return (h,m)
print("09:00 Gaston arrive au bureau.")
while h < H_MAX:
    he,mi = temps(h)
    print("{00:02d}:{01:02d}".format(he,mi), "OK, pause !")
    randint(1,3)
    r = randint(0,50) # Heure d'arrivée aléatoire du courriel pendant une pause.
    h_arrivée = h + r + 60 # Heure d'arrivée de Prunelle
    h += 50
    if randint(1,3) == 1 and h_arrivée < H_MAX: # 1 chance sur 3 que Prunelle vienne et qu'il arrive avant 18h00.
        a = h_arrivée - h # Temps restant avant l'arrivée de Prunelle.
        he,mi = temps(h)
        he2,mi2 = temps(h_arrivée)
        print("{00:02d}:{01:02d}".format(he,mi), "Attention, Prunelle arrive à", "{00:02d}:{01:02d}".format(he2,mi2))
        if a >= 50:
            print("{00:02d}:{01:02d}".format(he,mi), "OK, pause !")
            h += 50
            a -= 50
        if a >= 40 and a <= 49:
            he,mi = temps(h)
            print("{00:02d}:{01:02d}".format(he,mi), "C'est bon, encore le temps de faire une sieste. Zzz")
            h += 20
            a -= 20
        if a >= 20 and a <= 39:
            he,mi = temps(h)
            print("{00:02d}:{01:02d}".format(he,mi), "C'est bon, encore le temps de faire une sieste. Zzz")
            h += 20
            a -= 20
        if a < 20:
            t_tot += 90 + a
            he,mi = temps(h)
            print("{00:02d}:{01:02d}".format(he,mi), "Il faut travailler. M'enfin.")
            h += 90 + a
            if h < H_MAX: # Condition qui détermine si Prunelle quitte le bureau avant 18h00.
                he,mi = temps(h)
                print("{00:02d}:{01:02d}".format(he,mi), "Prunelle est parti. \\O/")
            else:
                t_tot -= h-H_MAX # Le travail total est corrigé pour ne pas faire du temps supplémentaire.
ht,mt = temps(t_tot)
print("18:00 Fin du service, dure journée.")
print("Temps total travaillé:", ht, "h", mt, "min")

"""
   projet_1 = "M'enfin"
   author = "Jeremy Blumenthal"
   matricule = "000397371"
   cours = "INFO-F-101"
   groupe_tp_et_assistant = "Groupe 1, Thierry Massart"
"""
