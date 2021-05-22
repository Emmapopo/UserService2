
import unittest
from uuid import UUID
import grpc
from unittest.mock import patch
import logging

import os
import sys

from datetime import date

from sqlalchemy.sql.functions import user
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
grandparentdir = os.path.dirname(parentdir)
sys.path.append(grandparentdir)

from server import UserServicer, user_pb2, ValidationFailed
from model.user_model import User


# Disable logging details. You can highlight code to include logging details back.
logging.disable(logging.CRITICAL)


class TestDeleteUser(unittest.TestCase):

    def test_valid_id(self):
        class UserControllerMock:
            def add_user(self, user):
                return None

            def user_exist(self, email):
                return None

            def user_name_available(self, username):
                return None

            def delete_user(self, id):
                return None

        request = user_pb2.DeleteUserRequest(id = '16fd2706-8baf-433b-82eb')

        expected = user_pb2.DeleteUserResponse()
        expected.status = "p.id is not a valid UUID"

        self.assertEqual(UserServicer(UserControllerMock()).DeleteUser(
            request, context=1), expected)

    def test_user_not_found(self):

        class UserControllerMock:
            def add_user(self, user):
                return None

            def user_exist(self, email):
                return None

            def user_name_available(self, username):
                return None

            def delete_user(self, id):
                return None

            def get_user(self,id):
                return None

        request = user_pb2.DeleteUserRequest(id='3376172f-8740-4898-bdbb-b10ce6ae20e2')

        expected = user_pb2.DeleteUserResponse()
        expected.status = "user not found for deletion"

        self.assertEqual(UserServicer(UserControllerMock()).DeleteUser(
            request, context=1), expected)


    def test_valid_deletion(self):
        class UserControllerMock:
            def add_user(self, user):
                return None

            def user_exist(self, email):
                return None

            def user_name_available(self, username):
                return None
            
            def get_user(self, id):
                dob = date.fromisoformat('2000-01-01')
                user = User(id="3376172f-8740-4898-bdbb-b10ce6ae20e2", first_name="Emmanuel", last_name="Dayo", user_name="popo1",
                            email="emman@yahoo.com", password="Abayomi20", phone_number="08166321187", date_of_birth=dob, state_id=5, version=1)

                return user

            def delete_user(self, id):
                return "Deleted"

        
        request = user_pb2.DeleteUserRequest(id="3376172f-8740-4898-bdbb-b10ce6ae20e2")

        expected = user_pb2.DeleteUserResponse()
        expected.status = "user deleted successfully"

        self.assertEqual(UserServicer(UserControllerMock()).DeleteUser(
            request, context=1), expected)


if __name__ == '__main__':
    unittest.main()



        
