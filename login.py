from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


app = Flask(__name__)
manager = Manager(app)
manager.add_command('mysql', MigrateCommand)



@app.route("/index")
def index():
    return "index"




if __name__ == '__main__':
    manager.run()





num1 = 10
num2 = 20
num3 = 30
num4 = 40
num5 = 50
num6 = 60
