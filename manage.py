from app import create_app,db
from flask_script import Manager,Server
from app.models import User,Comment,Pitch


#Creating app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)



@manager.shell
def make_shell_context():
   return dict(db = db, app = app, User = User, Pitch = Pitch, )

if __name__ == '__main__':
    manager.run()







