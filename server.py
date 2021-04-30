import grpc
from concurrent import futures
from google.protobuf import json_format
import time
import json
import datetime
import os

#import the generated class
from proto import user_pb2
from proto import user_pb2_grpc
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

#import the database connection
import psycopg2
from controller.user_controller import UserController
from model.user_model import User
from controller.functions import PBtimeToPtime, PtimeToPBtime

from dateutil.relativedelta import relativedelta

from protoc_gen_validate.validator import validate, ValidationFailed

host=os.environ.get('POSTGRES_HOST')
database= os.environ.get('POSTGRES_DB_NAME')
user=os.environ.get('POSTGRES_USER')
password= os.environ.get('POSTGRES_PASSWORD')

db_link = 'postgresql://' + user + ':' + password + '@' + host + '/' + database

engine = create_engine(db_link)
Session = sessionmaker(bind=engine)
session = Session()


user_controller = UserController(session)


class UserServicer(user_pb2_grpc.UserServicer):

    def CreateUser(self, request, context):
        response = user_pb2.CreateUserResponse()
        version = int(1)

        try:
            validate(request)
        except ValidationFailed as err:
            response.status = str(err)
            return response
    
        try:
            #age verification
        
            if user_controller.user_exist(request.email) is not None:
                response.status = "Email already used to register"

            elif user_controller.user_name_available(request.user_name) is not None:
                response.status = "user name taken!"

            elif relativedelta(datetime.datetime.now(),PBtimeToPtime(request.date_of_birth)).years < int(18):
                response.status = "You have to be over 18 years to register"
                
            else:   
                user_controller.add_user(User(request.id, request.first_name, request.last_name, request.user_name, request.email, request.password, request.phone_number, PBtimeToPtime(request.date_of_birth), request.state_id, version))
                response.status = "success"

        except:
            response.status = "failed"

        print(response)
       
        return response


    def UpdateUser(self, request, context):
        response = user_pb2.UpdateUserResponse()

        try:
            validate(request)
        except ValidationFailed as err:
            response.status = str(err)
            return response

        try: 
            user = user_controller.get_user(request.id)
          
            if request.first_name != '':
                user.first_name = request.first_name

            if request.last_name != '':
                user.last_name = request.last_name

            if request.password != '':
                user.password = request.password

            if request.phone_number != '':
                user.phone_number = request.phone_number

            if request.state_id != 0:
                user.state_id = request.state_id

        
            user_controller.update_user(user)

            response.status = "user update successful"

        except:
            response.status = "user update failed"

        return response


    def DeleteUser(self, request, context):
        response = user_pb2.DeleteUserResponse()

        try:
            validate(request)
        except ValidationFailed as err:
            response.status = str(err)
            return response

        try:
            user_controller.delete_user(request.id)
            response.status = "success"
        except:
            response.status = "failed"

        return response


    def GetUser(self, request, context):
        response = user_pb2.GetUserResponse()
        
        try:
            validate(request)
        except ValidationFailed as err:
            response.status = str(err)
            return response

        user = user_controller.get_user(request.id)
        response.id = user.id
        response.first_name = user.first_name
        response.last_name = user.last_name
        response.user_name = user.user_name
        response.email = user.email
        response.password = user.password
        response.phone_number = user.phone_number
        dob = user.date_of_birth
        dob = datetime.datetime(dob.year, dob.month, dob.day)
        response.date_of_birth.seconds = PtimeToPBtime(dob).seconds
        response.date_of_birth.nanos = PtimeToPBtime(dob).nanos
        response.state_id = user.state_id

        return response


#create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function 'add_UserServicer_to_server'
# to add the defined class to the server.

user_pb2_grpc.add_UserServicer_to_server(UserServicer(), server)

#listen on port 50051
print('Starting server. listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

#since server.start() will not block,
# a sleep-loop is added to keep alive

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)

