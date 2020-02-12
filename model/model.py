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

    def get_all(self):
        try:
            self.curseur=self.con.cursor()
            self.curseur.execute("""select s.nom,s.prenom,c.titre,c.resume,c.date from 
                                speakrs as s join conference as c on s.id_speaker = c.id_speaker;""")
            rows=self.curseur.fetchall()
            self.curseur.close()
            liste = list()
            for row in rows:
                liste.append({'nom':row[0],'prenom': row[1], 'titre':row[2],'resume':row[3], 'date': row[4]})
            return liste
        except(Exception ,psycopg2.Error):
            print("erreur while selecting")