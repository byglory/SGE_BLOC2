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

---

### **Captura 5: Lectura d'un camp específic d'un registre**
![image5](/fotos/foto5.png)

Aquesta captura mostra com s'ha extret un camp específic d'un registre de la taula `Clientes`. S'ha utilitzat l'arxiu `read_registre.py` per obtenir el telèfon del client amb `id_cliente = 5`. La consulta SQL utilitzada és `SELECT teléfono_cliente FROM Clientes WHERE id_cliente = 5;`. La captura mostra el telèfon del client.

---

### **Captura 6: Exercicis addicionals**
![image6](/fotos/foto6.png)


---

### **Captura 7: Actualització d'un registre**
![image7](/fotos/foto7.png)

Aquesta captura mostra la modificació d'un registre a la taula `Clientes`. S'ha utilitzat l'arxiu `update_registre.py` per actualitzar el telèfon del client amb `id_cliente = 1`. La consulta SQL utilitzada és `UPDATE Clientes SET teléfono_cliente = '000000000' WHERE id_cliente = 1;`. La captura mostra la taula després de l'actualització, on es pot veure que el telèfon del client ha canviat correctament.

---

### **Captura 8: Exercicis addicionals**
![image8](/fotos/foto8.png)

Aquesta captura mostra els resultats dels exercicis addicionals on s'han extret dades específiques de la taula `Clientes`:
1. Les dades de l'Andreu.
2. El correu de l'Andreu.
3. Les dades de la Vivian.
4. La direcció de la Vivian.
5. Les dades de l'Albert.
6. La data de cumpleanys de l'Albert.

S'han utilitzat consultes SQL amb condicions `WHERE` per extreure aquestes dades i s'han imprès a la terminal.

---

### **Captura 9: Actualització del telèfon del client 1**
![image9](/fotos/foto9.png)

Aquesta captura mostra la resposta de la terminal després d'executar l'arxiu `main.py`. Es pot veure que el telèfon del client amb `id_cliente = 1` ha estat actualitzat correctament.



---

### **Captura 10: Eliminació d'un registre**
![image10](/fotos/foto10.png)

En aquesta captura s'ha eliminat un registre de la taula `Clientes` utilitzant l'arxiu `delete_registre.py`. S'ha fet una consulta SQL amb la condició `DELETE FROM Clientes WHERE id_cliente = 28;` per eliminar el registre amb aquest identificador. La captura mostra la taula després de l'eliminació, on es pot veure que el registre ja no està present.

no funciona no se per que
---

### **Commits realitzats**
- `result del read_registre`: Commit realitzat després de llegir tots els registres de la taula.
- `result d’un registre del read_registre`: Commit realitzat després de llegir un registre específic.
- `result d’un camp d’un registre del read_registre`: Commit realitzat després de llegir un camp específic d'un registre.
- `INTENTS mini exercicis LISTS`: Commit realitzat després de completar els exercicis addicionals.
