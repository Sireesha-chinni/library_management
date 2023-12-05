from django.shortcuts import render
from django.http import HttpResponse
import json
from book_manage.models import Book,Patron,Borrow
# Create your views here.

def display(request):
    details = Borrow.objects.all()
    details_list=[]
    for i in details:
        details_list.append({'name':i.name,
                             'Borrow_date':i.borrow_dt,
                             'Due_date':i.return_dt})
    print(details_list)
    return HttpResponse(details_list)