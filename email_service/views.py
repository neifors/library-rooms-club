from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings


def send_email(request):
    subject = 'Hello from futureproof'
    message = 'Hey there!'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [request.session['email']]

    send_mail( subject, message, email_from, recipient_list )

    return redirect("library-home")
