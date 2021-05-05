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
    para1="Hi I am a sophomore at "
    para1_1=". I am majoring in Computer Science with Applied Mathematics."
    para2="I do web development, CP and other stuff. I like playing CTF, and Django is my favourite backend stack. Contact for projects."
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
        to=[""]
        to[0]=config("SEND_TO")
        if name!="" and email!="" and phone!="" and message!="":
            try:
                data1={"from": from_,
                "to": to,
                "text": body,
                "subject":subject,
                }
                # print("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
                key= config("API")
                # print(key)
                
                t=requests.post(
                 key,
            auth=("api", config("API_KEY")),
            data=data1
                )
                send=False
                error=False
                if t.status_code==200:
                    send=True
                else:
                    send=False
                    error=True
                return render(request,'index.html',{
                    "send":send,
                    "error":error
                })
            except error as e:
                print(e)
                return render(request,'index.html',{
                    "error":True
                })
        else:
            return render(request,'index.html',{
                "error":True
            })
    else:
        return render(request,'contact.html')

