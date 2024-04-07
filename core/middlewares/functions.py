import sqlite3


def get_spisok():
    con = sqlite3.connect("data")
    cur = con.cursor()
    studes = cur.execute(f"""SELECT tg, id_person, chat_id, groups FROM Users
WHERE stat == "student" """).fetchall()
    gr = []
    for i in studes:
        gr = cur.execute(f"""SELECT name, description FROM Groups
        WHERE id == "{i[3]}" """).fetchall()
    teaches = cur.execute(f"""SELECT tg, id_person, chat_id FROM Users
WHERE stat == "teacher" """).fetchall()
    admins = cur.execute(f"""SELECT tg, id_person, chat_id FROM Users
    WHERE stat == "admin" """).fetchall()
    con.commit()
    con.close()
    return (studes, teaches, admins, gr)