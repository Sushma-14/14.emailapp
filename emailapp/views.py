from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
import random

class Home(View):
    def get(self,request):
        return render(request,'input.html')
class Send(View):
    def get(self,request):
        subject = 'Thankyou for contacting us'
        otp= str(random.randint(10000000,99999999))
        print(otp)
        From_mail = settings.EMAIL_HOST_USER
        email=request.GET["t1"]
        to_list = [email]
        send_mail(subject, otp, From_mail, to_list, fail_silently=False)
        return HttpResponse("mail sent successfully")