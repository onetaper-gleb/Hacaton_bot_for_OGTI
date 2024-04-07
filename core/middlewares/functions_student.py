import sqlite3


def subjects_student_choose(group_name):
    con = sqlite3.connect("data")
    cur = con.cursor()
    result = cur.execute(f"""SELECT subs FROM Groups
    WHERE (name == "{group_name}")""").fetchall()[0][0].split()
    ans = []
    for i in range(len(result)):
        result_2 = " - ".join(cur.execute(f"""SELECT name_subject, teacher FROM Subjects
        WHERE (id == "{result[i]}")""").fetchall()[0])
        ans.append(f'{str(i + 1)}. {result_2}')
    con.commit()
    con.close()
    return ans


def get_schedule(group_name):
    con = sqlite3.connect("data")
    cur = con.cursor()
    result = cur.execute(f"""SELECT schedule FROM Groups
    WHERE (name == "{group_name}")""").fetchall()[0][0]
    if result:
        result = f'schedules/{result}'
    con.commit()
    con.close()
    return result
