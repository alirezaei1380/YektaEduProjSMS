from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Info
from .tasks import send

def success_view(request):
    info = Info.objects.order_by('-time').first()
    print(send.delay(info.body, info.phone))
    return HttpResponse("successfully sent")


class FormView(CreateView):

    model = Info
    template_name = 'sms/form.html'
    success_url = 'http://127.0.0.1:8000/success'
    fields = ['body', 'phone']
