from django.shortcuts import render
from FloraRoomApp import models

# Create your views here.


def main_page(request):
    context = {'short_articles': models.Article.objects.all()}

    return render(request, 'mainPage.html', context)
