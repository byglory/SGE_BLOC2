## Captures de pantalla del projecte

### **Captura 1: Connexió a la base de dades**
![image1](/fotos/foto1.png)

Aquesta captura mostra la resposta de la connexió a la base de dades PostgreSQL des de Python. S'ha utilitzat l'arxiu `connect.py` per establir la connexió i s'ha comprovat que la connexió és correcta mitjançant un missatge a la terminal que no es mostra perquè estic fent servir Windows. Això indica que la configuració de la base de dades i la connexió des de Python han estat exitoses.

---

### **Captura 2: Creació de la taula i inserció de dades**
![image2](/fotos/foto2.png)

En aquesta captura es mostra la taula `Clientes` creada a la base de dades PostgreSQL. S'ha utilitzat l'arxiu `create_table_to_db.py` per crear la taula amb els camps necessaris (`id_cliente`, `nombre_cliente`, `dirección_cliente`, `teléfono_cliente`, `correo_electrónico_cliente`, `fecha_cumpleaños`). A més, s'ha inserit un registre de prova mitjançant l'arxiu `create_registre.py`. La captura mostra la taula amb el registre inserit correctament.

---

### **Captura 3: Lectura de tots els registres**
![image3](/fotos/foto3.png)

Aquesta captura mostra la lectura de tots els registres de la taula `Clientes` mitjançant l'arxiu `read_registre.py`. S'ha utilitzat una consulta SQL `SELECT * FROM Clientes;` per obtenir tots els registres i s'han imprès a la terminal. Es pot veure la llista completa de registres, incloent el nom, adreça, telèfon, correu electrònic i data de cumpleanys de cada client.

---

### Captures de pantalla LISTS

### **Captura 4: Lectura d'un registre específic**
![image4](/fotos/foto4.png)

En aquesta captura s'ha extret un registre específic de la taula `Clientes` utilitzant l'arxiu `read_registre.py`. S'ha fet una consulta SQL amb la condició `WHERE id_cliente = 5;` per obtenir les dades del client amb aquest identificador. La captura mostra les dades completes d'aquest registre, incloent el nom, adreça, telèfon, correu electrònic i data de cumpleanys.
