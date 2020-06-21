import os

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm


# Create your views here.
def contact(request):
    """
    A view to return contact page and render the form, allowing a user
    to contact the website owner/manager by submitting the form.
    """
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            full_name = contact_form.cleaned_data['full_name']
            user_email = contact_form.cleaned_data['email']
            message = contact_form.cleaned_data['message']
            send_mail(full_name, message, user_email, [
                       os.environ.get("EMAIL_HOST_USER")], fail_silently=False)
            messages.success(
                request, "Thank you! Your message has been sent successfully,\
                     we will get back to you soon.")
            return redirect('landing')
    else:
        contact_form = ContactForm()

    context = {
        'contact_form': contact_form
    }

    return render(request, 'contact/contact.html', context)
