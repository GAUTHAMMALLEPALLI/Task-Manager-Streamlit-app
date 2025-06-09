from db import get_connection

def get_users():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    return cur.fetchall()

def add_user(name):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()

def get_projects(user_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT p.id, p.name, pu.role
        FROM projects p
        LEFT JOIN project_users pu ON p.id = pu.project_id AND pu.user_id = ?
        WHERE p.owner_id = ? OR pu.user_id = ?
    """, (user_id, user_id, user_id))
    return cur.fetchall()

def add_project(name, owner_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO projects (name, owner_id) VALUES (?, ?)", (name, owner_id))
    conn.commit()
    conn.close()

def get_tasks(project_id, parent_task_id=None):
    conn = get_connection()
    cur = conn.cursor()
    if parent_task_id is None:
        cur.execute("SELECT id, name, description, status, due_date FROM tasks WHERE project_id = ? AND parent_task_id IS NULL", (project_id,))
    else:
        cur.execute("SELECT id, name, description, status, due_date FROM tasks WHERE project_id = ? AND parent_task_id = ?", (project_id, parent_task_id))
    return cur.fetchall()
