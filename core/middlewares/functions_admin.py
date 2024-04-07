import sqlite3

from core.middlewares.extra_gen import generate_password


def checker(name):
    con = sqlite3.connect("data")
    cur = con.cursor()
    try:
        result = cur.execute(f"""SELECT id FROM admins
    WHERE (id == "{name}")""").fetchall()[0][0]
    except:
        result = False
    con.commit()
    con.close()
    return result


def checker_2():
    con = sqlite3.connect("data")
    cur = con.cursor()
    result = cur.execute(f"""SELECT id FROM admins""").fetchall()
    con.commit()
    con.close()
    return result


def add_admin_to_bd(admin, add=True):
    con = sqlite3.connect("data")
    cur = con.cursor()
    if add:
        result = cur.execute(f"""INSERT INTO admins VALUES ("{admin}")""")
    else:
        result = cur.execute(f"""DELETE FROM admins WHERE (id == "{admin}")""")
    con.commit()
    con.close()


def groups_to_see(one=False):
    con = sqlite3.connect("data")
    cur = con.cursor()
    if not one:
        result = cur.execute(f"""SELECT name, P_id FROM Groups""").fetchall()
        con.commit()
        con.close()
        return result
    else:
        result = cur.execute(f"""SELECT name, P_id, description, subs FROM Groups
        WHERE (id = "{one}")""").fetchall()
        result_2 = cur.execute(f"""SELECT surname, name, second_name, number, email FROM Users
        WHERE (groups LIKE "%{one}%")""").fetchall()
        result_3 = []
        if result:
            for i in result:
                res = ''
                for j in i[-1].split():
                    res += cur.execute(f"""SELECT name_subject, teacher FROM Subjects
                    WHERE (id = "{j}")""").fetchall()[0][0]
                    res += " - "
                    res += cur.execute(f"""SELECT name_subject, teacher FROM Subjects
                                    WHERE (id = "{j}")""").fetchall()[0][1]
                    result_3.append(res)
                    res = ''
            con.commit()
            con.close()
            return result, result_2, result_3
        con.commit()
        con.close()
        return False


def get_subs(page, id=False):
    con = sqlite3.connect("data")
    cur = con.cursor()
    res = cur.execute(f"""SELECT id, name_subject, teacher, tg FROM Subjects""").fetchall()
    result_3 = ''
    result = []
    ans = []
    if not id:
        for i in res:
            result_3 += f'{i[0]}. {i[1]} - {i[2]}'
            result.append(result_3)
            result_3 = ('')
        for i in range(20):
            try:
                ans.append(result[(20 * page + i) % len(result)])
            except:
                ans.append(result[0])
    else:
        for i in res:
            result_3 += f'{i[0]}. {i[1]} - {i[2]} (@{i[3]})'
            result.append(result_3)
            result_3 = ('')
        for i in range(20):
            try:
                ans.append(result[(20 * page + i) % len(result)])
            except:
                ans.append(result[0])
    con.commit()
    con.close()
    return ans


def create_group_bd(sp):
    con = sqlite3.connect("data")
    cur = con.cursor()
    password = generate_password()
    passes = []
    for i in range(int(sp[2])):
        passes.append(generate_password())
    result = cur.execute(f"""SELECT id FROM Groups""").fetchall()
    result_2 = cur.execute(f"""INSERT INTO Groups VALUES ("{len(result) + 1}", "{password}", "{sp[0]}", "{sp[1]}", "None", "None", "None", "None", "{sp[3]}", "{" ".join(passes)}")""")
    for i in range(int(sp[2])):
        passes[i] = f'{i + 1}. {passes[i]}'
    con.commit()
    con.close()
    return (passes, password)


def schedule_add():
    con = sqlite3.connect("data")
    cur = con.cursor()
    result = cur.execute(f"""SELECT id FROM Groups""").fetchall()
    result_2 = cur.execute(f"""UPDATE Groups SET schedule = '{f"file{result[-1][0]}.pdf"}' WHERE id = '{result[-1][0]}'""")
    con.commit()
    con.close()
    return f"file{result[-1][0]}.pdf"


def create_teacher_bd(sp):
    con = sqlite3.connect("data")
    cur = con.cursor()
    result = cur.execute(f"""SELECT id FROM Subjects""").fetchall()
    result_2 = cur.execute(f"""INSERT INTO Subjects VALUES ("{len(result) + 1}", "{sp[0]}", "{sp[1]}", "{sp[2]}")""")
    con.commit()
    con.close()