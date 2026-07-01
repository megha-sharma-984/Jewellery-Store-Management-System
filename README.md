# Jewellery Store Management System

A console-based mini project developed using **Python** and **MySQL** to manage jewellery inventory across multiple brands. The application allows users to register/login, manage jewellery records, and perform database operations through a menu-driven interface.

## Features

- User Registration and Login
- Add Jewellery Records
- Update Jewellery Details
- Delete Jewellery Records
- Display Jewellery Inventory
- Multiple Jewellery Brand Support
- Menu-Driven Interface
- Formatted Table Display

## Technologies Used

- Python
- MySQL
- mysql-connector-python
- tabulate

## Python Concepts Demonstrated

- Functions
- Conditional Statements
- Loops
- MySQL Database Connectivity
- CRUD Operations
- User Authentication
- Modular Programming

## How to Run

1. Install Python 3.
2. Install the required libraries:

```bash
pip install mysql-connector-python tabulate
```

3. Install and start MySQL Server.
4. Update the MySQL username and password in `jewellery_store_management.py`.
5. Follow the **Database Setup** steps for the first-time setup.
6. Run:

```bash
python jewellery_store_management.py
```

## Database Setup

1. Install MySQL Server and create a MySQL user.
2. Open `jewellery_store_management.py` and update the MySQL username and password.
3. The application automatically creates the `Jewellery_Mall` database.
4. For the first-time setup, uncomment the `CREATE TABLE` and `INSERT INTO` statements, run the program once, and then comment them again to avoid inserting duplicate records.


## Future Improvements

- Graphical User Interface (GUI)
- Search and Filter Functionality
- Billing System
- Customer Management
- Sales Reports
