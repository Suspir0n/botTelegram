import os

def connect_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@{}/{}'.format(
        os.getenv('DB_USER', 'flask'),
        os.getenv('DB_PASSWORD', ''),
        os.getenv('DB_HOST', 'mysql'),
        os.getenv('DB_NAME', 'flask')
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # 'mysql+pymysql://root:example@db:3306/api_bot''mysql+mysqlconnector://root:example@localhost/3306'