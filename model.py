import sqlite3

def show_color(username):
    connection=sqlite3.connect('flask_tuto.db',check_same_thread=False)
    cursor=connection.cursor()
    
    cursor.execute(
        """ SELECT passeword FROM users WHERE username='{username}' ORDER BY pk DESC;""".format(username=username)
    )
    extracted=cursor.fetchone()[0]

    connection.commit()
    cursor.close()
    connection.close()
    message="[Info]: '{username}', '{extracted}'.".format(username=username, extracted=extracted)

    return message

def check_pw(username):
    connection=sqlite3.connect('flask_tuto.db',check_same_thread=False)
    cursor=connection.cursor()
    
    cursor.execute(
        """ SELECT passeword FROM users WHERE username='{username}' ORDER BY pk DESC;""".format(username=username)
    )
    passeword=cursor.fetchone()

    connection.commit()
    cursor.close()
    connection.close()

    return passeword

def signup(username,passeword,favorit_color):
    connection=sqlite3.connect('flask_tuto.db',check_same_thread=False)
    cursor=connection.cursor()

    cursor.execute(
        """ SELECT passeword FROM users WHERE username='{username}';""".format(username=username)
    )
    exist=cursor.fetchone()
    
    if exist is None:
        cursor.execute(
        """ INSERT INTO users (username,passeword,favorit_color)VALUES('{username}','{passeword}','{favorit_color}');""".format(username=username,passeword=passeword,favorit_color=favorit_color))
        connection.commit()
        cursor.close()
        connection.close()

    else:
        return('User already existed !!!')

    return 'You have signed up successfully !!!'