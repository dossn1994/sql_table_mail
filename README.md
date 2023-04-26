# README

This is a Python script that retrieves data from an SQL Server database and sends an email containing an HTML table of the data. The script uses the Pandas library to read the data from the database and convert it to an HTML table. The smtplib library is used to send the email, and the email.mime library is used to create the email message.

## Prerequisites

To run this script, you will need to have the following:

- Python 3.x installed on your machine.
- The Pandas, smtplib, email.mime, and sqlalchemy libraries installed.

## Setup

1. Replace the values of the `server`, `database`, `driver`, `from_email`, `to_email`, `smtp_username`, and `smtp_password` variables in the code with your own values.
2. Update the SQL query in the `query` variable to retrieve the data you want.
3. Run the script.

## How to use

To use this script, simply run it in a Python environment or IDE. The script will retrieve the data from the SQL Server database, convert it to an HTML table, and send it as an email to the specified recipient.

If the email is sent successfully, the script will print a message indicating that the email was sent successfully. If an exception occurs during the execution of the script, the exception will be printed to the console.
