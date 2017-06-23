import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from api.utils.database import db
from api.utils.factory import create_app
from api import models
app = create_app(config_name=os.getenv('APP_SETTING'))

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
