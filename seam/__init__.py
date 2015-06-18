from seam.core import app
from seam.views import bp
from typogrify.templatetags.jinja_filters import register

app.register_blueprint(bp)
register(app.jinja_env)
