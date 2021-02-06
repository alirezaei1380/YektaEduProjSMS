from celery import Celery
from kavenegar import *
from celery import shared_task

@shared_task
def send(body, phone):
    print(body)
    api = KavenegarAPI('5738716E755A364F77686A647345437164366D47683836656538326A77316C35775A2B54364453732B4B4D3D')
    params = {'sender': '1000596446', 'receptor': repr(phone), 'message': body}
    response = api.sms_send(params)
    return response