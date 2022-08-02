import os
from urllib import response
from django.shortcuts import redirect, render
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # check if user has made inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry for this listing')
                return redirect('/listings/'+listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)

        contact.save()
        # Send Email
        
        # send_mail(
        #     'Subject here', 
        #     'Here is the message.', 
        #     'andrewemoshi@gmail.com', 
        #     ['andrewemoshi@gmail.com'], 
        #     fail_silently=False
        #     )





        # send_message = mail(
        #     from_email='sales@tendampya.com',
        #     to_emails='andrewemoshi@gmail.com',
        #     subject='Sending with Twilio SendGrid is Fun',
        #     plain_text_content='and easy to do anywhere, even with Python.',
        #     html_content='<strong>and easy to do anywhere, even with Paython</strong>')
        # try:
        #     sg = SendGridAPIClient(os.environ['SENDGRID_API_KEY'])
        #     response = sg.send(send_message)
        #     print(response.status_code)
        #     print(response.body)
        #     print(response.headers)
        # except Exception as e:
        #     print(e.send_message)



        
    

        messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
        return redirect('/listings/'+listing_id)





