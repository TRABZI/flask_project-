import sqlite3

connection=sqlite3.connect('flask_tuto.db',check_same_thread=False)
cursor=connection.cursor()

cursor.execute(
    """ INSERT INTO users(
            username,
            passeword,
            favorit_color
            )VALUES(
                'TRABZI',
                'amine',
                'bleu'
            );"""
)

cursor.execute(
    """ INSERT INTO users(
            username,
            passeword,
            favorit_color
            )VALUES(
                'Dellys',
                'Algeria',
                'green'
            );"""

)

connection.commit()
cursor.close()
connection.close()

