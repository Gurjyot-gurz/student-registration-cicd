import os
import mysql.connector
from mysql.connector import pooling


_pool = None


def get_db_config():
    return {
        "host": os.getenv("DB_HOST", "localhost"),
        "port": int(os.getenv("DB_PORT", "3306")),
        "user": os.getenv("DB_USER", "student_user"),
        "password": os.getenv("DB_PASSWORD", ""),
        "database": os.getenv("DB_NAME", "student_db"),
    }


def get_connection():
    global _pool

    if _pool is None:
        _pool = pooling.MySQLConnectionPool(
            pool_name="student_pool",
            pool_size=5,
            **get_db_config(),
        )

    return _pool.get_connection()


def get_all_students():
    connection = get_connection()
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(
            "SELECT id, name, email, course, created_at "
            "FROM students ORDER BY id DESC"
        )
        return cursor.fetchall()
    finally:
        cursor.close()
        connection.close()


def create_student(name, email, course):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO students (name, email, course) VALUES (%s, %s, %s)",
            (name, email, course),
        )
        connection.commit()
        return cursor.lastrowid
    finally:
        cursor.close()
        connection.close()
