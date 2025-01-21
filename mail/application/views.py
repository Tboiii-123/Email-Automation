from django.shortcuts import render

# Create your views here.

#For sending Emails
import smtplib

#For pop up messages
from django.contrib import messages


#Email and password for the server
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#To encode files 

from email.mime.base import MIMEBase
from email import encoders


#make sure u delete your password before uploading to the github
passwordName ='roue egvy bumj wkez'








                   


def my_mail(request):

    if request.method =="POST":

                    #Names of the mail 
        usernames =request.POST.get('usernames')
        #The actual mail
        mails =request.POST.get('mails')

        
        sender_name =request.POST.get('sname')

        sender_mail = request.POST.get('smail')

            #Redirect mail name
        redirect_name =request.POST.get('rname')

            #Redirect mail
        redirect_mail =request.POST.get('rmail')

        #Title
        email_title =request.POST.get('etitle')

        #Body  
        email_body =request.POST.get('ebody')

        #File Upload
        #We use getlist for multile files
        uploaded_files =request.FILES.getlist('file')




        
        # Split the usernames and emails by line

        username_actual =usernames.strip().splitlines()

        mails_actual=mails.strip().splitlines()
        
                    


        

        try:

            
            
            for username,email in zip(username_actual,mails_actual) :
                    
                # Create a MIMEText object
                Message = MIMEMultipart()
                Message['From'] = f"{sender_name} <{sender_mail}>"
                Message['To'] = email
                Message['Reply-To'] = f"{redirect_name} <{redirect_mail}>"

                Message['Subject'] = email_title


                body= f"Hi {username},\n\n\n{email_body}"


                
                # Attach the uploaded file
                for uploaded_file in uploaded_files:

                    mime_base = MIMEBase('application', 'octet-stream')
                    mime_base.set_payload(uploaded_file.read())  # Read the uploaded file content
                    encoders.encode_base64(mime_base)
                    mime_base.add_header('Content-Disposition', f'attachment; filename={uploaded_file.name}')
                    Message.attach(mime_base)
                                
                


                


                



            

                # Attach the email body to the message
                Message.attach(MIMEText(body, 'plain'))

                            

                                
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(sender_mail, passwordName)

                    # Send the email
                server.sendmail(sender_mail, email, Message.as_string())

                
            server.quit()

            messages.success(request, 'Email Sent Successfully......')
                        

        except Exception as e:

            messages.error(request,('There is an error pls Retry again......'))
                    



            



    return render(request,'index.html',{

    })