import streamlit as st
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

# Email credentials
sender_email = "jahnvidubey99@gmail.com"
app_password = "xpbz vtxk fxnc onbo"  # Replace with your App Password

# Resume PDF to attach
resume_pdf = 'assets/Jahnvi_Dubey_Resume.pdf'  # Replace with the path to your resume PDF

# Function to send email
def send_email(receiver_email, company_name):
    try:
        # Create the email message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = f"Python Associate Software Developer Position - Jahnvi Dubey"

        # Email body
        body = (
            "Dear HR,\n\n"
            "I hope this email finds you well.\n\n"
            "I am writing to express my interest in the Python Developer position at {company_name}. "
            "With over a year of experience in Python development and experience in FastAPI, Django, web scraping, ML, "
            "and data analysis, I am excited about the opportunity to contribute to your team.\n\n"
            "Attached is my resume for your review. I look forward to discussing how my skills and background "
            "align with the needs of your team.\n\n"
            "Thank you for considering my application.\n\n"
            "Best regards,\n"
            "Jahnvi Dubey\n"
            "9131488473\n"
            "jahnvidubey99@gmail.com\n"
            "https://github.com/Jahnvidubey"
        ).format(company_name=company_name)
        message.attach(MIMEText(body, 'plain'))

        # Attach the resume PDF
        with open(resume_pdf, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f"attachment; filename={os.path.basename(resume_pdf)}")
            message.attach(part)

        # Establish connection to Gmail's SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Encrypt the connection
        server.login(sender_email, app_password)  # Use the App Password here

        # Send the email
        server.sendmail(sender_email, receiver_email, message.as_string())
        st.success(f"Email sent to {company_name} ({receiver_email}) successfully!")

    except Exception as e:
        st.error(f"Failed to send email to {company_name} ({receiver_email}): {e}")

    finally:
        server.quit()

# Streamlit app layout
st.title("Automated Resume Email Sender")

with st.form(key="email_form"):
    company_name = st.text_input("Enter Company Name", placeholder="e.g., ABC Corp")
    company_email = st.text_input("Enter HR Email Address", placeholder="e.g., hr@abccorp.com")
    submit_button = st.form_submit_button(label="Send Email")

if submit_button:
    if company_name and company_email:
        send_email(company_email, company_name)
    else:
        st.warning("Please fill in both Company Name and HR Email Address.")
