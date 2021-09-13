import sqlite3

def show_color(username):
    connection=sqlite3.connect('flask_tuto.db',check_same_thread=False)
    cursor=connection.cursor()
    
    cursor.execute(
        """ SELECT passeword FROM users WHERE username='{username}' ORDER BY pk DESC;""".format(username=username)
    )
    color=cursor.fetchone()[0]

    connection.commit()
    cursor.close()
    connection.close()
    message="'{username}'s favorite color is '{color}'.".format(username=username, color=color)

    return message

def check_pw(username):
    connection=sqlite3.connect('flask_tuto.db',check_same_thread=False)
    cursor=connection.cursor()
    
    cursor.execute(
        """ SELECT passeword FROM users WHERE username='{username}' ORDER BY pk DESC;""".format(username=username)
    )
    passeword=cursor.fetchone()[0]

    connection.commit()
    cursor.close()
    connection.close()

    return passeword