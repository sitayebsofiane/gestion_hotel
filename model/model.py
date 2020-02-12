import psycopg2

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
            self.curseur.execute("""select  s.nom,s.prenom,c.id_conference,c.titre,c.resume,c.date from 
                                speakrs as s join conference as c on s.id_speaker = c.id_speaker;""")
            rows=self.curseur.fetchall()
            self.curseur.close()
            liste = list()
            for row in rows:
                liste.append({'nom':row[0],'prenom': row[1], 'id_conference':row[2],
                'titre':row[3],'resume':row[4], 'date': row[5]})
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
    """ insert to confercence """
    def insert_conf(self,titre,resume,date,id_speaker):
        try:
            self.curseur = self.con.cursor()
            self.curseur.execute("INSERT INTO conference(titre,resume, date,id_speaker)VALUES (%s,%s,%s,%s);",
            (titre,resume,date,id_speaker))
            self.con.commit()
            self.curseur.close()
            return True
        except:
            return False
    """ insert to speakers """
    def insert_speaker(self,nom,prenom,desc,profession):
        try:
            self.curseur = self.con.cursor()
            self.curseur.execute("INSERT INTO speakrs(nom,prenom, description,profession)VALUES (%s,%s,%s,%s);",
            (nom,prenom,desc,profession))
            self.con.commit()
            self.curseur.close()
            return True
        except:
            return False

    """ delete conference """
    def delete_conf(self,id_conf):
        try:
            self.curseur = self.con.cursor()
            self.curseur.execute("DELETE FROM conference WHERE id_conference = %s;",(id_conf,))
            self.con.commit()
            self.curseur.close()
            return True
        except:
            return False
    """ delete speakers """
    def delete_speaker(self,id_speaker):
        try:
            self.curseur = self.con.cursor()
            self.curseur.execute("DELETE FROM speakrs WHERE id_speaker = %s;",(id_speaker,))
            self.con.commit()
            self.curseur.close()
            return True
        except:
            return False


