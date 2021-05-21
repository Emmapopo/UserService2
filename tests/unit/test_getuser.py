import unittest
from uuid import UUID
import grpc
from unittest.mock import patch
import logging
from datetime import date
import os
import sys

from sqlalchemy.sql.functions import user
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
grandparentdir = os.path.dirname(parentdir)
sys.path.append(grandparentdir)

from server import UserServicer, user_pb2, ValidationFailed
from model.user_model import User

# Disable logging details. You can highlight code to include logging details back.
logging.disable(logging.CRITICAL)


class TestGetUser(unittest.TestCase):

    def test_valid_id(self):
        class UserControllerMock:
            def get_user(self, id):
                return None

        request = user_pb2.GetUserRequest(id='16fd2706-8baf-433b-82eb')

        expected = user_pb2.GetUserResponse()
        expected.status = "p.id is not a valid UUID"
    
        self.assertEqual(UserServicer(UserControllerMock()).GetUser(
            request, context=1), expected)


    def test_user_not_found(self):
        class UserControllerMock:

            def get_user(self, id):
                return None

        request = user_pb2.GetUserRequest(id="4be5ccf3-fbd4-441d-b7ff-c4a9f406274e")

        expected = user_pb2.GetUserResponse()
        expected.status = "user does not exist"

        self.assertEqual(UserServicer(UserControllerMock()).GetUser(
            request, context=1), expected)

    def test_valid_get_user(self):
        class UserControllerMock:
            def get_user(self, id):
                dob = date.fromisoformat('2000-01-01')
                user = User(id="16fd2706-8baf-433b-82eb-8c7fada847da", first_name="Emmanuel", last_name="Dayo", user_name="popo1",
                            email="emman@yahoo.com", password="Abayomi20", phone_number="08166321187", date_of_birth=dob, state_id=5, version=1)
                return user

        request = user_pb2.GetUserRequest(id="16fd2706-8baf-433b-82eb-8c7fada847da")

        expected = user_pb2.GetUserResponse()
        expected.status = "success"
        expected.user.id = "16fd2706-8baf-433b-82eb-8c7fada847da"
        expected.user.first_name = "Emmanuel"
        expected.user.last_name = "Dayo"
        expected.user.user_name = "popo1"
        expected.user.email = "emman@yahoo.com"
        expected.user.password = "Abayomi20"
        expected.user.phone_number = "08166321187"
        expected.user.date_of_birth.seconds = 946684800
        expected.user.date_of_birth.nanos = 0
        expected.user.state_id = 5
        expected.user.version = 2

        self.assertEqual(UserServicer(UserControllerMock()).GetUser(
            request, context=1), expected)



if __name__ == '__main__':
    unittest.main()
