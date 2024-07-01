import os
import time
import pytest
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import zipfile

# Run the test case and generate the report
folder_path = "C:/Users/HP/PycharmProjects/spur-automations/Reports/"
timestamp = str(int(time.time()))

# Create a unique file name using the timestamp
file_name = f"{timestamp}.html"
file_path = os.path.join(folder_path, file_name)

# Run the test case with the specified marker
pytest.main(["--html=" + file_path, "-m alltest"])


def send_email_with_report(recipient_email):
    # Email details
    sender_email = "projectonqa@gmail.com"
    sender_password = "reqfailndcijwifo"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Create message container
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = "Automation Test Report of Spur"

    # # Attach report file
    # with open(report_file, "rb") as file:
    #     attachment = MIMEApplication(file.read(), _subtype="html")
    #     attachment.add_header("Content-Disposition", "attachment", filename=os.path.basename(report_file))
    #     message.attach(attachment)
    # Compress the report folder into a zip file
    zip_filename = "report.zip"
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), folder_path))

    # Attach the zip file to the email
    with open(zip_filename, "rb") as file:
        attachment = MIMEApplication(file.read())
        attachment.add_header("Content-Disposition", "attachment", filename=zip_filename)
        message.attach(attachment)

        # Add a custom message to the email
        custom_message = '''Hello sir,
                            please find attached Zip file for the automation test report of Spur Experiences.
                            
                            Thank you
                            Balkishan Dhankhar'''
        message.attach(MIMEText(custom_message, "plain"))

    # Connect to SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)

    # Send email
    server.send_message(message)

    # Disconnect from SMTP server
    server.quit()


# report file path and recipient email
report_file_path = file_path
recipient_emails = "balkishan.dhankhar@owebest.in, bharat.singh@owebest.com, mahendra.singh@owebest.in"

# Call the function to send the email with the report
send_email_with_report(recipient_emails)
