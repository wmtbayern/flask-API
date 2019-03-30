from flask import Flask

from app.apis import init_apis
from app.exts import init_ext
from app.settings import init_app
from app.views import init_view


def create_app(env_name='default'):
    app = Flask(__name__)

    init_app(app,env_name)

    init_view(app)

    init_ext(app)

    init_apis(app)


    return app