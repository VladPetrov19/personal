from django.http import HttpResponse
import datetime

tday = datetime.datetime.now()
date_time = tday.strftime("Now is: %m/%d/%Y, %H:%M:%S")


def info(request):
    return HttpResponse(date_time)
