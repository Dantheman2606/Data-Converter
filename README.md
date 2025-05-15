# Excel to MySQL Data Transfer Tool

## Overview

This Python-based tool allows you to transfer data from Excel files (.xlsx, .xls, .csv) into a MySQL database.  It provides a graphical user interface (GUI) built with `customtkinter` for easy interaction.

## Features

* **Excel File Selection:** Uses a file dialog to select the Excel file for data transfer.
* **MySQL Connectivity:** Connects to a MySQL database using provided credentials (hostname, username, password, database name).
* **Sheet Handling:** Processes all sheets within the Excel file.
* **Table Creation:** Automatically creates tables in the MySQL database, mirroring the structure of the Excel sheets.  Column data types (INT, FLOAT, VARCHAR) are inferred from the Excel data.
* **Data Insertion:** Inserts the data from each Excel sheet into the corresponding MySQL table.
* **GUI Interface:** Provides a user-friendly interface for selecting files, entering database credentials, and initiating the data transfer.
* **Error Handling:** Includes basic error handling.
* **Table and Row Counts:** Displays the number of rows and columns processed for each table.

## How it Works

The script reads data from an Excel file, infers the data type of each column, and creates corresponding tables in the specified MySQL database.  It then iterates through each sheet, extracting the data and inserting it into the newly created tables.

## Dependencies

* Python 3.x
* `customtkinter`
* `xlrd`
* `mysql-connector-python`
* `pandas`

## Setup

1.  **Install Dependencies:**

    ```bash
    pip install customtkinter xlrd mysql-connector-python pandas
    ```
2.  **Clone the Repository:** (If applicable)

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```
3.  **Ensure MySQL Server is running and you have the necessary permissions**

## Usage

1.  Run the `run.py` script:

    ```bash
    python run.py
    ```
2.  The GUI will appear.
3.  Click "Choose File" to select your Excel file.
4.  Enter your MySQL database credentials (hostname, username, password, database name).
5.  Click "Transfer the Data".
6.  The program will create tables and transfer the data.  A confirmation message will be displayed in the GUI.
7.  Click "Close Window" to exit.
