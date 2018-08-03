## WebServise

``WebServise`` is a simple application for user management.


### Basic functions:
* user login
* user singup(only logged in users can add new users)
* remove existing users (only logged in users can remove users)

### Getting Started

1. Clone project:
```
> git clone https://github.com/Smidels/WebService_for_Deloitte.git
```
2. Create virtual environment:
```
> cd WebService_for_Deloitte
> python -m venv venv
```
3. Install requirements:
```
> pip install -r requirements.txt
```
4. Set variable enviroment FLASK_APP:
```
(venv)>export FLASK_APP=web_service.py
```
5. You can enable debug mode(not required):
```
(venv)>export FLASK_DEBUG=1
```
6. Run our server:
```
(venv)>flask run
```


### Usage Blog API


#### Login

For Login you must be logged user. For first login you can use an admin account:

##### Username:
admin

##### Password: 
1111

#### Register New User

Registration of a new user takes place on the main page. Validators control the correctness of the data entered.

#### Delete users

You enter username in the delete form and press to "Delete User".
### Note: you can't delete own and "admin" account