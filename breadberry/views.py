from django.shortcuts import render

from breadberry.models import Category, Position


def home(request):
    position = Position.objects.all()
    context = {'position': position}
    print(context)
    return render(request, 'breadberry/base.html', context)
