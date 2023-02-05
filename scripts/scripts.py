from . import db

BotDB = db.BotDB()

class Main:
    def save_questions(self, data, admin_id):
        data['table_name'] = 'TEST_' + str(data['table_name'])
        BotDB.create_questons_table(data['table_name'])
        BotDB.save_questions(data, admin_id)

    def get_questions(self, table_name):
        res = BotDB.get_questions(table_name)
        data = []
        for i in res:
            data.append(i[0])
        return data

    def save_answers(self,data):
        BotDB.create_answers_table(data)
        BotDB.save_answers(data)

    def check_is_done(self, user_id, test_name):
        return BotDB.is_done(user_id, test_name)


    def get_tests(self):
        return BotDB.get_tests()
