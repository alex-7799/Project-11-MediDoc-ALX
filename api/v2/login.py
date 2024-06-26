from lib2to3.pytree import convert
from flask_login import login_user
from flask import Blueprint, json, request, jsonify
from utils.general import convert_records_to_dicts, convert_single_record_to_dict, init_db_connection
from flask_bcrypt import Bcrypt

bp = Blueprint("login", __name__, url_prefix="/login")
bcrypt = Bcrypt()


@bp.route("/", methods=["POST"])
def login_post():
    from app import User

    username = request.form.get("username")
    password = request.form.get("password")
    cn = init_db_connection()
    cursor = cn.cursor()
    cursor.execute("SELECT * FROM Users WHERE username = ?", (username,))
    user = cursor.fetchone()
    cn.close()
    if user and bcrypt.check_password_hash(user["password"], password):
        user_obj = User(
            id=user["id"],
            username=user["username"],
            password=user["password"],
            role=user["role"],
        )
        login_user(user_obj)

        # result = {"username": user["username"], "role": user["role"]}
        return jsonify(user_obj.to_dict())
    else:
        return jsonify({"error": "Invalid username or password"}), 401


@bp.route("/patient", methods=["POST"])
def login_as_patient_post():
    from app import User

    username = request.form.get("username")
    password = request.form.get("password")
    cn = init_db_connection()
    cursor = cn.cursor()
    cursor.execute(
        "SELECT * FROM Users Join Patients On Users.id = Patients.user_id WHERE username = ?",
        (username,),
    )
    user = cursor.fetchone()
    cn.close()
    if user and bcrypt.check_password_hash(user["password"], password):
        user_obj = User(
            id=user["id"],
            username=user["username"],
            password=user["password"],
            role=user["role"],
        )
        login_user(user_obj)
        result = convert_single_record_to_dict(cursor, user)
        result.pop("password")
        # result = {"username": user["username"], "role": user["role"]}
        return jsonify(result)
    else:
        return jsonify({"error": "Invalid username or password"}), 401
