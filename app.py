import streamlit as st
import model
import db  # Correct import now

def render_tasks_tree(project_id, parent_task_id=None):
    tasks = model.get_tasks(project_id, parent_task_id)
    for task in tasks:
        task_id, name, desc, status, due = task
        expander = st.expander(f"{name} [{status}] - Due: {due}")
        with expander:
            st.write(f"Description: {desc}")
            render_tasks_tree(project_id, task_id)

def main():
    st.title("Task Manager App with Modular Code")

    current_user_id = 1  # mock logged-in user

    users = model.get_users()
    st.sidebar.header("Users")
    for u in users:
        st.sidebar.write(f"{u[0]}: {u[1]}")

    st.sidebar.header("Add User")
    new_user = st.sidebar.text_input("User name")
    if st.sidebar.button("Add User"):
        if new_user.strip():
            model.add_user(new_user.strip())
            st.sidebar.success("User added!")

    st.sidebar.header("Projects")
    projects = model.get_projects(current_user_id)
    for p in projects:
        st.sidebar.write(f"{p[0]}: {p[1]} (Role: {p[2] or 'Owner'})")

    st.sidebar.header("Add Project")
    new_project = st.sidebar.text_input("Project name")
    if st.sidebar.button("Add Project"):
        if new_project.strip():
            model.add_project(new_project.strip(), current_user_id)
            st.sidebar.success("Project added!")

    st.header("Tasks")
    if projects:
        project_ids = [p[0] for p in projects]
        selected_project_id = st.selectbox("Select Project", project_ids)
        render_tasks_tree(selected_project_id)
    else:
        st.write("No projects found. Add one!")

if __name__ == "__main__":
    db.create_tables()
    main()
