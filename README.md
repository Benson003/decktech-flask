To make sure this project runs Do these commands first

Set the Flask Enviroment Variables

on Linux
export FLASK_APP=main:create_app

on Windows
set FLASK_APP=main:create_app

set up the Database

flask db init
flask db migrate -m "Optional Message" //The "-m" flag is optional
flask db upgrade