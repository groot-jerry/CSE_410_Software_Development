# Repair Anything – Web-Based Repair Request Platform

##  Project Overview

**Repair Anything** is a web-based repair request management platform developed using **Python** and the **Django Framework**. The platform allows customers to submit repair requests for electronic devices, track repair status, communicate with technicians, and manage bookings through an intuitive web interface.

The system also provides dedicated dashboards for administrators and technicians, enabling efficient management of repair requests, users, and services.

---

##  Objectives

* Develop a centralized online repair request platform.
* Simplify the repair booking process for customers.
* Enable technicians to manage assigned repair jobs efficiently.
* Provide administrators with complete control over users and repair services.
* Gain hands-on experience in full-stack web development using Django.

---

##  Features

### Customer

* User Registration & Login
* Secure Authentication
* Create Repair Requests
* Select Device Type
* Describe Repair Issues
* Track Repair Status
* View Repair History
* Update Profile

### Technician

* Technician Dashboard
* View Assigned Repairs
* Update Repair Progress
* Change Repair Status
* Manage Customer Requests

### Administrator

* Admin Dashboard
* User Management
* Technician Management
* Repair Request Management
* Service Management
* Database Administration

---

##  Technologies Used

### Backend

* Python
* Django

### Frontend

* HTML5
* CSS3
* Bootstrap
* JavaScript

### Database

* SQLite (Development)
* MySQL (Optional)

### Tools

* Visual Studio Code
* Git
* GitHub

---

## 📂 Project Structure

```text
Repair-Anything/

├── accounts/
├── customer/
├── technician/
├── admin_panel/
├── repair/
├── templates/
├── static/
├── media/
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

---

##  Getting Started

### Clone the Repository

```bash
git clone https://github.com/groot-jerry/CSE_410_Software_Development.git
```

### Navigate to the Project

```bash
cd CSE_410_Software_Development
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Database Migrations

```bash
python manage.py migrate
```

### Create an Admin User

```bash
python manage.py createsuperuser
```

### Run the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

```
http://127.0.0.1:8000/
```

---

##  Database Design

The application includes models for:

* Users
* Customers
* Technicians
* Repair Requests
* Device Categories
* Repair Status
* Feedback

The database is managed using Django's ORM, providing secure and efficient CRUD operations.

---

##  Security Features

* Django Authentication System
* Password Hashing
* CSRF Protection
* Session Management
* Form Validation
* Secure Database Access
* Role-Based Authorization

---

##  Screenshots

* Home Page
* Login Page
* Registration Page
* Customer Dashboard
* Technician Dashboard
* Admin Dashboard
* Repair Request Form
* Repair Status Page

---

##  Learning Outcomes

Through this project, I gained practical experience in:

* Full-Stack Web Development
* Django Framework
* Python Programming
* MVC (Model-View-Template) Architecture
* Database Design
* SQL & Django ORM
* Authentication & Authorization
* CRUD Operations
* Git & GitHub Version Control

---

##  Future Improvements

* Online Payment Integration
* Email & SMS Notifications
* Live Chat Support
* Repair Cost Estimation
* Service Rating & Reviews
* REST API Development
* Mobile Application Integration
* Cloud Deployment (AWS, Azure, or Heroku)

---

##  Author

**Junaed Hossain Jibon**

**Project Leader**

Department of Computer Science and Engineering (CSE)

University of Asia Pacific

---

##  License

This project was developed for academic purposes as part of the **CSE 410 – Software Development** course at the **University of Asia Pacific**.

---

##  Acknowledgements

* University of Asia Pacific
* Django Documentation
* Python Community
* Bootstrap Framework
* Open Source Contributors
