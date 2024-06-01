from flask import Flask

from infra.views import init_views
from infra.database import init_database


def init_app():
    app = Flask(
        __name__, template_folder="../ui/templates", static_folder="../ui/static"
    )

    init_database()
    init_views(app)

    return app
