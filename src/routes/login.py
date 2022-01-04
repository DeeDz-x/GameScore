from flask import Blueprint

blueprint = Blueprint("login", __name__)


@blueprint.route("/login", methods=["POST"])
def login():
    return """{
"password": "string",
"e_mail": "string"
}""", 200, {"Content-Type": "application/json"}


@blueprint.route("/logout", methods=["POST"])
def logout():
    #login status ändern
    return "", 200


@blueprint.route("/forgot", methods=["POST"])
def forgot():
    return """{
  "e-mail": "string"
}""", 200, {"Content-Type": "application/json"}


@blueprint.route("/update_password", methods=["POST"])
def update_password():
    return "", 200
