from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from main. models import Profile,Education,Skill,Contact,Photos,Project
from . forms import ContactForm

from django.contrib import messages
import datetime
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

class TemplateShow(TemplateView):
    template_name = 'index.html'

# class detail(ListView):
#     model = Profile
#     template_name = "index.html"
#     context_object_name = 'detail'
    
#     def get_queryset(self):
#         return Profile.objects.first()

# class Education(ListView):
#     model = Education
#     template_name = "index.html"
#     context_object_name = 'edu'


def Details(request):
    personal_detail = Profile.objects.first()
    education = Education.objects.all()
    skill = Skill.objects.all()
    image = Photos.objects.first()
    projects = Project.objects.all()

    return render(request,"index.html",{'detail':personal_detail,'edus':education,'skill':skill,'image':image,'projects':projects})


def ContactDetail(request):
    if request.method == 'POST':
        data = request.POST
        dbcontact = Contact()
        dbcontact.name = data.get('name')
        dbcontact.email = data.get('email')
        dbcontact.message = data.get('message')
        dbcontact.date_sent = datetime.datetime.now()
        dbcontact.save()

        subject = 'New Contact Message'
        from_email = 'info.demodjango@gmail.com'
        recipient_list = ['info.demodjango@gmail.com'] 
        
        context = {
            'name': dbcontact.name,
            'email': dbcontact.email,
            'message': dbcontact.message,
        }
        text_content = f"Name: {dbcontact.name}\nEmail: {dbcontact.email}\nMessage: {dbcontact.message}"
        html_content = render_to_string('contact_email.html', context)

        # Send email
        email = EmailMultiAlternatives(subject, text_content, from_email, recipient_list)
        email.attach_alternative(html_content, "text/html")
        email.send()

        messages.success(request, 'This data has been sent to the admin.')
        return redirect('home')
    
    return redirect('home')

