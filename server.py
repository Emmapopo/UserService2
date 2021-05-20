import datetime

from sqlalchemy.sql.expression import null
import json
from google.protobuf.json_format import MessageToJson, Parse

#import the generated class
from proto import user_pb2
from proto import user_pb2_grpc
from sqlalchemy import create_engine

# import logger
from log.logging_func import logger

from model.user_model import User
from controller.functions import PBtimeToPtime, PtimeToPBtime

from dateutil.relativedelta import relativedelta

from protoc_gen_validate.validator import validate, ValidationFailed


class UserServicer(user_pb2_grpc.UserServicer):
    def __init__(self, userController) -> None:
        super().__init__()
        self.UserController = userController

    def CreateUser(self, request, context):
        logger.info(f'{request.first_name} at {request.email} from state id {request.state_id} tried to register ')
        
        response = user_pb2.CreateUserResponse()

        version = int(1)

        try:
            validate(request)
        except ValidationFailed as err:
            response.status = str(err)
            logger.error("ValidationFailed occured", exc_info=True)
            return response
       

        # Other validations: Age verification; email uniqueness; and user name availability
        try:
            #age verification to see user is over 18.

            if relativedelta(datetime.datetime.now(), PBtimeToPtime(request.date_of_birth)).years < int(18):
                response.status = "You have to be over 18 years to register"
                logger.error(
                    f'{request.user_name}:You have to be over 18 years old to register')
        
            elif self.UserController.user_exist(request.email) is not None:
                response.status = "Email already used to register"
                logger.error(f'{request.email} is already taken')

            elif self.UserController.user_name_available(request.user_name) is not None:
                response.status = "user name taken!"
                logger.error(f'user name, {request.user_name} is already taken') 

            else:
                # Inserting the validated information into the database.
                try:
                    self.UserController.add_user(User(request.id, request.first_name, request.last_name, request.user_name, request.email,
                                                    request.password, request.phone_number, PBtimeToPtime(request.date_of_birth), request.state_id, version))
                    response.status = "success"
                    logger.info(
                        f'{request.user_name} registered successfully with {request.email}')

                except:
                    response.status = "failed"
                    logger.error("Database exception occured", exc_info=True)
                                
        except:
            response.status = "failed"
            logger.error("Exception occured", exc_info=True)

       
        return response

    def UserToPB(self, user):
        user = user_pb2.UserMessage()
        
        return user


    def UpdateUser(self, request, context):
        response = user_pb2.UpdateUserResponse()
        

        update_variables = []
        update_values = []
        if request.first_name != '':
            update_variables.append("first_name")
            update_values.append(request.first_name)

        if request.last_name != '':
            update_variables.append("last_name")
            update_values.append(request.last_name)

        if request.password != '':
            update_variables.append("password")
            update_values.append(request.password)

        if request.phone_number != '':
            update_variables.append("phone_number")
            update_values.append(request.phone_number)

        if request.state_id != 0:
            update_variables.append("state_id")
            update_values.append(request.state_id)
            
        logger.info(f"user {request.id} tried to update {update_variables} with : {update_values}")

        try:
            validate(request)
        except ValidationFailed as err:
            response.status = str(err)
            logger.error("ValidationFailed occured", exc_info=True)
            return response

        try: 
            user = self.UserController.get_user(request.id)
            
            if request.first_name != '':
                user.first_name = request.first_name
                logger.info(f"user {request.id} updated first_name with {request.first_name}")

            if request.last_name != '':
                user.last_name = request.last_name
                logger.info(f"user {request.id} updated last_name with {request.last_name}")

            if request.password != '':
                user.password = request.password
                logger.info(f"user {request.id} updated password")

            if request.phone_number != '':
                user.phone_number = request.phone_number
                logger.info(f"user {request.id} updated phone_number")

            if request.state_id != 0:
                user.state_id = request.state_id
                logger.info(f"user {request.id} updated state_id with {request.state_id}")


            user.version = int(user.version) + 1
            self.UserController.update_user(user)

            dob = user.date_of_birth
            dob_str = str(dob.year) + '-' + str(dob.month) + '-' + str(dob.day) 
            dob_obj = datetime.datetime.strptime(dob_str, "%Y-%m-%d")
            dob = PtimeToPBtime(dob_obj)
        
            response.status = "user update successful"
            response.user.id = user.id
            response.user.first_name = user.first_name
            response.user.last_name = user.last_name
            response.user.user_name = user.user_name
            response.user.email = user.email
            response.user.password = user.password
            response.user.phone_number = user.phone_number
            response.user.date_of_birth.seconds = dob.seconds
            response.user.date_of_birth.nanos = dob.nanos
            response.user.state_id = user.state_id
            response.user.version = user.version

            logger.info(f"user {request.id} update complete")

        except:
            response.status = "user update failed"
   
        return response


    def DeleteUser(self, request, context):
        response = user_pb2.DeleteUserResponse()
        logger.info(f"user {request.id} sends request to delete their account")

        try:
            validate(request)
        except ValidationFailed as err:
            response.status = str(err)
            logger.error("ValidationFailed occured", exc_info=True)
            return response

        try:
            self.UserController.delete_user(request.id)
            logger.info(f"user {request.id} account deleted")
            response.status = "success"
        except:
            logger.error("Exception occured", exc_info=True)
            response.status = "failed"

        return response


    def GetUser(self, request, context):
        logger.info(f"user {request.id} sends request to get his details")
        response = user_pb2.GetUserResponse()
        
        try:
            validate(request)
        except ValidationFailed as err:
            response.status = str(err)
            logger.error("ValidationFailed occured", exc_info=True)
            return response

        user = self.UserController.get_user(request.id)
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

        logger.info(f"returns user {request.id} account details")

        return response

