### This is the User Service ###

The user service is mainly used for four things. They include:

1) Register a new user
2) Delete a user
3) Get a user's details
4) Update a user

--------------------------------------------------------------------------
But before any of these happen, some things have to be put in place. 
1) Create a database 

2) Run the the yoyo migration files. Here are the Command Line Usage to note:

a) To start a new migration:
yoyo new ./migrations -m "Add column to foo"

b) To apply a migration:
yoyo apply --database postgresql://scott:tiger@localhost/db ./migrations

c) To rollback a migration:
yoyo rollback --database postgresql://scott:tiger@localhost/db ./migrations

d) To list available migrations:
yoyo apply --database postgresql://scott:tiger@localhost/db ./migrations

3) Run the server.py file to start the server on port 50051

4) Run the client.py file to connect to the API gateway on port 5000

-----------------------------------------------------------------------------------

Here is a full description of  how each of the method works:

1) REGISTER A NEW USER
This is a POST Request
The path is - http://127.0.0.1:5000/users/register
To register a new user, you need to fill in the following details in a form field. 

a) first_name
b) last_name
c) user_name
d) email
e) password
f) phone_number
g) date_of_birth . The format is: 'YYYY-MM-DD'
h) state_id . Can range from 1 to 37

Here is a sample request:
first_name: Emmanuel
last_name: Oyedeji
user_name: Emmapopo
email: emmanueloyedeji20@yahoo.com
password: popo1234
phone_number: 2348166321187
date_of_birth: 1999-11-14
state_id: 1

Based on this request, there are three possible responses:

{"status": "success"} - if the data has been successfully stored in the database
{"status": "You have to be over 18 years to register"} - if the user is under 18 years
{"status": "failed"} - if there is an error processing the input fields


2) DELETE A USER
This is a DELETE Request
The path is http://127.0.0.1:5000/users/delete

To delete a user, you need to supply only the user_id

Sample request:
user_id: 1 - means delete user with id of 1

Sample responses:
Two types of responses are possible:
{"status": "success"} - if the user has been successfully deleted
{"status": "failed"} - if deleting the user wasn't successful


3) GET USER DETAILS
This is a GET request
The path is http://127.0.0.1:5000/users/<id>   ; where id is the user_id

To get a user, you only need to supply the user_id

Sample request:
user_id: 1 - means get user with id of 1
http://127.0.0.1:5000/users/1

Sample response:
This request returns all the details of the user including:

a) id
b) first_name
c) last_name
d) user_name
e) email
f) password
g) phone_number
h) date_of_birth . The format is: 'YYYY-MM-DD'
i) state_id . Can range from 1 to 37

Here's what one looks like:
{
"id": "d3f76674-731d-493a-8e69-d6d656602ef2",
"firstName": "Emmanuel",
"lastName": "Aluko",
"userName": "Aluko123",
"email": "aluko1192@gmail.com",
"password": "Abayomi20",
"phoneNumber": "08166321187",
"dateOfBirth": "1997-11-14T00:00:00Z",
"stateId": 12
}


4) UPDATE USER DETAILS
This is a POST REQUEST

The path is http://127.0.0.1:5000/users/update

You then need to supply the id in the form field. 

Here are the other fields that may be updated:

a) first_name 
b) last_name 
c) password 
d) phone_number
e) state_id 

A sample request will be:

id: "4be5ccf3-fbd4-441d-b7ff-c4a9f406274e"
first_name: "Popo"
last_name: "Aluko"
state_id: 15

In this case, all other fields are updated except the password and phone_number

Sample response
If the update is successful, it returns:
{
"status": "user update successful"
}

If the update isn't successful, it returns:
{
"status": "user update failed"
}

