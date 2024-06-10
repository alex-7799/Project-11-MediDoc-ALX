from flask_login import login_user
from flask import Blueprint, request, jsonify
from utils.general import convert_records_to_dicts, init_db_connection
from flask_bcrypt import Bcrypt

bp = Blueprint("patient", __name__, url_prefix="/patient")
bcrypt = Bcrypt()


@bp.route("/", methods=["GET"])
def patient_get_basic_info():
    user_id = request.form.get("user_id")
    cn = init_db_connection()
    cursor = cn.cursor()
    cursor.execute(
        "SELECT * FROM Users Join Patients On Users.id = Patients.user_id WHERE Users.id = ?",
        (user_id,),
    )
    user = cursor.fetchone()
    cn.close()
    # Convert the tuple to a dictionary
    user_dict = {
        description[0]: value for description, value in zip(cursor.description, user)
    }
    user_dict.pop("password")

    return jsonify(user_dict)


@bp.route("/get_record", methods=["GET"])
def patient_get_record():
    patient_id = request.form.get("patient_id")
    cn = init_db_connection()
    cursor = cn.cursor()
    # Allergy
    cursor.execute(
        "SELECT * FROM Allergy WHERE Allergy.patient_id = ?",
        (patient_id,),
    )
    records = cursor.fetchall()

    allergy_list = convert_records_to_dicts(cursor, records)

    # Document
    cursor.execute(
        "SELECT * FROM Document WHERE Document.patient_id = ?",
        (patient_id,),
    )
    records = cursor.fetchall()
    document_list = convert_records_to_dicts(cursor, records)

    # Immunisation
    cursor.execute(
        "SELECT * FROM Immunisation WHERE Immunisation.patient_id = ?",
        (patient_id,),
    )
    records = cursor.fetchall()
    immunisation_list = convert_records_to_dicts(cursor, records)

    # Medicine
    cursor.execute(
        "SELECT * FROM Medicine WHERE Medicine.patient_id = ?",
        (patient_id,),
    )
    records = cursor.fetchall()
    medicine_list = convert_records_to_dicts(cursor, records)

    # Test Results
    cursor.execute(
        "SELECT * FROM TestResult WHERE TestResult.patient_id = ?",
        (patient_id,),
    )
    records = cursor.fetchall()
    testresult_list = convert_records_to_dicts(cursor, records)

    cn.close()

    result = {
        "allergy": allergy_list,
        "document": document_list,
        "immunisation": immunisation_list,
        "medicine": medicine_list,
        "testresult": testresult_list,
    }

    return jsonify(result)
