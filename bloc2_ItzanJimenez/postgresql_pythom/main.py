from connect import connection_db
if __name__ == "__main__":
    conn = connection_db()
import create_registre as cr


#Trucada per executar la funció a l'arxiu create_registre.py
cr.create_reg()

import read_registre as rr

results = rr.read_reg()
for i in results:
    print('\n')
    print('Nom: ' + i[1])
    print('Adreça: ' + i[2])
    print('telèfon: ' + i[3])
    print('email: ' + i[4])
    print('neixament: ' + i[5])