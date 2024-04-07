import sqlite3

import pygame


class User(pygame.sprite.Sprite):
    def __init__(self, id, username, chat_id, group):
        super().__init__(group)
        self.id = id
        self.username = username
        self.chat_id = chat_id


class Student(pygame.sprite.Sprite):
    def __init__(self, id, username, chat_id, group, add=False):
        super().__init__(group)
        self.id = id
        self.username = username
        self.chat_id = chat_id
        self.group_name = ''
        self.group_description = ''
        self.previous_actions = []
        self.registration_list = []
        if add:
            print("add")
            self.append_to_bd()

    def append_to_bd(self):
        print("TO BD")
        con = sqlite3.connect("data")
        cur = con.cursor()
        cur.execute(f"""INSERT INTO Users 
        VALUES ("None", "None", "None", "None", "None", "None", "None", "student", "{self.username}", "{self.id}", "{self.chat_id}", "None")""")
        con.commit()
        con.close()


class Admin(pygame.sprite.Sprite):
    def __init__(self, id, username, chat_id, group, add=False):
        super().__init__(group)
        self.id = id
        self.username = username
        self.chat_id = chat_id
        self.previous_actions = []
        self.new_cours = []
        self.page = 0
        if add:
            self.append_to_bd()

    def append_to_bd(self):
        con = sqlite3.connect("data")
        cur = con.cursor()
        cur.execute(f"""INSERT INTO Users 
            VALUES ("None", "None", "None", "None", "None", "None", "None", "admin", "{self.username}", "{self.id}", "{self.chat_id}", "None")""")
        con.commit()
        con.close()


class Teacher(pygame.sprite.Sprite):
    def __init__(self, id, username, chat_id, group, add=False):
        super().__init__(group)
        self.id = id
        self.username = username
        self.chat_id = chat_id
        self.previous_actions = []
        self.page = 0
        if add:
            self.append_to_bd()

    def append_to_bd(self):
        con = sqlite3.connect("data")
        cur = con.cursor()
        cur.execute(f"""INSERT INTO Users 
            VALUES ("None", "None", "None", "None", "None", "None", "None", "teacher", "{self.username}", "{self.id}", "{self.chat_id}", "None")""")
        con.commit()
        con.close()