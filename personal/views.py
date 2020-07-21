from django.http import HttpResponse
import datetime

tday = datetime.datetime.now()


def info(request):
    return HttpResponse(tday)
