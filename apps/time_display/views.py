# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime, localtime
def index(request):
    context = {
        "gmtime": strftime("%b %d, %Y %I:%M %p", gmtime()),
        "localtime": strftime("%b %d, %Y %I:%M %p", localtime())
    }
    return render(request,'time_display/index.html', context)