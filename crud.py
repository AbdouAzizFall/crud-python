import mysql.connector
from mysql.connector import Error
from connexion import Creer_une_connection

#Insertion
def inserer_personne(nom, prenom, age):
    try:
        conn = Creer_une_connection()
        if conn:
            cursor = conn.cursor()
            requete = "INSERT INTO personne (nom, prenom, age) VALUES (%s,%s,%s)"
            valeurs = (nom,prenom,age)
            cursor.execute(requete,valeurs)
            conn.commit()
            print("Ajout terminé")
            cursor.close()
            conn.close()
    except Error as e:
        print(f"Erreur lors de l'ajout:{e}")
        
#Lister les personnes       
def lister_personne():
    conn = None
    cursor = None
    try:
        conn = Creer_une_connection()
        if conn:
            cursor = conn.cursor()
            requete = "SELECT * FROM personne"
            cursor.execute(requete)
            personnes = cursor.fetchall()
            print("Liste des personnes")
            for personne in personnes:
                print(f"ID : {personne[0]}, NOM : {personne[1]}, PRENOM : {personne[2]}, AGE {personne[3]}")
            cursor.close()
            conn.close()
    except Error as e:
        print(f"Erreur lors de l'affichage:{e}")
        
#Modification
def modifier_personne(id,nom, prenom, age):
    try:
        conn = Creer_une_connection()
        if conn:
            cursor = conn.cursor()
            requete = "UPDATE personne set nom = %s, prenom = %s, age = %s WHERE id = %s"
            valeurs = (nom,prenom,age,id)
            cursor.execute(requete,valeurs)
            conn.commit()
            print("Modification terminée")
            cursor.close()
            conn.close()
        else:
            print("Erreur lors de la connexion à la base de donnée")
    except Error as e:
        print(f"Erreur lors de la modification:{e}")
                
#Supprimer une personne
def supprimer_personne(id):
    try:
        conn = Creer_une_connection()
        if conn:
            cursor = conn.cursor()
            requete = "DELETE FROM personne WHERE id=%s"
            cursor.execute(requete,(id,))
            conn.commit()
            print(f"Personne {id} supprimée de la base de donnée")
            cursor.close()
            conn.close()
        else:
            print("Erreur lors de la connexion à la base de donnée")
    except Error as e:
        print(f"Erreur lors de la suppression:{e}")
        
        
#Lister les personnes       
def rechercher_personne(nom):
    conn = None
    cursor = None
    try:
        conn = Creer_une_connection()
        if conn:
            cursor = conn.cursor()
            requete = "SELECT * FROM personne WHERE nom = %s"
            cursor.execute(requete, (nom,))
            personnes = cursor.fetchall()
            if personnes:
                print("Resultat : ")
                for personne in personnes:
                    print(f"ID : {personne[0]}, NOM : {personne[1]}, PRENOM : {personne[2]}, AGE {personne[3]}")
            else:
                print(f"Une personne de nom {nom} ne figure pas dans la base de donnée")
            cursor.close()
            conn.close()
    except Error as e:
        print(f"Erreur lors de l'affichage:{e}")