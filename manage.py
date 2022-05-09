from app import create_app,db
from flask_script import Manager,Server
from app.models import User,Pitch,Comment


#Creating app instance
app = create_app('test')

manager = Manager(app)
manager.add_command('server',Server)



@manager.shell
def make_shell_context():
   return dict(db = db, app = app, User = User, Pitch = Pitch, Comment = Comment)


@manager.command
def test():
    """
    Run the unit tests
    """
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)



if __name__ == '__main__':
    manager.run()







