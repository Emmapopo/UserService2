#from protoc_gen_validate.validator import ValidationFailed

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


class TestUpdateUser(unittest.TestCase):
    def setUp(self):
        class UserControllerMock:
            def get_user(self, id):
                dob = date.fromisoformat('2000-01-01')
                user = User(id="16fd2706-8baf-433b-82eb-8c7fada847da", first_name="Emmanuel", last_name="Dayo", user_name="popo1",
                            email="emman@yahoo.com", password="Abayomi20", phone_number="08166321187", date_of_birth=dob, state_id=5, version=1)
                return user

            def add_user(self, user):
                return None

            def update_user(self, update_request):
                return None

        self.UserControllerMock = UserControllerMock()

        pass

    def tearDown(self):
        pass

    def test_update_first_name(self):
        request = user_pb2.UpdateUserRequest(id='16fd2706-8baf-433b-82eb-8c7fada847da', first_name="Toyosi", last_name="",
                                               password="", phone_number="", state_id=0)

        expected = user_pb2.UpdateUserResponse()
        expected.status = "user update successful"
        expected.user.id = "16fd2706-8baf-433b-82eb-8c7fada847da"
        expected.user.first_name = "Toyosi"
        expected.user.last_name = "Dayo"
        expected.user.user_name = "popo1"
        expected.user.email = "emman@yahoo.com"
        expected.user.password = "Abayomi20"
        expected.user.phone_number = "08166321187"
        expected.user.date_of_birth.seconds = 946684800
        expected.user.date_of_birth.nanos = 0
        expected.user.state_id = 5
        expected.user.version = 2

        self.assertEqual(UserServicer(self.UserControllerMock).UpdateUser(
            request, context=1), expected)

    def test_update_last_name(self):
        request = user_pb2.UpdateUserRequest(id='16fd2706-8baf-433b-82eb-8c7fada847da', first_name="", last_name="Tobi",
                                               password="", phone_number="", state_id=0)

        expected = user_pb2.UpdateUserResponse()
        expected.status = "user update successful"
        expected.user.id = "16fd2706-8baf-433b-82eb-8c7fada847da"
        expected.user.first_name = "Emmanuel"
        expected.user.last_name = "Tobi"
        expected.user.user_name = "popo1"
        expected.user.email = "emman@yahoo.com"
        expected.user.password = "Abayomi20"
        expected.user.phone_number = "08166321187"
        expected.user.date_of_birth.seconds = 946684800
        expected.user.date_of_birth.nanos = 0
        expected.user.state_id = 5
        expected.user.version = 2

        self.assertEqual(UserServicer(self.UserControllerMock).UpdateUser(
            request, context=1), expected)

    def test_update_password(self):
        request = user_pb2.UpdateUserRequest(id='16fd2706-8baf-433b-82eb-8c7fada847da', first_name="", last_name="",
                                             password="Morerin", phone_number="", state_id=0)

        expected = user_pb2.UpdateUserResponse()
        expected.status = "user update successful"
        expected.user.id = "16fd2706-8baf-433b-82eb-8c7fada847da"
        expected.user.first_name = "Emmanuel"
        expected.user.last_name = "Dayo"
        expected.user.user_name = "popo1"
        expected.user.email = "emman@yahoo.com"
        expected.user.password = "Morerin"
        expected.user.phone_number = "08166321187"
        expected.user.date_of_birth.seconds = 946684800
        expected.user.date_of_birth.nanos = 0
        expected.user.state_id = 5
        expected.user.version = 2

        self.assertEqual(UserServicer(self.UserControllerMock).UpdateUser(
            request, context=1), expected)

    def test_update_phone_number(self):
        request = user_pb2.UpdateUserRequest(id='16fd2706-8baf-433b-82eb-8c7fada847da', first_name="", last_name="",
                                             password="", phone_number="08023526224", state_id=0)

        expected = user_pb2.UpdateUserResponse()
        expected.status = "user update successful"
        expected.user.id = "16fd2706-8baf-433b-82eb-8c7fada847da"
        expected.user.first_name = "Emmanuel"
        expected.user.last_name = "Dayo"
        expected.user.user_name = "popo1"
        expected.user.email = "emman@yahoo.com"
        expected.user.password = "Abayomi20"
        expected.user.phone_number = "08023526224"
        expected.user.date_of_birth.seconds = 946684800
        expected.user.date_of_birth.nanos = 0
        expected.user.state_id = 5
        expected.user.version = 2

        self.assertEqual(UserServicer(self.UserControllerMock).UpdateUser(
            request, context=1), expected)

    def test_update_state_id(self):
        request_1 = user_pb2.UpdateUserRequest(id='16fd2706-8baf-433b-82eb-8c7fada847da', first_name="", last_name="",
                                             password="", phone_number="", state_id=40)

        expected_1 = user_pb2.UpdateUserResponse()
        expected_1.status = "p.state_id is not in range (38, 0)"

        self.assertEqual(UserServicer(self.UserControllerMock).UpdateUser(
            request_1, context=1), expected_1)

        request_2 = user_pb2.UpdateUserRequest(id='16fd2706-8baf-433b-82eb-8c7fada847da', first_name="", last_name="",
                                               password="", phone_number="", state_id=8)

        expected_2 = user_pb2.UpdateUserResponse()
        expected_2.status = "user update successful"
        expected_2.user.id = "16fd2706-8baf-433b-82eb-8c7fada847da"
        expected_2.user.first_name = "Emmanuel"
        expected_2.user.last_name = "Dayo"
        expected_2.user.user_name = "popo1"
        expected_2.user.email = "emman@yahoo.com"
        expected_2.user.password = "Abayomi20"
        expected_2.user.phone_number = "08166321187"
        expected_2.user.date_of_birth.seconds = 946684800
        expected_2.user.date_of_birth.nanos = 0
        expected_2.user.state_id = 8
        expected_2.user.version = 2

        self.assertEqual(UserServicer(self.UserControllerMock).UpdateUser(
            request_2, context=1), expected_2)

    
    def test_update_multiple_fields(self):

        # update first_name and last_name only
        request_1 = user_pb2.UpdateUserRequest(id='16fd2706-8baf-433b-82eb-8c7fada847da', first_name="Toyosi", last_name="Kosoko",
                                             password="", phone_number="", state_id=0)

        expected_1 = user_pb2.UpdateUserResponse()
        expected_1.status = "user update successful"
        expected_1.user.id = "16fd2706-8baf-433b-82eb-8c7fada847da"
        expected_1.user.first_name = "Toyosi"
        expected_1.user.last_name = "Kosoko"
        expected_1.user.user_name = "popo1"
        expected_1.user.email = "emman@yahoo.com"
        expected_1.user.password = "Abayomi20"
        expected_1.user.phone_number = "08166321187"
        expected_1.user.date_of_birth.seconds = 946684800
        expected_1.user.date_of_birth.nanos = 0
        expected_1.user.state_id = 5
        expected_1.user.version = 2

        self.assertEqual(UserServicer(self.UserControllerMock).UpdateUser(
            request_1, context=1), expected_1)


        # update password and state_id
        request_2 = user_pb2.UpdateUserRequest(id='16fd2706-8baf-433b-82eb-8c7fada847da', first_name="", last_name="",
                                             password="Morerin", phone_number="", state_id=15)

        expected_2 = user_pb2.UpdateUserResponse()
        expected_2.status = "user update successful"
        expected_2.user.id = "16fd2706-8baf-433b-82eb-8c7fada847da"
        expected_2.user.first_name = "Emmanuel"
        expected_2.user.last_name = "Dayo"
        expected_2.user.user_name = "popo1"
        expected_2.user.email = "emman@yahoo.com"
        expected_2.user.password = "Morerin"
        expected_2.user.phone_number = "08166321187"
        expected_2.user.date_of_birth.seconds = 946684800
        expected_2.user.date_of_birth.nanos = 0
        expected_2.user.state_id = 15
        expected_2.user.version = 2

        self.assertEqual(UserServicer(self.UserControllerMock).UpdateUser(
            request_2, context=1), expected_2)


        # update last_name and phone_number
        request_3 = user_pb2.UpdateUserRequest(id='16fd2706-8baf-433b-82eb-8c7fada847da', first_name="", last_name="Tobi",
                                             password="", phone_number="08023526224", state_id=0)

        expected_3 = user_pb2.UpdateUserResponse()
        expected_3.status = "user update successful"
        expected_3.user.id = "16fd2706-8baf-433b-82eb-8c7fada847da"
        expected_3.user.first_name = "Emmanuel"
        expected_3.user.last_name = "Tobi"
        expected_3.user.user_name = "popo1"
        expected_3.user.email = "emman@yahoo.com"
        expected_3.user.password = "Abayomi20"
        expected_3.user.phone_number = "08023526224"
        expected_3.user.date_of_birth.seconds = 946684800
        expected_3.user.date_of_birth.nanos = 0
        expected_3.user.state_id = 5
        expected_3.user.version = 2

        self.assertEqual(UserServicer(self.UserControllerMock).UpdateUser(
            request_3, context=1), expected_3)


        # update password, phone_number and state_id
        request_4 = user_pb2.UpdateUserRequest(id='16fd2706-8baf-433b-82eb-8c7fada847da', first_name="", last_name="",
                                               password="Morerin", phone_number="08166321189", state_id=11)

        expected_4 = user_pb2.UpdateUserResponse()
        expected_4.status = "user update successful"
        expected_4.user.id = "16fd2706-8baf-433b-82eb-8c7fada847da"
        expected_4.user.first_name = "Emmanuel"
        expected_4.user.last_name = "Dayo"
        expected_4.user.user_name = "popo1"
        expected_4.user.email = "emman@yahoo.com"
        expected_4.user.password = "Morerin"
        expected_4.user.phone_number = "08166321189"
        expected_4.user.date_of_birth.seconds = 946684800
        expected_4.user.date_of_birth.nanos = 0
        expected_4.user.state_id = 11
        expected_4.user.version = 2

        self.assertEqual(UserServicer(self.UserControllerMock).UpdateUser(
            request_4, context=1), expected_4)

        # update all fields
        request_5 = user_pb2.UpdateUserRequest(id='16fd2706-8baf-433b-82eb-8c7fada847da', first_name="Dayo", last_name="Ala",
                                               password="Popo", phone_number="08166321189", state_id=8)

        expected_5 = user_pb2.UpdateUserResponse()
        expected_5.status = "user update successful"
        expected_5.user.id = "16fd2706-8baf-433b-82eb-8c7fada847da"
        expected_5.user.first_name = "Dayo"
        expected_5.user.last_name = "Ala"
        expected_5.user.user_name = "popo1"
        expected_5.user.email = "emman@yahoo.com"
        expected_5.user.password = "Popo"
        expected_5.user.phone_number = "08166321189"
        expected_5.user.date_of_birth.seconds = 946684800
        expected_5.user.date_of_birth.nanos = 0
        expected_5.user.state_id = 8
        expected_5.user.version = 2

        self.assertEqual(UserServicer(self.UserControllerMock).UpdateUser(
            request_5, context=1), expected_5)
        

if __name__ == '__main__':
    unittest.main()
