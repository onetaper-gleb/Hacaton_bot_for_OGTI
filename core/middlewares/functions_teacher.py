import sqlite3


def checker_teach(tg):
    con = sqlite3.connect("data")
    cur = con.cursor()
    res = ''
    try:
        result = cur.execute(f"""SELECT id FROM Subjects
        WHERE (tg == "{tg}")""").fetchall()
        for i in result:
            res += f'{i[0]} '
        result = res
    except:
        result = False
    con.commit()
    con.close()
    return result


def lecture_add(name, ids):
    con = sqlite3.connect("data")
    cur = con.cursor()
    for i in ids.split():
        result_2 = cur.execute(f"""UPDATE Subjects SET lectures = '{f"file{name}.pdf"}' WHERE id = '{i}'""")
    con.commit()
    con.close()
    return f"file{name}.pdf"


def lab_add(name, ids):
    con = sqlite3.connect("data")
    cur = con.cursor()
    for i in ids.split():
        result_2 = cur.execute(f"""UPDATE Subjects SET labs = '{f"file{name}.pdf"}' WHERE id = '{i}'""")
    con.commit()
    con.close()
    return f"file{name}.pdf"


def test_add(name, ids):
    con = sqlite3.connect("data")
    cur = con.cursor()
    for i in ids.split():
        result_2 = cur.execute(f"""UPDATE Subjects SET tests = '{f"file{name}.pdf"}' WHERE id = '{i}'""")
    con.commit()
    con.close()
    return f"file{name}.pdf"