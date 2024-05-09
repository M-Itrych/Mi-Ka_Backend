import json
from email.mime.text import MIMEText
from flask import Blueprint, jsonify, request
import smtplib
from ..utils import validate_email, validate_phone

form_bp = Blueprint('form_bp', __name__)


@form_bp.route('/api/send_email', methods=['POST'])
def contact():
    with open('config.json', 'r') as f:
        config = json.load(f).get("SMTP")

    email_data = request.json
    if not email_data or 'email' not in email_data or 'phone' not in email_data or 'text' not in email_data:
        return jsonify({"error": "Incomplete data."}), 400

    sender_email = email_data.get("email")
    sender_phone = email_data.get("phone")
    sender_text = email_data.get("text")

    if not validate_email(sender_email):
        return jsonify({"error": "Invalid email format."}), 400

    if not validate_phone(sender_phone):
        return jsonify({"error": "Invalid phone format. It should be 9 digits long."}), 400

    message_body = f"Email Address: {sender_email}\nPhone Number: {sender_phone}\n\n{sender_text}"
    message = MIMEText(message_body)
    message['Subject'] = 'Message from mi-ka.pl'

    try:
        server = smtplib.SMTP(config.get('HOST'), config.get('PORT'))
        server.starttls()
        server.login(config.get('USER'), config.get('PASS'))
        server.sendmail(sender_email, sender_email, message.as_string())
        server.quit()
        return jsonify({"message": "Email sent successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
