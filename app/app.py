import os

import mysql.connector
from flask import Flask, flash, redirect, render_template, request, url_for

from db import create_student, get_all_students

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "local-development-only-change-me")


@app.get("/")
def index():
    try:
        students = get_all_students()
    except mysql.connector.Error:
        app.logger.exception("Unable to retrieve students")
        flash("Database is temporarily unavailable. Please try again.", "error")
        students = []

    return render_template("index.html", students=students)


@app.post("/register")
def register():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip().lower()
    course = request.form.get("course", "").strip()

    if not name or not email or not course:
        flash("All fields are required.", "error")
        return redirect(url_for("index"))

    if len(name) > 100 or len(email) > 255 or len(course) > 100:
        flash("One or more fields exceed the allowed length.", "error")
        return redirect(url_for("index"))

    if "@" not in email or "." not in email.rsplit("@", 1)[-1]:
        flash("Please enter a valid email address.", "error")
        return redirect(url_for("index"))

    try:
        create_student(name, email, course)
        flash("Student registered successfully!", "success")
    except mysql.connector.IntegrityError:
        flash("This email is already registered.", "error")
    except mysql.connector.Error:
        app.logger.exception("Unable to register student")
        flash("Registration failed because the database is unavailable.", "error")

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
