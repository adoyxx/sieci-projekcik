from flask import jsonify, request, session, redirect, url_for, Flask, Response
from .models import Student, Grade
from utils.auth import requires_auth
from . import google
from utils.db import db
from pydantic import ValidationError


def register_routes(app: Flask) -> None:
    @app.route("/students", methods=["GET"])
    def get_all_students() -> tuple[Response, int]:
        students = db.all()
        if not students:
            return jsonify({"message": "No students found"}), 404
        return jsonify(students), 200

    @app.route("/students/<int:id>", methods=["GET"])
    def get_student(id: int) -> tuple[Response, int]:
        student = db.get(doc_id=id)
        if not student:
            return jsonify({"message": "Student not found"}), 404
        return jsonify(student), 200

    @app.route("/students", methods=["POST"])
    def create_student() -> tuple[Response, int]:
        try:
            student = Student(**request.get_json())
        except ValidationError:
            return jsonify({"error": "Błędne dane wejściowe"}), 400
        student_id = db.insert(student.model_dump())
        return jsonify({"id": student_id, "message": "Created"}), 201

    @app.route("/students/<int:id>", methods=["PUT"])
    @requires_auth
    def update_grade(id: int) -> tuple[Response, int]:
        if not db.get(doc_id=id):
            return jsonify({"message": "Student not found"}), 404
        try:
            grade = Grade(**request.get_json())
        except ValidationError:
            return jsonify({"error": "Błędne dane wejściowe"}), 400
        db.update({"grade": grade.grade}, doc_ids=[id])
        return jsonify({"message": "Grade updated"}), 200

    @app.route("/students/<int:id>", methods=["DELETE"])
    def delete_student(id: int) -> tuple[Response, int]:
        if not db.get(doc_id=id):
            return jsonify({"message": "Student not found"}), 404
        db.remove(doc_ids=[id])
        return jsonify({"message": "Student deleted"}), 200

    @app.route("/login")
    def login() -> Response:
        return google.authorize(callback=url_for("authorized", _external=True))

    @app.route("/callback")
    def authorized() -> Response | tuple[str, int]:
        response = google.authorized_response()
        if response is None or response.get("access_token") is None:
            return "Login failed.", 401
        session["google_token"] = (response["access_token"], "")
        return redirect(url_for("google_profile"))

    @app.route("/google-profile")
    def google_profile() -> tuple[Response, int] | str:
        if "google_token" not in session:
            return 'Hello! Log in with your Google account: <a href="/login">Log in</a>'
        me = google.get("userinfo")
        return jsonify({"email": me.data.get("email")}), 200
