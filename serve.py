import grpc
from concurrent import futures
import time
import os

#import the generated class
from proto import user_pb2_grpc
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# import logger
from log.logging_func import logger

from controller.user_controller import UserController

from server import UserServicer

host = os.environ.get('POSTGRES_HOST')
database = os.environ.get('POSTGRES_DB_NAME')
user = os.environ.get('POSTGRES_USER')
password = os.environ.get('POSTGRES_PASSWORD')

db_link = 'postgresql://' + user + ':' + password + '@' + host + '/' + database

engine = create_engine(db_link)
Session = sessionmaker(bind=engine)
session = Session()


user_controller = UserController(session)


#create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function 'add_UserServicer_to_server'
# to add the defined class to the server.

user_pb2_grpc.add_UserServicer_to_server(UserServicer(user_controller), server)

#listen on port 50051
print('Starting server. listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()
logger.info("gRPC server started on port 50051")

#since server.start() will not block,
# a sleep-loop is added to keep alive

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
