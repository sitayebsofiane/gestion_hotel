import psycopg2
import hashlib
import calendar
from datetime import datetime

class Model:

    """ connect to bdd in postgreSQL """
    def __init__(self,bdd,user,password,host,port):
        try:
            self.con=psycopg2.connect(database=bdd,user=user,password=password,host=host,port=port)
            self.curseur=None
        except(Exception ,psycopg2.Error):
            print("erreur while connecting to postgresSQL")
    """ display speakers and conferences """
    def get_all(self):
        try:
            self.curseur=self.con.cursor()
            self.curseur.execute("""select s.id_speaker, s.nom,s.prenom,c.titre,c.resume,c.date from 
                                speakrs as s join conference as c on s.id_speaker = c.id_speaker;""")
            rows=self.curseur.fetchall()
            self.curseur.close()
            liste = list()
            for row in rows:
                liste.append({'id_speaker':row[0],'nom':row[1],'prenom': row[2], 'titre':row[3],'resume':row[4], 'date': row[5]})
            return liste
        except(Exception ,psycopg2.Error):
            print("erreur while selecting")

    """ display speakers """
    def get_all_speakers(self):
        try:
            self.curseur=self.con.cursor()
            self.curseur.execute("""select * from speakrs;""")
            rows=self.curseur.fetchall()
            self.curseur.close()
            liste = list()
            for row in rows:
                liste.append({'id_speaker':row[0],'nom': row[1], 'prenom':row[2],'description':row[3],
                 'profession': row[4],'statut':row[5]})
            return liste
        except(Exception ,psycopg2.Error):
            print("erreur while selecting")