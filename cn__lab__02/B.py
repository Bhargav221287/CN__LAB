import smtplib
import logging
from email.mime.text import MIMEText

logging.basicConfig(filename="smtp_log.txt", level=logging.INFO)

smtp_server = "smtp.gmail.com"
port = 587
sender_email = "bhargav159509@gmail.com"
password = "********"  
receiver_email = "mahipalmaddu@gmail.com"

try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(sender_email, password)

    msg = MIMEText("""hi""")
    msg["Subject"] = "this is a test"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    server.sendmail(sender_email, receiver_email, msg.as_string())
    logging.info("Email sent successfully")
    print("✅ Email sent successfully!")
    server.quit()

except Exception as e:
    logging.error(f"SMTP error: {e}")
    print("❌ Error:", e)
