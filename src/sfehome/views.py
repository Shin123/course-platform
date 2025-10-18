from django.shortcuts import render
from django.conf import settings
from emails.forms import EmailForm

from emails.models import EmailVerificationEvent, Email
from emails import services as email_services


EMAIL_ADDRESS = settings.EMAIL_ADDRESS


def home_view(request, *args, **kwargs):
    template_name = "home.html"
    # request POST data
    print(request.POST)
    form = EmailForm(request.POST or None)
    context = {"form": form, "message": ""}
    if form.is_valid():
        email_val = form.cleaned_data.get("email")
        obj = email_services.start_verification_event(email_val)
        print(obj)
        context["form"] = EmailForm()
        context["message"] = (
            f"Success! Check your email for verification from {EMAIL_ADDRESS}"
        )
    else:
        print(form.errors)
    print(request.session.get("email_id"), "email_id")
    return render(request, template_name, context)
