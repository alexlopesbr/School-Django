from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings

def send_email(subject, message, to_email):
    from_email = settings.EMAIL_HOST_USER

    try:
        send_mail(subject, message, from_email, [to_email])
    except BadHeaderError as er:
        return HttpResponse("Invalid header found.")
    return HttpResponseRedirect("/contact/thanks/")

