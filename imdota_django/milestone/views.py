from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Championship

# Create your views here.


def index(request):
    latest_question_list = Championship.objects.order_by('year')
    template = loader.get_template('milestone/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'milestone/index.html', context)
