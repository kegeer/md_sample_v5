import os
from api.utils.factory import create_app

config_name = os.getenv('APP_SETTINGS', 'default')
app = create_app(config_name)

if __name__ == '__main__':
    app.run()
