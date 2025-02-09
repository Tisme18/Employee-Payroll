"Lazapee" Payroll System
A Web-Based Payroll Management System for Employee Salary Tracking

📌 Project Overview
"Lazapee" Payroll System is a Django-based web application designed to help businesses efficiently manage employee salaries, deductions, and payslip generation. The system allows HR teams to:
- Maintain employee records
- Calculate salaries with automated tax & deduction computations
- Manage overtime pay & allowances
- Generate monthly & bi-monthly payslips

This group project is built as part of MSYS 22: Introduction to Programming II at Ateneo de Manila University as a final requirement.

Features
- Employee Management
View, add, update, and delete employee records
Track rate per hour, allowance, and overtime pay
Auto-reset overtime hours after payslip generation

- Payslip Generation
Generate bi-monthly payslips (Cycle 1 & Cycle 2)
Automatically compute:
Tax (20%)
Pag-IBIG (PHP 100 flat) (Cycle 1)
PhilHealth (4%) & SSS (4.5%) (Cycle 2)
Overtime pay: (Rate/160) × 1.5 × Hours Worked
Prevent duplicate payslips for the same cycle

- Payroll Reports & Payslip Viewing
View all payslips in a summary table
Filter payslips by employee ID, month, and year
Display detailed payslips with breakdown of earnings & deductions

- User-Friendly Interface
Navigation bar for quick access to employees & payslips
Responsive Bootstrap-based UI for a clean and modern look

- Tech Stack
Backend: Django (Python)
Frontend: HTML, CSS (Bootstrap)
Database: SQLite (default) / PostgreSQL (optional)
📂 Project Structure
lazapee/
- │── payroll_app/         # Main Django app
- │   ├── models.py        # Database models for Employees & Payslips
- │   ├── views.py         # Application logic
- │   ├── urls.py          # URL routing
- │   ├── templates/       # HTML templates
- │   ├── static/          # CSS, JS, and images
- │── db.sqlite3           # Database file
- │── manage.py            # Django project management script
- │── README.md            # Project documentation
- │── requirements.txt     # Required Python packages

Getting Started
- Clone the Repository
git clone https://github.com/yourusername/lazapee-payroll.git
cd lazapee-payroll
- Install Dependencies
pip install -r requirements.txt
- Run Database Migrations
python manage.py migrate
- Start the Development Server
python manage.py runserver
- Access the Application
Open http://127.0.0.1:8000/ in your browser.
