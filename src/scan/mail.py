import smtplib, ssl

port = 465  # For SSL
password = "WyKioHD99"

# Create a secure SSL context
context = ssl.create_default_context()

sender_email = "damien.sga@gmail.com"  # Enter your address
receiver_email = "damien.sga@gmail.com"  # Enter receiver address
message = "oui"

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("damien.sga@gmail.com", password)
    server.sendmail(sender_email, receiver_email, message)

