# # Assuming the recipient email is in the format 'username@gmail.com'
# recipient_email = "example@gmail.com"

# # Using split method to remove the domain part
# username = recipient_email.split('@')[0]

# # Alternatively, you can use partition (works similarly)
# username = recipient_email.partition('@')[0]

# # Print or use the username
# print(f"Username: {username}")




# mail='''lawal
# taye
# taye
# taye
# taye
# taye'''


# result =mail.split('\n')
# result =mail.splitlines()

# #So bascially the splitlines split a variable comprises of worrs or sentnece by new line
# print(result)



mails='''lawal@gmail
taye@gmail
taye@gmail
taye@gmail
taye@gmail
taye@gmail'''

mails=mails.strip().splitlines()

umails='''lawal
taye
taye
taye
taye
taye'''
umails=umails.strip().splitlines()
for mail, umail in  zip(mails,umails):

    print(f"Sending email to {umail} at {mail}")



from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# Input data: usernames and emails
usernames_input = """user1
user2
user3"""
emails_input = """user1@example.com
user2@example.com
user3@example.com"""

# Split the usernames and emails by line

usernames = usernames_input.strip().split('\n')
emails = emails_input.strip().split('\n')

# Check if the number of usernames matches the number of emails
if len(usernames) != len(emails):
    print("Error: The number of usernames and emails do not match!")
else:
    # Loop through usernames and emails and send personalized emails
    sender_mail = "your_email@example.com"
    email_title = "Your Personalized Email"
    
    # Send emails to each user
    for username, email in zip(usernames, emails):
        # Create the email message
        Message = MIMEMultipart()
        Message['From'] = sender_mail
        Message['To'] = email
        Message['Subject'] = email_title
        Message['Reply-To'] = sender_mail  # Add reply-to if needed

        # Personalized email content
        email_content = f"Hello {username},\n\nThis is your personalized message."
        Message.attach(MIMEText(email_content, 'plain'))

        # Send the email
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login(sender_mail, 'your_password')
            server.sendmail(sender_mail, email, Message.as_string())
        
        print(f"Email sent to {username} at {email}.")

