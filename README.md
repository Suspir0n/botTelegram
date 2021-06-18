#  Bo Codin - API Rest in python flask and application bot telegram

## Description
This project illustrates an api in python and Flask, use docker, TDD and database

## Starting

To run the project, you will need to install the following programs:

- [Python: Required to create the project](https://www.python.org/downloads/)
- [Docker: Required to create the containers](https://www.docker.com/)
- [VS Code: For project development](https://code.visualstudio.com/)

## ⌨️ Development

Use Gitpod, a free online dev environment for GitHub.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/Suspir0n/botTelegram.git)

Or use code locally using:
```
$ cd "directory of your choice"
$ git clone https://github.com/Suspir0n/botTelegram.git
```

### Construction

To build the api with Flask, execute the commands below:

```
$ pip3 install -r requirements.txt
```

These are the requirements.txt dependencies:

```
flask==2.0.1
amqp==5.0.6
celery==5.1.0
pytest==6.1.2
behave
python_telegram_bot==13.6
flask-sqlalchemy==2.5.1
pymysql==1.0.2
flask-marshmallow==0.14.0
jsonmix
mysql-connector==2.2.9
requests==2.25.1
```

Make these settings so that your Flask application works perfectly

use the file Dockerfile

#### Database configuration 

I will show you how to connect to the mySQL database 
and its configuration. Remember, it does not create the 
database alone or the table so you have to create the 
database and tables first.

```
def connect_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@{}/{}'.format(
        os.getenv('DB_USER', 'flask'),
        os.getenv('DB_PASSWORD', ''),
        os.getenv('DB_HOST', 'mysql'),
        os.getenv('DB_NAME', 'flask')
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
def config_db(app):
    db.init_app(app)
    app.app_context().push()
    db.create_all(app=app)
    app.db = db
```

After you set up the database, run docker-compose.yml
```
$ docker-compose up --build -d
```

The exit of container flask_app:

```
* Serving Flask app "yourfile.py"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://your_ip:5000/ (Press CTRL+C to quit)
```

when the bot accepts the user needs this command on the telegram:

```
/start
```

With that he will respond as follows:

```
Hi 'your name'
Would you mind sharing your contact with me?
```

After he says this a custom button will appear for you to share your contact with the bot, 
it will send some data to the bank, it has possible questions you can ask:

```
hello
what is your name?
how are you?
fine too
what are you doing?
nothing
nothing, and you?
```

If you say something that does not contain or is not written in the same way as the names in this list, it will answer you the following:

```
No understand, ask again
```

## Project Structure

```
|-- app
   |-- controllers
      |-- __init__.py
      |-- message_controller.py
      |-- user_controller.py
   |-- models
      |-- __init__.py
      |-- message_model.py
      |-- user_model.py
   |-- routes
      |-- __init__.py
      |-- message_routes.py
      |-- user_routes.py
   |-- schemas
      |-- __init__.py
      |-- message_serealize.py
      |-- user_serealize.py
   |-- settings
      |-- __init__.py
      |-- config.py
      |-- connection.py
   |-- __init__.py
|-- bot
   |-- __init__.py
   |-- bot_telegram.py
|-- tests
   |-- __init__.py
   |-- app_test.py
   |-- conftest.py
   |-- routes_users_test.py
   |-- validation_json_test.py
|-- venv
|-- .gitignore
|-- main.py
|-- README.md    
|-- requirements.txt
|-- bot.Dockerfile
|-- Dockerfile
|-- docker-compose.yml
|-- BDD_planning.txt
|-- TDD_planning.txt
```
app >> folder contains all API data, controlles, models, schemas, 
settings, all necessary data.
<br><br>
bot >> folder contains all configuration of bot telegram
<br><br>
test folder >> contains route tests and field validation on the 
sad and happy path.
<br><br>
venv >> folder contains all the data of the premises that you 
will use.
<br><br>

## Features

The project can be used as a model to start the development of a Python project using Flask. It also demonstrates in a practical way how to create a Flask api quickly and easily.

## Configuration

To execute the project, it is necessary to use VsCode or an IDE of your preference, so that it identifies the dependencies necessary for execution in the repository. Once the project is imported, it will be possible to test its functionality in real time.

## Contributions

Contributions are always welcome! I hope I have helped someone in need.

## 🔓 License
MIT © [Evandro Silva](https://www.linkedin.com/in/suspir0n/)
