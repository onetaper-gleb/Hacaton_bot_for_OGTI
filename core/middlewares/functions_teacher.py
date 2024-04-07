import sqlite3


def checker_teach(tg):
    con = sqlite3.connect("data")
    cur = con.cursor()
    try:
        result = cur.execute(f"""SELECT tg FROM Subjects
        WHERE (tg == "{tg}")""").fetchall()[0][0]
    except:
        result = False
    con.commit()
    con.close()
    return result
