from flask import Flask
import routes.game
import routes.list
import routes.login
import routes.notification
import routes.register
import routes.review
import routes.social
import routes.user

app = Flask(__name__, static_folder="../pic", static_url_path="/pic")

app.register_blueprint(routes.game.blueprint)
app.register_blueprint(routes.list.blueprint)
app.register_blueprint(routes.login.blueprint)
app.register_blueprint(routes.notification.blueprint)
app.register_blueprint(routes.register.blueprint)
app.register_blueprint(routes.review.blueprint)
app.register_blueprint(routes.social.blueprint)
app.register_blueprint(routes.user.blueprint)
