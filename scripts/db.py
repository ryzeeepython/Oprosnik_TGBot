import sqlite3

class BotDB:

    def __init__(self):
        self.conn = sqlite3.connect('db.db')
        self.cursor = self.conn.cursor()

    def create_questons_table(self,table_name):
        self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS {table_name}(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            admin_id INT,
            question_text TEXT);
            """)
        self.conn.commit()

    def delete_questions_table(self, table_name):
        self.cursor.execute(f"""DROP TABLE IF EXISTS {table_name};""")
        self.conn.commit()
    
    def create_answers_table(self, data):
        table_name = ''
        test_name = data['test_name']
        tg_name = data['tg_name']
        tg_name = "".join(c for c in tg_name if c.isalnum())
        table_name = f'RES_{test_name}_{tg_name}'

        self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS {table_name}(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tg_name STRING,
            user_id INT NOT NULL,
            answer TEXT,
            question_id INT NOT NULL);
            """)
        self.conn.commit()

    def get_questions(self, table_name):
        questions = self.cursor.execute(f"SELECT `question_text`FROM `{table_name}`")
        return questions.fetchall()

    def save_questions(self, data, admin_id):
        table_name = data['table_name']
        for i in range(len(data)- 1):
            question = data['q'+str(i+1)]
            self.cursor.execute(f"INSERT INTO `{table_name}` (`question_text`, `admin_id`) VALUES (?, ?)", (question, admin_id))
        return self.conn.commit()


    def save_answers(self, data):
        tg_name = data['tg_name']
        test_name = data['test_name']
        tg_name = "".join(c for c in tg_name if c.isalnum())
        table_name = f'RES_{test_name}_{tg_name}'
        user_id = data['user_id']

        for i in range(len(data) -3):
            question_id = f'q{i+1}'
            answer = data[question_id]
            self.cursor.execute(f"INSERT INTO `{table_name}` (`tg_name`, `user_id`, `answer`, `question_id`) VALUES (?, ?, ?, ?)", (tg_name, user_id, answer, question_id))
        return self.conn.commit()

    def get_tables(self):
        self.cursor.execute("""select * from sqlite_master
            where type = 'table'""")
        return self.cursor.fetchall()    

    def is_done(self, user_id, test_name):
        tables = self.get_tables()    
        for table in tables:
            if f'RES_{test_name}' in str(table[1]):
                result = self.cursor.execute(f"SELECT `id` FROM `{table[1]}` WHERE `user_id` = ?", (user_id,))
                return bool(len(result.fetchall()))
            
        return False
    

    def get_tests(self):
        tables = self.get_tables()  
        res = []
        for table in tables:
            if not 'RES_' in str(table[1]) and not 'sqlite' in str(table[1]):
                res.append(table[1])
        return res

    def close(self):
        """Закрываем соединение с БД"""
        self.connection.close()


