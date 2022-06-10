from django.http import JsonResponse
from .models import Book

def first_insert():
    Book.objects.create()
    raise Exception('some problem')

def second_insert():
    Book.objects.create()

def home(_):
    first_insert()
    second_insert()
    return JsonResponse({'success': True})

