import sqlite3

def create_connection(db_file="company.db"):
    conn = sqlite3.connect(db_file)
    conn.execute("PRAGMA foreign_keys = ON")
    conn.row_factory = sqlite3.Row
    return conn


def create_table(conn):
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS company (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            department TEXT,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sections (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            department_id INTEGER,
            employee TEXT,
            salary INTEGER NOT NULL DEFAULT 0,
            FOREIGN KEY (department_id) REFERENCES company(id)
            ON UPDATE CASCADE 
            ON DELETE CASCADE
        )
    """)

    conn.commit()


def insert_into_table(conn,company):
    cursor = conn.cursor()

    for department, obj in company.items():
        cursor.execute("""
            INSERT INTO company (department) VALUES (?)
        """,(department,)
        )

        department_id = cursor.lastrowid

        for employee , salary in obj.sections.items():

            cursor.execute(
                """INSERT INTO sections (department_id, employee, salary) VALUES (?,?,?)""",
                (department_id, employee, salary)
                )

    conn.commit()


