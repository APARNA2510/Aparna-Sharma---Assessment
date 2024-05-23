import smtplib
import os
from email.message import EmailMessage
from email.utils import make_msgid

def send_email(subject, body, to_email, image_path):
    # Email credentials
    from_email = 'sharmaaaparna@gmail.com'  # Replace with your email
    password = 'pljf vjem foyv lsbd'     # Replace with your email password

    # Create the email message
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email
    msg.set_content(body)
    
    # Verify if the image file exists and is of allowed type
    if not os.path.isfile(image_path):
        print(f"Error: The file {image_path} does not exist.")
        return
    
    file_extension = os.path.splitext(image_path)[1].lower()
    if file_extension not in ['.png', '.jpg', '.jpeg']:
        print("Error: Only images of type PNG, JPG, JPEG are allowed.")
        return
    
    # Read the image file and attach it to the email
    with open(image_path, 'rb') as img:
        img_data = img.read()
        img_cid = make_msgid()
        msg.add_attachment(img_data, maintype='image', subtype=file_extension[1:], filename=os.path.basename(image_path), cid=img_cid)
    
    # Send the email via SMTP server
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(from_email, password)
            smtp.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

def main():
    # Email details
    subject = "Challenge 3 Completed"
    body = """
    Name: Aparna Sharma
    Semester: Pass
    Branch: CSE
    Roll Number: 1900540100044
    """
    to_email = "hr@ignitershub.com"
    image_path = r"C:\Users\sharm\Aparna Sharma - Assessment\image.jpg"  # Replace with the path to your image file
    
    # Send the email
    send_email(subject, body, to_email, image_path)

if __name__ == "__main__":
    main()
