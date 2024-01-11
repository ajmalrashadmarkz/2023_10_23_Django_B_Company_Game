from django.core.mail import EmailMessage
import os
import random

class Util:
  @staticmethod
  def send_email(data):
    email = EmailMessage(
      subject=data['subject'],
      body=data['body'],
      from_email=os.environ.get('EMAIL_FROM'),
      to=[data['to_email']]
    )
    email.send()

def generate_otp(length):
    # Create an empty string to store the OTP
  otp = random.randint(10**(length-1), 10**length - 1)
    # Return the OTP
  return str(otp)
# Import the Util class and the os module


# Define a function to send an OTP to a user's email
def send_otp_email(user):
    # Generate a 6-digit OTP
    otp = generate_otp(6)
    # Store the OTP in the user's model
    user.otp = otp
    user.save()
    # Create a data dictionary for the email
    data = {
        'subject': 'Your OTP',
        'body': f'Your OTP is {otp}',
        'from_email': os.environ.get('EMAIL_FROM'),
        'to_email': user.email
    }
    # Use the Util class to send the email
    Util.send_email(data)