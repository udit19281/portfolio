from django.shortcuts import render
from django.core.mail import send_mail
from decouple import config
import requests
from re import error
from . import models
# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    para1="Hi I am a third year Btech. Student at "
    para1_1=""
    para2="I do web development, CP and other stuff.I like playing CTF and Django is my favourite backend stack. Contact me for projects."
    context={
        "para1": para1,
        "para1_1": para1_1,
        "para2": para2
    }
    return render(request,'about.html',context)

def project(request):
    obj=models.Project.objects.all()
    context={
        "obj":obj
    }
    return render(request,'project.html',context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        subject="Website Contact Form:"+str(name)
        body=f"You have received a new message from your website contact form.\n\n.Here are the details:\n\nName: {name}\n\nEmail: {email}\n\nPhone: {phone}\n\nMessage:\n{message}".format(name=name,email=email,phone=phone,message=message)
        from_=email
        to=[config("SEND_TO")]
        if name!="" and email!="" and phone!="" and message!="":
            try:
                data1={"from": from_,
                "to": to,
                "text": body,
                "subject":subject,
                }
                t=requests.post(
            config["API"],
            auth=("api", config("API_KEY")),
            data=data1
                )
                send=False
                if t.status_code==200:
                    send=True
                else:
                    send=False
                return render(request,'index.html',{
                    "send":send
                })
            except error as e:
                print(e)
                return render(request,'index.html')
        else:
            return render(request,'index.html')
    else:
        return render(request,'contact.html')

