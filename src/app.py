from flask import Flask

from views import main
from db import db


app = Flask(__name__)
app.config.from_pyfile('settings.py')
db.init_app(app)
app.register_blueprint(main)


if __name__ == '__main__':
    app.run(debug=True)
