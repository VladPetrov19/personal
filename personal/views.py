from django.http import HttpResponse
import datetime

tday = datetime.datetime.now()
date_time = tday.strftime("Now is: %Y/%m/%d, %H:%M")


def info(request):
    return HttpResponse(date_time)
