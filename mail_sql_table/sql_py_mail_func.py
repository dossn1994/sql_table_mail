import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from sqlalchemy import create_engine, text


def sendmailing(html_table):
 try:
# Set up the email parameters
  from_email = 'your_mail'
  to_email = 'to_mail'
  subject = 'Table'
  body = f'<html><body><p>Please find below the Report.Merchants table:</p>{html_table}</body></html>'

# Create the email message
  msg = MIMEMultipart()
  msg['From'] = from_email
  msg['To'] = to_email
  msg['Subject'] = subject
  msg.attach(MIMEText(body, 'html'))

# Send the email
  smtp_server = 'smtp.gmail.com'
  smtp_port = '587'
  smtp_username = ''
  smtp_password = ''
  smtp_conn = smtplib.SMTP(smtp_server, smtp_port)
  smtp_conn.starttls()
  smtp_conn.login(smtp_username, smtp_password)
  smtp_conn.sendmail(from_email, to_email, msg.as_string())
  smtp_conn.quit()
 except Exception as e:
  print("the excetion is : " ,e)
 else:
  print("mail sent successfully") 
  
 


if __name__ == "__main__":
# Set up a connection to the database using Windows Authentication
 server = ''
 database = ''
 driver = ''
 connection_string = f'mssql+pyodbc://{server}/{database}?driver={driver}&Trusted_Connection=yes'
 engine = create_engine(connection_string)
 connection = engine.connect()

# Define the SQL query to execute
 query = text('select * from table')

# Execute the SQL query and retrieve the results as a Pandas DataFrame
 df = pd.read_sql_query(query, connection)

# Convert the DataFrame to an HTML table
 html_table = df.to_html(index=False)

 final = sendmailing(html_table)

# Close the database connection
 connection.close()
 engine.dispose()