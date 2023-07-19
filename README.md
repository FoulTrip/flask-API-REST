# Flask User Credentials API
This is a simple RESTful API built using Flask, which allows you to manage user credentials (username, password, and email) in a MySQL database. The API provides endpoints for retrieving, adding, updating, and deleting user data.

# Getting Started
To run the API on your local machine, follow the steps below:

# Prerequisites
 - Python (version 3.6 or higher) should be installed on your machine.
 - Install the required Python packages using the following command:
   ```bash
   pip install Flask Flask-MySQLdb flask-cors

# Setting up the Database
 - Ensure you have MySQL installed, and you can access it with a valid username and password.
 - Create a new database named 'usersdetails' using the MySQL client or any MySQL management tool of your choice.
   
# Running the API
 - Clone this repository to your local machine or download the source code as a ZIP file and extract it.
 - Navigate to the project directory in your terminal or command prompt.
 - Modify the database connection configuration in the app.py file:
   ```python
   app.config['MYSQL_HOST'] = 'localhost'
   app.config['MYSQL_USER'] = 'your_mysql_username'
   app.config['MYSQL_PASSWORD'] = 'your_mysql_password'
   app.config['MYSQL_DB'] = 'usersdetails'
  Replace 'your_mysql_username' and 'your_mysql_password' with your actual MySQL credentials.

 - Run the application:
   ```python
   python app.py
  The API will start running on http://localhost:3000. If you want to change the port, you can modify the app.run() call in app.py.

# Endpoints
# 1. Get all user credentials
 - URL: /api
 - Method: GET
 - Response:
   ```json
   {
    "credentials": [
    {
      "username": "user1",
      "password": "password1",
      "email": "user1@example.com"
    },
    {
      "username": "user2",
      "password": "password2",
      "email": "user2@example.com"
    },
    ...
    ],
   "message": "Credentials found"
   }

# 2. Get user credentials by username
 - URL: /api/<username>
 - Method: GET
 - Response:
   ```json
   {
     "username": {
       "username": "user1",
       "password": "password1",
       "email": "user1@example.com"
     },
     "message": "User found"
   }

# 3. Register a new user
 - URL: /api
 - Method: POST
 - Request Body:
   ```json
   {
     "username": "new_user",
     "password": "new_password",
     "email": "new_user@example.com"
   }
 - Response:
   ```json
   {
     "message": "Usuario Registrado"
   }
   
# 4. Update user credentials by username
 - URL: /api/<username>
 - Method: PUT
 - Request Body:
   ```json
   {
     "password": "updated_password",
     "email": "updated_email@example.com"
   }
 - Response:
   ```json
   {
     "message": "Updated user"
   }

# 5. Delete user by username
 - URL: /api/<username>
 - Method: DELETE
 - Response:
   ```json
   {
     "message": "User delete"
   }

# Error Handling
The API handles common errors and responds with appropriate messages. If an endpoint does not exist, a custom 404 page will be displayed.


Note: Make sure to replace 'your_mysql_username' and 'your_mysql_password' in the README with your actual MySQL credentials.
