# SMTP service
import smtplib
# Non ASCII
from email.mime.text import MIMEText
from config import Config

MAIL_ACCOUNT = Config.MAIL_ACCOUNT
TO_ADDR = Config.TO_ADDR
MAIL_PASSWORD = Config.MAIL_PASSWORD


# Send email function
def send_email(subject_name, pages, detail, reminding_time):
    # Email content
    mime=MIMEText(f"{subject_name} ready to start!!\nPages: {pages}\nDetail: {detail}",
        "plain",
        "utf-8"
    )
    # Email subject
    mime["Subject"] = f"{subject_name} Reminding"
    # Email from address
    mime["From"] = MAIL_ACCOUNT
    # Email to address
    mime["TO"] = TO_ADDR
    # Transfer to string
    msg = mime.as_string()

    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    # Register SMTP server
    smtp.ehlo()
    # Use TLS
    smtp.starttls()
    smtp.login(MAIL_ACCOUNT, MAIL_PASSWORD)
    from_addr = MAIL_ACCOUNT
    to_addr = TO_ADDR

    status = smtp.sendmail(from_addr, to_addr, msg)
    if status == {}:
        print("SUCCESS")
    else:
        print("FAILED")
    smtp.quit()