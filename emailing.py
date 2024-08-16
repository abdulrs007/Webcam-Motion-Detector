import smtplib
from email.message import EmailMessage
import imghdr


PASSWORD = "xuekhwymhdgcpdmd "
SENDER = "abdulrasheeds13@gmail.com"
RECEIVER = "abdulrasheeds13@gmail.com"


def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "Home Security Camera"
    email_message.set_content("Hey, there is movement in your home garden perimeter")

    with open (image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    # send the email
    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()

if __name__ == "__main__":
    send_email(image_path="images/36.png")



