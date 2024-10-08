from django.shortcuts import render, HttpResponse, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.contrib import messages
from .models import Team
# Create your views here.


def index(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Contact Email"
            body = {
                'name': form.cleaned_data["name"],
                'email': form.cleaned_data['email'],
                'subject': form.cleaned_data['subject'],
                'message': form.cleaned_data['message']
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject,message,settings.EMAIL_HOST_USER,
                          ["eannor707@gmail.com"], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            messages.success(request, "Successfully contacted us. We will get back to you shortly.")
            return redirect("home:index")
    
    form = ContactForm()
    # Query the Team model to get all team members
    team_members = Team.objects.all()

    # Pass the team members to the context
    context = {
        "form": form,
        "team_members": team_members
    }

    return render(request, 'home/index.html', context)