import os
import psycopg2

from model.user_model import User


class UserController:
    session = None
    def __init__(self, session):
        self.session = session


    def add_user(self, user_data):
        self.session.add(user_data)
        try:
            self.session.commit()
        except:
            self.session.rollback()

    def delete_user(self, id):
        self.session.query(User).filter_by(id=id).delete()
        try:
            self.session.commit()
        except:
            self.session.rollback()

    def get_user(self, id):
        user = self.session.query(User).filter_by(id=id).first()
        return user


    def update_user(self, user_data):
        try:
            self.session.commit()
        except:
            self.session.rollback()


    #This method returns None if user does not exist. 
    def user_exist(self, email):
        exists = self.session.query(User.id).filter_by(email=email).first()
        return exists

    def user_name_available(self, user_name):
        exists = self.session.query(User.user_name).filter_by(user_name=user_name).first()
        return exists

    # def update_user(self, user_data):
    # function for version



    # def add_bettor (self, first_name=None, last_name=None, user_name=None, email=None, password=None, phone_number=None, date_of_birth=None, location=None): 
    #     add_query = """ INSERT INTO bettor (first_name, last_name, user_name, email, password, phone_number, date_of_birth, location)
    #                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
    #     self.cur.execute(add_query, (first_name, last_name, user_name, email, password, phone_number, date_of_birth, location))
    #     self.cur.close()
    #     self.conn.commit()

    # def delete_bettor (self, bettor_id):
    #     delete_query = """DELETE FROM bettor WHERE bettor_id = %s"""
    #     self.cur.execute(delete_query, (bettor_id,))
    #     self.cur.close()
    #     self.conn.commit()

    # # def update_bettor(self, bettor_id, first_name=None, last_name=None, user_name=None, email=None, password=None, phone_number=None, date_of_birth=None, location=None):


    # def get_bettor (self,bettor_id):
    #     get_query = """SELECT * FROM bettor WHERE bettor_id = %s"""
    #     bettor = self.cur.execute(get_query, (bettor_id,))
    #     return bettor