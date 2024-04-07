import random
import sqlite3


def generate_password():
    allowed_chars = 'ABCDEFGHIJKLMNPQRSTUVWXYZ123456789'
    password = ''

    for i in range(10):
        random_index = random.randint(0, len(allowed_chars) - 1)
        password += allowed_chars[random_index]

    return password


def exists(message, id):
    password = message.text.upper()
    con = sqlite3.connect("data")
    cur = con.cursor()
    result = cur.execute(f"""SELECT id, P_id, name, description FROM Groups""").fetchall()
    for i in result:
        if password in i:
            result_2 = cur.execute(f"""SELECT groups FROM Users
            WHERE (id_person == "{id}")""").fetchall()
            s = result_2[0][0]
            if result_2[0][0] != 'None' and str(i[0]) not in s.split():
                s += f' {i[0]}'
            elif str(i[0]) not in s.split():
                s = str(i[0])
            result_3 = cur.execute(f"""UPDATE Users SET groups = "{s}" WHERE (id_person = "{id}")""")
            con.commit()
            con.close()
            print(i[2], i[3])
            return (True, i[2], i[3])
    con.commit()
    con.close()
    return False


def existing_id(message, id):
    password = message.text.upper()
    con = sqlite3.connect("data")
    cur = con.cursor()
    idi = cur.execute(f"""SELECT groups FROM Users
    WHERE (id_person == "{id}")""").fetchall()
    idi = idi[0][0].split()[0]
    result = cur.execute(f"""SELECT ids FROM Groups
    WHERE (id == "{int(idi)}")""").fetchall()
    m = result[0][0].split()
    if password in m:
        m.pop(m.index(password))
        s = m
        if s:
            result_3 = cur.execute(f"""UPDATE Groups SET ids = "{' '.join(s)}" WHERE (id = "{idi}")""").fetchall()
        else:
            result_3 = cur.execute(f"""UPDATE Groups SET ids = "" WHERE (id = "{idi}")""").fetchall()
        con.commit()
        con.close()
        return True
    con.commit()
    con.close()
    return False


def append_all(lis, id):
    con = sqlite3.connect("data")
    cur = con.cursor()
    idi = cur.execute(f"""UPDATE Users SET id = "{lis[0]}", name = "{lis[2]}", surname = "{lis[1]}", second_name = "{lis[3]}", number = "{lis[4]}", email = "{lis[5]}" WHERE (id_person = "{id}")""").fetchall()
    con.commit()
    con.close()


def append_all_2(lis, id):
    con = sqlite3.connect("data")
    cur = con.cursor()
    idi = cur.execute(f"""UPDATE Users SET id = "None", name = "{lis[1]}", surname = "{lis[0]}", second_name = "{lis[1]}", number = "{lis[3]}", email = "{lis[4]}" WHERE (id_person = "{id}")""").fetchall()
    con.commit()
    con.close()
