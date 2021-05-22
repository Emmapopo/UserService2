#from protoc_gen_validate.validator import ValidationFailed
import unittest
from uuid import UUID
import grpc
from unittest.mock import patch
import logging

import os
import sys

from sqlalchemy.sql.functions import user
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
grandparentdir=os.path.dirname(parentdir)
sys.path.append(grandparentdir)

from server import UserServicer, user_pb2, ValidationFailed

# Disable logging details. You can highlight code to include logging details back.
logging.disable(logging.CRITICAL)

class TestCreateUser(unittest.TestCase):
    def test_valid_id (self):
        class UserControllerMock:
            def add_user(self, user):
                return None

            def user_exist(self, email):
                return None

            def user_name_available(self, username):
                return None

        user_1 = user_pb2.CreateUserRequest(id='16fd2706-8baf-433b-82eb-8c7fada847da', first_name="Emmanuel", last_name="Dayo", user_name="popo1",
                                            email="emman@yahoo.com", password="Abayomi20", phone_number="08166321187", date_of_birth={
                                                "seconds": 12,
                                                "nanos": 10
                                            }, state_id=1)
        expected = user_pb2.CreateUserResponse()
        expected.status = "success"
        self.assertEqual(UserServicer(UserControllerMock()).CreateUser(
            user_1, context=1), expected)
        
        user_2 = user_pb2.CreateUserRequest(id="", first_name="Emmanuel", last_name="Dayo", user_name="popo1",
                                            email="emman@yahoo.com", password="Abayomi20", phone_number="08166321187", date_of_birth={
                                                "seconds": 12,
                                                "nanos": 10
                                            }, state_id=1)
        expected = user_pb2.CreateUserResponse()
        expected.status = "p.id is not a valid UUID"
        self.assertEqual(UserServicer(UserControllerMock()).CreateUser(
            user_2, context=1), expected)


        user_3 = user_pb2.CreateUserRequest(id="16fd2706-", first_name="Emmanuel", last_name="Dayo", user_name="popo1",
                                            email="emman@yahoo.com", password="Abayomi20", phone_number="08166321187", date_of_birth={
                                                "seconds": 12,
                                                "nanos": 10
                                            }, state_id=1)
        expected = user_pb2.CreateUserResponse()
        expected.status = "p.id is not a valid UUID"
        self.assertEqual(UserServicer(UserControllerMock()).CreateUser(
            user_3, context=1), expected)


    def test_valid_first_name(self):
        class UserControllerMock:
            def add_user(self, user):
                return None

            def user_exist(self, email):
                return None

            def user_name_available(self, username):
                return None

        user_1 = user_pb2.CreateUserRequest(id='16fd2706-8baf-433b-82eb-8c7fada847da', first_name="", last_name="Dayo", user_name="popo1",
                                            email="emman@yahoo.com", password="Abayomi20", phone_number="08166321187", date_of_birth={
                                                "seconds": 12,
                                                "nanos": 10
                                            }, state_id=1)
        expected = user_pb2.CreateUserResponse()
        expected.status = "p.first_name length is less than 1"
        self.assertEqual(UserServicer(UserControllerMock()).CreateUser(
            user_1, context=1), expected)

        user_2 = user_pb2.CreateUserRequest(id='16fd2706-8baf-433b-82eb-8c7fada847da', first_name="Emmanuel", last_name="Dayo", user_name="popo1",
                                            email="emman@yahoo.com", password="Abayomi20", phone_number="08166321187", date_of_birth={
                                                "seconds": 12,
                                                "nanos": 10
                                            }, state_id=1)
        expected = user_pb2.CreateUserResponse()
        expected.status = "success"
        self.assertEqual(UserServicer(UserControllerMock()).CreateUser(
            user_2, context=1), expected)

    def test_valid_last_name(self):
        class UserControllerMock:
            def add_user(self, user):
                return None

            def user_exist(self, email):
                return None

            def user_name_available(self, username):
                return None

        user_1 = user_pb2.CreateUserRequest(id='16fd2706-8baf-433b-82eb-8c7fada847da', first_name="Emmanuel", last_name="", user_name="popo1",
                                            email="emman@yahoo.com", password="Abayomi20", phone_number="08166321187", date_of_birth={
                                                "seconds": 12,
                                                "nanos": 10
                                            }, state_id=1)
        expected = user_pb2.CreateUserResponse()
        expected.status = "p.last_name length is less than 1"
        self.assertEqual(UserServicer(UserControllerMock()).CreateUser(
            user_1, context=1), expected)

        user_2 = user_pb2.CreateUserRequest(id='16fd2706-8baf-433b-82eb-8c7fada847da', first_name="Emmanuel", last_name="Dayo", user_name="popo1",
                                            email="emman@yahoo.com", password="Abayomi20", phone_number="08166321187", date_of_birth={
                                                "seconds": 12,
                                                "nanos": 10
                                            }, state_id=1)
        expected = user_pb2.CreateUserResponse()
        expected.status = "success"
        self.assertEqual(UserServicer(UserControllerMock()).CreateUser(
            user_2, context=1), expected)

    def test_valid_user_name(self):

        class UserControllerMock1:
            def add_user(self, user):
                return None

            def user_exist(self, email):
                return None

            def user_name_available(self, username):
                return None


        user_1 = user_pb2.CreateUserRequest(id='16fd2706-8baf-433b-82eb-8c7fada847da', first_name="Emmanuel", last_name="Dayo", user_name="",
                                            email="emman@yahoo.com", password="Abayomi20", phone_number="08166321187", date_of_birth={
                                                "seconds": 12,
                                                "nanos": 10
                                            }, state_id=1)
        expected = user_pb2.CreateUserResponse()
        expected.status = "p.user_name length is less than 1"
        self.assertEqual(UserServicer(UserControllerMock1()).CreateUser(
            user_1, context=1), expected)

        user_2 = user_pb2.CreateUserRequest(id='16fd2706-8baf-433b-82eb-8c7fada847da', first_name="Emmanuel", last_name="Dayo", user_name="popo1",
                                            email="emman@yahoo.com", password="Abayomi20", phone_number="08166321187", date_of_birth={
                                                "seconds": 12,
                                                "nanos": 10
                                            }, state_id=1)
        expected = user_pb2.CreateUserResponse()
        expected.status = "success"
        self.assertEqual(UserServicer(UserControllerMock1()).CreateUser(
            user_2, context=1), expected)

        class UserControllerMock2:
            def add_user(self, user):
                return None

            def user_exist(self, email):
                return None

            def user_name_available(self, username):
                return "user_name is taken"

        user_3 = user_pb2.CreateUserRequest(id='16fd2706-8baf-433b-82eb-8c7fada847da', first_name="Emmanuel", last_name="Dayo", user_name="popo1",
                                            email="emman@yahoo.com", password="Abayomi20", phone_number="08166321187", date_of_birth={
                                                "seconds": 12,
                                                "nanos": 10
                                            }, state_id=1)
        expected = user_pb2.CreateUserResponse()
        expected.status = "user name taken!"
        self.assertEqual(UserServicer(UserControllerMock2()).CreateUser(
            user_3, context=1), expected)

    def test_valid_email(self):

        class UserControllerMock1:
            def add_user(self, user):
                return None

            def user_exist(self, email):
                return None

            def user_name_available(self, username):
                return None

        user_1 = user_pb2.CreateUserRequest(id='16fd2706-8baf-433b-82eb-8c7fada847da', first_name="Emmanuel", last_name="Dayo", user_name="Popo1",
                                            email="", password="Abayomi20", phone_number="08166321187", date_of_birth={
                                                "seconds": 12,
                                                "nanos": 10
                                            }, state_id=1)
        expected = user_pb2.CreateUserResponse()
        expected.status = "p.email is not a valid email"
        self.assertEqual(UserServicer(UserControllerMock1()).CreateUser(
            user_1, context=1), expected)

        user_2 = user_pb2.CreateUserRequest(id='16fd2706-8baf-433b-82eb-8c7fada847da', first_name="Emmanuel", last_name="Dayo", user_name="Popo1",
                                            email="popo", password="Abayomi20", phone_number="08166321187", date_of_birth={
                                                "seconds": 12,
                                                "nanos": 10
                                            }, state_id=1)
        expected = user_pb2.CreateUserResponse()
        expected.status = "p.email is not a valid email"
        self.assertEqual(UserServicer(UserControllerMock1()).CreateUser(
            user_2, context=1), expected)

        user_3 = user_pb2.CreateUserRequest(id='16fd2706-8baf-433b-82eb-8c7fada847da', first_name="Emmanuel", last_name="Dayo", user_name="popo1",
                                            email="emman@yahoo.com", password="Abayomi20", phone_number="08166321187", date_of_birth={
                                                "seconds": 12,
                                                "nanos": 10
                                            }, state_id=1)
        expected = user_pb2.CreateUserResponse()
        expected.status = "success"
        self.assertEqual(UserServicer(UserControllerMock1()).CreateUser(
            user_3, context=1), expected)

        class UserControllerMock2:
            def add_user(self, user):
                return None

            def user_exist(self, email):
                return "email is taken"

            def user_name_available(self, username):
                return None

        user_4 = user_pb2.CreateUserRequest(id='16fd2706-8baf-433b-82eb-8c7fada847da', first_name="Emmanuel", last_name="Dayo", user_name="popo1",
                                            email="emman@yahoo.com", password="Abayomi20", phone_number="08166321187", date_of_birth={
                                                "seconds": 12,
                                                "nanos": 10
                                            }, state_id=1)
        expected = user_pb2.CreateUserResponse()
        expected.status = "Email already used to register"
        self.assertEqual(UserServicer(UserControllerMock2()).CreateUser(
            user_4, context=1), expected)

    def test_valid_password(self):
        class UserControllerMock:
            def add_user(self, user):
                return None

            def user_exist(self, email):
                return None

            def user_name_available(self, username):
                return None

        user_1 = user_pb2.CreateUserRequest(id='16fd2706-8baf-433b-82eb-8c7fada847da', first_name="Emmanuel", last_name="Dayo", user_name="popo1",
                                            email="emman@yahoo.com", password="", phone_number="08166321187", date_of_birth={
                                                "seconds": 12,
                                                "nanos": 10
                                            }, state_id=1)
        expected = user_pb2.CreateUserResponse()
        expected.status = "p.password length is less than 1"
        self.assertEqual(UserServicer(UserControllerMock()).CreateUser(
            user_1, context=1), expected)

        user_2 = user_pb2.CreateUserRequest(id='16fd2706-8baf-433b-82eb-8c7fada847da', first_name="Emmanuel", last_name="Dayo", user_name="popo1",
                                            email="emman@yahoo.com", password="Abayomi20", phone_number="08166321187", date_of_birth={
                                                "seconds": 12,
                                                "nanos": 10
                                            }, state_id=1)
        expected = user_pb2.CreateUserResponse()
        expected.status = "success"
        self.assertEqual(UserServicer(UserControllerMock()).CreateUser(
            user_2, context=1), expected)

    def test_valid_phone_number(self):
        class UserControllerMock:
            def add_user(self, user):
                return None

            def user_exist(self, email):
                return None

            def user_name_available(self, username):
                return None

        user_1 = user_pb2.CreateUserRequest(id='16fd2706-8baf-433b-82eb-8c7fada847da', first_name="Emmanuel", last_name="Dayo", user_name="popo1",
                                            email="emman@yahoo.com", password="Abayomi20", phone_number="", date_of_birth={
                                                "seconds": 12,
                                                "nanos": 10
                                            }, state_id=1)
        expected = user_pb2.CreateUserResponse()
        expected.status = "success"
        self.assertEqual(UserServicer(UserControllerMock()).CreateUser(
            user_1, context=1), expected)

        user_2 = user_pb2.CreateUserRequest(id='16fd2706-8baf-433b-82eb-8c7fada847da', first_name="Emmanuel", last_name="Dayo", user_name="popo1",
                                            email="emman@yahoo.com", password="Abayomi20", phone_number="08166321187", date_of_birth={
                                                "seconds": 12,
                                                "nanos": 10
                                            }, state_id=1)
        expected = user_pb2.CreateUserResponse()
        expected.status = "success"
        self.assertEqual(UserServicer(UserControllerMock()).CreateUser(
            user_2, context=1), expected)

    def test_valid_age(self):

        class UserControllerMock:
            def add_user(self, user):
                return None

            def user_exist(self, email):
                return None

            def user_name_available(self, username):
                return None

        #test for underage - date of birth set at 2018
        user_1 = user_pb2.CreateUserRequest(id='16fd2706-8baf-433b-82eb-8c7fada847da', first_name="Emmanuel", last_name="Dayo", user_name="popo1",
                                            email="emman@yahoo.com", password="Abayomi20", phone_number="08166321187", date_of_birth={
                                                "seconds": 1526652375,
                                                "nanos": 0
                                            }, state_id=1)
        expected = user_pb2.CreateUserResponse()
        expected.status = "You have to be over 18 years to register"
        self.assertEqual(UserServicer(UserControllerMock()).CreateUser(
            user_1, context=1), expected)

        #test set for qualified age. DOB is 1970
        user_2 = user_pb2.CreateUserRequest(id='16fd2706-8baf-433b-82eb-8c7fada847da', first_name="Emmanuel", last_name="Dayo", user_name="popo1",
                                            email="emman@yahoo.com", password="Abayomi20", phone_number="08166321187", date_of_birth={
                                                "seconds": 12,
                                                "nanos": 10
                                            }, state_id=1)
        expected = user_pb2.CreateUserResponse()
        expected.status = "success"
        self.assertEqual(UserServicer(UserControllerMock()).CreateUser(
            user_2, context=1), expected)

    def test_valid_state_id(self):

        class UserControllerMock:
            def add_user(self, user):
                return None

            def user_exist(self, email):
                return None

            def user_name_available(self, username):
                return None

        user_1 = user_pb2.CreateUserRequest(id='16fd2706-8baf-433b-82eb-8c7fada847da', first_name="Emmanuel", last_name="Dayo", user_name="popo1",
                                            email="emman@yahoo.com", password="Abayomi20", phone_number="08166321187", date_of_birth={
                                                "seconds": 12,
                                                "nanos": 0
                                            }, state_id=0)
        expected = user_pb2.CreateUserResponse()
        expected.status = "p.state_id is not in range (38, 1)"
        self.assertEqual(UserServicer(UserControllerMock()).CreateUser(
            user_1, context=1), expected)

        user_2 = user_pb2.CreateUserRequest(id='16fd2706-8baf-433b-82eb-8c7fada847da', first_name="Emmanuel", last_name="Dayo", user_name="popo1",
                                            email="emman@yahoo.com", password="Abayomi20", phone_number="08166321187", date_of_birth={
                                                "seconds": 12,
                                                "nanos": 10
                                            }, state_id=-6)
        expected = user_pb2.CreateUserResponse()
        expected.status = "p.state_id is not in range (38, 1)"
        self.assertEqual(UserServicer(UserControllerMock()).CreateUser(
            user_2, context=1), expected)

        user_3 = user_pb2.CreateUserRequest(id='16fd2706-8baf-433b-82eb-8c7fada847da', first_name="Emmanuel", last_name="Dayo", user_name="popo1",
                                            email="emman@yahoo.com", password="Abayomi20", phone_number="08166321187", date_of_birth={
                                                "seconds": 12,
                                                "nanos": 10
                                            }, state_id=38)
        expected = user_pb2.CreateUserResponse()
        expected.status = "p.state_id is not in range (38, 1)"
        self.assertEqual(UserServicer(UserControllerMock()).CreateUser(
            user_3, context=1), expected)

        user_2 = user_pb2.CreateUserRequest(id='16fd2706-8baf-433b-82eb-8c7fada847da', first_name="Emmanuel", last_name="Dayo", user_name="popo1",
                                            email="emman@yahoo.com", password="Abayomi20", phone_number="08166321187", date_of_birth={
                                                "seconds": 12,
                                                "nanos": 10
                                            }, state_id=15)
        expected = user_pb2.CreateUserResponse()
        expected.status = "success"
        self.assertEqual(UserServicer(UserControllerMock()).CreateUser(
            user_2, context=1), expected)
        

if __name__ == '__main__':
    unittest.main()




    
