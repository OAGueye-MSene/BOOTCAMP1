import os
import pickle
from random import choice

import gamedata
from gamedata import *
import time


def recup_scores():
    """
        Objectif: Cette fonction récupère les scores enregistrés si le fichier existe.
        Methode: Ouverture de fichier log_game.txt et on enregistre le score
        Besoins: fichier contenant les scores
        Connus: log_game.txt
        Entrées: fichier score
        Sorties: --
        Résultats: on renvoie un dictionnaire dépicklé ou vide.
        Hyphothèses: l'ouverture du fichier log_game doit etre effective

    """

    if os.path.exists(fichierScore):

        fichier = open(fichierScore, "rb")
        mon_depickler = pickle.Unpickler(fichier)
        scores = mon_depickler.load()
        fichier.close()
    else:
        scores = {}
    return scores


def enregistrerScores(scores):
    """
        Objectif: enregistrement des donnees dans log_game.txt
        Methode: recoit en parametre le dictionnaire des scores
        Besoins: le score du gamer a la fin de la partie
        Connus:  log_game.txt
        Entrées: scores
        Sorties: --
        Résultats: Cette fonction se charge d'enregistrer les scores dans le fichier log_game.txt
        Hyphothèses: il faut faudra que le fichier log_game soit bien ouvert
    """
    fichier_scores = open(fichierScore, "wb")
    mon_pickler = pickle.Pickler(fichier_scores)
    mon_pickler.dump(scores)
    fichier_scores.close()


def recupLettre():
    """

        Objectif: recuperation de la lettre saisie par l'utilisateur
        Methode: demander d'entrer une lettre par la fonction input de python
        Besoins:
        Connus: --
        Entrées: --
        Sorties: envoie la lettre saisie
        Résultats:envoie une lettre minuscule a la fonction main
        Hyphothèses: il faut que l'utilisateur emtre une lettre alphabet
    """
    lettre = input("Tapez une lettre: ")
    lettre = lettre.lower()
    return lettre


def choisirMot(niveau):
    """
        Objectif: Recuperer un mot a deviner a partir du fichier mots.text ou mot.txt
        Methode: Ouvrir le fichier et recuperer un mot au hazard avec le niveau choisie
        Besoins: le niveau que l'utilisateur souhaite jouer
        Connus: la liste des mots
        Entrées: niveau
        Sorties: mot
        Résultats: renvoie un resultat a deviner
        Hyphothèses: il faut faudra que le fichier log_game soit bien ouvert
    """
    # print("le niveau est {0}".format(niveau))
    f = open('mot.txt', 'r', encoding='utf8')
    contenu = f.readlines()
    mot = choice(contenu).lower().replace('\n', '')
    # print("le mot est {0}".format(mot))
    if niveau == 1:
        while len(mot) > 4:
            f.close()
            return choisirMot(niveau)

        return mot
    elif niveau == 2:
        while len(mot) < 5 or len(mot) > 7:
            f.close()
            return choisirMot(niveau)

        return mot
    elif niveau == 3:
        while len(mot) < 7:
            f.close()
            return choisirMot(niveau)

        return mot
    else:
        return ""


def recup_mot_masque(mot_complet, lettres_trouvees):
    """
        Objectif: Obtenir un mot masque tout ou en partie
        Methode: recuperer une lettre et tester si elle est dans le mot ou pas
        Besoins: le mot complet et la lettre trouver
        Connus: --
        Entrées:mot_complet et lettres_trouvees
        Sorties: on retour le mot masques
        Résultats: on montre les parties trouvees dans le mot masque
        Hyphothèses: il faudra que les valeurs envoyer soit un mot et une lettre alphbetique
    """
    mot_masque = ""
    for lettre in mot_complet:
        if lettre in lettres_trouvees:
            mot_masque += lettre
        else:
            mot_masque += "_"
    return mot_masque


def recup_nom_utilisateur():
    nom_utilisateur = input("Tapez votre nom: ")

    nom_utilisateur = nom_utilisateur.capitalize()
    if not nom_utilisateur.isalnum():
        print("Ce nom est invalide.")

        return recup_nom_utilisateur()
    else:
        return nom_utilisateur


def Voyelle(lettre):
    """
        Objectif: Tester si une lettre est  une voyelle ou un consonne
        Methode: recuperer une lettre et tester si c'est une voyelle ou nom
        Besoins:un lettre
        Connus: la liste des voyelles
        Entrées: --
        Sorties: 0 ou 1
        Résultats: renvoie 1 si c'est une voyelle 0 le cas contraire
        Hyphothèses: il faudra envoyer une lettre
    """
    voyelles = ['a', 'o', 'i', 'u', 'y', 'e']
    for voyelle in voyelles:
        if lettre == voyelle:
            return 1
    return 0


def choixNiveau():
    """
         Objectif: Savoir quel niveau que l'utilisateur veut jouer
         Methode: on demande un chiffre a l'utilisateur et on lui affiche le niveau choisi
         Besoins:Un Chiffre
         Connus: les trois niveaux
         Entrées: Un chiffre qui le niveau
         Sorties: le niveau
         Résultats: le niveau choisi
         Hyphothèses: il faudra que l'utilisateur entre un entier
    """

    niveau = input(
        "\n\tchoississez un niveau: \n\t Niveau 1: 2-4 lettres à deviner \n\t Niveau 2: 5-7 lettre à deviner \n\t Niveau 3: plus de 7 lettres à deviner :")

    if niveau.isalpha():
        print("\n\t\t- Entrer un nombre !\n")
        return choixNiveau()

    niveau = int(niveau)
    if niveau == 1:
        print("Vous avez choisie le niveau {0}".format(niveau))
        chargementdesdonnes()
        return 1
    elif niveau == 2:
        print("Vous avez choisie le niveau {0}".format(niveau))
        chargementdesdonnes()
        return 2
    else:
        print("Vous avez choisie le niveau {0}".format(niveau))
        chargementdesdonnes()
        return 3


def chargementdesdonnes():
    print("\nChargement des donnees", end='')
    time.sleep(1)
    print(".", end='')
    time.sleep(1)
    print(".", end='')
    time.sleep(1)
    print(".", end='')
    time.sleep(1)
    print("\n")
    chargement()


def Affichage(nbr_chances, nbr_pointErreur):
    """
        Objectif: Afficher l'etat de de validité de l'utilisateur dans le jeu
        Methode:recuperation et affichage du nonbre tentative et du nombre de point-erreur.
        Besoins: On a besoin la valeur de nombre de tentative et de celle du point-erreur
        Connus: --
        Entrées: nbr_chances et nb_pointErreur
        Sorties: Affichage du nombre de tentative et du nombre de point d'erreur
        Résultats: Affichage des oint
        Hyphothèses: il faudra envoyer des valeur correct de point tentative et de point erreur
    """
    print("##############################################\n\n")
    print("Vous avez {0} point-erreur".format(nbr_pointErreur))
    print("##############################################\n\n")
    print("Vous avez {0} tentative".format(nbr_chances))
    print("##############################################\n\n")
    var = 'o'

    if nbr_chances == 5:
        print("  +-----+ \n"
              "  |     |\n"
              "  |     |\n"
              "  |     |\n"
              "  |     O\n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "######")
    elif nbr_chances == 4:
        print("  +-----+ \n"
              "  |     |\n"
              "  |     |\n"
              "  |     |\n"
              "  |     O\n"
              "  |    / \n"
              "  |      \n"
              "  |      \n"
              "######")
    elif nbr_chances == 3:
        print("  +-----+ \n"
              "  |     |\n"
              "  |     |\n"
              "  |     |\n"
              "  |     O\n"
              "  |    /| \n"
              "  |      \n"
              "  |      \n"
              "######")
    elif nbr_chances == 2:
        print("  +-----+ \n"
              "  |     |\n"
              "  |     |\n"
              "  |     |\n"
              "  |     O\n"
              "  |    /|\ \n"
              "  |      \n"
              "  |      \n"
              "######")
    elif nbr_chances == 1:
        print("  +-----+ \n"
              "  |     |\n"
              "  |     |\n"
              "  |     |\n"
              "  |     O\n"
              "  |    /|\ \n"
              "  |    / \n"
              "  |      \n"
              "######")
    elif nbr_chances == 0 or nbr_chances == -1:
        print("  +-----+ \n"
              "  |     |\n"
              "  |     |\n"
              "  |     |\n"
              "  |     O\n"
              "  |    /|\ \n"
              "  |    / \ \n"
              "  |      \n"
              "######")
    else:
        print("  +-----+\n"
              "  |     |\n"
              "  |     |\n"
              "  |     |\n"
              "  |     O\n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "######")


def chargement():
    """
        Objectif: Compter les nombre de la fichier
        Methode: Ouvrir le fichier et les donnes ligne par ligne
        Besoins:Le fichier mots.txt
        Connus:mots.txt
        Entrées: --
        Sorties:le nombre de mots dans le fichier
        Résultats: nombreMots
        Hyphothèses: l'ouverture du fichier mots.txt
    """

    nombreMots = 0

    f = open('mots.txt', 'r', encoding='utf8')
    contenus = f.readlines()
    for contenu in contenus:
        nombreMots += 1
    print("\n\t\t {0} mots charges".format(nombreMots))


def maingame():
    """
           Objectif: C'est la partie principale du jeu
           Methode: fait appel aux fonctions dont il a besoin pour que le jeu marche bien
           Besoins: mots.txt, log_game.text , fichier scores et mot.txt
           Connus: --
           Entrées: --
           Sorties: jeu du pendu
           Résultats: gagner ou perdre
           Hyphothèses: de permettre a l'utilisateur de deviner le mot transformer en underscore
    """
    Affichage(nombreTentative, point_erreur)
    scores = recup_scores()
    utilisateur = recup_nom_utilisateur()
    if utilisateur not in scores.keys():
        scores[utilisateur] = 0

    niveau = choixNiveau()
    perdu = 0
    continuer_partie = 0

    while continuer_partie != 1:
        numeroParti =gamedata.numeroParti
        numeroParti += 1
        print("\t\tJoueur {0}: {1} point(s)".format(utilisateur, scores[utilisateur]))
        mot_a_trouver = choisirMot(niveau)
        lettres_trouvees = []
        mot_trouve = recup_mot_masque(mot_a_trouver, lettres_trouvees)

        nb_chances = nombreTentative
        nb_pointErreur = point_erreur

        while mot_a_trouver != mot_trouve and nb_chances > 0:
            print("\t\tMot à déviner {0} \n".format(mot_trouve))
            lettre = recupLettre()
            if lettre in lettres_trouvees:
                nb_pointErreur -= 1
                print("Déjà trouvé. Essayer une autre lettre\n")

                Affichage(nb_chances, nb_pointErreur)
            elif lettre in mot_a_trouver:
                lettres_trouvees.append(lettre)
                print("Félicitation!!!, lettre correcte")
            elif len(lettre) > 1:
                nb_pointErreur -= 1
                print("Vous devez saisir qu'un seul lettre. \nVous perdez 1 point erreur.")
                Affichage(nb_chances, nb_pointErreur)

            elif not lettre.isalpha():
                nb_pointErreur -= 1
                print("Vous n'avez pas saisi une lettre valide,\nVous perdez un point erreur\n .")

                if nb_pointErreur == 0:
                    nb_pointErreur = 3
                    nb_chances -= 1
                Affichage(nb_chances, nb_pointErreur)
            else:
                if Voyelle(lettre) == 1:
                    print( "Vous avez saisi une voyelle qui n'est pas dans le mot.\n Vous perdez deux tentatives\n")
                    nb_chances -= 2
                    Affichage(nb_chances, nb_pointErreur)
                else:
                    print("Vous avez saisi un cosonne qui n'est pas dans le mot.\nVous perdez 1 tentative\n")
                    nb_chances -= 1
                    Affichage(nb_chances, nb_pointErreur)

            mot_trouve = recup_mot_masque(mot_a_trouver, lettres_trouvees)

        if mot_a_trouver != mot_trouve:
            print(" Vous avez perdu le mot a deviner etait {0}.".format(mot_a_trouver))
            continuer_partie = input("Souhaitez-vous continuer la partie taper 0 pour continuer et 1 pour quitter ?")
            continuer_partie = int(continuer_partie)
        else:
            continuer_partie = 1
            print("Félicitation : Vous avez deviné le mot: {0}.".format(mot_a_trouver))

            scoreParti = nb_chances * len(mot_a_trouver)

            perdu = 1
            print("Vous score est {0}. \n\n Votre score total est passer de {1} a {2}".format(scoreParti,scores[utilisateur],scores[utilisateur] + scoreParti))


            scores[utilisateur] += scoreParti
            enregistrerScores(scores)

    if perdu == 0:
        print("Votre score {0} n\'as pas changé ".format(scores[utilisateur]))

    print("------------------Merci d'avoir joué au jeu du pendu----------------------")





