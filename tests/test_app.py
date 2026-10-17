import os
import sys
from pathlib import Path

import mysql.connector
import pytest

# Make app/app.py importable when pytest runs from the project root.
APP_DIR = str(Path(__file__).resolve().parents[1] / "app")
sys.path.insert(0, APP_DIR)

import app as flask_app


@pytest.fixture()
def client():
    flask_app.app.config.update(
        TESTING=True,
        SECRET_KEY="test-secret-key",
    )

    with flask_app.app.test_client() as test_client:
        yield test_client


def test_home_page_displays_students(client, monkeypatch):
    monkeypatch.setattr(
        flask_app,
        "get_all_students",
        lambda: [
            {
                "id": 1,
                "name": "Test Student",
                "email": "student@example.com",
                "course": "Cloud Computing",
                "created_at": None,
            }
        ],
    )

    response = client.get("/")

    assert response.status_code == 200
    assert b"Student Registration System" in response.data
    assert b"Test Student" in response.data


def test_home_page_handles_database_error(client, monkeypatch):
    def fail_database():
        raise mysql.connector.Error("Simulated database error")

    monkeypatch.setattr(flask_app, "get_all_students", fail_database)

    response = client.get("/")

    assert response.status_code == 200
    assert b"Database is temporarily unavailable" in response.data


def test_valid_registration(client, monkeypatch):
    created = {}

    def fake_create_student(name, email, course):
        created["student"] = (name, email, course)
        return 1

    monkeypatch.setattr(flask_app, "create_student", fake_create_student)

    response = client.post(
        "/register",
        data={
            "name": "Test Student",
            "email": "STUDENT@example.com",
            "course": "Cloud Computing",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert created["student"] == (
        "Test Student",
        "student@example.com",
        "Cloud Computing",
    )
    assert b"Student registered successfully" in response.data


def test_registration_requires_all_fields(client, monkeypatch):
    def should_not_run(*args, **kwargs):
        pytest.fail("Database insert should not run for invalid input")

    monkeypatch.setattr(flask_app, "create_student", should_not_run)

    response = client.post(
        "/register",
        data={"name": "", "email": "student@example.com", "course": "DevOps"},
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"All fields are required" in response.data


def test_registration_rejects_invalid_email(client, monkeypatch):
    def should_not_run(*args, **kwargs):
        pytest.fail("Database insert should not run for invalid email")

    monkeypatch.setattr(flask_app, "create_student", should_not_run)

    response = client.post(
        "/register",
        data={"name": "Test Student", "email": "invalid-email", "course": "DevOps"},
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"valid email address" in response.data


def test_duplicate_email_shows_error(client, monkeypatch):
    def duplicate_student(*args, **kwargs):
        raise mysql.connector.IntegrityError("Duplicate email")

    monkeypatch.setattr(flask_app, "create_student", duplicate_student)

    response = client.post(
        "/register",
        data={
            "name": "Another Student",
            "email": "student@example.com",
            "course": "DevOps",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"This email is already registered" in response.data
