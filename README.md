# Task Manager Web App Using Streamlit and SQLite

## 🗂 Overview

This repository contains all the necessary files for creating a **Task Manager Web Application** using **Streamlit** and **SQLite**. The app allows user and project management, with full support for creating tasks and recursive sub-tasks, making it ideal for organizing projects in a clean and structured manner.

---

## 🧱 Project Components

### 1. Database and Models

- `📦 db.py`  
  Handles SQLite database connection and table creation.

- `📦 model.py`  
  Contains all CRUD (Create, Read, Update, Delete) operations for users, projects, and tasks.

---

### 2. Frontend Web Application

- `🌐 app.py`  
  The main Streamlit app that:
  - Displays the task tree
  - Allows adding users and projects
  - Displays sidebar options for user and project management
  - Uses `model.py` for backend interactions

---

### 3. Folder Structure

