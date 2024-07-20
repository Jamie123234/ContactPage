from flask import Flask, render_template, request
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("contact.html")

@app.route("/submit_form", methods=["POST","GET"])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        print(data.get("first_name"))
        print(data.get("last_name"))
        print(data.get("email_address"))
        send_email()
        return render_template("sent.html")
    else: return "Something went wrong!"

def send_email():
    data = request.form.to_dict()
    msg = EmailMessage()
    msg["From"] = data.get("email_address")
    msg["To"] = "jamieabrahams123234@gmail.com"
    msg["Subject"] = data.get("subject")
    msg.set_content("From: " + data.get("first_name") + " " + data.get("last_name") + 
                    "\n" + "Email: " + data.get("email_address") + "\n" +
                    "Message: " + data.get("message_content"))
    
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login("pythonemailserver.smtp@gmail.com", "iyzo jopq octf ojad")
        smtp.send_message(msg)
        print("Message Sent!")


if __name__ == "__main__":
    app.run()
